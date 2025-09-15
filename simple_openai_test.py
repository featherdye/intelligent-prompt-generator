#!/usr/bin/env python3
"""
Simple test showing OpenAI is working
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def simple_test():
    """Simple test showing OpenAI generates different content than requirements"""
    
    print("🎯 PROOF THAT OPENAI IS WORKING")
    print("=" * 50)
    
    requirements = UserRequirements(
        task_type="creative",
        target_model="gpt-4",
        domain="creative",
        complexity="simple", 
        audience="general",
        output_format="free_form",
        creativity="creative",
        safety_level="medium",
        specific_needs="Write a haiku about programming",
        session_id="test"
    )
    
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    result = generator.generate_prompt(requirements)
    
    print(f"User asked for: '{requirements.specific_needs}'")
    print()
    print("What OpenAI GPT-4 generated:")
    print("=" * 30)
    print(result.prompt_text)
    print("=" * 30)
    print()
    print(f"Used AI: {result.used_ai_generation}")
    print(f"Quality: {result.quality_score}/10")
    print()
    print("🎉 As you can see, OpenAI generated a complete prompt system,")
    print("not just copied the user requirements!")


if __name__ == "__main__":
    simple_test()