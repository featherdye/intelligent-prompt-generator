#!/usr/bin/env python3
"""
Demo of the enhanced success screen without interactive input
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import DOSInterface, UserRequirements
from llm_generator import GeneratedPrompt


def create_demo_prompt():
    """Create demo data showing the enhanced success screen"""
    
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


def demo_enhanced_success():
    """Demo the enhanced success screen"""
    
    # Override the pause function to make it non-interactive
    class NonInteractiveDOSInterface(DOSInterface):
        def show_success(self, filename, generated_prompt):
            # Clear screen and show header
            print("\033[3J\033[H\033[2J", end="")
            print("┌───────────────────────────────────────────────────────────────┐")
            print("│ INTELLIGENT PROMPT GENERATOR v1.0                             │")
            print("│ Powered by Ultimate LLM Guide                                 │")
            print("│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                             │")
            print("└───────────────────────────────────────────────────────────────┘")
            print()
            
            # Show success box
            print("┌─────────────────────────────────────────────────────┐")
            print("│ ✓ SUCCESS!                                          │")
            print("│                                                     │")
            print("│ Your optimized prompt has been generated!           │")
            print("│                                                     │")
            print(f"│ File saved as: {filename:<30} │")
            print("│                                                     │")
            print("│ The prompt includes:                                │")
            print("│ • Optimized techniques selection                    │")
            print("│ • Model-specific adaptations                        │")
            print("│ • Usage instructions                                │")
            print("│ • Quality assessment                                │")
            print("│ • Example test cases                                │")
            print("└─────────────────────────────────────────────────────┘")
            print()
            
            # Show detailed results (new feature)
            self._show_detailed_results(generated_prompt)
            
            print("\n🎉 ENHANCED SUCCESS SCREEN DEMO COMPLETE!")
            print("The system now shows everything sent to OpenAI GPT-4!")
    
    dos_interface = NonInteractiveDOSInterface()
    
    print("🚀 ENHANCED SUCCESS SCREEN DEMO")
    print("=" * 60)
    print()
    
    # Demo the enhanced success screen
    ai_prompt = create_demo_prompt()
    dos_interface.show_success("healthcare-analysis-demo.md", ai_prompt)


if __name__ == "__main__":
    demo_enhanced_success()