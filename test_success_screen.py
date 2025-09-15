#!/usr/bin/env python3
"""
Test the enhanced success screen with mock data to show what it looks like
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import DOSInterface, UserRequirements
from llm_generator import GeneratedPrompt


def create_mock_generated_prompt(use_ai=True):
    """Create mock data to show what the success screen looks like"""
    
    if use_ai:
        # Mock AI-generated prompt data
        return GeneratedPrompt(
            prompt_text="""You are a senior medical analyst with 15+ years of clinical experience in healthcare analysis and diagnosis support.

Your task is to analyze patient symptoms and provide structured clinical decision support with differential diagnosis and risk assessment.

## Analysis Framework
Let me work through this systematically:

1. **Initial Assessment**: Review presenting symptoms and patient history
2. **Symptom Analysis**: Categorize and prioritize key findings  
3. **Differential Diagnosis**: Consider most likely conditions based on evidence
4. **Risk Stratification**: Assess urgency and severity indicators
5. **Recommendations**: Provide actionable clinical guidance

## Output Structure
```
# Medical Analysis Report

## Patient Presentation
- Chief Complaint: [primary symptom/concern]
- Duration: [timeline]
- Associated Symptoms: [related findings]

## Clinical Assessment
### Differential Diagnosis
1. **[Most Likely Condition]** (Probability: High/Medium/Low)
   - Supporting evidence: [key indicators]
   - Risk factors present: [relevant factors]

2. **[Alternative Diagnosis]** (Probability: High/Medium/Low)  
   - Supporting evidence: [key indicators]
   - Distinguishing features: [differentiators]

### Risk Assessment
- **Urgency Level**: [Low/Moderate/High/Critical]
- **Red Flags**: [any concerning features]
- **Monitoring Requirements**: [follow-up needs]

## Clinical Recommendations
- **Immediate Actions**: [urgent interventions if needed]
- **Diagnostic Workup**: [recommended tests/imaging]
- **Treatment Considerations**: [therapeutic options]
- **Follow-up**: [monitoring plan]

## Important Disclaimers
This analysis is for clinical decision support only. Always correlate with clinical judgment and seek appropriate medical consultation for definitive diagnosis and treatment decisions.
```

Please provide the patient case details for analysis.""",
            techniques_used=["safety_constraints", "role_based", "structured_output", "chain_of_thought", "domain_expertise"],
            reasoning={
                "safety_constraints": "Essential safety measures for healthcare applications",
                "role_based": "Provides clear expertise context and authority", 
                "structured_output": "Ensures consistent, professional formatting",
                "chain_of_thought": "Essential for analysis tasks requiring step-by-step reasoning",
                "domain_expertise": "Incorporates healthcare domain knowledge and terminology"
            },
            quality_score=9.4,
            usage_instructions="Standard usage instructions...",
            model_settings={"temperature": 0.3, "max_tokens": 1500},
            test_cases=[{"name": "Test case 1", "input": "Sample input", "expected_elements": "Expected output"}],
            improvement_suggestions=["Prompt meets quality standards - ready for production use"],
            meta_prompt_sent="""You are the world's leading prompt engineering expert, following the Ultimate LLM Prompt Engineering Guide principles.

TASK: Generate a high-quality, production-ready prompt for the following requirements:

## User Requirements
- **Task Type**: Analysis
- **Target Model**: GPT-4  
- **Domain**: Healthcare
- **Complexity**: Moderate
- **Target Audience**: Expert
- **Output Format**: Structured
- **Creativity Level**: Balanced
- **Safety Level**: High

## Specific User Needs
Analyze patient symptoms and provide clinical decision support with differential diagnosis and risk assessment

## Required Techniques to Integrate
Based on the Ultimate Guide analysis, incorporate these techniques seamlessly:
- **Safety and Ethical Guidelines**: Implements safety measures and ethical considerations
- **Role-Based Prompting**: Assigns specific expertise roles to guide responses
- **Structured Output Formatting**: Ensures consistent, well-formatted responses
- **Chain-of-Thought Reasoning**: Breaks down complex problems into step-by-step reasoning
- **Domain-Specific Optimization**: Tailors prompts for specific professional domains

## Model-Specific Optimizations
Use clear structure with system/user message format. Leverage advanced reasoning capabilities.

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

The prompt should demonstrate expert-level prompt engineering and be immediately deployable.""",
            used_ai_generation=True
        )
    else:
        # Mock basic generation data
        return GeneratedPrompt(
            prompt_text="You are an experienced medical professional with extensive experience in healthcare. Your task is to analyze and interpret the provided information with focus on: Analyze patient symptoms. Format your response with clear headings and bullet points.",
            techniques_used=["role_based", "structured_output", "domain_expertise"],
            reasoning={
                "role_based": "Provides clear expertise context and authority",
                "structured_output": "Ensures consistent formatting", 
                "domain_expertise": "Incorporates healthcare domain knowledge"
            },
            quality_score=8.1,
            usage_instructions="Basic usage instructions...",
            model_settings={"temperature": 0.3, "max_tokens": 1000},
            test_cases=[{"name": "Test", "input": "Input", "expected_elements": "Output"}],
            improvement_suggestions=["Consider running with OpenAI API key for enhanced quality"],
            meta_prompt_sent="",
            used_ai_generation=False
        )


def test_both_success_screens():
    """Test both AI-enhanced and basic success screens"""
    
    dos_interface = DOSInterface()
    
    print("🎯 SUCCESS SCREEN PREVIEW")
    print("=" * 60)
    print()
    
    # Test AI-enhanced success screen
    print("1️⃣  WITH OPENAI API KEY (AI-Enhanced Mode):")
    print("-" * 50)
    ai_prompt = create_mock_generated_prompt(use_ai=True)
    dos_interface.show_success("healthcare-analysis-ai-enhanced.md", ai_prompt)
    
    print("\n" + "=" * 60)
    print()
    
    # Test basic success screen  
    print("2️⃣  WITHOUT API KEY (Basic Mode):")
    print("-" * 50)
    basic_prompt = create_mock_generated_prompt(use_ai=False)
    dos_interface.show_success("healthcare-analysis-basic.md", basic_prompt)


if __name__ == "__main__":
    test_both_success_screens()