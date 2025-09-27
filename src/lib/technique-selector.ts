// Technique Selection Engine - TypeScript Port
// Based on the Ultimate LLM Prompt Engineering Guide

export enum Technique {
  ZERO_SHOT = "zero_shot",
  FEW_SHOT = "few_shot",
  CHAIN_OF_THOUGHT = "chain_of_thought",
  SELF_CONSISTENCY = "self_consistency",
  GENERATE_KNOWLEDGE = "generate_knowledge",
  RETRIEVAL_AUGMENTED = "retrieval_augmented",
  REACT = "react",
  REFLEXION = "reflexion",
  META_PROMPTING = "meta_prompting",
  STRUCTURED_OUTPUT = "structured_output",
  ROLE_BASED = "role_based",
  SAFETY_CONSTRAINTS = "safety_constraints",
  DOMAIN_EXPERTISE = "domain_expertise",
  MODEL_SPECIFIC = "model_specific",
  CREATIVE_STIMULUS = "creative_stimulus",
  QUALITY_CONTROLS = "quality_controls",
  // Image-specific techniques
  IMAGE_COMPOSITION = "image_composition",
  IMAGE_STYLE_GUIDANCE = "image_style_guidance",
  IMAGE_TECHNICAL_PARAMS = "image_technical_params",
  IMAGE_NEGATIVE_PROMPTS = "image_negative_prompts",
  IMAGE_MODEL_OPTIMIZATION = "image_model_optimization"
}

export interface TechniqueInfo {
  name: string
  description: string
  bestFor: string[]
  modelCompatibility: string[]
  complexityRequirement: string
  tokenCost: string
  combinesWellWith: string[]
  implementation: string
}

export interface UserRequirements {
  taskType: string
  targetModel: string
  domain: string
  complexity: string
  audience: string
  outputFormat: string
  creativity: string
  safetyLevel: string
  specificNeeds?: string
  // Image-specific fields
  promptType?: 'text' | 'image'
  imageModel?: string
  imageStyle?: string
  composition?: string
  artMedium?: string
}

