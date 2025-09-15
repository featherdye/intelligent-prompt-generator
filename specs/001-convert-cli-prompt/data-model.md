# Data Model: Web-Based Prompt Generator

## Core Entities

### PromptConfiguration
Represents user input for prompt generation configuration.

**Fields**:
- `taskDescription`: string (required) - Free-form description of the task/goal
- `targetModel`: 'gpt-4' | 'gpt-3.5-turbo' | 'claude-3' | 'claude-sonnet' | 'gemini-pro' | 'custom'
- `domain`: 'general' | 'healthcare' | 'legal' | 'finance' | 'education' | 'creative' | 'technical' | 'research' | 'other'
- `complexityLevel`: 'simple' | 'moderate' | 'complex' | 'expert'
- `specificRequirements`: string (optional) - Additional context or constraints
- `outputFormat`: 'structured' | 'conversational' | 'json' | 'markdown' | 'custom'
- `creativityLevel`: number (1-10) - Controls creativity vs precision balance

**Validation Rules**:
- taskDescription: minimum 10 characters, maximum 2000 characters
- targetModel: must be from predefined enum
- domain: must be from predefined enum
- complexityLevel: must be from predefined enum
- specificRequirements: maximum 1000 characters
- creativityLevel: integer between 1 and 10

**State Transitions**:
- Draft → Validating → Valid/Invalid
- Valid → Submitting → Success/Error

### GeneratedPrompt
Represents the AI-optimized prompt output.

**Fields**:
- `id`: string - Unique identifier for the generated prompt
- `content`: string - The optimized prompt text
- `metadata`: PromptMetadata - Additional information about the prompt
- `quality`: QualityAssessment - Quality scores and analysis
- `techniques`: TechniqueSelection[] - Applied prompt engineering techniques
- `generatedAt`: Date - Timestamp of generation
- `model`: string - Model used for generation
- `configuration`: PromptConfiguration - Original configuration used

**Relationships**:
- One-to-one with PromptConfiguration
- One-to-many with TechniqueSelection
- One-to-one with QualityAssessment

### PromptMetadata
Additional context and information about the generated prompt.

**Fields**:
- `wordCount`: number - Total words in the prompt
- `estimatedTokens`: number - Approximate token count for target model
- `readabilityScore`: number (1-10) - How clear and readable the prompt is
- `completenessScore`: number (1-10) - How well it covers the requirements
- `usageInstructions`: string - How to use the prompt effectively
- `testScenarios`: string[] - Suggested test cases for validation

### TechniqueSelection
Represents a prompt engineering technique applied to the prompt.

**Fields**:
- `technique`: TechniqueType - The specific technique used
- `reason`: string - Why this technique was selected
- `implementation`: string - How it was implemented in the prompt
- `confidence`: number (0-1) - Confidence in technique selection

**Technique Types**:
```typescript
enum TechniqueType {
  ZERO_SHOT = 'zero_shot',
  FEW_SHOT = 'few_shot',
  CHAIN_OF_THOUGHT = 'chain_of_thought',
  SELF_CONSISTENCY = 'self_consistency',
  GENERATE_KNOWLEDGE = 'generate_knowledge',
  RETRIEVAL_AUGMENTED = 'retrieval_augmented',
  REACT = 'react',
  REFLEXION = 'reflexion',
  META_PROMPTING = 'meta_prompting',
  STRUCTURED_OUTPUT = 'structured_output',
  ROLE_BASED = 'role_based',
  SAFETY_CONSTRAINTS = 'safety_constraints',
  DOMAIN_EXPERTISE = 'domain_expertise',
  MODEL_SPECIFIC = 'model_specific',
  CREATIVE_STIMULUS = 'creative_stimulus'
}
```

### QualityAssessment
Comprehensive quality evaluation of the generated prompt.

**Fields**:
- `overallScore`: number (1-10) - Combined quality score
- `clarity`: number (1-10) - How clear and unambiguous the prompt is
- `completeness`: number (1-10) - How well it addresses all requirements
- `effectiveness`: number (1-10) - Predicted effectiveness for the task
- `specificity`: number (1-10) - Level of detail and precision
- `feedback`: string[] - Specific improvement suggestions
- `strengths`: string[] - Identified strong points
- `weaknesses`: string[] - Areas for improvement

