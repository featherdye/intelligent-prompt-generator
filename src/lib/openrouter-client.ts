import OpenAI from 'openai'
import { IntelligentTechniqueSelector, UserRequirements, Technique } from './technique-selector'

export interface OpenRouterConfig {
  apiKey: string
  model: string
  baseURL?: string
  defaultHeaders?: Record<string, string>
}

export class OpenRouterClient {
  private client: OpenAI
  private techniqueSelector: IntelligentTechniqueSelector

  constructor(config: OpenRouterConfig) {
    this.client = new OpenAI({
      apiKey: config.apiKey,
      baseURL: config.baseURL || 'https://openrouter.ai/api/v1',
      defaultHeaders: {
        'HTTP-Referer': window.location.origin,
        'X-Title': 'Intelligent Prompt Generator',
        ...config.defaultHeaders,
      },
      dangerouslyAllowBrowser: true
    })

    this.techniqueSelector = new IntelligentTechniqueSelector()
  }

  async generateCompletion(
    messages: Array<{ role: 'system' | 'user' | 'assistant'; content: string }>,
    model: string,
    options?: {
      temperature?: number
      maxTokens?: number
    }
  ) {
    try {
      const response = await this.client.chat.completions.create({
        model,
        messages,
        temperature: options?.temperature || 0.7,
        max_tokens: options?.maxTokens || 1000,
        stream: false, // Always disable streaming for simplicity
      })

      return response
    } catch (error) {
      console.error('OpenRouter API Error:', error)
      throw error
    }
  }

  async generatePrompt(taskDescription: string, config: {
    model: string
    domain: string
    complexity: string
    requirements?: string
    examples?: string
    promptType?: 'text' | 'image'
    imageModel?: string
    imageStyle?: string
    composition?: string
    artMedium?: string
  }) {
    // Determine task type from description
    const taskType = this.inferTaskType(taskDescription)

    // Create user requirements
    const requirements: UserRequirements = {
      taskType: config.promptType === 'image' ? 'image_generation' : taskType,
      targetModel: config.model,
      domain: config.domain,
      complexity: config.complexity,
      audience: "general", // Could be extracted from form later
      outputFormat: config.promptType === 'image' ? "image_prompt" : "text",
      creativity: "balanced", // Could be extracted from form later
      safetyLevel: config.domain === "healthcare" || config.domain === "legal" ? "high" : "moderate",
      specificNeeds: config.requirements,
      // Image-specific fields
      promptType: config.promptType,
      imageModel: config.imageModel,
      imageStyle: config.imageStyle,
      composition: config.composition,
      artMedium: config.artMedium
    }

    // Select optimal techniques
    const { techniques, reasoning } = this.techniqueSelector.selectTechniques(requirements)

    console.log('Selected techniques:', techniques.map(t => t))
    console.log('Reasoning:', reasoning)

    // Build optimized prompt using selected techniques
    const optimizedPrompt = this.buildPromptWithTechniques(
      taskDescription,
      config,
      techniques,
      requirements
    )

    console.log('Making OpenRouter API call with optimized prompt...')

    // Now use the optimized prompt to make the actual API call
    const response = await this.generateCompletion([
      { role: 'user', content: optimizedPrompt }
    ], config.model)

    // Type assertion since we know we're not streaming
    const completion = response as any
    const generatedContent = completion.choices[0]?.message?.content || 'No response generated'

    return {
      prompt: generatedContent,
      techniques: techniques.map(t => t),
      reasoning,
      optimizedPrompt // Include the prompt template for debugging
    }
  }

  private inferTaskType(taskDescription: string): string {
    const description = taskDescription.toLowerCase()

    if (description.includes('analy') || description.includes('research') || description.includes('study')) {
      return 'analysis'
    } else if (description.includes('creat') || description.includes('design') || description.includes('brainstorm')) {
      return 'creative'
    } else if (description.includes('reason') || description.includes('solve') || description.includes('logic')) {
      return 'reasoning'
    } else if (description.includes('summar') || description.includes('explain') || description.includes('describe')) {
      return 'explanation'
    } else if (description.includes('write') || description.includes('content') || description.includes('draft')) {
      return 'writing'
    } else {
      return 'general'
    }
  }

