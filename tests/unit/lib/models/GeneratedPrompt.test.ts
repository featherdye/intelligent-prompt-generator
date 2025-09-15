import { describe, it, expect, beforeEach } from 'vitest'
import { GeneratedPrompt, PromptMetadata, QualityAssessment } from '@/lib/models/GeneratedPrompt'
import type { PromptConfiguration, TechniqueSelection } from '@/types'

describe('GeneratedPrompt Model', () => {
  const mockConfiguration: PromptConfiguration = {
    taskDescription: 'Write a product review for a smartphone',
    targetModel: 'gpt-4',
    domain: 'general',
    complexityLevel: 'moderate',
    outputFormat: 'structured',
    creativityLevel: 6,
    specificRequirements: 'Focus on camera and battery'
  }

  const mockContent = `You are an experienced technology reviewer who has tested hundreds of smartphones. Your reviews are trusted by consumers for their balanced, detailed analysis.

**Task**: Write a comprehensive review of the smartphone that helps potential buyers make an informed purchasing decision.

**Review Structure**:
1. **Overview** (50 words): Brief introduction and first impressions
2. **Camera Performance** (100-120 words): Photo/video quality, features
3. **Battery Life** (80-100 words): Usage patterns, charging speed
4. **Pros & Cons** (60-80 words): Balanced list of strengths and weaknesses
5. **Verdict** (30-50 words): Final recommendation`

  const mockTechniques: TechniqueSelection[] = [
    {
      technique: 'role_based',
      reason: 'Product review requires domain expertise',
      implementation: 'Defined as experienced technology reviewer',
      confidence: 0.9
    },
    {
      technique: 'structured_output',
      reason: 'User requested structured format',
      implementation: 'Clear sections with word count guidance',
      confidence: 0.8
    }
  ]

  describe('Creation and Metadata Calculation', () => {
    it('should create GeneratedPrompt with calculated metadata', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.id).toBeDefined()
      expect(prompt.content).toBe(mockContent)
      expect(prompt.model).toBe('gpt-4')
      expect(prompt.configuration).toEqual(mockConfiguration)
      expect(prompt.techniques).toEqual(mockTechniques)
      expect(prompt.generatedAt).toBeInstanceOf(Date)

      // Check metadata calculation
      expect(prompt.metadata.wordCount).toBeGreaterThan(0)
      expect(prompt.metadata.estimatedTokens).toBeGreaterThan(0)
      expect(prompt.metadata.readabilityScore).toBeGreaterThanOrEqual(1)
      expect(prompt.metadata.readabilityScore).toBeLessThanOrEqual(10)
      expect(prompt.metadata.completenessScore).toBeGreaterThanOrEqual(1)
      expect(prompt.metadata.completenessScore).toBeLessThanOrEqual(10)
    })

    it('should calculate word count correctly', () => {
      const simpleContent = 'This is a test prompt with exactly ten words here.'
      const prompt = GeneratedPrompt.create({
        content: simpleContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.metadata.wordCount).toBe(10)
    })

    it('should estimate token count approximately', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const expectedTokens = Math.ceil(prompt.metadata.wordCount * 1.3) // Rough estimate
      expect(prompt.metadata.estimatedTokens).toBeCloseTo(expectedTokens, -1) // Within 10% margin
    })

    it('should calculate readability score based on content complexity', () => {
      const simpleContent = 'This is simple. Easy to read. Short sentences.'
      const complexContent = 'This comprehensive analysis encompasses multifarious considerations regarding technological implementations and their consequential ramifications.'

      const simplePrompt = GeneratedPrompt.create({
        content: simpleContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const complexPrompt = GeneratedPrompt.create({
        content: complexContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(simplePrompt.metadata.readabilityScore).toBeGreaterThan(complexPrompt.metadata.readabilityScore)
    })
  })

  describe('Quality Assessment', () => {
    it('should generate quality assessment scores', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.quality.overallScore).toBeGreaterThanOrEqual(1)
      expect(prompt.quality.overallScore).toBeLessThanOrEqual(10)
      expect(prompt.quality.clarity).toBeGreaterThanOrEqual(1)
      expect(prompt.quality.clarity).toBeLessThanOrEqual(10)
      expect(prompt.quality.completeness).toBeGreaterThanOrEqual(1)
      expect(prompt.quality.completeness).toBeLessThanOrEqual(10)
      expect(prompt.quality.effectiveness).toBeGreaterThanOrEqual(1)
      expect(prompt.quality.effectiveness).toBeLessThanOrEqual(10)
      expect(prompt.quality.specificity).toBeGreaterThanOrEqual(1)
      expect(prompt.quality.specificity).toBeLessThanOrEqual(10)

      expect(prompt.quality.feedback).toBeInstanceOf(Array)
      expect(prompt.quality.strengths).toBeInstanceOf(Array)
      expect(prompt.quality.weaknesses).toBeInstanceOf(Array)
    })

    it('should provide higher scores for well-structured prompts', () => {
      const wellStructuredContent = `You are an expert analyst with 10+ years of experience.

Task: Analyze the quarterly financial report.

Requirements:
1. Revenue analysis (compare to previous quarter)
2. Cost structure evaluation
3. Key performance indicators
4. Risk assessment
5. Strategic recommendations

Format: Professional business report with executive summary.

Constraints: 500-750 words, data-driven insights only.`

      const poorlyStructuredContent = 'analyze financial report quickly'

      const wellStructuredPrompt = GeneratedPrompt.create({
        content: wellStructuredContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const poorPrompt = GeneratedPrompt.create({
        content: poorlyStructuredContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(wellStructuredPrompt.quality.overallScore).toBeGreaterThan(poorPrompt.quality.overallScore)
      expect(wellStructuredPrompt.quality.specificity).toBeGreaterThan(poorPrompt.quality.specificity)
      expect(wellStructuredPrompt.quality.completeness).toBeGreaterThan(poorPrompt.quality.completeness)
    })

    it('should identify strengths and weaknesses accurately', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.quality.strengths.length).toBeGreaterThan(0)
      expect(prompt.quality.strengths.some(strength =>
        strength.toLowerCase().includes('structure') ||
        strength.toLowerCase().includes('clear') ||
        strength.toLowerCase().includes('role')
      )).toBe(true)

      // Should provide constructive feedback
      if (prompt.quality.weaknesses.length > 0) {
        expect(prompt.quality.weaknesses.some(weakness =>
          weakness.length > 10 // Meaningful feedback, not just single words
        )).toBe(true)
      }
    })
  })

  describe('Usage Instructions Generation', () => {
    it('should generate appropriate usage instructions', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.metadata.usageInstructions).toBeDefined()
      expect(prompt.metadata.usageInstructions!.length).toBeGreaterThan(20)
      expect(prompt.metadata.usageInstructions).toMatch(/use|copy|paste|model|temperature/i)
    })

    it('should include model-specific recommendations', () => {
      const gpt4Prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const gpt35Prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-3.5-turbo',
        configuration: { ...mockConfiguration, targetModel: 'gpt-3.5-turbo' },
        techniques: mockTechniques
      })

      expect(gpt4Prompt.metadata.usageInstructions).toMatch(/gpt-4|GPT-4/i)
      expect(gpt35Prompt.metadata.usageInstructions).toMatch(/gpt-3.5|GPT-3.5/i)
    })
  })

  describe('Test Scenarios Generation', () => {
    it('should generate relevant test scenarios', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      expect(prompt.metadata.testScenarios).toBeDefined()
      expect(prompt.metadata.testScenarios!.length).toBeGreaterThan(0)

      prompt.metadata.testScenarios!.forEach(scenario => {
        expect(scenario.length).toBeGreaterThan(10)
        expect(scenario).toMatch(/test|try|example|sample/i)
      })
    })

    it('should generate domain-specific test scenarios', () => {
      const healthcareConfig = { ...mockConfiguration, domain: 'healthcare' as const }
      const prompt = GeneratedPrompt.create({
        content: 'You are a medical professional. Analyze patient data...',
        model: 'gpt-4',
        configuration: healthcareConfig,
        techniques: mockTechniques
      })

      const scenarios = prompt.metadata.testScenarios!
      expect(scenarios.some(scenario =>
        scenario.toLowerCase().includes('medical') ||
        scenario.toLowerCase().includes('patient') ||
        scenario.toLowerCase().includes('healthcare')
      )).toBe(true)
    })
  })

  describe('Serialization and Persistence', () => {
    it('should serialize to JSON correctly', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const json = prompt.toJSON()

      expect(json.id).toBe(prompt.id)
      expect(json.content).toBe(prompt.content)
      expect(json.metadata).toEqual(prompt.metadata)
      expect(json.quality).toEqual(prompt.quality)
      expect(json.techniques).toEqual(prompt.techniques)
      expect(json.generatedAt).toBe(prompt.generatedAt.toISOString())
      expect(json.configuration).toEqual(prompt.configuration)
    })

    it('should deserialize from JSON correctly', () => {
      const originalPrompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const json = originalPrompt.toJSON()
      const deserializedPrompt = GeneratedPrompt.fromJSON(json)

      expect(deserializedPrompt.id).toBe(originalPrompt.id)
      expect(deserializedPrompt.content).toBe(originalPrompt.content)
      expect(deserializedPrompt.model).toBe(originalPrompt.model)
      expect(deserializedPrompt.generatedAt).toEqual(originalPrompt.generatedAt)
      expect(deserializedPrompt.metadata).toEqual(originalPrompt.metadata)
      expect(deserializedPrompt.quality).toEqual(originalPrompt.quality)
    })
  })

  describe('Comparison and Analysis', () => {
    it('should compare prompts by quality scores', () => {
      const prompt1 = GeneratedPrompt.create({
        content: 'Simple task description',
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: [mockTechniques[0]]
      })

      const prompt2 = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const comparison = prompt1.compareTo(prompt2)

      expect(comparison.betterPrompt).toBeDefined()
      expect(comparison.qualityDifference).toBeGreaterThan(0)
      expect(comparison.strengths).toBeInstanceOf(Array)
      expect(comparison.improvements).toBeInstanceOf(Array)
    })

    it('should analyze technique effectiveness', () => {
      const prompt = GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })

      const analysis = prompt.analyzeTechniques()

      expect(analysis.mostEffective).toBeDefined()
      expect(analysis.effectiveness).toBeInstanceOf(Array)
      expect(analysis.recommendations).toBeInstanceOf(Array)

      analysis.effectiveness.forEach(item => {
        expect(item.technique).toBeDefined()
        expect(item.impact).toBeGreaterThanOrEqual(0)
        expect(item.impact).toBeLessThanOrEqual(1)
      })
    })
  })

  describe('Edge Cases and Error Handling', () => {
    it('should handle empty content gracefully', () => {
      expect(() => GeneratedPrompt.create({
        content: '',
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })).toThrow('Content cannot be empty')
    })

    it('should handle malformed techniques array', () => {
      const malformedTechniques = [
        {
          technique: 'invalid_technique',
          reason: '',
          implementation: 'test',
          confidence: 1.5 // Invalid confidence
        }
      ] as any

      expect(() => GeneratedPrompt.create({
        content: mockContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: malformedTechniques
      })).toThrow(/invalid technique|confidence|reason/)
    })

    it('should handle very long content efficiently', () => {
      const longContent = mockContent.repeat(100) // Very long prompt

      const startTime = performance.now()
      const prompt = GeneratedPrompt.create({
        content: longContent,
        model: 'gpt-4',
        configuration: mockConfiguration,
        techniques: mockTechniques
      })
      const endTime = performance.now()

      expect(endTime - startTime).toBeLessThan(1000) // Should complete within 1 second
      expect(prompt.metadata.wordCount).toBeGreaterThan(1000)
      expect(prompt.quality.overallScore).toBeGreaterThanOrEqual(1)
    })
  })
})