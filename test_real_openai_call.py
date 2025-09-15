#!/usr/bin/env python3
"""
Test if the system is actually calling OpenAI API
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def test_real_openai_call():
    """Test actual OpenAI API call"""
    
    print("🔍 TESTING REAL OPENAI API INTEGRATION")
    print("=" * 50)
    print(f"API Key Status: {OPENAI_API_KEY[:20]}..." if OPENAI_API_KEY != "your-openai-api-key-here" else "No API key set")
    print()
    
    # Create simple test requirements
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4", 
        domain="healthcare",
        complexity="simple",
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Test if OpenAI API is working",
        session_id="api_test"
    )
    
    # Initialize generator
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    
    try:
        print("🔄 Attempting to generate prompt with OpenAI...")
        result = generator.generate_prompt(requirements)
        
        print(f"✅ Generation completed!")
        print(f"Used AI Generation: {result.used_ai_generation}")
        print(f"Quality Score: {result.quality_score}")
        
        if result.used_ai_generation:
            print("🎉 SUCCESS: OpenAI API was called!")
            print(f"Meta-prompt length: {len(result.meta_prompt_sent)} characters")
            print(f"Generated prompt preview: {result.prompt_text[:200]}...")
        else:
            print("⚠️  OpenAI API was NOT used - fell back to basic generation")
            print("Possible reasons:")
            print("• Invalid API key")
            print("• No credits in account") 
            print("• API key permissions issue")
            print("• Network connectivity problem")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("This suggests an issue with the API key or OpenAI setup")


if __name__ == "__main__":
    test_real_openai_call()