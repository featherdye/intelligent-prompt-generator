#!/usr/bin/env python3
"""
Self-Correction and Reflection Prompt Enhancement

Adds self-correction and iterative improvement capabilities to generated prompts
based on 2025 prompt engineering best practices.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from typing import Dict, List
from technique_selector import Technique


class SelfCorrectionEnhancer:
    """Adds self-correction and reflection capabilities to prompts"""
    
    def __init__(self):
        self.reflection_patterns = self._build_reflection_patterns()
    
    def enhance_prompt_with_reflection(self, prompt_text: str, techniques_used: List[str], domain: str) -> str:
        """Add self-correction and reflection elements to a prompt"""
        
        # Determine what kind of reflection to add based on techniques and domain
        reflection_type = self._determine_reflection_type(techniques_used, domain)
        reflection_addition = self._get_reflection_addition(reflection_type, domain)
        
        # Insert reflection at the appropriate point in the prompt
        enhanced_prompt = self._insert_reflection(prompt_text, reflection_addition)
        
        return enhanced_prompt
    
    def _determine_reflection_type(self, techniques_used: List[str], domain: str) -> str:
        """Determine what type of reflection is most appropriate"""
        
        # High-stakes domains get comprehensive reflection
        if domain in ["healthcare", "legal", "finance"]:
            return "comprehensive"
        
        # Analysis tasks get systematic reflection
        if "chain_of_thought" in techniques_used:
            return "systematic"
        
        # Creative tasks get iterative reflection
        if "creative_stimulus" in techniques_used:
            return "iterative"
        
        # Default to quality-focused reflection
        return "quality_focused"
    
    def _get_reflection_addition(self, reflection_type: str, domain: str) -> str:
        """Get the appropriate reflection addition for the prompt"""
        
        reflections = {
            "comprehensive": f"""

## Self-Review and Quality Assurance

Before finalizing your response, please review it carefully:

1. **Accuracy Check**: Verify that all information is factually correct and up-to-date for the {domain} domain.

2. **Completeness Review**: Ensure you've addressed all aspects of the request and haven't missed any important considerations.

3. **Safety Validation**: Confirm that your response includes appropriate disclaimers and safety considerations, especially for {domain} applications.

4. **Quality Assessment**: Rate your response on:
   - Clarity and organization (1-10)
   - Practical usefulness (1-10)  
   - Professional appropriateness (1-10)

5. **Iterative Improvement**: If any area scores below 8, briefly explain what could be improved and provide an enhanced version.

Please include this self-assessment at the end of your response.""",

            "systematic": """

## Systematic Self-Verification

After completing your analysis, please:

1. **Logic Check**: Review your reasoning step-by-step. Are there any logical gaps or unsupported conclusions?

2. **Alternative Perspectives**: Consider if there are other valid approaches or viewpoints you should mention.

3. **Error Detection**: Look for any factual errors, inconsistencies, or areas where clarification is needed.

4. **Confidence Assessment**: Rate your confidence in each major conclusion (high/medium/low) and explain why.

If you identify any issues during this review, please correct them and note what was improved.""",

            "iterative": """

## Creative Refinement Process

After your initial response, please:

1. **Fresh Perspective**: Step back and consider: "How could this be even more innovative or effective?"

2. **Audience Alignment**: Ensure your creative output truly serves the intended audience and purpose.

3. **Enhancement Opportunities**: Identify 2-3 specific ways to make your response more engaging or impactful.

4. **Final Polish**: Refine your response incorporating these improvements.

Note any significant changes you made during this refinement process.""",

            "quality_focused": """

## Quality Improvement Review

Please review your response and:

1. **Clarity Check**: Is everything clearly explained and easy to understand?

2. **Completeness**: Have you fully addressed the request?

3. **Usefulness**: Will this response actually help the user achieve their goal?

4. **Professional Standards**: Does this meet professional quality standards?

If you notice any areas for improvement, please refine your response accordingly."""
        }
        
        return reflections.get(reflection_type, reflections["quality_focused"])
    
    def _insert_reflection(self, prompt_text: str, reflection_addition: str) -> str:
        """Insert reflection at the appropriate point in the prompt"""
        
        # Look for common ending patterns
        ending_patterns = [
            "Please provide the",
            "Please analyze the", 
            "Now, please",
            "Based on the",
            "Please process the following"
        ]
        
        # Try to insert before the final instruction
        for pattern in ending_patterns:
            if pattern in prompt_text:
                parts = prompt_text.rsplit(pattern, 1)
                if len(parts) == 2:
                    return parts[0] + reflection_addition + "\n\n" + pattern + parts[1]
        
        # If no pattern found, append at the end
        return prompt_text + reflection_addition
    
    def _build_reflection_patterns(self) -> Dict[str, List[str]]:
        """Build library of reflection patterns for different scenarios"""
        
        return {
            "accuracy_checks": [
                "Please double-check your facts and figures for accuracy.",
                "Verify that your information is current and reliable.",
                "Ensure all claims are properly supported by evidence."
            ],
            "completeness_checks": [
                "Review whether you've addressed all aspects of the request.",
                "Check if any important considerations have been missed.",
                "Ensure your response fully satisfies the user's needs."
            ],
            "safety_checks": [
                "Confirm that your response includes appropriate safety disclaimers.",
                "Verify that ethical considerations have been properly addressed.",
                "Check for any potential harmful or misleading information."
            ]
        }


def test_self_correction_enhancement():
    """Test the self-correction enhancement system"""
    
    print("🧪 TESTING SELF-CORRECTION ENHANCEMENT")
    print("=" * 60)
    
    enhancer = SelfCorrectionEnhancer()
    
    # Test with a healthcare prompt
    original_prompt = """You are an expert healthcare professional. Analyze the patient symptoms and provide a differential diagnosis.

Please provide a structured analysis with:
1. Symptom categorization
2. Possible conditions
3. Recommended next steps

Please analyze the following patient information."""

    techniques_used = ["chain_of_thought", "role_based", "structured_output", "safety_constraints"]
    domain = "healthcare"
    
    enhanced_prompt = enhancer.enhance_prompt_with_reflection(original_prompt, techniques_used, domain)
    
    print("📝 ORIGINAL PROMPT:")
    print("-" * 40)
    print(original_prompt)
    print("-" * 40)
    
    print("\n🔄 ENHANCED PROMPT WITH SELF-CORRECTION:")
    print("-" * 40)
    print(enhanced_prompt)
    print("-" * 40)
    
    print("\n✅ ENHANCEMENT FEATURES ADDED:")
    print("   • Comprehensive quality assurance process")
    print("   • Multi-dimensional self-assessment")
    print("   • Iterative improvement capability")
    print("   • Domain-specific safety validation")
    print("   • Confidence rating system")
    
    print(f"\n📊 PROMPT LENGTH INCREASE: {len(enhanced_prompt) - len(original_prompt)} characters")
    print("🎯 This enhancement encourages the model to self-reflect and improve its responses!")


if __name__ == "__main__":
    test_self_correction_enhancement()