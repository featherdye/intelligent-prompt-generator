import { create } from 'zustand'
import { PromptFormData as PromptFormDataType } from '../types'

// Local storage utilities
const STORAGE_KEY = 'prompt_history'
const API_KEY_STORAGE_KEY = 'openrouter_api_key'

const saveToLocalStorage = (history: GeneratedPrompt[]) => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history))
  } catch (error) {
    console.warn('Failed to save prompt history to localStorage:', error)
  }
}

const loadFromLocalStorage = (): GeneratedPrompt[] => {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved) {
      const parsed = JSON.parse(saved)
      // Convert createdAt strings back to Date objects
      return parsed.map((prompt: any) => ({
        ...prompt,
        createdAt: new Date(prompt.createdAt)
      }))
    }
  } catch (error) {
    console.warn('Failed to load prompt history from localStorage:', error)
  }
  return []
}

const saveApiKeyToLocalStorage = (apiKey: string) => {
  try {
    localStorage.setItem(API_KEY_STORAGE_KEY, apiKey)
  } catch (error) {
    console.warn('Failed to save API key to localStorage:', error)
  }
}

const loadApiKeyFromLocalStorage = (): string => {
  try {
    return localStorage.getItem(API_KEY_STORAGE_KEY) || ''
  } catch (error) {
    console.warn('Failed to load API key from localStorage:', error)
  }
  return ''
}

const clearApiKeyFromLocalStorage = () => {
  try {
    localStorage.removeItem(API_KEY_STORAGE_KEY)
  } catch (error) {
    console.warn('Failed to clear API key from localStorage:', error)
  }
}

const generateId = () => {
  return Date.now().toString(36) + Math.random().toString(36).substr(2)
}

export type PromptFormData = PromptFormDataType

export interface GeneratedPrompt {
  id: string
  content: string
  originalTask: string
  promptType: 'text' | 'image'
  formData: PromptFormData
  qualityScore: number
  estimatedCost: number
  wordCount: number
  characterCount: number
  techniques: string[]
  createdAt: Date
}

interface PromptStore {
  // API Key management
  apiKey: string
  setApiKey: (key: string) => void
  clearApiKey: () => void
  hasApiKey: () => boolean

  // Form data
  formData: PromptFormData
  updateFormData: (data: Partial<PromptFormData>) => void
  resetFormData: () => void

  // Generated prompt
  generatedPrompt: GeneratedPrompt | null
  setGeneratedPrompt: (prompt: GeneratedPrompt) => void
  clearGeneratedPrompt: () => void

  // UI state
  isGenerating: boolean
  setIsGenerating: (loading: boolean) => void

  // History
  promptHistory: GeneratedPrompt[]
  addToHistory: (prompt: GeneratedPrompt) => void
  loadPromptFromHistory: (id: string) => void
  deleteFromHistory: (id: string) => void
  clearHistory: () => void
  searchHistory: (query: string) => GeneratedPrompt[]

  // History panel UI state
  isHistoryPanelVisible: boolean
  setHistoryPanelVisible: (visible: boolean) => void

  // Settings
  settings: {
    theme: 'light' | 'dark' | 'system'
    autoSave: boolean
    showQualityMetrics: boolean
  }
  updateSettings: (settings: Partial<PromptStore['settings']>) => void
}

const initialFormData: PromptFormData = {
  task: '',
  model: 'gpt-4',
  domain: 'general',
  complexity: 'moderate',
  requirements: '',
  examples: '',
  promptType: 'text',
  imageModel: 'dall-e-3',
  imageStyle: 'photorealistic',
  composition: 'centered',
  artMedium: 'digital-art'
}

const initialSettings = {
  theme: 'system' as const,
  autoSave: true,
  showQualityMetrics: true
}

export const usePromptStore = create<PromptStore>((set, get) => ({
  // API Key management
  apiKey: loadApiKeyFromLocalStorage(),
  setApiKey: (key) => {
    set({ apiKey: key })
    saveApiKeyToLocalStorage(key)
  },
  clearApiKey: () => {
    set({ apiKey: '' })
    clearApiKeyFromLocalStorage()
  },
  hasApiKey: () => {
    const key = get().apiKey
    return key.length > 0 && key.startsWith('sk-or-v1-')
  },

  // Form data
  formData: initialFormData,
  updateFormData: (data) =>
    set((state) => ({
      formData: { ...state.formData, ...data }
    })),
  resetFormData: () => set({ formData: initialFormData }),

  // Generated prompt
  generatedPrompt: null,
  setGeneratedPrompt: (prompt) => {
    // Add ID if not present
    const promptWithId = {
      ...prompt,
      id: prompt.id || generateId()
    }
    set({ generatedPrompt: promptWithId })
    get().addToHistory(promptWithId)
  },
  clearGeneratedPrompt: () => set({ generatedPrompt: null }),

  // UI state
  isGenerating: false,
  setIsGenerating: (loading) => set({ isGenerating: loading }),

  // History
  promptHistory: loadFromLocalStorage(),
  addToHistory: (prompt) => {
    const newHistory = [prompt, ...get().promptHistory.slice(0, 49)] // Keep last 50
    set({ promptHistory: newHistory })
    saveToLocalStorage(newHistory)
  },
  loadPromptFromHistory: (id) => {
    const prompt = get().promptHistory.find(p => p.id === id)
    if (prompt) {
      set({
        generatedPrompt: prompt,
        formData: prompt.formData
      })
    }
  },
  deleteFromHistory: (id) => {
    const newHistory = get().promptHistory.filter(p => p.id !== id)
    set({ promptHistory: newHistory })
    saveToLocalStorage(newHistory)
  },
  clearHistory: () => {
    set({ promptHistory: [] })
    saveToLocalStorage([])
  },
  searchHistory: (query) => {
    const lowerQuery = query.toLowerCase()
    return get().promptHistory.filter(prompt =>
      prompt.originalTask.toLowerCase().includes(lowerQuery) ||
      prompt.content.toLowerCase().includes(lowerQuery) ||
      prompt.techniques.some(t => t.toLowerCase().includes(lowerQuery))
    )
  },

  // History panel UI state
  isHistoryPanelVisible: true,
  setHistoryPanelVisible: (visible) => set({ isHistoryPanelVisible: visible }),

  // Settings
  settings: initialSettings,
  updateSettings: (newSettings) =>
    set((state) => ({
      settings: { ...state.settings, ...newSettings }
    }))
}))