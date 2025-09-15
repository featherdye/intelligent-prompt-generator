#!/usr/bin/env python3
"""
Analyze technique implementation in generated prompts
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def analyze_technique_implementation():
    """Test what techniques are actually implemented vs claimed"""
    
    print("🔍 ANALYZING TECHNIQUE IMPLEMENTATION")
    print("=" * 60)
    print()
    
    # Create test case - legal extraction (like the example)
    requirements = UserRequirements(
        task_type="extraction",
        target_model="gpt-4",
        domain="legal",
        complexity="expert", 
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Generate legal chronology from case documents with proper citations",
        session_id="technique_test"
    )
    
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    result = generator.generate_prompt(requirements)
    
    print("📋 REQUIREMENTS:")
    print(f"   Task: {requirements.task_type} in {requirements.domain}")
    print(f"   Complexity: {requirements.complexity}")
    print(f"   Safety: {requirements.safety_level}")
    print()
    
    print("🎯 CLAIMED TECHNIQUES:")
    for i, technique in enumerate(result.techniques_used, 1):
        print(f"   {i}. {technique.replace('_', ' ').title()}")
    print()
    
    print("🔍 ACTUAL IMPLEMENTATION ANALYSIS:")
    prompt_text = result.prompt_text.lower()
    
    # Check for actual technique implementation
    implementations = {}
    
    # Role Based - Look for role assignment
    if any(phrase in prompt_text for phrase in ["you are", "as a", "your role"]):
        implementations["role_based"] = "✅ IMPLEMENTED - Clear role assignment found"
    else:
        implementations["role_based"] = "❌ MISSING - No clear role assignment"
    
    # Chain of Thought - Look for step-by-step language
    cot_phrases = ["step by step", "first", "then", "next", "systematically", "let me work through", "step 1", "step 2"]
    if any(phrase in prompt_text for phrase in cot_phrases):
        implementations["chain_of_thought"] = "✅ IMPLEMENTED - Step-by-step reasoning found"
    else:
        implementations["chain_of_thought"] = "❌ MISSING - No explicit reasoning steps"
    
    # Safety Constraints - Look for safety/ethical language
    safety_phrases = ["safety", "ethical", "privacy", "confidential", "bias", "discrimination"]
    if any(phrase in prompt_text for phrase in safety_phrases):
        implementations["safety_constraints"] = "✅ IMPLEMENTED - Safety measures found"
    else:
        implementations["safety_constraints"] = "❌ MISSING - No safety constraints"
    
    # Structured Output - Look for format instructions
    structure_phrases = ["format", "structure", "organize", "list", "numbered", "bullet", "table"]
    if any(phrase in prompt_text for phrase in structure_phrases):
        implementations["structured_output"] = "✅ IMPLEMENTED - Format instructions found"
    else:
        implementations["structured_output"] = "❌ MISSING - No format guidance"
    
    # Domain Expertise - Look for domain-specific terms
    if requirements.domain == "legal":
        domain_phrases = ["legal", "court", "law", "attorney", "judge", "case", "evidence"]
        if any(phrase in prompt_text for phrase in domain_phrases):
            implementations["domain_expertise"] = "✅ IMPLEMENTED - Legal terminology found"
        else:
            implementations["domain_expertise"] = "❌ MISSING - No domain-specific language"
    
    # Display analysis
    for technique in result.techniques_used:
        if technique in implementations:
            print(f"   • {technique.replace('_', ' ').title()}: {implementations[technique]}")
        else:
            print(f"   • {technique.replace('_', ' ').title()}: ⚠️  NOT ANALYZED")
    
    print()
    print("📤 GENERATED PROMPT PREVIEW:")
    print("-" * 50)
    print(result.prompt_text[:500] + "...")
    print("-" * 50)
    
    # Count implementation vs claims
    claimed = len(result.techniques_used)
    implemented = len([impl for impl in implementations.values() if impl.startswith("✅")])
    
    print()
    print(f"📊 IMPLEMENTATION SCORE: {implemented}/{claimed} techniques properly implemented")
    
    if implemented < claimed:
        print("⚠️  ISSUE DETECTED: Some claimed techniques are not properly implemented!")
        print("   This suggests the prompt generator needs improvement.")
    else:
        print("✅ All claimed techniques appear to be implemented correctly!")
    
    return result, implementations


if __name__ == "__main__":
    analyze_technique_implementation()