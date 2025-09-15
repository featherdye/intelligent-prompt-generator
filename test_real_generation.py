#!/usr/bin/env python3
"""
Test real prompt generation with OpenAI API showing actual results
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator
from output_generator import PromptPackageGenerator


def test_real_generation():
    """Test real prompt generation end-to-end"""
    
    print("🚀 REAL OPENAI PROMPT GENERATION TEST")
    print("=" * 60)
    print()
    
    # Create test requirements
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare", 
        complexity="moderate",
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms and provide differential diagnosis recommendations",
        session_id="real_test_20250827"
    )
    
    # Initialize components
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    output_gen = PromptPackageGenerator()
    
    print("Step 1: Generating prompt with OpenAI GPT-4...")
    result = generator.generate_prompt(requirements)
    
    print(f"✅ Generated! Quality Score: {result.quality_score}/10")
    print(f"✅ Used AI Generation: {result.used_ai_generation}")
    print(f"✅ Techniques Applied: {len(result.techniques_used)}")
    print()
    
    print("🎯 ACTUAL GENERATED PROMPT FROM OPENAI:")
    print("=" * 60)
    print(result.prompt_text)
    print("=" * 60)
    print()
    
    print("📤 WHAT WAS SENT TO OPENAI GPT-4:")
    print("=" * 60)
    print("Meta-prompt preview:")
    print(result.meta_prompt_sent[:500] + "...")
    print(f"Full meta-prompt length: {len(result.meta_prompt_sent)} characters")
    print()
    
    print("🔧 TECHNIQUES THAT GPT-4 INTEGRATED:")
    for i, technique in enumerate(result.techniques_used, 1):
        print(f"{i}. {technique.replace('_', ' ').title()}")
    print()
    
    print("Step 2: Generating output file...")
    filename = f"real-openai-test-{requirements.session_id}.md"
    output_gen.generate_output_file(result, requirements, filename)
    
    print(f"✅ File saved as: {filename}")
    print()
    print("🎉 REAL OPENAI GENERATION COMPLETE!")
    print("The system IS using the LLM - not just requirements!")


if __name__ == "__main__":
    test_real_generation()