// Core types for the application
export interface PromptFormData {
  task: string
  model: string
  domain: string
  complexity: string
  requirements: string
  examples: string
  promptType: 'text' | 'image'
  imageModel?: string
  imageStyle?: string
  composition?: string
  artMedium?: string
}

export interface GeneratedPrompt {
  content: string
  qualityScore: number
  estimatedCost: number
  wordCount: number
  characterCount: number
  techniques: string[]
  createdAt: Date
}

export interface PromptTechnique {
  id: string
  name: string
  description: string
  category: 'reasoning' | 'context' | 'format' | 'performance'
  applicable: boolean
  weight: number
}

export interface OpenAIResponse {
  choices: Array<{
    message: {
      content: string
    }
  }>
  usage?: {
    prompt_tokens: number
    completion_tokens: number
    total_tokens: number
  }
}

export interface QualityMetrics {
  clarity: number
  specificity: number
  completeness: number
  structure: number
  overall: number
}

export type Theme = 'light' | 'dark' | 'system'
export type Model = 'gpt-4' | 'gpt-4-turbo' | 'gpt-3.5-turbo' | 'claude-3' | 'other'
export type Domain = 'general' | 'business' | 'technical' | 'creative' | 'academic' | 'data-analysis' | 'coding'
export type Complexity = 'simple' | 'moderate' | 'complex' | 'expert'

// Image generation specific types
export type ImageModel = 'midjourney-v7' | 'dall-e-3' | 'flux-1-kontext' | 'stable-diffusion' | 'gemini-flash-image'
export type ImageStyle = 'photorealistic' | 'artistic' | 'cartoon' | 'sketch' | 'digital-art' | 'oil-painting' | 'watercolor' | 'ui-mock'
export type Composition = 'portrait' | 'landscape' | 'close-up' | 'wide-shot' | 'birds-eye-view' | 'low-angle' | 'centered' | 'rule-of-thirds'
export type ArtMedium = 'photography' | 'digital-art' | 'oil-painting' | 'watercolor' | 'pencil-sketch' | 'ink-drawing' | 'acrylic' | '3d-render'