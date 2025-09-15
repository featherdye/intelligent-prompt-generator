import { describe, it, expect, beforeEach } from 'vitest'
import { PromptConfiguration, PromptConfigurationValidator } from '@/lib/prompt-config/PromptConfiguration'

describe('PromptConfiguration Model', () => {
  let validator: PromptConfigurationValidator

  beforeEach(() => {
    validator = new PromptConfigurationValidator()
  })

  describe('Creation and Validation', () => {
    const validData = {
      taskDescription: 'Write a comprehensive product review for a smartphone',
      targetModel: 'gpt-4' as const,
      domain: 'general' as const,
      complexityLevel: 'moderate' as const,
      outputFormat: 'structured' as const,
      creativityLevel: 6,
      specificRequirements: 'Focus on camera quality and battery life'
    }

    it('should create valid configuration', () => {
      const config = PromptConfiguration.create(validData)

      expect(config.isValid()).toBe(true)
      expect(config.getErrors()).toHaveLength(0)
      expect(config.taskDescription).toBe(validData.taskDescription)
      expect(config.targetModel).toBe(validData.targetModel)
      expect(config.domain).toBe(validData.domain)
    })

    it('should validate task description length', () => {
      const shortDescription = { ...validData, taskDescription: 'Too short' }
      const config = PromptConfiguration.create(shortDescription)

      expect(config.isValid()).toBe(false)
      expect(config.getErrors()).toContain('Task description must be at least 10 characters')

      const longDescription = { ...validData, taskDescription: 'x'.repeat(2001) }
      const config2 = PromptConfiguration.create(longDescription)

      expect(config2.isValid()).toBe(false)
      expect(config2.getErrors()).toContain('Task description must not exceed 2000 characters')
    })

    it('should validate required fields', () => {
      const incomplete = { ...validData, taskDescription: '' }
      const config = PromptConfiguration.create(incomplete)

      expect(config.isValid()).toBe(false)
      expect(config.getErrors()).toContain('Task description is required')
    })

    it('should validate creativity level range', () => {
      const lowCreativity = { ...validData, creativityLevel: 0 }
      const config1 = PromptConfiguration.create(lowCreativity)

      expect(config1.isValid()).toBe(false)
      expect(config1.getErrors()).toContain('Creativity level must be between 1 and 10')

      const highCreativity = { ...validData, creativityLevel: 11 }
      const config2 = PromptConfiguration.create(highCreativity)

      expect(config2.isValid()).toBe(false)
      expect(config2.getErrors()).toContain('Creativity level must be between 1 and 10')
    })

    it('should validate enum values', () => {
      const invalidModel = { ...validData, targetModel: 'invalid-model' as any }
      const config = PromptConfiguration.create(invalidModel)

      expect(config.isValid()).toBe(false)
      expect(config.getErrors()).toContain('Invalid target model')
    })
  })

  describe('State Transitions', () => {
    const validData = {
      taskDescription: 'Write a product review',
      targetModel: 'gpt-4' as const,
      domain: 'general' as const,
      complexityLevel: 'simple' as const,
      outputFormat: 'conversational' as const,
      creativityLevel: 5
    }

    it('should transition from Draft to Valid', () => {
      const config = PromptConfiguration.create(validData)

      expect(config.getState()).toBe('draft')

      const validationResult = config.validate()

      expect(validationResult.isValid).toBe(true)
      expect(config.getState()).toBe('valid')
    })

    it('should transition from Draft to Invalid', () => {
      const invalidData = { ...validData, creativityLevel: 15 }
      const config = PromptConfiguration.create(invalidData)

      expect(config.getState()).toBe('draft')

      const validationResult = config.validate()

      expect(validationResult.isValid).toBe(false)
      expect(config.getState()).toBe('invalid')
    })

    it('should transition from Valid to Submitting', () => {
      const config = PromptConfiguration.create(validData)
      config.validate()

      expect(config.getState()).toBe('valid')

      config.markSubmitting()

      expect(config.getState()).toBe('submitting')
    })

    it('should transition from Submitting to Success/Error', () => {
      const config = PromptConfiguration.create(validData)
      config.validate()
      config.markSubmitting()

      expect(config.getState()).toBe('submitting')

      // Success path
      config.markSuccess()
      expect(config.getState()).toBe('success')

      // Reset and test error path
      const config2 = PromptConfiguration.create(validData)
      config2.validate()
      config2.markSubmitting()
      config2.markError('API error')

      expect(config2.getState()).toBe('error')
      expect(config2.getErrorMessage()).toBe('API error')
    })

    it('should not allow invalid state transitions', () => {
      const config = PromptConfiguration.create(validData)

      // Cannot go from draft directly to submitting
      expect(() => config.markSubmitting()).toThrow('Cannot transition from draft to submitting')

      // Cannot mark success without submitting first
      config.validate()
      expect(() => config.markSuccess()).toThrow('Cannot transition from valid to success')
    })
  })

  describe('Data Serialization', () => {
    it('should serialize to plain object', () => {
      const validData = {
        taskDescription: 'Write a product review',
        targetModel: 'gpt-4' as const,
        domain: 'technical' as const,
        complexityLevel: 'complex' as const,
        outputFormat: 'json' as const,
        creativityLevel: 3,
        specificRequirements: 'Include technical specifications'
      }

      const config = PromptConfiguration.create(validData)
      const serialized = config.toJSON()

      expect(serialized).toEqual({
        ...validData,
        state: 'draft',
        errors: [],
        createdAt: expect.any(String),
        updatedAt: expect.any(String)
      })
    })

    it('should deserialize from plain object', () => {
      const data = {
        taskDescription: 'Write a product review',
        targetModel: 'gpt-4' as const,
        domain: 'technical' as const,
        complexityLevel: 'complex' as const,
        outputFormat: 'json' as const,
        creativityLevel: 3,
        state: 'valid' as const,
        errors: [],
        createdAt: '2024-01-01T00:00:00.000Z',
        updatedAt: '2024-01-01T00:00:00.000Z'
      }

      const config = PromptConfiguration.fromJSON(data)

      expect(config.taskDescription).toBe(data.taskDescription)
      expect(config.getState()).toBe('valid')
      expect(config.creativityLevel).toBe(3)
    })
  })

  describe('Edge Cases', () => {
    it('should handle undefined optional fields', () => {
      const minimalData = {
        taskDescription: 'Write a simple review',
        targetModel: 'gpt-3.5-turbo' as const,
        domain: 'general' as const,
        complexityLevel: 'simple' as const,
        outputFormat: 'conversational' as const,
        creativityLevel: 5
      }

      const config = PromptConfiguration.create(minimalData)

      expect(config.isValid()).toBe(true)
      expect(config.specificRequirements).toBeUndefined()
    })

    it('should handle special characters in task description', () => {
      const specialCharsData = {
        taskDescription: 'Write a review with émojis 🚀 and spëcial chars & symbols!',
        targetModel: 'gpt-4' as const,
        domain: 'general' as const,
        complexityLevel: 'simple' as const,
        outputFormat: 'conversational' as const,
        creativityLevel: 5
      }

      const config = PromptConfiguration.create(specialCharsData)

      expect(config.isValid()).toBe(true)
      expect(config.taskDescription).toBe(specialCharsData.taskDescription)
    })

    it('should sanitize potentially dangerous input', () => {
      const dangerousData = {
        taskDescription: 'Write a review <script>alert("xss")</script> safely',
        targetModel: 'gpt-4' as const,
        domain: 'general' as const,
        complexityLevel: 'simple' as const,
        outputFormat: 'conversational' as const,
        creativityLevel: 5
      }

      const config = PromptConfiguration.create(dangerousData)

      expect(config.taskDescription).not.toContain('<script>')
      expect(config.taskDescription).toBe('Write a review  safely')
    })

    it('should handle concurrent modifications', () => {
      const config = PromptConfiguration.create({
        taskDescription: 'Original task description',
        targetModel: 'gpt-4' as const,
        domain: 'general' as const,
        complexityLevel: 'simple' as const,
        outputFormat: 'conversational' as const,
        creativityLevel: 5
      })

      const originalUpdatedAt = config.getUpdatedAt()

      // Simulate concurrent update
      setTimeout(() => {
        config.updateTaskDescription('Modified task description')
      }, 10)

      // Another update
      config.updateCreativityLevel(8)

      expect(config.taskDescription).toBe('Modified task description')
      expect(config.creativityLevel).toBe(8)
      expect(config.getUpdatedAt()).not.toBe(originalUpdatedAt)
    })
  })

  describe('Performance', () => {
    it('should handle large task descriptions efficiently', () => {
      const largeDescription = 'A'.repeat(1500) // Close to max length

      const startTime = performance.now()
      const config = PromptConfiguration.create({
        taskDescription: largeDescription,
        targetModel: 'gpt-4' as const,
        domain: 'general' as const,
        complexityLevel: 'complex' as const,
        outputFormat: 'structured' as const,
        creativityLevel: 5
      })

      const validationTime = performance.now()
      config.validate()
      const endTime = performance.now()

      expect(config.isValid()).toBe(true)
      expect(endTime - startTime).toBeLessThan(100) // Should be fast
      expect(validationTime - startTime).toBeLessThan(50) // Creation should be very fast
    })

    it('should cache validation results', () => {
      const config = PromptConfiguration.create({
        taskDescription: 'Test caching behavior',
        targetModel: 'gpt-4' as const,
        domain: 'general' as const,
        complexityLevel: 'simple' as const,
        outputFormat: 'conversational' as const,
        creativityLevel: 5
      })

      // First validation
      const start1 = performance.now()
      const result1 = config.validate()
      const end1 = performance.now()

      // Second validation (should use cache)
      const start2 = performance.now()
      const result2 = config.validate()
      const end2 = performance.now()

      expect(result1.isValid).toBe(result2.isValid)
      expect(end2 - start2).toBeLessThan(end1 - start1) // Second should be faster due to caching
    })
  })
})