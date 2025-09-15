import { describe, it, expect } from 'vitest'
import { validatePromptConfiguration, validateGeneratedPrompt } from '@/lib/validation/schema-validator'
import type { PromptConfiguration, GeneratedPrompt } from '@/types'

describe('Prompt Generation Schema Validation', () => {
  describe('PromptConfiguration Validation', () => {
    const validConfig: PromptConfiguration = {
      taskDescription: 'Write a comprehensive product review for a smartphone',
      targetModel: 'gpt-4',
      domain: 'general',
      complexityLevel: 'moderate',
      outputFormat: 'structured',
      creativityLevel: 6,
      specificRequirements: 'Focus on camera quality and battery life'
    }

    it('should validate valid configuration', () => {
      const result = validatePromptConfiguration(validConfig)
      expect(result.valid).toBe(true)
      expect(result.errors).toHaveLength(0)
    })

    describe('taskDescription validation', () => {
      it('should reject empty task description', () => {
        const config = { ...validConfig, taskDescription: '' }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Task description is required (minimum 10 characters)')
      })

      it('should reject task description too short', () => {
        const config = { ...validConfig, taskDescription: 'Too short' }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Task description must be at least 10 characters')
      })

      it('should reject task description too long', () => {
        const config = { ...validConfig, taskDescription: 'x'.repeat(2001) }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Task description must not exceed 2000 characters')
      })

      it('should reject invalid characters in task description', () => {
        const config = { ...validConfig, taskDescription: 'Invalid chars: <script>alert("xss")</script>' }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Task description contains invalid characters')
      })
    })

    describe('targetModel validation', () => {
      it('should accept valid model names', () => {
        const validModels = ['gpt-4', 'gpt-3.5-turbo', 'claude-3', 'claude-sonnet', 'gemini-pro', 'custom']

        validModels.forEach(model => {
          const config = { ...validConfig, targetModel: model as any }
          const result = validatePromptConfiguration(config)

          expect(result.valid).toBe(true)
        })
      })

      it('should reject invalid model names', () => {
        const config = { ...validConfig, targetModel: 'invalid-model' as any }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Target model must be one of: gpt-4, gpt-3.5-turbo, claude-3, claude-sonnet, gemini-pro, custom')
      })
    })

    describe('domain validation', () => {
      it('should accept valid domains', () => {
        const validDomains = ['general', 'healthcare', 'legal', 'finance', 'education', 'creative', 'technical', 'research', 'other']

        validDomains.forEach(domain => {
          const config = { ...validConfig, domain: domain as any }
          const result = validatePromptConfiguration(config)

          expect(result.valid).toBe(true)
        })
      })

      it('should reject invalid domains', () => {
        const config = { ...validConfig, domain: 'invalid-domain' as any }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Domain must be one of the predefined options')
      })
    })

    describe('creativityLevel validation', () => {
      it('should accept valid creativity levels', () => {
        for (let level = 1; level <= 10; level++) {
          const config = { ...validConfig, creativityLevel: level }
          const result = validatePromptConfiguration(config)

          expect(result.valid).toBe(true)
        }
      })

      it('should reject creativity level below 1', () => {
        const config = { ...validConfig, creativityLevel: 0 }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Creativity level must be between 1 and 10')
      })

      it('should reject creativity level above 10', () => {
        const config = { ...validConfig, creativityLevel: 11 }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Creativity level must be between 1 and 10')
      })

      it('should reject non-integer creativity levels', () => {
        const config = { ...validConfig, creativityLevel: 5.5 }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Creativity level must be an integer')
      })
    })

    describe('specificRequirements validation', () => {
      it('should accept empty specific requirements', () => {
        const config = { ...validConfig, specificRequirements: undefined }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(true)
      })

      it('should reject specific requirements too long', () => {
        const config = { ...validConfig, specificRequirements: 'x'.repeat(1001) }
        const result = validatePromptConfiguration(config)

        expect(result.valid).toBe(false)
        expect(result.errors).toContain('Specific requirements must not exceed 1000 characters')
      })
    })
  })

  describe('GeneratedPrompt Validation', () => {
    const validGeneratedPrompt: GeneratedPrompt = {
      id: 'prompt-12345',
      content: 'You are an expert product reviewer with 10+ years of experience...',
      metadata: {
        wordCount: 150,
        estimatedTokens: 200,
        readabilityScore: 8.5,
        completenessScore: 9.0,
        usageInstructions: 'Use this prompt to generate detailed product reviews',
        testScenarios: ['Test with iPhone 15', 'Test with Samsung Galaxy S24']
      },
      quality: {
        overallScore: 8.8,
        clarity: 9.0,
        completeness: 8.5,
        effectiveness: 9.0,
        specificity: 8.5,
        feedback: ['Consider adding more specific examples'],
        strengths: ['Clear role definition', 'Specific task description'],
        weaknesses: ['Could benefit from more examples']
      },
      techniques: [
        {
          technique: 'role_based',
          reason: 'Product review requires domain expertise',
          implementation: 'Defined as expert reviewer with experience',
          confidence: 0.9
        }
      ],
      generatedAt: new Date(),
      model: 'gpt-4',
      configuration: {
        taskDescription: 'Write a product review',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'moderate',
        outputFormat: 'structured',
        creativityLevel: 6
      }
    }

    it('should validate valid generated prompt', () => {
      const result = validateGeneratedPrompt(validGeneratedPrompt)
      expect(result.valid).toBe(true)
      expect(result.errors).toHaveLength(0)
    })

    it('should require all mandatory fields', () => {
      const incompletePrompt = { ...validGeneratedPrompt, content: undefined } as any
      const result = validateGeneratedPrompt(incompletePrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Content is required')
    })

    it('should validate content length', () => {
      const shortContentPrompt = { ...validGeneratedPrompt, content: 'Too short' }
      const result = validateGeneratedPrompt(shortContentPrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Content must be at least 50 characters long')
    })

    it('should validate quality score ranges', () => {
      const invalidQualityPrompt = {
        ...validGeneratedPrompt,
        quality: {
          ...validGeneratedPrompt.quality,
          overallScore: 15
        }
      }
      const result = validateGeneratedPrompt(invalidQualityPrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Quality scores must be between 1 and 10')
    })

    it('should validate technique structure', () => {
      const invalidTechniquePrompt = {
        ...validGeneratedPrompt,
        techniques: [
          {
            technique: 'invalid_technique',
            reason: '',
            implementation: 'Some implementation',
            confidence: 1.5
          }
        ]
      }
      const result = validateGeneratedPrompt(invalidTechniquePrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Invalid technique name')
      expect(result.errors).toContain('Technique reason cannot be empty')
      expect(result.errors).toContain('Confidence must be between 0 and 1')
    })

    it('should require at least one technique', () => {
      const noTechniquesPrompt = { ...validGeneratedPrompt, techniques: [] }
      const result = validateGeneratedPrompt(noTechniquesPrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('At least one technique must be applied')
    })
  })

  describe('Cross-field validation', () => {
    it('should validate consistency between configuration and result', () => {
      const inconsistentPrompt = {
        ...validGeneratedPrompt,
        model: 'gpt-3.5-turbo',
        configuration: {
          ...validGeneratedPrompt.configuration,
          targetModel: 'gpt-4'
        }
      }

      const result = validateGeneratedPrompt(inconsistentPrompt)

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Model in result does not match configuration')
    })

    it('should validate technique appropriateness for domain', () => {
      const healthcareConfig = {
        ...validGeneratedPrompt.configuration,
        domain: 'healthcare' as const
      }

      const inappropriateTechniques = [{
        technique: 'creative_stimulus',
        reason: 'Adding creativity',
        implementation: 'Some creative elements',
        confidence: 0.8
      }]

      const result = validateGeneratedPrompt({
        ...validGeneratedPrompt,
        configuration: healthcareConfig,
        techniques: inappropriateTechniques
      })

      expect(result.valid).toBe(false)
      expect(result.errors).toContain('Creative techniques not recommended for healthcare domain')
    })
  })
})