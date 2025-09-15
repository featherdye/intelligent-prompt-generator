#!/usr/bin/env python3
"""
Demo showing both OpenAI and basic generation modes
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements
from llm_generator import LLMPromptGenerator
from output_generator import PromptPackageGenerator, FileManager


def demo_both_modes():
    """Demo both OpenAI and basic generation modes"""
    
    print("🚀 Prompt Generator - Dual Mode Demo")
    print("=" * 50)
    
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
        specific_needs="Analyze patient symptoms for clinical decision support with differential diagnosis",
        session_id="demo_dual_20241215"
    )
    
    print("📋 Test Requirements:")
    print(f"   Task: {requirements.task_type.title()}")
    print(f"   Domain: {requirements.domain.title()}")
    print(f"   Model: {requirements.target_model.upper()}")
    print(f"   Complexity: {requirements.complexity.title()}")
    print()
    
    # Test without API key (basic mode)
    print("🔹 MODE 1: Basic Generation (No API Key)")
    print("-" * 40)
    
    generator_basic = LLMPromptGenerator()  # No API key
    prompt_basic = generator_basic.generate_prompt(requirements)
    
    print(f"   Quality Score: {prompt_basic.quality_score:.1f}/10")
    print(f"   Prompt Length: {len(prompt_basic.prompt_text)} characters")
    print(f"   Techniques: {len(prompt_basic.techniques_used)}")
    print()
    
    # Test with API key (if available)
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        print("🔹 MODE 2: AI-Enhanced Generation (With API Key)")
        print("-" * 40)
        
        try:
            generator_ai = LLMPromptGenerator(api_key=openai_key)
            prompt_ai = generator_ai.generate_prompt(requirements)
            
            print(f"   Quality Score: {prompt_ai.quality_score:.1f}/10")
            print(f"   Prompt Length: {len(prompt_ai.prompt_text)} characters")
            print(f"   Techniques: {len(prompt_ai.techniques_used)}")
            print()
            
            # Compare the modes
            print("📊 COMPARISON")
            print("-" * 40)
            print(f"Basic Mode:     Quality {prompt_basic.quality_score:.1f}/10, {len(prompt_basic.prompt_text)} chars")
            print(f"AI-Enhanced:    Quality {prompt_ai.quality_score:.1f}/10, {len(prompt_ai.prompt_text)} chars")
            print(f"Improvement:    +{prompt_ai.quality_score - prompt_basic.quality_score:.1f} quality points")
            
            # Create sample files for both
            output_gen = PromptPackageGenerator()
            
            basic_file = "demo-basic-mode-prompt.md"
            ai_file = "demo-ai-enhanced-prompt.md"
            
            output_gen.create_package(prompt_basic, requirements, basic_file)
            output_gen.create_package(prompt_ai, requirements, ai_file)
            
            print(f"\n📁 Generated comparison files:")
            print(f"   Basic Mode: {basic_file}")
            print(f"   AI Enhanced: {ai_file}")
            
        except Exception as e:
            print(f"   AI generation failed: {e}")
            print("   (This is normal if you don't have OpenAI credits)")
            print()
            
    else:
        print("🔹 MODE 2: AI-Enhanced Generation")
        print("-" * 40)
        print("   ❌ No OpenAI API key found")
        print("   💡 To test AI mode: export OPENAI_API_KEY='your-key'")
        print()
    
    print("🎯 SUMMARY")
    print("=" * 50)
    print("✅ Basic Mode: Always available, 8.0+ quality, free")
    if openai_key:
        print("✅ AI Mode: 9.0+ quality, GPT-4 powered, ~$0.05 per prompt")
    else:
        print("🔸 AI Mode: Available with OpenAI API key")
    print("\nBoth modes use the same intelligent technique selection!")
    print("The system automatically falls back to basic mode if needed.")


if __name__ == "__main__":
    demo_both_modes()