  private buildPromptWithTechniques(
    taskDescription: string,
    config: any,
    techniques: Technique[],
    requirements: UserRequirements
  ): string {
    let prompt = ""

    // Role-based prompting (usually first)
    if (techniques.includes(Technique.ROLE_BASED)) {
      prompt += this.addRoleBasedSection(requirements)
    }

    // Domain expertise
    if (techniques.includes(Technique.DOMAIN_EXPERTISE)) {
      prompt += this.addDomainExpertiseSection(requirements)
    }

    // Safety constraints (for sensitive domains)
    if (techniques.includes(Technique.SAFETY_CONSTRAINTS)) {
      prompt += this.addSafetyConstraintsSection(requirements)
    }

    // Task description with context
    prompt += `\n## TASK\n${taskDescription}\n`

    // Additional requirements
    if (config.requirements) {
      prompt += `\n## ADDITIONAL REQUIREMENTS\n${config.requirements}\n`
    }

    // Chain of thought reasoning
    if (techniques.includes(Technique.CHAIN_OF_THOUGHT)) {
      prompt += this.addChainOfThoughtSection()
    }

    // Few-shot examples
    if (techniques.includes(Technique.FEW_SHOT) && config.examples) {
      prompt += this.addFewShotSection(config.examples)
    } else if (techniques.includes(Technique.FEW_SHOT)) {
      prompt += this.addGeneratedExamplesSection(requirements)
    }

    // Structured output
    if (techniques.includes(Technique.STRUCTURED_OUTPUT)) {
      prompt += this.addStructuredOutputSection()
    }

    // Quality controls
    if (techniques.includes(Technique.QUALITY_CONTROLS)) {
      prompt += this.addQualityControlsSection()
    }

    // Image-specific techniques
    if (techniques.includes(Technique.IMAGE_COMPOSITION)) {
      prompt += this.addImageCompositionSection(requirements)
    }

    if (techniques.includes(Technique.IMAGE_STYLE_GUIDANCE)) {
      prompt += this.addImageStyleSection(requirements)
    }

    if (techniques.includes(Technique.IMAGE_TECHNICAL_PARAMS)) {
      prompt += this.addImageTechnicalSection(requirements)
    }

    if (techniques.includes(Technique.IMAGE_NEGATIVE_PROMPTS)) {
      prompt += this.addImageNegativePromptsSection()
    }

    if (techniques.includes(Technique.IMAGE_MODEL_OPTIMIZATION)) {
      prompt += this.addImageModelOptimizationSection(requirements)
    }

    // Model-specific optimizations
    if (techniques.includes(Technique.MODEL_SPECIFIC)) {
      prompt += this.addModelSpecificSection(requirements.targetModel)
    }

    return prompt.trim()
  }

  private addRoleBasedSection(requirements: UserRequirements): string {
    const roleMap: Record<string, string> = {
      'healthcare': 'medical professional with expertise in healthcare documentation and patient privacy',
      'legal': 'legal expert specializing in contract law and document analysis',
      'finance': 'financial analyst with expertise in financial documentation and compliance',
      'technical': 'senior technical expert with deep knowledge of software engineering and technical documentation',
      'creative': 'creative professional with expertise in content creation and innovative problem-solving',
      'academic': 'academic researcher with expertise in scholarly analysis and research methodology',
      'business': 'business consultant with expertise in professional analysis and strategic thinking',
      'data-analysis': 'data scientist with expertise in analytical thinking and data interpretation',
      'coding': 'senior software engineer with expertise in programming and technical problem-solving'
    }

    const role = roleMap[requirements.domain] || 'expert professional'

    return `You are a ${role}. You approach tasks with precision, expertise, and attention to detail appropriate for the ${requirements.domain} domain.\n\n`
  }

  private addDomainExpertiseSection(requirements: UserRequirements): string {
    const domainGuidelines: Record<string, string> = {
      'healthcare': 'Follow HIPAA guidelines and medical best practices. Ensure patient privacy and medical accuracy.',
      'legal': 'Maintain legal accuracy and proper terminology. Consider legal implications and compliance requirements.',
      'finance': 'Apply financial regulations and industry standards. Ensure numerical accuracy and regulatory compliance.',
      'technical': 'Use precise technical terminology and follow industry best practices.',
      'academic': 'Apply scholarly rigor and proper citation practices. Use evidence-based reasoning.',
      'business': 'Focus on practical business value and professional standards.',
      'data-analysis': 'Apply statistical rigor and data validation principles.'
    }

    const guidelines = domainGuidelines[requirements.domain]
    if (guidelines) {
      return `## DOMAIN GUIDELINES\n${guidelines}\n\n`
    }
    return ''
  }

  private addSafetyConstraintsSection(requirements: UserRequirements): string {
    return `## SAFETY AND ETHICAL GUIDELINES
- Prioritize accuracy and avoid speculation
- Respect privacy and confidentiality requirements
- Follow professional and ethical standards for ${requirements.domain}
- If uncertain about any aspect, clearly state limitations

`
  }