export class TechniqueDatabase {
  techniques: Record<Technique, TechniqueInfo> = {
    [Technique.ZERO_SHOT]: {
      name: "Zero-Shot Prompting",
      description: "Direct instruction without examples, relies on model's pre-trained knowledge",
      bestFor: ["simple", "general", "quick"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["role_based", "structured_output"],
      implementation: "Provide clear, direct instructions without examples."
    },

    [Technique.FEW_SHOT]: {
      name: "Few-Shot Prompting",
      description: "Provides examples to guide model behavior and output format",
      bestFor: ["standardized", "specific_format", "pattern_recognition"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "medium",
      combinesWellWith: ["structured_output", "domain_expertise"],
      implementation: "Include 2-3 concrete examples showing input-output pairs in the exact format desired."
    },

    [Technique.CHAIN_OF_THOUGHT]: {
      name: "Chain-of-Thought Reasoning",
      description: "Breaks down complex problems into step-by-step reasoning",
      bestFor: ["reasoning", "analysis", "complex", "mathematical"],
      modelCompatibility: ["gpt-4", "claude-3", "large_models"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["self_consistency", "structured_output"],
      implementation: "Add 'Think step by step' and break down the reasoning process into numbered steps."
    },

    [Technique.SELF_CONSISTENCY]: {
      name: "Self-Consistency",
      description: "Generates multiple reasoning paths and selects most consistent answer",
      bestFor: ["reasoning", "complex", "high_accuracy"],
      modelCompatibility: ["gpt-4", "claude-3"],
      complexityRequirement: "complex",
      tokenCost: "high",
      combinesWellWith: ["chain_of_thought"],
      implementation: "Ask the model to consider multiple approaches and verify consistency."
    },

    [Technique.GENERATE_KNOWLEDGE]: {
      name: "Generate Knowledge Prompting",
      description: "Generates relevant background knowledge before making predictions",
      bestFor: ["analysis", "research", "knowledge_intensive"],
      modelCompatibility: ["any"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["chain_of_thought", "retrieval_augmented"],
      implementation: "First ask to generate relevant background knowledge, then proceed with the main task."
    },

    [Technique.RETRIEVAL_AUGMENTED]: {
      name: "Retrieval Augmented Generation",
      description: "Enhances responses with external knowledge sources",
      bestFor: ["knowledge_intensive", "factual", "research"],
      modelCompatibility: ["any"],
      complexityRequirement: "moderate",
      tokenCost: "high",
      combinesWellWith: ["generate_knowledge", "structured_output"],
      implementation: "Provide relevant context and sources, then ask to use this information in the response."
    },

    [Technique.REACT]: {
      name: "ReAct (Reasoning and Acting)",
      description: "Combines reasoning traces with external tool interactions",
      bestFor: ["tool_use", "dynamic", "interactive"],
      modelCompatibility: ["gpt-4", "claude-3"],
      complexityRequirement: "complex",
      tokenCost: "high",
      combinesWellWith: ["chain_of_thought"],
      implementation: "Structure as Thought -> Action -> Observation cycles with explicit reasoning."
    },

    [Technique.STRUCTURED_OUTPUT]: {
      name: "Structured Output Formatting",
      description: "Ensures consistent, well-formatted responses",
      bestFor: ["json", "structured", "markdown", "standardized"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["few_shot", "quality_controls"],
      implementation: "Specify exact output format with clear structure (JSON, markdown, numbered lists, etc.)."
    },

    [Technique.ROLE_BASED]: {
      name: "Role-Based Prompting",
      description: "Assigns specific expertise roles to guide responses",
      bestFor: ["domain_specific", "expert_level", "professional"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["domain_expertise", "quality_controls"],
      implementation: "Start with 'You are a [specific expert role]' and define expertise clearly."
    },

    [Technique.SAFETY_CONSTRAINTS]: {
      name: "Safety and Ethical Guidelines",
      description: "Implements safety measures and ethical considerations",
      bestFor: ["healthcare", "legal", "sensitive_domains"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["domain_expertise", "quality_controls"],
      implementation: "Include explicit safety guidelines and ethical considerations relevant to the domain."
    },

    [Technique.DOMAIN_EXPERTISE]: {
      name: "Domain-Specific Optimization",
      description: "Tailors prompts for specific professional domains",
      bestFor: ["healthcare", "legal", "finance", "technical"],
      modelCompatibility: ["any"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["role_based", "safety_constraints"],
      implementation: "Include domain-specific terminology, standards, and best practices."
    },

    [Technique.MODEL_SPECIFIC]: {
      name: "Model-Specific Adaptations",
      description: "Optimizes prompts for specific model architectures",
      bestFor: ["performance", "efficiency", "model_optimization"],
      modelCompatibility: ["specific"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["any"],
      implementation: "Adapt language and structure for the specific model's strengths and preferences."
    },

    [Technique.CREATIVE_STIMULUS]: {
      name: "Creative Stimulus Techniques",
      description: "Encourages innovative and creative responses",
      bestFor: ["creative", "brainstorming", "innovative"],
      modelCompatibility: ["any"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["few_shot", "structured_output"],
      implementation: "Encourage exploration of multiple perspectives and creative approaches."
    },

    [Technique.QUALITY_CONTROLS]: {
      name: "Quality Control Measures",
      description: "Implements verification and quality assurance steps",
      bestFor: ["high_accuracy", "professional", "critical"],
      modelCompatibility: ["any"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["any"],
      implementation: "Include self-verification steps and quality criteria in the prompt."
    },

    [Technique.REFLEXION]: {
      name: "Reflexion",
      description: "Self-reflection and iterative improvement of responses",
      bestFor: ["complex", "iterative", "self_improvement"],
      modelCompatibility: ["gpt-4", "claude-3"],
      complexityRequirement: "complex",
      tokenCost: "high",
      combinesWellWith: ["chain_of_thought", "self_consistency"],
      implementation: "Ask the model to reflect on and improve its initial response."
    },

    [Technique.META_PROMPTING]: {
      name: "Meta-Prompting",
      description: "Uses prompts to generate or improve other prompts",
      bestFor: ["prompt_optimization", "recursive", "meta_tasks"],
      modelCompatibility: ["gpt-4", "claude-3"],
      complexityRequirement: "complex",
      tokenCost: "high",
      combinesWellWith: ["self_consistency", "quality_controls"],
      implementation: "Use the model to optimize the prompt itself through iteration."
    },

    // Image-specific techniques
    [Technique.IMAGE_COMPOSITION]: {
      name: "Image Composition Guidance",
      description: "Provides specific composition and framing instructions for image generation",
      bestFor: ["image_generation", "visual_composition", "artistic_control"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["image_style_guidance", "image_technical_params"],
      implementation: "Include specific composition terms like 'rule of thirds', 'centered', 'close-up', etc."
    },

    [Technique.IMAGE_STYLE_GUIDANCE]: {
      name: "Image Style Specification",
      description: "Defines artistic style, medium, and aesthetic approach for image generation",
      bestFor: ["image_generation", "artistic_style", "medium_specification"],
      modelCompatibility: ["any"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["image_composition", "quality_controls"],
      implementation: "Specify art style, medium (oil painting, digital art, photography) and aesthetic approach."
    },

    [Technique.IMAGE_TECHNICAL_PARAMS]: {
      name: "Image Technical Parameters",
      description: "Includes technical specifications like quality, resolution, and rendering details",
      bestFor: ["image_generation", "technical_control", "quality_optimization"],
      modelCompatibility: ["stable_diffusion", "midjourney"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["image_model_optimization"],
      implementation: "Add technical quality terms and model-specific parameters for optimal output."
    },

    [Technique.IMAGE_NEGATIVE_PROMPTS]: {
      name: "Image Negative Prompting",
      description: "Specifies what to avoid in image generation for quality control",
      bestFor: ["image_generation", "quality_control", "stable_diffusion"],
      modelCompatibility: ["stable_diffusion"],
      complexityRequirement: "simple",
      tokenCost: "low",
      combinesWellWith: ["quality_controls", "image_technical_params"],
      implementation: "Include negative prompt suggestions to avoid common image generation issues."
    },

    [Technique.IMAGE_MODEL_OPTIMIZATION]: {
      name: "Image Model-Specific Optimization",
      description: "Tailors prompts for specific image generation model capabilities and syntax",
      bestFor: ["image_generation", "model_optimization", "performance"],
      modelCompatibility: ["specific"],
      complexityRequirement: "moderate",
      tokenCost: "medium",
      combinesWellWith: ["image_technical_params", "image_style_guidance"],
      implementation: "Optimize prompt structure and parameters for the target image generation model."
    }
  }
}

export class IntelligentTechniqueSelector {
  private db = new TechniqueDatabase()

  selectTechniques(requirements: UserRequirements): {
    techniques: Technique[],
    reasoning: Record<string, string>
  } {
    const selected = new Set<Technique>()
    const reasoning: Record<string, string> = {}

    // Core technique selection
    const coreTechniques = this.selectCoreTechniques(requirements)
    coreTechniques.forEach(t => selected.add(t))
    Object.assign(reasoning, this.explainCoreSelection(requirements, coreTechniques))

    // Domain-specific additions
    const domainTechniques = this.selectDomainTechniques(requirements)
    domainTechniques.forEach(t => selected.add(t))
    Object.assign(reasoning, this.explainDomainSelection(requirements, domainTechniques))

    // Model-specific optimizations
    const modelTechniques = this.selectModelTechniques(requirements)
    modelTechniques.forEach(t => selected.add(t))
    Object.assign(reasoning, this.explainModelSelection(requirements, modelTechniques))

    // Quality and safety enhancements
    const qualityTechniques = this.selectQualityTechniques(requirements)
    qualityTechniques.forEach(t => selected.add(t))
    Object.assign(reasoning, this.explainQualitySelection(requirements, qualityTechniques))

    // Image-specific techniques
    if (requirements.promptType === 'image') {
      const imageTechniques = this.selectImageTechniques(requirements)
      imageTechniques.forEach(t => selected.add(t))
      Object.assign(reasoning, this.explainImageSelection(requirements, imageTechniques))
    }

    // Remove conflicts
    const resolved = this.resolveConflicts(selected)

    return {
      techniques: Array.from(resolved),
      reasoning
    }
  }

  private selectCoreTechniques(req: UserRequirements): Set<Technique> {
    const techniques = new Set<Technique>()

    // Always include role-based prompting
    techniques.add(Technique.ROLE_BASED)

    // Complexity-based selection
    if (req.complexity === "simple") {
      techniques.add(Technique.ZERO_SHOT)
    } else if (req.complexity === "moderate") {
      techniques.add(Technique.FEW_SHOT)
      if (req.taskType === "reasoning" || req.taskType === "analysis") {
        techniques.add(Technique.CHAIN_OF_THOUGHT)
      }
    } else { // complex or expert
      techniques.add(Technique.CHAIN_OF_THOUGHT)
      if (req.taskType === "reasoning" || req.taskType === "analysis") {
        techniques.add(Technique.SELF_CONSISTENCY)
      }
    }

    // Task-type specific selections
    if (req.taskType === "creative") {
      techniques.add(Technique.CREATIVE_STIMULUS)
    } else if (req.taskType === "analysis" || req.taskType === "research") {
      techniques.add(Technique.GENERATE_KNOWLEDGE)
    }

    // Output format considerations
    if (["structured", "json", "markdown"].includes(req.outputFormat)) {
      techniques.add(Technique.STRUCTURED_OUTPUT)
    }

    return techniques
  }

  private selectDomainTechniques(req: UserRequirements): Set<Technique> {
    const techniques = new Set<Technique>()

    // High-stakes domains need safety and expertise
    if (["healthcare", "legal", "finance"].includes(req.domain)) {
      techniques.add(Technique.DOMAIN_EXPERTISE)
      techniques.add(Technique.SAFETY_CONSTRAINTS)
      techniques.add(Technique.QUALITY_CONTROLS)
    }

    // Knowledge-intensive domains
    if (["healthcare", "legal", "academic", "data-analysis"].includes(req.domain)) {
      techniques.add(Technique.RETRIEVAL_AUGMENTED)
    }

    return techniques
  }

  private selectModelTechniques(req: UserRequirements): Set<Technique> {
    const techniques = new Set<Technique>()

    // Always include model-specific adaptations
    techniques.add(Technique.MODEL_SPECIFIC)

    // Advanced techniques for capable models
    if (req.targetModel.includes("gpt-4") || req.targetModel.includes("claude-3")) {
      if (req.complexity === "complex" || req.complexity === "expert") {
        techniques.add(Technique.REACT)
      }
    }

    return techniques
  }

  private selectQualityTechniques(req: UserRequirements): Set<Technique> {
    const techniques = new Set<Technique>()

    // High safety requirements
    if (req.safetyLevel === "high" || req.safetyLevel === "critical") {
      techniques.add(Technique.SAFETY_CONSTRAINTS)
      techniques.add(Technique.QUALITY_CONTROLS)
    }

    // Expert audience needs quality controls
    if (req.audience === "expert") {
      techniques.add(Technique.QUALITY_CONTROLS)
    }

    return techniques
  }

  private resolveConflicts(techniques: Set<Technique>): Set<Technique> {
    // Zero-shot conflicts with few-shot
    if (techniques.has(Technique.ZERO_SHOT) && techniques.has(Technique.FEW_SHOT)) {
      techniques.delete(Technique.ZERO_SHOT) // Few-shot is more specific
    }

    return techniques
  }

  private explainCoreSelection(req: UserRequirements, techniques: Set<Technique>): Record<string, string> {
    const explanations: Record<string, string> = {}

    techniques.forEach(tech => {
      switch (tech) {
        case Technique.ROLE_BASED:
          explanations[tech] = "Provides clear expertise context and authority"
          break
        case Technique.CHAIN_OF_THOUGHT:
          explanations[tech] = `Essential for ${req.taskType} tasks requiring step-by-step reasoning`
          break
        case Technique.FEW_SHOT:
          explanations[tech] = `Guides output format and style for ${req.complexity} complexity`
          break
        case Technique.ZERO_SHOT:
          explanations[tech] = "Efficient approach for straightforward tasks"
          break
        case Technique.SELF_CONSISTENCY:
          explanations[tech] = "Improves accuracy for complex reasoning tasks"
          break
      }
    })

    return explanations
  }

  private explainDomainSelection(req: UserRequirements, techniques: Set<Technique>): Record<string, string> {
    const explanations: Record<string, string> = {}

    techniques.forEach(tech => {
      switch (tech) {
        case Technique.DOMAIN_EXPERTISE:
          explanations[tech] = `Incorporates ${req.domain} domain knowledge and terminology`
          break
        case Technique.SAFETY_CONSTRAINTS:
          explanations[tech] = `Essential safety measures for ${req.domain} applications`
          break
        case Technique.RETRIEVAL_AUGMENTED:
          explanations[tech] = `Enhances factual accuracy for knowledge-intensive ${req.domain} tasks`
          break
      }
    })

    return explanations
  }

  private explainModelSelection(req: UserRequirements, techniques: Set<Technique>): Record<string, string> {
    const explanations: Record<string, string> = {}

    techniques.forEach(tech => {
      switch (tech) {
        case Technique.MODEL_SPECIFIC:
          explanations[tech] = `Optimized specifically for ${req.targetModel} architecture`
          break
        case Technique.REACT:
          explanations[tech] = `Leverages ${req.targetModel}'s advanced reasoning capabilities`
          break
      }
    })

    return explanations
  }

  private explainQualitySelection(req: UserRequirements, techniques: Set<Technique>): Record<string, string> {
    const explanations: Record<string, string> = {}

    techniques.forEach(tech => {
      switch (tech) {
        case Technique.QUALITY_CONTROLS:
          explanations[tech] = `Ensures high quality output for ${req.audience} audience`
          break
        case Technique.SAFETY_CONSTRAINTS:
          explanations[tech] = `Meets ${req.safetyLevel} safety requirements`
          break
      }
    })

    return explanations
  }

  private selectImageTechniques(req: UserRequirements): Set<Technique> {
    const techniques = new Set<Technique>()

    // Always include image composition for any image generation
    techniques.add(Technique.IMAGE_COMPOSITION)
    techniques.add(Technique.IMAGE_STYLE_GUIDANCE)
    techniques.add(Technique.IMAGE_MODEL_OPTIMIZATION)

    // Add technical parameters for complex requests or specific models
    if (req.complexity === "complex" || req.complexity === "expert" ||
        req.imageModel === "stable-diffusion" || req.imageModel === "midjourney-v7") {
      techniques.add(Technique.IMAGE_TECHNICAL_PARAMS)
    }

    // Add negative prompts for Stable Diffusion
    if (req.imageModel === "stable-diffusion") {
      techniques.add(Technique.IMAGE_NEGATIVE_PROMPTS)
    }

    return techniques
  }

  private explainImageSelection(req: UserRequirements, techniques: Set<Technique>): Record<string, string> {
    const explanations: Record<string, string> = {}

    techniques.forEach(tech => {
      switch (tech) {
        case Technique.IMAGE_COMPOSITION:
          explanations[tech] = `Essential for controlling visual layout and framing in ${req.imageModel} generation`
          break
        case Technique.IMAGE_STYLE_GUIDANCE:
          explanations[tech] = `Ensures consistent ${req.imageStyle} style with ${req.artMedium} medium specification`
          break
        case Technique.IMAGE_MODEL_OPTIMIZATION:
          explanations[tech] = `Optimized specifically for ${req.imageModel} capabilities and syntax`
          break
        case Technique.IMAGE_TECHNICAL_PARAMS:
          explanations[tech] = `Advanced quality control for ${req.complexity} complexity requirements`
          break
        case Technique.IMAGE_NEGATIVE_PROMPTS:
          explanations[tech] = `Quality enhancement technique essential for Stable Diffusion models`
          break
      }
    })

    return explanations
  }

  getTechniqueInfo(technique: Technique): TechniqueInfo {
    return this.db.techniques[technique]
  }
}