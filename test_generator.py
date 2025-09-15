#!/usr/bin/env python3
"""
Test Script for Prompt Generator

Quick test to verify all components work together.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements
from technique_selector import IntelligentTechniqueSelector
from llm_generator import LLMPromptGenerator
from output_generator import PromptPackageGenerator, FileManager


def test_technique_selection():
    """Test the technique selection engine"""
    print("Testing Technique Selection...")
    
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
        specific_needs="Analyze patient symptoms for clinical decision support",
        session_id="test_20241215"
    )
    
    # Test technique selection
    selector = IntelligentTechniqueSelector()
    techniques, reasoning = selector.select_techniques(requirements)
    
    print(f"✓ Selected {len(techniques)} techniques:")
    for tech in techniques:
        print(f"  - {tech.value}")
    
    print(f"✓ Generated {len(reasoning)} reasoning explanations")
    return True


def test_prompt_generation():
    """Test the prompt generation system"""
    print("\nTesting Prompt Generation...")
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare", 
        complexity="moderate",
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms for clinical decision support",
        session_id="test_20241215"
    )
    
    # Test prompt generation
    generator = LLMPromptGenerator()
    prompt = generator.generate_prompt(requirements)
    
    print(f"✓ Generated prompt with {len(prompt.prompt_text)} characters")
    print(f"✓ Quality score: {prompt.quality_score:.1f}/10")
    print(f"✓ Applied {len(prompt.techniques_used)} techniques")
    print(f"✓ Generated {len(prompt.test_cases)} test cases")
    
    return True


def test_output_generation():
    """Test the output file generation"""
    print("\nTesting Output Generation...")
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="moderate", 
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms for clinical decision support",
        session_id="test_20241215"
    )
    
    # Generate full prompt
    llm_generator = LLMPromptGenerator()
    prompt = llm_generator.generate_prompt(requirements)
    
    # Test output generation
    output_generator = PromptPackageGenerator()
    filename = "test-healthcare-analysis-prompt.md"
    
    created_file = output_generator.create_package(prompt, requirements, filename)
    
    # Check file was created
    if os.path.exists(created_file):
        file_size = os.path.getsize(created_file)
        print(f"✓ Created output file: {created_file}")
        print(f"✓ File size: {file_size} bytes")
        
        # Clean up test file
        os.remove(created_file)
        print("✓ Test file cleaned up")
        return True
    else:
        print("✗ Failed to create output file")
        return False


def test_integration():
    """Test full system integration"""
    print("\nTesting Full Integration...")
    
    try:
        # Run technique selection test
        assert test_technique_selection()
        
        # Run prompt generation test  
        assert test_prompt_generation()
        
        # Run output generation test
        assert test_output_generation()
        
        print("\n🎉 All tests passed! System is ready to use.")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        return False


def demo_prompt_preview():
    """Show a preview of what the system generates"""
    print("\n" + "="*60)
    print("DEMO: Sample Generated Prompt")
    print("="*60)
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="moderate",
        audience="expert", 
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms for clinical decision support",
        session_id="demo_20241215"
    )
    
    generator = LLMPromptGenerator()
    prompt = generator.generate_prompt(requirements)
    
    print("GENERATED PROMPT PREVIEW:")
    print("-" * 40)
    print(prompt.prompt_text[:500] + "...")
    print("-" * 40)
    print(f"Quality Score: {prompt.quality_score:.1f}/10")
    print(f"Techniques Used: {', '.join(prompt.techniques_used)}")
    print("="*60)


if __name__ == "__main__":
    print("🚀 Intelligent Prompt Generator - Test Suite")
    print("=" * 50)
    
    # Run tests
    success = test_integration()
    
    if success:
        # Show demo
        demo_prompt_preview()
        
        print("\n✅ System is ready! Run 'python prompt_generator.py' to start.")
    else:
        print("\n❌ Tests failed. Please check the error messages above.")
        sys.exit(1)