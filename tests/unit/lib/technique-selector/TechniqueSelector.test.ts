import { describe, it, expect, beforeEach } from 'vitest'
import { TechniqueSelector, TechniqueType } from '@/lib/technique-selector/TechniqueSelector'
import type { PromptConfiguration } from '@/types'

describe('TechniqueSelector', () => {
  let selector: TechniqueSelector

  beforeEach(() => {
    selector = new TechniqueSelector()
  })

  describe('Basic Technique Selection', () => {
    it('should select appropriate techniques for simple tasks', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Write a short product description',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'simple',
        outputFormat: 'conversational',
        creativityLevel: 5
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.ZERO_SHOT)
      expect(techniques).toContain(TechniqueType.ROLE_BASED)
      expect(techniques.length).toBeGreaterThan(0)
      expect(techniques.length).toBeLessThan(6) // Simple tasks shouldn't need many techniques
    })

    it('should select more techniques for complex tasks', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Analyze complex financial data and provide strategic recommendations with risk assessment',
        targetModel: 'gpt-4',
        domain: 'finance',
        complexityLevel: 'expert',
        outputFormat: 'structured',
        creativityLevel: 3
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.CHAIN_OF_THOUGHT)
      expect(techniques).toContain(TechniqueType.DOMAIN_EXPERTISE)
      expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)
      expect(techniques.length).toBeGreaterThan(3) // Complex tasks need multiple techniques
    })
  })

  describe('Domain-Specific Selection', () => {
    it('should select domain expertise for healthcare tasks', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Analyze medical symptoms and provide diagnostic suggestions',
        targetModel: 'gpt-4',
        domain: 'healthcare',
        complexityLevel: 'complex',
        outputFormat: 'structured',
        creativityLevel: 2
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.DOMAIN_EXPERTISE)
      expect(techniques).toContain(TechniqueType.SAFETY_CONSTRAINTS)
      expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)
    })

    it('should select appropriate techniques for legal domain', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Draft a contract clause for intellectual property rights',
        targetModel: 'gpt-4',
        domain: 'legal',
        complexityLevel: 'expert',
        outputFormat: 'structured',
        creativityLevel: 1
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.DOMAIN_EXPERTISE)
      expect(techniques).toContain(TechniqueType.SAFETY_CONSTRAINTS)
      expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)
      expect(techniques).not.toContain(TechniqueType.CREATIVE_STIMULUS) // Low creativity for legal
    })

    it('should select creative techniques for creative domains', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Write an engaging story with unique characters',
        targetModel: 'gpt-4',
        domain: 'creative',
        complexityLevel: 'moderate',
        outputFormat: 'conversational',
        creativityLevel: 9
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.CREATIVE_STIMULUS)
      expect(techniques).toContain(TechniqueType.FEW_SHOT) // Examples help with creative writing
      expect(techniques).not.toContain(TechniqueType.SAFETY_CONSTRAINTS) // Less restrictive for creative tasks
    })
  })

  describe('Complexity-Based Selection', () => {
    const baseConfig: PromptConfiguration = {
      taskDescription: 'Analyze market trends',
      targetModel: 'gpt-4',
      domain: 'finance',
      outputFormat: 'structured',
      creativityLevel: 5
    }

    it('should use zero-shot for simple tasks', () => {
      const config = { ...baseConfig, complexityLevel: 'simple' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.ZERO_SHOT)
      expect(techniques).not.toContain(TechniqueType.CHAIN_OF_THOUGHT)
    })

    it('should use chain-of-thought for complex tasks', () => {
      const config = { ...baseConfig, complexityLevel: 'complex' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.CHAIN_OF_THOUGHT)
      expect(techniques).toContain(TechniqueType.SELF_CONSISTENCY)
    })

    it('should use advanced techniques for expert tasks', () => {
      const config = { ...baseConfig, complexityLevel: 'expert' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.CHAIN_OF_THOUGHT)
      expect(techniques).toContain(TechniqueType.SELF_CONSISTENCY)
      expect(techniques).toContain(TechniqueType.META_PROMPTING)
    })
  })

  describe('Model-Specific Optimizations', () => {
    const baseConfig: PromptConfiguration = {
      taskDescription: 'Analyze data and provide insights',
      domain: 'general',
      complexityLevel: 'moderate',
      outputFormat: 'structured',
      creativityLevel: 5
    }

    it('should optimize for GPT-4', () => {
      const config = { ...baseConfig, targetModel: 'gpt-4' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.MODEL_SPECIFIC)

      const modelOptimizations = selector.getModelOptimizations('gpt-4')
      expect(modelOptimizations.maxTokens).toBeGreaterThan(2000)
      expect(modelOptimizations.supportsComplexReasoning).toBe(true)
    })

    it('should optimize for GPT-3.5-turbo', () => {
      const config = { ...baseConfig, targetModel: 'gpt-3.5-turbo' as const }
      const techniques = selector.selectTechniques(config)

      const modelOptimizations = selector.getModelOptimizations('gpt-3.5-turbo')
      expect(modelOptimizations.maxTokens).toBeLessThan(4000)
      expect(modelOptimizations.requiresMoreGuidance).toBe(true)
    })

    it('should adapt techniques based on model capabilities', () => {
      const gpt4Config = { ...baseConfig, targetModel: 'gpt-4' as const, complexityLevel: 'expert' as const }
      const gpt35Config = { ...baseConfig, targetModel: 'gpt-3.5-turbo' as const, complexityLevel: 'expert' as const }

      const gpt4Techniques = selector.selectTechniques(gpt4Config)
      const gpt35Techniques = selector.selectTechniques(gpt35Config)

      // GPT-4 can handle more advanced techniques
      expect(gpt4Techniques).toContain(TechniqueType.META_PROMPTING)

      // GPT-3.5 might need more explicit guidance
      expect(gpt35Techniques).toContain(TechniqueType.FEW_SHOT)
    })
  })

  describe('Output Format Influence', () => {
    const baseConfig: PromptConfiguration = {
      taskDescription: 'Create a project report',
      targetModel: 'gpt-4',
      domain: 'general',
      complexityLevel: 'moderate',
      creativityLevel: 5
    }

    it('should select structured output techniques for structured format', () => {
      const config = { ...baseConfig, outputFormat: 'structured' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)
    })

    it('should select appropriate techniques for JSON format', () => {
      const config = { ...baseConfig, outputFormat: 'json' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)

      const formatGuidance = selector.getFormatGuidance('json')
      expect(formatGuidance).toContain('JSON')
      expect(formatGuidance).toContain('valid syntax')
    })

    it('should be flexible with conversational format', () => {
      const config = { ...baseConfig, outputFormat: 'conversational' as const }
      const techniques = selector.selectTechniques(config)

      expect(techniques).not.toContain(TechniqueType.STRUCTURED_OUTPUT)
      expect(techniques.length).toBeGreaterThan(1) // Should still have guidance techniques
    })
  })

  describe('Technique Justification', () => {
    it('should provide reasons for each selected technique', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Analyze customer feedback and provide actionable insights',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'complex',
        outputFormat: 'structured',
        creativityLevel: 4
      }

      const selections = selector.selectTechniquesWithReasoning(config)

      expect(selections.length).toBeGreaterThan(0)

      selections.forEach(selection => {
        expect(selection.technique).toBeDefined()
        expect(selection.reason).toBeDefined()
        expect(selection.reason.length).toBeGreaterThan(10)
        expect(selection.confidence).toBeGreaterThan(0)
        expect(selection.confidence).toBeLessThanOrEqual(1)
      })

      // Should have reasoning for chain-of-thought selection
      const cotSelection = selections.find(s => s.technique === TechniqueType.CHAIN_OF_THOUGHT)
      expect(cotSelection?.reason).toMatch(/complex|reasoning|analysis|step/i)
    })

    it('should provide implementation guidance for techniques', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Write a technical documentation',
        targetModel: 'gpt-4',
        domain: 'technical',
        complexityLevel: 'moderate',
        outputFormat: 'structured',
        creativityLevel: 3
      }

      const selections = selector.selectTechniquesWithReasoning(config)

      const domainExpertise = selections.find(s => s.technique === TechniqueType.DOMAIN_EXPERTISE)
      expect(domainExpertise?.implementation).toBeDefined()
      expect(domainExpertise?.implementation.length).toBeGreaterThan(15)
    })
  })

  describe('Technique Combinations and Conflicts', () => {
    it('should avoid conflicting techniques', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Provide creative marketing ideas',
        targetModel: 'gpt-4',
        domain: 'creative',
        complexityLevel: 'simple',
        outputFormat: 'conversational',
        creativityLevel: 8
      }

      const techniques = selector.selectTechniques(config)

      // Should not combine highly creative with overly structured approaches
      if (techniques.includes(TechniqueType.CREATIVE_STIMULUS)) {
        expect(techniques).not.toContain(TechniqueType.SAFETY_CONSTRAINTS)
      }
    })

    it('should select complementary techniques', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Analyze legal document and extract key terms',
        targetModel: 'gpt-4',
        domain: 'legal',
        complexityLevel: 'expert',
        outputFormat: 'structured',
        creativityLevel: 1
      }

      const techniques = selector.selectTechniques(config)

      // These should work well together
      if (techniques.includes(TechniqueType.DOMAIN_EXPERTISE)) {
        expect(techniques).toContain(TechniqueType.STRUCTURED_OUTPUT)
        expect(techniques).toContain(TechniqueType.SAFETY_CONSTRAINTS)
      }
    })

    it('should limit total number of techniques to avoid overcomplexity', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Create a comprehensive business analysis with multiple perspectives',
        targetModel: 'gpt-4',
        domain: 'finance',
        complexityLevel: 'expert',
        outputFormat: 'structured',
        creativityLevel: 5
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques.length).toBeLessThanOrEqual(7) // Reasonable upper limit
      expect(techniques.length).toBeGreaterThanOrEqual(2) // Should have some guidance
    })
  })

  describe('Edge Cases and Error Handling', () => {
    it('should handle missing or invalid configuration gracefully', () => {
      expect(() => selector.selectTechniques({} as any)).toThrow('Invalid configuration')

      expect(() => selector.selectTechniques({
        taskDescription: '',
        targetModel: 'invalid' as any,
        domain: 'general',
        complexityLevel: 'simple',
        outputFormat: 'conversational',
        creativityLevel: 5
      })).toThrow(/task description|target model/)
    })

    it('should provide fallback techniques for unknown domains', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Analyze specialized scientific data',
        targetModel: 'gpt-4',
        domain: 'other',
        complexityLevel: 'complex',
        outputFormat: 'structured',
        creativityLevel: 4
      }

      const techniques = selector.selectTechniques(config)

      expect(techniques.length).toBeGreaterThan(0)
      expect(techniques).toContain(TechniqueType.CHAIN_OF_THOUGHT) // Good general technique
    })

    it('should handle extreme creativity levels appropriately', () => {
      const maxCreativityConfig: PromptConfiguration = {
        taskDescription: 'Create innovative solutions',
        targetModel: 'gpt-4',
        domain: 'creative',
        complexityLevel: 'moderate',
        outputFormat: 'conversational',
        creativityLevel: 10
      }

      const minCreativityConfig: PromptConfiguration = {
        taskDescription: 'Analyze factual data',
        targetModel: 'gpt-4',
        domain: 'finance',
        complexityLevel: 'moderate',
        outputFormat: 'structured',
        creativityLevel: 1
      }

      const maxTechniques = selector.selectTechniques(maxCreativityConfig)
      const minTechniques = selector.selectTechniques(minCreativityConfig)

      expect(maxTechniques).toContain(TechniqueType.CREATIVE_STIMULUS)
      expect(minTechniques).toContain(TechniqueType.SAFETY_CONSTRAINTS)
      expect(minTechniques).not.toContain(TechniqueType.CREATIVE_STIMULUS)
    })
  })

  describe('Performance and Caching', () => {
    it('should cache technique selections for identical configurations', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Standard analysis task',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'moderate',
        outputFormat: 'structured',
        creativityLevel: 5
      }

      const start1 = performance.now()
      const techniques1 = selector.selectTechniques(config)
      const end1 = performance.now()

      const start2 = performance.now()
      const techniques2 = selector.selectTechniques(config)
      const end2 = performance.now()

      expect(techniques1).toEqual(techniques2)
      expect(end2 - start2).toBeLessThan(end1 - start1) // Second call should be faster
    })

    it('should perform technique selection efficiently', () => {
      const config: PromptConfiguration = {
        taskDescription: 'Performance test task with moderate complexity',
        targetModel: 'gpt-4',
        domain: 'general',
        complexityLevel: 'moderate',
        outputFormat: 'structured',
        creativityLevel: 5
      }

      const start = performance.now()
      const techniques = selector.selectTechniques(config)
      const end = performance.now()

      expect(end - start).toBeLessThan(100) // Should be very fast
      expect(techniques.length).toBeGreaterThan(0)
    })
  })
})