### APIKey
Client-side API key management.

**Fields**:
- `value`: string - The actual API key (stored securely)
- `isValid`: boolean - Whether the key format is valid
- `isVerified`: boolean - Whether the key has been tested with API
- `masked`: string - Display-safe version (e.g., "sk-proj-***...***")
- `lastUsed`: Date | null - When the key was last used successfully

**Security Rules**:
- Never logged or persisted to localStorage
- Stored only in sessionStorage
- Cleared on tab close or explicit user action
- Validated before first use

### ApplicationState
Global application state managed by Zustand.

**Fields**:
- `apiKey`: APIKey | null - Current API key
- `currentConfiguration`: PromptConfiguration | null - Active form data
- `generatedPrompt`: GeneratedPrompt | null - Latest generated prompt
- `isGenerating`: boolean - Loading state for prompt generation
- `error`: string | null - Last error message
- `history`: GeneratedPrompt[] - Recent prompt generations (session only)

**State Actions**:
- `setApiKey(key: string)` - Store and validate API key
- `clearApiKey()` - Remove API key from state
- `updateConfiguration(config: Partial<PromptConfiguration>)` - Update form data
- `generatePrompt(config: PromptConfiguration)` - Trigger prompt generation
- `clearError()` - Clear error state
- `addToHistory(prompt: GeneratedPrompt)` - Add to history

## Data Flow

### Form Submission Flow
1. User inputs → PromptConfiguration (with validation)
2. PromptConfiguration + APIKey → OpenAI API request
3. API response → GeneratedPrompt creation
4. GeneratedPrompt → TechniqueSelection analysis
5. Final prompt → QualityAssessment scoring
6. Complete GeneratedPrompt → ApplicationState + History

### Error Handling Flow
1. API errors → ApplicationState.error
2. Validation errors → Form field errors
3. Network errors → Retry mechanism with exponential backoff
4. Rate limit errors → User guidance and retry suggestions

### State Persistence
- **Session Storage**: APIKey (cleared on tab close)
- **Memory Only**: All other state (no persistence)
- **No Server State**: Completely client-side application

## Validation Schema

### PromptConfiguration Validation
```typescript
const configSchema = {
  taskDescription: {
    required: true,
    minLength: 10,
    maxLength: 2000,
    pattern: /^[a-zA-Z0-9\s\.,!?;:'"()-]+$/
  },
  targetModel: {
    required: true,
    enum: ['gpt-4', 'gpt-3.5-turbo', 'claude-3', 'claude-sonnet', 'gemini-pro', 'custom']
  },
  domain: {
    required: true,
    enum: ['general', 'healthcare', 'legal', 'finance', 'education', 'creative', 'technical', 'research', 'other']
  },
  complexityLevel: {
    required: true,
    enum: ['simple', 'moderate', 'complex', 'expert']
  },
  specificRequirements: {
    required: false,
    maxLength: 1000
  },
  creativityLevel: {
    required: true,
    type: 'integer',
    min: 1,
    max: 10
  }
}
```

### APIKey Validation
```typescript
const apiKeySchema = {
  value: {
    required: true,
    pattern: /^sk-[a-zA-Z0-9-_]{40,}$/,
    minLength: 45
  }
}
```

## TypeScript Definitions

```typescript
// Export types for use across the application
export interface PromptConfiguration {
  taskDescription: string;
  targetModel: TargetModel;
  domain: Domain;
  complexityLevel: ComplexityLevel;
  specificRequirements?: string;
  outputFormat: OutputFormat;
  creativityLevel: number;
}

export interface GeneratedPrompt {
  id: string;
  content: string;
  metadata: PromptMetadata;
  quality: QualityAssessment;
  techniques: TechniqueSelection[];
  generatedAt: Date;
  model: string;
  configuration: PromptConfiguration;
}

export interface ApplicationState {
  apiKey: APIKey | null;
  currentConfiguration: PromptConfiguration | null;
  generatedPrompt: GeneratedPrompt | null;
  isGenerating: boolean;
  error: string | null;
  history: GeneratedPrompt[];
}
```

---

**Data Model Complete**: All entities, relationships, and validation rules defined
**Next**: API contracts and integration patterns