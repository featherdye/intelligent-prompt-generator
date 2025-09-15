#!/usr/bin/env python3
"""
Test the improved technique implementation
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def test_improved_technique_implementation():
    """Test that techniques are now properly implemented"""
    
    print("🧪 TESTING IMPROVED TECHNIQUE IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Test case: Legal extraction with Chain of Thought
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="moderate",
        audience="expert", 
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms step-by-step with differential diagnosis",
        session_id="improved_test"
    )
    
    print("📋 TEST CASE:")
    print(f"   Task: {requirements.task_type} in {requirements.domain}")
    print(f"   Focus: Step-by-step analysis (should trigger Chain of Thought)")
    print(f"   Safety: {requirements.safety_level} (should include safety constraints)")
    print()
    
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    
    print("🔧 Generating prompt with improved technique implementation...")
    result = generator.generate_prompt(requirements)
    
    print("✅ GENERATION COMPLETE!")
    print()
    print("🎯 SELECTED TECHNIQUES:")
    for i, technique in enumerate(result.techniques_used, 1):
        print(f"   {i}. {technique.replace('_', ' ').title()}")
    print()
    
    print("📝 GENERATED PROMPT:")
    print("=" * 60)
    print(result.prompt_text)
    print("=" * 60)
    print()
    
    # Analyze implementation
    prompt_lower = result.prompt_text.lower()
    
    print("🔍 TECHNIQUE IMPLEMENTATION CHECK:")
    
    # Check Chain of Thought
    cot_indicators = ["step by step", "first", "then", "next", "systematically", "step 1", "step 2"]
    cot_found = any(indicator in prompt_lower for indicator in cot_indicators)
    print(f"   Chain of Thought: {'✅ IMPLEMENTED' if cot_found else '❌ MISSING'}")
    if cot_found:
        found_indicators = [ind for ind in cot_indicators if ind in prompt_lower]
        print(f"     Found: {', '.join(found_indicators)}")
    
    # Check Role-Based
    role_indicators = ["you are", "as a", "your role", "expert", "professional"]
    role_found = any(indicator in prompt_lower for indicator in role_indicators)
    print(f"   Role-Based: {'✅ IMPLEMENTED' if role_found else '❌ MISSING'}")
    
    # Check Safety Constraints
    safety_indicators = ["safety", "ethical", "privacy", "confidential", "disclaimer", "professional consultation"]
    safety_found = any(indicator in prompt_lower for indicator in safety_indicators)
    print(f"   Safety Constraints: {'✅ IMPLEMENTED' if safety_found else '❌ MISSING'}")
    
    # Check Structured Output
    structure_indicators = ["format", "structure", "organize", "list", "numbered", "bullet"]
    structure_found = any(indicator in prompt_lower for indicator in structure_indicators)
    print(f"   Structured Output: {'✅ IMPLEMENTED' if structure_found else '❌ MISSING'}")
    
    # Check Domain Expertise
    domain_indicators = ["medical", "healthcare", "patient", "clinical", "diagnosis", "symptoms"]
    domain_found = any(indicator in prompt_lower for indicator in domain_indicators)
    print(f"   Domain Expertise: {'✅ IMPLEMENTED' if domain_found else '❌ MISSING'}")
    
    # Overall score
    techniques_implemented = sum([cot_found, role_found, safety_found, structure_found, domain_found])
    total_techniques = len(result.techniques_used)
    
    print()
    print(f"📊 IMPLEMENTATION SCORE: {techniques_implemented}/{total_techniques} techniques properly implemented")
    
    if techniques_implemented >= total_techniques * 0.8:  # 80% threshold
        print("🎉 EXCELLENT! Techniques are properly implemented!")
    elif techniques_implemented >= total_techniques * 0.6:  # 60% threshold
        print("👍 GOOD! Most techniques are implemented correctly.")
    else:
        print("⚠️  NEEDS IMPROVEMENT: Many techniques are missing implementation.")
    
    print(f"🏆 Quality Score: {result.quality_score}/10")


if __name__ == "__main__":
    test_improved_technique_implementation()