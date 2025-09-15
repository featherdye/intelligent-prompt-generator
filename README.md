# Intelligent Prompt Generator

A DOS-style command-line tool that generates high-quality, optimized prompts using the Ultimate LLM Prompt Engineering Guide principles.

## Features

- **Interactive DOS-style Interface** - Classic menu-driven navigation
- **Intelligent Technique Selection** - Automatically chooses optimal prompt engineering techniques
- **Model-Specific Optimization** - Tailored for GPT-4, Claude-3, and other models
- **Professional Output** - Complete documentation packages with usage instructions
- **Quality Assessment** - Built-in scoring and improvement recommendations
- **Domain Expertise** - Specialized optimization for healthcare, legal, finance, and more

## Quick Start

```bash
python prompt_generator.py
```

Follow the interactive menus to specify your requirements, and the system will generate a comprehensive prompt package.

## System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  DOS Interface  │────│  Requirements    │────│  Technique      │
│  Menu System    │    │  Collector       │    │  Selector       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  LLM Prompt     │────│  Output          │────│  Quality        │
│  Generator      │    │  Generator       │    │  Assessor       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Generated Output

Each prompt package includes:

- **Optimized Prompt** - Ready-to-use, technique-enhanced prompt
- **Model Configuration** - Recommended settings (temperature, max tokens, etc.)
- **Usage Instructions** - Implementation guidelines and best practices  
- **Quality Assessment** - Scoring and improvement recommendations
- **Test Cases** - Validation scenarios and expected outputs
- **Technique Explanation** - Why specific techniques were selected

## Supported Techniques

The system intelligently selects from 15+ prompt engineering techniques:

### Core Techniques
- Zero-Shot Prompting
- Few-Shot Prompting  
- Chain-of-Thought Reasoning
- Self-Consistency

### Advanced Techniques
- Retrieval Augmented Generation
- ReAct (Reasoning and Acting)
- Meta-Prompting
- Generate Knowledge

### Optimization Techniques
- Structured Output Formatting
- Role-Based Prompting
- Domain-Specific Expertise
- Model-Specific Adaptations
- Safety Constraints
- Quality Controls

## Requirements Collection

The system collects comprehensive requirements through an intuitive menu system:

### Basic Information
- Task Type (9 options from classification to creative)
- Target Model (6 major models supported)
- Domain (9 specialized domains)
- Complexity Level (4 levels from simple to expert)

### Advanced Configuration
- Target Audience (beginner to expert)
- Output Format (structured, JSON, markdown, etc.)
- Creativity Level (conservative to highly creative)
- Safety Requirements (standard to critical)
- Specific Requirements (free-form input)

## File Structure

```
├── prompt_generator.py      # Main application with DOS interface
├── technique_selector.py    # Intelligent technique selection engine
├── llm_generator.py        # Prompt generation using templates/LLM
├── output_generator.py     # Professional documentation generator
└── README.md               # This file
```

## Example Output

```markdown
# Analysis Prompt - Healthcare Domain

**Generated**: 2024-12-15 14:30:22
**Quality Score**: 9.2/10 ⭐⭐⭐⭐⭐
**Target Model**: GPT-4

## 🎯 Optimized Prompt

You are a senior medical analyst with 15+ years of clinical experience...
[Complete optimized prompt with integrated techniques]

## 📋 Prompt Metadata
| Attribute | Value |
|-----------|-------|
| Task Type | Analysis |
| Domain | Healthcare |
| Techniques | Chain-of-Thought, Structured Output, Domain Expertise |

[Continues with full documentation...]
```

## Requirements

- Python 3.7+
- Optional: OpenAI API key for AI-enhanced generation
- Install: `pip install openai` (for full AI capabilities)

### Setup for AI Generation
```bash
pip install openai
export OPENAI_API_KEY="your-key-here"  
```

**Note**: System works great without API key too! You'll get solid 8.0+ quality prompts using intelligent rule-based generation.

## Advanced Usage

### Batch Processing
For multiple prompts, run the tool multiple times or modify for batch input.

### API Integration  
The system can be extended to use actual LLM APIs for meta-prompt generation by adding API keys.

### Custom Domains
Add new domains by extending the technique selector's domain mappings.

## Quality Assurance

All generated prompts include:
- **Technique Validation** - Ensures selected techniques are appropriate
- **Quality Scoring** - Multi-dimensional assessment (clarity, completeness, effectiveness)
- **Test Cases** - Validation scenarios for prompt testing
- **Improvement Suggestions** - Actionable recommendations for enhancement

## Contributing

This tool implements the Ultimate LLM Prompt Engineering Guide principles. To contribute:

1. Review the guide for prompt engineering best practices
2. Extend technique selection logic for new use cases
3. Add new output formats or model optimizations
4. Enhance quality assessment metrics

## License

Open source - use and modify as needed for your prompt engineering projects.

---

*Generated prompts are ready for production use and demonstrate expert-level prompt engineering techniques.*