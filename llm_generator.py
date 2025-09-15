#!/usr/bin/env python3
"""
LLM Integration for Prompt Generation - OpenAI API Version

This module handles prompt generation using OpenAI's GPT models and our
Ultimate Guide principles through meta-prompting techniques.
"""

import json
import os
import sys
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("Warning: openai package not installed. Run: pip install openai")

from technique_selector import IntelligentTechniqueSelector, Technique
from llm_technique_selector import HybridTechniqueSelector


@dataclass
class GeneratedPrompt:
    """Container for generated prompt and metadata"""
    prompt_text: str
    techniques_used: List[str]
    reasoning: Dict[str, str]
    quality_score: float
    usage_instructions: str
    model_settings: Dict[str, any]
    test_cases: List[Dict[str, str]]
    improvement_suggestions: List[str]
    meta_prompt_sent: str = ""  # What was actually sent to OpenAI
    used_ai_generation: bool = False  # Whether OpenAI API was used


class LLMPromptGenerator:
    """Generates high-quality prompts using OpenAI API and the Ultimate Guide"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        # Use hybrid selector that tries LLM first, falls back to rules
        self.technique_selector = HybridTechniqueSelector(self.api_key)
        
        # Initialize OpenAI client if available
        if OPENAI_AVAILABLE and self.api_key:
            self.client = openai.OpenAI(api_key=self.api_key)
            print("✓ OpenAI API initialized successfully")
        elif not self.api_key:
            print("⚠️  Warning: No OpenAI API key found.")
            print("   Set OPENAI_API_KEY environment variable or pass api_key parameter.")
            print("   System will use basic fallback generation.")
            self.client = None
        else:
            self.client = None
    
    def generate_prompt(self, requirements) -> GeneratedPrompt:
        """
        Generate a complete prompt using OpenAI API and our guide
        
        Args:
            requirements: UserRequirements object
            
        Returns:
            GeneratedPrompt with complete prompt and documentation
        """
        
        # Step 1: Select optimal techniques
        selected_techniques, reasoning = self.technique_selector.select_techniques(requirements)
        print(f"✓ Selected {len(selected_techniques)} techniques: {', '.join([t.value for t in selected_techniques])}")
        
        # Step 2: Generate the actual prompt using OpenAI
        prompt_text, meta_prompt_sent, used_ai = self._generate_prompt_with_openai(requirements, selected_techniques)
        
        # Step 3: Generate supporting materials
        usage_instructions = self._generate_usage_instructions(requirements, selected_techniques)
        model_settings = self._generate_model_settings(requirements)
        test_cases = self._generate_test_cases(requirements, prompt_text)
        
        # Step 4: Quality assessment
        quality_score = self._assess_quality(prompt_text, requirements, selected_techniques)
        
        # Step 5: Improvement suggestions
        improvements = self._generate_improvements(prompt_text, requirements, quality_score)
        
        return GeneratedPrompt(
            prompt_text=prompt_text,
            techniques_used=[t.value for t in selected_techniques],
            reasoning=reasoning,
            quality_score=quality_score,
            usage_instructions=usage_instructions,
            model_settings=model_settings,
            test_cases=test_cases,
            improvement_suggestions=improvements,
            meta_prompt_sent=meta_prompt_sent,
            used_ai_generation=used_ai
        )
    
    def _generate_prompt_with_openai(self, requirements, techniques: List[Technique]) -> tuple:
        """Generate the actual prompt using OpenAI API"""
        
        # Create the meta-prompt for generating prompts
        meta_prompt = self._create_meta_prompt(requirements, techniques)
        
        # Use OpenAI API if available
        if OPENAI_AVAILABLE and self.client:
            try:
                print("🔄 Generating prompt with OpenAI GPT-4...")
                prompt_text = self._call_openai_api(meta_prompt)
                return prompt_text, meta_prompt, True
            except Exception as e:
                print(f"❌ OpenAI API call failed: {e}")
                print("🔄 Falling back to basic generation...")
                fallback_prompt = self._generate_basic_fallback(requirements, techniques)
                return fallback_prompt, meta_prompt, False
        else:
            print("🔄 OpenAI API not available. Using basic generation.")
            fallback_prompt = self._generate_basic_fallback(requirements, techniques)
            return fallback_prompt, "", False
    
    def _create_meta_prompt(self, requirements, techniques: List[Technique]) -> str:
        """Create the meta-prompt for OpenAI generation"""
        
        technique_descriptions = []
        technique_implementations = []
        
        for tech in techniques:
            info = self.technique_selector.get_technique_info(tech)
            technique_descriptions.append(f"- **{info.name}**: {info.description}")
            
            # Add specific implementation guidance for each technique
            implementation = self._get_technique_implementation_guide(tech, requirements)
            if implementation:
                technique_implementations.append(implementation)
        
        techniques_text = "\n".join(technique_descriptions)
        implementations_text = "\n".join(technique_implementations)
        
        meta_prompt = f"""You are the world's leading prompt engineering expert, following the Ultimate LLM Prompt Engineering Guide principles.