  private addChainOfThoughtSection(): string {
    return `\n## APPROACH
Think step by step:
1. First, analyze the requirements and context
2. Consider relevant factors and constraints
3. Develop your response systematically
4. Verify your reasoning and conclusions

`
  }

  private addFewShotSection(examples: string): string {
    return `\n## EXAMPLES FOR REFERENCE\n${examples}\n\n`
  }

  private addGeneratedExamplesSection(requirements: UserRequirements): string {
    // Generate contextual examples based on domain and task type
    const exampleMap: Record<string, string> = {
      'legal': `
## EXAMPLE APPROACH
For legal document analysis:
Input: "Review this contract section..."
Process: 1) Identify key legal concepts, 2) Analyze obligations and rights, 3) Note potential risks
Output: Structured analysis with clear recommendations
`,
      'healthcare': `
## EXAMPLE APPROACH
For healthcare documentation:
Input: "Analyze this medical document..."
Process: 1) Identify medical terminology, 2) Ensure HIPAA compliance, 3) Maintain accuracy
Output: Professional medical analysis with appropriate disclaimers
`
    }

    return exampleMap[requirements.domain] || ''
  }

  private addStructuredOutputSection(): string {
    return `\n## OUTPUT FORMAT
Provide your response in a clear, well-structured format:
- Use headers and bullet points for organization
- Include clear sections for different aspects
- Provide actionable recommendations where appropriate
- Maintain professional formatting throughout

`
  }

  private addQualityControlsSection(): string {
    return `\n## QUALITY ASSURANCE
Before finalizing your response:
- Verify accuracy of all statements
- Ensure completeness of the analysis
- Check for clarity and professional tone
- Confirm all requirements have been addressed

`
  }

  private addModelSpecificSection(model: string): string {
    if (model.includes('gpt-4')) {
      return `\n## OPTIMIZATION NOTE
Leverage your advanced reasoning capabilities for thorough analysis and nuanced understanding.

`
    } else if (model.includes('claude')) {
      return `\n## OPTIMIZATION NOTE
Apply your analytical strengths and attention to detail for comprehensive analysis.

`
    }
    return ''
  }

  // Image-specific prompt building methods
  private addImageCompositionSection(requirements: UserRequirements): string {
    const composition = requirements.composition || 'centered'

    const compositionGuides: Record<string, string> = {
      'rule-of-thirds': 'using rule of thirds composition for dynamic visual balance',
      'centered': 'with centered, symmetrical composition',
      'portrait': 'portrait orientation with vertical framing',
      'landscape': 'landscape orientation with horizontal framing',
      'close-up': 'close-up framing focusing on main subject details',
      'wide-shot': 'wide establishing shot showing full scene context',
      'birds-eye-view': 'aerial birds-eye view perspective from above',
      'low-angle': 'dramatic low-angle perspective looking upward'
    }

    const guide = compositionGuides[composition] || 'with thoughtful composition'

    return `\n## COMPOSITION GUIDANCE\nFrame the image ${guide}. Consider visual balance, leading lines, and focal points to create an engaging composition.\n\n`
  }

  private addImageStyleSection(requirements: UserRequirements): string {
    const style = requirements.imageStyle || 'photorealistic'
    const medium = requirements.artMedium || 'digital-art'

    const styleDescriptions: Record<string, string> = {
      'photorealistic': 'photorealistic style with sharp detail and natural lighting',
      'artistic': 'artistic interpretation with creative liberties and enhanced aesthetics',
      'digital-art': 'digital art style with clean lines and modern techniques',
      'oil-painting': 'oil painting style with rich textures and classical techniques',
      'watercolor': 'watercolor style with soft washes and flowing colors',
      'cartoon': 'cartoon style with stylized features and vibrant colors',
      'sketch': 'sketch style with pencil-like lines and artistic roughness',
      'ui-mock': 'clean UI mockup style with modern interface elements and professional design aesthetics'
    }

    const mediumDetails: Record<string, string> = {
      'photography': 'professional photography techniques',
      'digital-art': 'digital art rendering',
      'oil-painting': 'traditional oil painting medium',
      'watercolor': 'watercolor painting medium',
      'pencil-sketch': 'pencil sketch techniques',
      'ink-drawing': 'ink drawing style',
      'acrylic': 'acrylic painting medium',
      '3d-render': '3D rendered visualization'
    }

    const styleDesc = styleDescriptions[style] || 'artistic style'
    const mediumDesc = mediumDetails[medium] || 'artistic medium'

    return `\n## STYLE AND MEDIUM\nCreate in ${styleDesc} using ${mediumDesc}. Maintain consistency in artistic approach throughout the image.\n\n`
  }

