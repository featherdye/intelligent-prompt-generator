#!/usr/bin/env python3
"""
Quick Demo - Generate a sample prompt without the full interactive interface
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements
from llm_generator import LLMPromptGenerator
from output_generator import PromptPackageGenerator, FileManager


def generate_demo_prompt():
    """Generate a demo prompt to show system capabilities"""
    
    print("🚀 Generating Demo Prompt...")
    print("=" * 50)
    
    # Create sample requirements (Healthcare Analysis)
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare", 
        complexity="moderate",
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms and provide clinical decision support with differential diagnosis and risk assessment",
        session_id="demo_20241215_143022"
    )
    
    print("Requirements:")
    print(f"  • Task: {requirements.task_type.title()}")
    print(f"  • Domain: {requirements.domain.title()}")
    print(f"  • Model: {requirements.target_model.upper()}")
    print(f"  • Complexity: {requirements.complexity.title()}")
    print(f"  • Audience: {requirements.audience.title()}")
    print()
    
    # Generate the prompt
    print("Generating optimized prompt...")
    llm_generator = LLMPromptGenerator()
    prompt = llm_generator.generate_prompt(requirements)
    
    print(f"✓ Generated prompt with quality score: {prompt.quality_score:.1f}/10")
    print(f"✓ Applied techniques: {', '.join(prompt.techniques_used)}")
    print()
    
    # Create output file
    print("Creating comprehensive documentation...")
    output_generator = PromptPackageGenerator()
    filename = FileManager.generate_filename(requirements)
    
    created_file = output_generator.create_package(prompt, requirements, filename)
    
    print(f"✓ Created: {created_file}")
    print(f"✓ File size: {os.path.getsize(created_file)} bytes")
    print()
    
    print("📋 Generated Package Contents:")
    print("  • Optimized prompt with integrated techniques")
    print("  • Model configuration and usage instructions") 
    print("  • Quality assessment and improvement recommendations")
    print("  • Test cases for validation")
    print("  • Detailed technique explanations")
    print()
    
    print(f"🎉 Demo complete! Check out: {created_file}")


if __name__ == "__main__":
    generate_demo_prompt()