TASK: Generate a high-quality, production-ready prompt for the following requirements:

## User Requirements
- **Task Type**: {requirements.task_type.replace('_', ' ').title()}
- **Target Model**: {requirements.target_model.upper()}  
- **Domain**: {requirements.domain.replace('_', ' ').title()}
- **Complexity**: {requirements.complexity.title()}
- **Target Audience**: {requirements.audience.title()}
- **Output Format**: {requirements.output_format.replace('_', ' ').title()}
- **Creativity Level**: {requirements.creativity.replace('_', ' ').title()}
- **Safety Level**: {requirements.safety_level.title()}

## Specific User Needs
{requirements.specific_needs if requirements.specific_needs else "No additional requirements specified"}

## Required Techniques to Integrate
Based on the Ultimate Guide analysis, incorporate these techniques seamlessly:
{techniques_text}

## CRITICAL: Technique Implementation Requirements
You MUST implement each technique using these specific patterns:
{implementations_text}

## Model-Specific Optimizations
{self._get_model_instructions(requirements.target_model)}

## Generation Requirements
Create a complete, professional prompt that:
1. **Role Definition**: Clear expertise and authority establishment
2. **Task Integration**: Incorporates all selected techniques naturally
3. **Domain Expertise**: Uses appropriate terminology and context
4. **Output Structure**: Specifies clear formatting requirements  
5. **Safety Measures**: Includes appropriate constraints and disclaimers
6. **Quality Controls**: Built-in validation and quality checks
7. **Professional Standards**: Ready for immediate production use

## Output Format
Generate ONLY the complete optimized prompt - no explanations, no markdown code blocks, just the ready-to-use prompt text.

