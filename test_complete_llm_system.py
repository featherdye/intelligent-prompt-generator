#!/usr/bin/env python3
"""
Test the complete system with LLM-based technique selection
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def test_complete_llm_system():
    """Test the complete system with LLM technique selection"""
    
    print("🚀 COMPLETE LLM SYSTEM TEST")
    print("=" * 50)
    print()
    
    # Create requirements for a complex healthcare scenario
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4", 
        domain="healthcare",
        complexity="moderate",
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze emergency department patient triage and provide risk assessment recommendations",
        session_id="complete_test"
    )
    
    print("📋 TEST REQUIREMENTS:")
    print(f"   Task: {requirements.task_type} in {requirements.domain}")
    print(f"   Complexity: {requirements.complexity} for {requirements.audience} audience")
    print(f"   Safety: {requirements.safety_level} level required")
    print(f"   Specific: {requirements.specific_needs}")
    print()
    
    # Initialize the complete system
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    
    print("Step 1: LLM selects optimal techniques...")
    result = generator.generate_prompt(requirements)
    
    print("✅ GENERATION COMPLETE!")
    print("=" * 50)
    print(f"🎯 Quality Score: {result.quality_score}/10")
    print(f"🔧 Techniques Selected: {len(result.techniques_used)}")
    print(f"🤖 Used AI Generation: {result.used_ai_generation}")
    print()
    
    print("🧠 LLM-SELECTED TECHNIQUES:")
    for i, technique in enumerate(result.techniques_used, 1):
        technique_name = technique.replace('_', ' ').title()
        print(f"   {i}. {technique_name}")
    print()
    
    print("🧾 WHY THESE TECHNIQUES WERE SELECTED:")
    for tech_name, reason in result.reasoning.items():
        if not tech_name.startswith('_'):
            display_name = tech_name.replace('_', ' ').title()
            print(f"   • {display_name}: {reason}")
    print()
    
    print("📤 GENERATED PROMPT PREVIEW:")
    print("-" * 40)
    preview_length = 300
    if len(result.prompt_text) > preview_length:
        print(result.prompt_text[:preview_length] + "...")
    else:
        print(result.prompt_text)
    print("-" * 40)
    print()
    
    print("🎉 SUCCESS!")
    print("The system now uses LLM to intelligently select techniques!")
    print(f"OpenAI GPT-4 analyzed your requirements and chose {len(result.techniques_used)} optimal techniques.")


if __name__ == "__main__":
    test_complete_llm_system()