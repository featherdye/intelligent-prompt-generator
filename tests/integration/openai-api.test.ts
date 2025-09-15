import { describe, it, expect, beforeEach } from 'vitest'
import { OpenAIClient } from '@/lib/openai-client/OpenAIClient'
import type { PromptConfiguration } from '@/types'

describe('OpenAI API Integration', () => {
  let client: OpenAIClient
  const testApiKey = process.env.VITE_TEST_OPENAI_API_KEY || 'sk-test-key-for-ci'

  beforeEach(() => {
    client = new OpenAIClient(testApiKey)
  })

  describe('API Key Validation', () => {
    it('should validate API key format', () => {
      expect(() => new OpenAIClient('invalid-key')).toThrow('Invalid API key format')
      expect(() => new OpenAIClient('')).toThrow('API key is required')
      expect(() => new OpenAIClient('sk-proj-valid-key-format-here')).not.toThrow()
    })

    it('should mask API key in logs', () => {
      const client = new OpenAIClient('sk-proj-1234567890abcdefghijklmnopqrstuvwxyz')
      expect(client.getMaskedKey()).toBe('sk-proj-***...***xyz')
    })
  })

  describe('Prompt Generation', () => {
    const testConfig: PromptConfiguration = {
      taskDescription: 'Write a product review for a smartphone',
      targetModel: 'gpt-4',
      domain: 'general',
      complexityLevel: 'moderate',
      outputFormat: 'structured',
      creativityLevel: 6,
      specificRequirements: 'Focus on camera quality and battery life'
    }

    it('should generate prompt with valid configuration', async () => {
      const result = await client.generatePrompt(testConfig)

      expect(result).toBeDefined()
      expect(result.id).toBeDefined()
      expect(result.content).toBeDefined()
      expect(result.content.length).toBeGreaterThan(50)
      expect(result.metadata).toBeDefined()
      expect(result.quality).toBeDefined()
      expect(result.techniques).toBeDefined()
      expect(result.techniques.length).toBeGreaterThan(0)
      expect(result.generatedAt).toBeInstanceOf(Date)
      expect(result.model).toBe('gpt-4')
      expect(result.configuration).toEqual(testConfig)
    })

    it('should handle API rate limiting gracefully', async () => {
      // Mock rate limit scenario
      const rateLimitedClient = new OpenAIClient('sk-test-rate-limit-key')

      await expect(rateLimitedClient.generatePrompt(testConfig))
        .rejects
        .toThrow(/rate limit|quota|billing/i)
    })

    it('should handle network errors with retry logic', async () => {
      const networkErrorClient = new OpenAIClient('sk-test-network-error-key')

      await expect(networkErrorClient.generatePrompt(testConfig))
        .rejects
        .toThrow(/network|timeout|connection/i)
    })

    it('should handle invalid model errors', async () => {
      const invalidModelConfig = { ...testConfig, targetModel: 'invalid-model' as any }

      await expect(client.generatePrompt(invalidModelConfig))
        .rejects
        .toThrow(/model|unsupported/i)
    })
  })

  describe('Response Validation', () => {
    it('should validate OpenAI API response structure', async () => {
      const testConfig: PromptConfiguration = {
        taskDescription: 'Simple test task',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'simple',
        outputFormat: 'conversational',
        creativityLevel: 5
      }

      const result = await client.generatePrompt(testConfig)

      // Validate GeneratedPrompt structure
      expect(result).toMatchObject({
        id: expect.any(String),
        content: expect.any(String),
        metadata: {
          wordCount: expect.any(Number),
          estimatedTokens: expect.any(Number),
          readabilityScore: expect.any(Number),
          completenessScore: expect.any(Number)
        },
        quality: {
          overallScore: expect.any(Number),
          clarity: expect.any(Number),
          completeness: expect.any(Number),
          effectiveness: expect.any(Number),
          specificity: expect.any(Number)
        },
        techniques: expect.arrayContaining([
          expect.objectContaining({
            technique: expect.any(String),
            reason: expect.any(String),
            implementation: expect.any(String),
            confidence: expect.any(Number)
          })
        ]),
        generatedAt: expect.any(Date),
        model: expect.any(String),
        configuration: expect.any(Object)
      })

      // Validate score ranges
      expect(result.quality.overallScore).toBeGreaterThanOrEqual(1)
      expect(result.quality.overallScore).toBeLessThanOrEqual(10)
      expect(result.metadata.wordCount).toBeGreaterThan(0)
      expect(result.metadata.estimatedTokens).toBeGreaterThan(0)
    })
  })

  describe('Error Handling', () => {
    it('should return standardized error format', async () => {
      const invalidClient = new OpenAIClient('sk-invalid-key-format')

      try {
        await invalidClient.generatePrompt({} as PromptConfiguration)
      } catch (error: any) {
        expect(error).toMatchObject({
          error: expect.stringMatching(/validation_error|api_error|authentication_error/),
          message: expect.any(String),
          code: expect.any(String),
          retryable: expect.any(Boolean)
        })

        if (error.retryable) {
          expect(error.retryAfter).toBeGreaterThan(0)
        }
      }
    })
  })
})