The prompt should demonstrate expert-level prompt engineering and be immediately deployable."""
        
        return meta_prompt
    
    def _call_openai_api(self, meta_prompt: str) -> str:
        """Call OpenAI API to generate the prompt"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert prompt engineer. Generate high-quality, production-ready prompts that follow advanced prompt engineering principles. Output only the final prompt - no explanations or formatting."
                    },
                    {
                        "role": "user", 
                        "content": meta_prompt
                    }
                ],
                temperature=0.3,
                max_tokens=2500,
                top_p=0.9
            )
            
            generated_prompt = response.choices[0].message.content.strip()
            
            # Clean up any unwanted formatting
            generated_prompt = self._clean_generated_prompt(generated_prompt)
            
            print("✓ OpenAI prompt generation successful")
            return generated_prompt
            
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    def _clean_generated_prompt(self, prompt: str) -> str:
        """Clean up the generated prompt"""
        
        # Remove markdown code blocks if present
        if prompt.startswith("```"):
            lines = prompt.split('\n')
            if lines[0].startswith("```") and lines[-1].strip() == "```":
                prompt = '\n'.join(lines[1:-1])
        
        # Remove any leading/trailing whitespace
        prompt = prompt.strip()
        
        # Ensure it doesn't start with explanatory text
        if prompt.lower().startswith(("here is", "here's", "the prompt is", "prompt:")):
            lines = prompt.split('\n')
            prompt = '\n'.join(lines[1:]).strip()
        
        return prompt
    
    def _generate_basic_fallback(self, requirements, techniques: List[Technique]) -> str:
        """Generate a basic prompt when OpenAI API is not available"""
        
        # Create role definition
        domain_experts = {
            "healthcare": "experienced medical professional",
            "legal": "senior legal analyst", 
            "finance": "financial expert",
            "technology": "technical specialist",
            "education": "education specialist",
            "creative": "creative professional"
        }
        
        expert = domain_experts.get(requirements.domain, "domain expert")
        role = f"You are an {expert} with extensive experience in {requirements.domain}."
        
        # Create task instruction
        task_actions = {
            "analysis": "analyze and interpret",
            "classification": "classify and categorize",
            "generation": "generate high-quality",
            "reasoning": "apply logical reasoning to", 
            "coding": "write, debug, or optimize code for",
            "creative": "create innovative content for"
        }
        
        action = task_actions.get(requirements.task_type, "process")
        task = f"Your task is to {action} the provided information"
        
        if requirements.specific_needs:
            task += f" with focus on: {requirements.specific_needs}"
        
        # Create constraints
        constraints = []
        
        if requirements.output_format == "structured":
            constraints.append("Format your response with clear headings and bullet points.")
        elif requirements.output_format == "json":
            constraints.append("Provide your response in valid JSON format.")
        
        if requirements.domain in ["healthcare", "legal", "finance"]:
            constraints.append("Include appropriate disclaimers and emphasize when professional consultation is needed.")
        
        if requirements.audience == "expert":
            constraints.append("Use professional terminology and provide detailed technical analysis.")
        
        constraint_text = "\n".join(constraints) if constraints else "Provide clear, professional responses."
        
        return f"""{role}

{task}

{constraint_text}

Please process the following input according to the specifications above:"""
    
    def _get_technique_implementation_guide(self, technique: Technique, requirements) -> str:
        """Get specific implementation instructions for each technique"""
        
        guides = {
            Technique.CHAIN_OF_THOUGHT: """
**Chain of Thought Implementation**:
- Include explicit reasoning structure: "Let me work through this step by step:"
- Use numbered steps: "Step 1:", "Step 2:", etc.
- Add thinking phrases: "First, I need to...", "Then I will...", "Finally..."
- Guide the model through the logical process systematically""",
            
            Technique.ROLE_BASED: """
**Role-Based Implementation**:
- Start with clear role assignment: "You are an expert [domain] professional with [X] years of experience"
- Define specific expertise areas and qualifications
- Establish authority and context for the role
- Use first-person perspective when appropriate""",
            
            Technique.SAFETY_CONSTRAINTS: """
**Safety Constraints Implementation**:
- Include explicit safety disclaimers appropriate for the domain
- Add ethical guidelines: "Ensure responses are unbiased and ethical"
- Include confidentiality/privacy requirements where applicable
- Add warning about professional consultation needs for critical domains""",
            
            Technique.STRUCTURED_OUTPUT: """
**Structured Output Implementation**:
- Specify exact format requirements: "Format your response as:", "Use the following structure:"
- Include template or example structure
- Define headers, bullet points, numbering systems
- Specify any required metadata or formatting elements""",
            
            Technique.DOMAIN_EXPERTISE: """
**Domain Expertise Implementation**:
- Use domain-specific terminology correctly and consistently
- Reference industry standards, procedures, and best practices
- Include domain-specific constraints and requirements
- Demonstrate deep understanding of the field's context""",
            
            Technique.FEW_SHOT: """
**Few-Shot Implementation**:
- Provide 2-3 concrete examples of the desired output format
- Show input-output pairs that demonstrate the task
- Use realistic examples relevant to the domain
- Ensure examples follow the exact format specification""",
            
            Technique.ZERO_SHOT: """
**Zero-Shot Implementation**:
- Provide clear, direct instructions without examples
- Be explicit about requirements and expectations
- Use precise language that leaves no ambiguity
- Focus on task definition and output specifications""",
            
            Technique.SELF_CONSISTENCY: """
**Self-Consistency Implementation**:
- Instruct to generate multiple approaches: "Consider this from multiple angles"
- Add verification steps: "Review your answer for consistency"
- Include cross-checking instructions: "Validate your reasoning"
- Request confidence assessment of the response""",
            
            Technique.REFLEXION: """
**Reflexion Implementation**:
- Include self-reflection prompts: "Let me review and improve my response"
- Add iterative improvement: "Upon reflection, I should also consider..."
- Request self-evaluation: "Analyzing my answer, I notice..."
- Include correction opportunities: "Let me refine this approach"=""",
            
            Technique.META_PROMPTING: """
**Meta-Prompting Implementation**:
- Reference prompt engineering: "This prompt is designed to..."
- Include prompt improvement suggestions: "For better results, consider..."
- Add meta-cognitive elements: "I am approaching this task by..."
- Guide prompt optimization: "This structure ensures..."=""",
            
            Technique.GENERATE_KNOWLEDGE: """
**Generate Knowledge Implementation**:
- Instruct to generate relevant background: "First, let me establish the relevant context"
- Add knowledge synthesis: "Based on established knowledge in this field"
- Include fact-gathering: "Let me compile the relevant information"
- Request knowledge validation: "Drawing from established principles"=""",
            
            Technique.RETRIEVAL_AUGMENTED: """
**Retrieval Augmented Implementation**:
- Reference external knowledge sources: "Based on current research and documentation"
- Add citation requirements: "Drawing from authoritative sources"
- Include knowledge integration: "Combining multiple information sources"
- Request source validation: "Verify information against reliable sources"=""",
            
            Technique.REACT: """
**ReAct Implementation**:
- Combine reasoning and action: "I need to think through this and then act"
- Add explicit reasoning traces: "My reasoning: ... My action: ..."
- Include tool interaction patterns: "Let me use the appropriate tool/method"
- Structure thought-action cycles: "Thought: ... Action: ... Observation: ..."=""",
            
            Technique.CREATIVE_STIMULUS: """
**Creative Stimulus Implementation**:
- Encourage creative thinking: "Think creatively and explore innovative approaches"
- Add divergent thinking prompts: "Consider unconventional solutions"
- Include brainstorming elements: "Generate multiple creative alternatives"
- Request novel perspectives: "Approach this from a fresh angle"=""",
            
            Technique.QUALITY_CONTROLS: """
**Quality Controls Implementation**:
- Add verification steps: "Double-check your response for accuracy"
- Include quality criteria: "Ensure your answer meets professional standards"
- Request self-assessment: "Rate the quality and completeness of your response"
- Add error checking: "Review for any errors or omissions"=""",
            
            Technique.MODEL_SPECIFIC: """
**Model-Specific Implementation**:
- Optimize for target model capabilities: "Leverage your advanced reasoning abilities"
- Add model-appropriate instructions: "Use your training to provide comprehensive analysis"
- Include capability-specific guidance: "Drawing on your extensive knowledge base"
- Structure for model strengths: "Apply your pattern recognition skills"=""",
        }
        
        return guides.get(technique, "")
    
    def _get_model_instructions(self, model: str) -> str:
        """Get model-specific instructions"""
        instructions = {
            "gpt-4": "Use clear structure with system/user message format. Leverage advanced reasoning capabilities.",
            "claude-3": "Use XML tags for structure. Emphasize step-by-step thinking with <thinking> tags.",
            "gpt-3.5": "Be explicit in instructions. Use clear formatting and provide examples.",
        }
        return instructions.get(model, "Use universal formatting that works across models.")
    
    def _generate_usage_instructions(self, requirements, techniques: List[Technique]) -> str:
        """Generate usage instructions"""
        
        return f"""## Usage Instructions

### Basic Usage
1. Copy the complete prompt above
2. Add your specific input after the prompt
3. Configure your model with the recommended settings below
4. Review the output for quality and completeness

### Model Configuration
- **Target Model**: {requirements.target_model.upper()}
- **Temperature**: {self._get_recommended_temperature(requirements)}
- **Max Tokens**: {self._get_recommended_max_tokens(requirements)}
- **Top-P**: 0.9

### Best Practices
- Test with multiple examples to ensure consistency
- Validate outputs meet your domain-specific requirements
- Consider adding more context for specialized use cases

### Troubleshooting
- **Output too brief**: Increase max_tokens or add "provide detailed analysis"
- **Inconsistent format**: Emphasize format requirements in your input
- **Not domain-specific**: Include more context about your specific use case"""
    
    def _generate_model_settings(self, requirements) -> Dict[str, any]:
        """Generate recommended model settings"""
        return {
            "temperature": self._get_recommended_temperature(requirements),
            "max_tokens": self._get_recommended_max_tokens(requirements),
            "top_p": 0.9,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0
        }
    
    def _get_recommended_temperature(self, requirements) -> float:
        """Get recommended temperature based on requirements"""
        if requirements.creativity == "conservative":
            return 0.2
        elif requirements.creativity == "creative":
            return 0.7
        elif requirements.creativity == "highly creative":
            return 0.9
        else:
            return 0.3
    
    def _get_recommended_max_tokens(self, requirements) -> int:
        """Get recommended max tokens based on requirements"""
        if requirements.complexity == "simple":
            return 500
        elif requirements.complexity == "moderate":
            return 1000
        else:
            return 2000
    
    def _generate_test_cases(self, requirements, prompt_text: str) -> List[Dict[str, str]]:
        """Generate test cases"""
        return [
            {
                "name": "Basic functionality test",
                "input": f"Sample {requirements.task_type} input for {requirements.domain}",
                "expected_elements": f"Should demonstrate {requirements.task_type} capabilities with proper formatting"
            },
            {
                "name": "Complex scenario test",
                "input": f"Challenging {requirements.task_type} case with multiple requirements",
                "expected_elements": "Should handle complexity with clear reasoning and professional output"
            }
        ]
    
    def _assess_quality(self, prompt_text: str, requirements, techniques: List[Technique]) -> float:
        """Assess the quality of the generated prompt"""
        score = 7.0  # Base score
        
        # OpenAI generated prompts get higher base score
        if OPENAI_AVAILABLE and self.client:
            score = 8.5
        
        # Check for key components
        if any(word in prompt_text.lower() for word in ["you are", "role", "expert"]):
            score += 0.3
        if requirements.domain.lower() in prompt_text.lower():
            score += 0.3
        if len(prompt_text) > 100:  # Reasonable length
            score += 0.2
        if any(word in prompt_text.lower() for word in ["format", "structure", "output"]):
            score += 0.2
        if requirements.safety_level in ["high", "critical"] and "disclaimer" in prompt_text.lower():
            score += 0.3
        
        return min(score, 10.0)
    
    def _generate_improvements(self, prompt_text: str, requirements, quality_score: float) -> List[str]:
        """Generate improvement suggestions"""
        improvements = []
        
        if quality_score < 8.5:
            improvements.append("Consider running with OpenAI API key for enhanced quality")
        
        if quality_score < 8.0:
            improvements.append("Add more specific examples relevant to your domain")
            improvements.append("Consider enhancing output format specification")
        
        if requirements.safety_level in ["high", "critical"] and "disclaimer" not in prompt_text.lower():
            improvements.append("Add appropriate safety disclaimers for sensitive domain")
        
        return improvements or ["Prompt meets quality standards - ready for production use"]