  private addImageTechnicalSection(requirements: UserRequirements): string {
    const imageModel = requirements.imageModel || 'dall-e-3'

    let technicalParams = ''

    if (imageModel === 'midjourney-v7') {
      technicalParams = `
## TECHNICAL PARAMETERS
For optimal Midjourney V7 results:
- High quality rendering with --quality 2
- Consider aspect ratio for composition (--ar 16:9, --ar 4:3, etc.)
- Use --stylize for artistic interpretation control
- Add lighting specifications (golden hour, dramatic, soft diffused)
- Include material details (weathered, polished, textured)

`
    } else if (imageModel === 'stable-diffusion') {
      technicalParams = `
## TECHNICAL PARAMETERS
For optimal Stable Diffusion results:
- Use quality enhancers: "masterpiece, best quality, ultra-detailed, 8k uhd"
- Include professional terminology: "sharp focus, physically-based rendering"
- Specify sampling method preferences in your workflow
- Consider CFG scale for prompt adherence

`
    } else if (imageModel === 'gemini-flash-image') {
      technicalParams = `
## TECHNICAL PARAMETERS
For optimal Gemini Flash Image (nano-banana) results:
- Keep prompts concise for speed optimization (50-150 tokens)
- Front-load important elements in first 50 tokens
- Use clear, descriptive language without complex nested phrases
- Leverage speed advantages for real-time generation

`
    } else {
      technicalParams = `
## TECHNICAL PARAMETERS
Include technical quality specifications:
- High resolution and sharp focus
- Professional rendering quality
- Appropriate lighting and exposure
- Color accuracy and detail enhancement

`
    }

    return technicalParams
  }

  private addImageNegativePromptsSection(): string {
    return `
## NEGATIVE PROMPT GUIDANCE
Suggest negative prompts to avoid common issues:
- Quality issues: "blurry, low quality, distorted, watermark, signature"
- Anatomical problems: "bad anatomy, deformed, mutation, extra limbs"
- Technical flaws: "cropped, out of frame, jpeg artifacts, noise"
- Unwanted elements: "text, watermark, duplicate, malformed"

`
  }

  private addImageModelOptimizationSection(requirements: UserRequirements): string {
    const imageModel = requirements.imageModel || 'dall-e-3'

    const optimizations: Record<string, string> = {
      'dall-e-3': `
## DALL-E 3 OPTIMIZATION
Optimize for DALL-E 3's strengths:
- Use natural, conversational language
- Describe scenes as you would to a human artist
- Focus on mood and atmosphere over technical parameters
- Leverage understanding of context and relationships
- Keep descriptions concise but vivid (1-2 sentences optimal)

`,
      'midjourney-v7': `
## MIDJOURNEY V7 OPTIMIZATION
Optimize for Midjourney V7's capabilities:
- Use specific art style references and artistic terminology
- Include detailed material and texture descriptions
- Leverage advanced parameter system (--ar, --style, --quality)
- Focus on artistic composition and visual storytelling
- Combine descriptive prompts with technical parameters

`,
      'flux-1-kontext': `
## FLUX.1 KONTEXT OPTIMIZATION
Optimize for FLUX.1's technical capabilities:
- Structure prompts clearly: Subject → Setting → Style → Technical
- Use 150-300 tokens for optimal results
- Front-load important details in first part of prompt
- Leverage advanced text rendering and spatial understanding
- Focus on detailed technical specifications

`,
      'stable-diffusion': `
## STABLE DIFFUSION OPTIMIZATION
Optimize for Stable Diffusion's flexibility:
- Use weighted prompt structure with emphasis tokens
- Include comprehensive quality tags
- Utilize negative prompts for quality control
- Specify sampling methods and technical parameters
- Leverage community-developed techniques and models

`,
      'gemini-flash-image': `
## GEMINI FLASH IMAGE (NANO-BANANA) OPTIMIZATION
Optimize for Gemini 2.5 Flash Image's speed and efficiency:
- Keep prompts concise and direct (50-150 tokens optimal)
- Use clear, structured descriptions
- Front-load most important elements
- Leverage multimodal understanding capabilities
- Balance speed with quality requirements

`
    }

    return optimizations[imageModel] || optimizations['dall-e-3']
  }
}

// Utility function to create client instance
export function createOpenRouterClient(apiKey: string): OpenRouterClient {
  return new OpenRouterClient({
    apiKey,
    model: 'openai/gpt-4-turbo', // default model
  })
}