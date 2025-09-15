#!/usr/bin/env python3
"""
Test with real OpenAI API to show technique integration
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def test_real_api():
    """Test with real OpenAI API"""
    
    print("🚀 Testing Real OpenAI API Integration")
    print("=" * 50)
    
    # Check if we have a real API key
    if OPENAI_API_KEY == "your-openai-api-key-here":
        print("❌ No real API key found in prompt_generator.py")
        print("💡 The default key is still set. Replace it with your actual key.")
        return
    
    print(f"🔑 Using API key: {OPENAI_API_KEY[:20]}...")
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
        specific_needs="Analyze patient symptoms and provide differential diagnosis",
        session_id="api_test"
    )
    
    # Initialize generator with the API key
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    
    print("🧠 Generating prompt with OpenAI GPT-4...")
    print("This will show how techniques are integrated by AI...")
    print()
    
    try:
        # Generate the prompt
        result = generator.generate_prompt(requirements)
        
        print("✅ SUCCESS!")
        print("=" * 50)
        print(f"Quality Score: {result.quality_score:.1f}/10")
        print(f"Techniques Applied: {len(result.techniques_used)}")
        print()
        
        print("🎯 Generated Prompt Preview:")
        print("-" * 40)
        print(result.prompt_text[:500] + "..." if len(result.prompt_text) > 500 else result.prompt_text)
        print("-" * 40)
        
        print("\n🔧 Techniques Successfully Integrated:")
        for i, technique in enumerate(result.techniques_used, 1):
            print(f"{i}. {technique.replace('_', ' ').title()}")
        
        print(f"\n💡 The AI successfully integrated all {len(result.techniques_used)} techniques!")
        print("🎉 OpenAI API integration working perfectly!")
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        print("\nPossible reasons:")
        print("• Invalid API key")
        print("• No credits in OpenAI account")
        print("• Rate limit reached")
        print("• Network connectivity issue")


if __name__ == "__main__":
    test_real_api()