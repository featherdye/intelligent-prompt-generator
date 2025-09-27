# Intelligent Prompt Generator

A modern web-based intelligent prompt generator with split-screen UI. Generate optimized prompts using advanced AI techniques powered by multiple AI models through OpenRouter.

## Features

- **Split-Screen Interface**: Configuration form on the left, generated prompt on the right
- **Intelligent Technique Selection**: Automatically chooses optimal prompt engineering techniques
- **15+ Prompt Engineering Techniques**: Zero-shot, few-shot, chain-of-thought, role-based, and more
- **Real-Time Validation**: Form validation with immediate feedback
- **Quality Assessment**: Built-in scoring and improvement recommendations
- **Copy & Download**: Easy prompt copying and file download functionality
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Frontend**: React 18 + TypeScript + Vite
- **Styling**: TailwindCSS + Headless UI
- **State Management**: Zustand + React Hook Form
- **API Integration**: OpenRouter with multiple AI models
- **Testing**: Vitest + React Testing Library + Playwright
- **Deployment**: Vercel

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- OpenRouter API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/featherdye/intelligent-prompt-generator.git
   cd intelligent-prompt-generator
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

### Usage

1. Enter your OpenRouter API key in the secure input field
2. Fill out the configuration form:
   - Describe your task or goal
   - Select target AI model
   - Choose domain and complexity level
   - Add any specific requirements
3. Click "Generate Prompt" to create your optimized prompt
4. Copy or download the generated prompt for use

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run test` - Run unit tests
- `npm run test:e2e` - Run end-to-end tests
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

### Testing

The project follows Test-Driven Development (TDD):

```bash
# Run unit tests
npm run test

# Run E2E tests
npm run test:e2e

# Run all tests
npm run test && npm run test:e2e
```

### Project Structure

```
src/
├── components/          # React components
│   ├── PromptForm/     # Configuration form
│   ├── PromptDisplay/  # Generated prompt display
│   ├── ApiKeyInput/    # Secure API key input
│   └── ...
├── lib/                # Core business logic
│   ├── technique-selector/  # Prompt engineering logic
│   ├── openai-client/      # API integration
│   ├── prompt-config/      # Form validation
│   └── store/              # State management
├── types/              # TypeScript definitions
└── styles/             # CSS and styling
```

## Deployment

The app is configured for deployment on Vercel:

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the configuration
3. Deploy with zero configuration required

## Security

- API keys are stored client-side only (sessionStorage)
- No server-side data persistence
- Input validation and sanitization
- Security headers configured

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`npm run test && npm run test:e2e`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with the Specify framework for systematic feature development
- Implements techniques from the Ultimate LLM Prompt Engineering Guide
- Generated with [Claude Code](https://claude.ai/code)