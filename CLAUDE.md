# Claude Code Context: Web-Based Prompt Generator

## Project Overview
Converting existing CLI prompt generator to web application with split-screen UI hosted on Vercel with OpenAI API integration.

## Current Feature: Web Application Conversion (001-convert-cli-prompt)
- **Branch**: `001-convert-cli-prompt`
- **Status**: Implementation planning complete
- **Goal**: Transform DOS-style CLI tool into modern web app

## Technology Stack
- **Frontend**: React 18 + TypeScript + Vite
- **Styling**: TailwindCSS + Headless UI
- **State**: Zustand + React Hook Form
- **API**: OpenAI JavaScript SDK
- **Testing**: Vitest + React Testing Library + Playwright
- **Deployment**: Vercel static hosting

## Architecture Principles
- **Library-First**: Core logic as reusable libraries
- **Client-Side Only**: No server-side persistence
- **Test-First**: RED-GREEN-Refactor cycle enforced
- **Simple**: Single project, minimal abstractions

## Key Components

### Core Libraries
- `prompt-config`: Form handling + validation
- `technique-selector`: Port from CLI (technique selection logic)
- `openai-client`: API integration layer
- `ui-components`: Reusable React components

### Data Models
- **PromptConfiguration**: User form inputs
- **GeneratedPrompt**: AI-optimized output with metadata
- **TechniqueSelection**: Applied engineering techniques
- **QualityAssessment**: Multi-dimensional scoring

### UI Structure
```
src/
├── components/          # React components
│   ├── PromptForm/     # Left panel configuration form
│   ├── PromptDisplay/  # Right panel prompt output
│   └── Layout/         # App shell and routing
├── lib/                # Core business logic
│   ├── prompt-config/  # Form state and validation
│   ├── technique-selector/  # Port from CLI version
│   ├── openai-client/  # API integration
│   └── utils/          # Shared utilities
└── types/              # TypeScript definitions
```

## Recent Implementation Progress

### Completed Phases
- ✅ **Phase 0**: Technology research and decisions
- ✅ **Phase 1**: Data models, API contracts, quickstart guide

### Current Status
- 📋 Ready for **Phase 2**: Task generation (/tasks command)
- 📋 Waiting for task breakdown and implementation

### Key Artifacts Generated
- `specs/001-convert-cli-prompt/research.md` - Technology decisions
- `specs/001-convert-cli-prompt/data-model.md` - Entity definitions
- `specs/001-convert-cli-prompt/contracts/` - API contracts & schemas
- `specs/001-convert-cli-prompt/quickstart.md` - User journey guide

## Important Context from CLI Version

### Existing Assets to Port
- `technique_selector.py` - 15+ prompt engineering techniques
- `llm_generator.py` - OpenAI integration patterns
- `prompt_generator.py` - Form structure and validation logic
- Quality assessment algorithms and scoring

### Technique Selection Logic
- **Zero-Shot**: Simple tasks, clear instructions
- **Few-Shot**: Examples needed for pattern recognition
- **Chain-of-Thought**: Complex reasoning tasks
- **Role-Based**: Domain expertise required
- **Structured Output**: Formatted responses needed

## Development Guidelines

### Testing Strategy
- **Contract Tests**: API integration points
- **Integration Tests**: Complete user flows
- **Unit Tests**: Component and utility functions
- **E2E Tests**: Full application workflows

### Code Style
- TypeScript strict mode enabled
- ESLint + Prettier for consistency
- Functional components with hooks
- Custom hooks for business logic

### Performance Targets
- <2s prompt generation time
- <1s UI responsiveness
- <150KB gzipped bundle size
- 95%+ user satisfaction scores

## Security Considerations
- Client-side API key storage (sessionStorage only)
- Input validation and sanitization
- Rate limiting awareness and error handling
- No server-side data persistence

## Deployment
- **Target**: Vercel static hosting
- **Build**: Vite production build to `dist/`
- **Config**: `vercel.json` for SPA routing
- **Domain**: Custom domain planned

---

*Last Updated: 2025-09-15 | Feature: 001-convert-cli-prompt | Phase: Planning Complete*