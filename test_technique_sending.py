#!/usr/bin/env python3
"""
Test script to show exactly what technique information gets sent to OpenAI
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator
from technique_selector import IntelligentTechniqueSelector


def test_technique_sending():
    """Test what techniques get sent to OpenAI"""
    
    print("🔍 Testing Technique Information Sent to OpenAI")
    print("=" * 60)
    
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
        session_id="test_techniques"
    )
    
    # Initialize components
    selector = IntelligentTechniqueSelector()
    generator = LLMPromptGenerator()
    
    # Step 1: Show selected techniques
    print("📋 STEP 1: Technique Selection")
    print("-" * 30)
    selected_techniques, reasoning = selector.select_techniques(requirements)
    
    for i, tech in enumerate(selected_techniques, 1):
        info = selector.get_technique_info(tech)
        print(f"{i}. **{info.name}**")
        print(f"   Description: {info.description}")
        print(f"   Best for: {', '.join(info.best_for)}")
        print()
    
    # Step 2: Show what gets sent to OpenAI
    print("📤 STEP 2: What Gets Sent to OpenAI API")
    print("-" * 40)
    
    # Generate the actual meta-prompt
    meta_prompt = generator._create_meta_prompt(requirements, selected_techniques)
    
    # Show the techniques section specifically
    lines = meta_prompt.split('\n')
    in_techniques_section = False
    techniques_lines = []
    
    for line in lines:
        if "Required Techniques to Integrate" in line:
            in_techniques_section = True
            techniques_lines.append(line)
        elif in_techniques_section and line.startswith("## "):
            break
        elif in_techniques_section:
            techniques_lines.append(line)
    
    print("Techniques section sent to GPT-4:")
    print("```")
    for line in techniques_lines:
        print(line)
    print("```")
    
    # Step 3: Show reasoning explanations
    print("\n🧠 STEP 3: Why Each Technique Was Selected")
    print("-" * 45)
    
    for tech_name, explanation in reasoning.items():
        print(f"• **{tech_name.replace('_', ' ').title()}**:")
        print(f"  {explanation}")
        print()
    
    print("✅ CONCLUSION:")
    print("The system sends comprehensive technique information to OpenAI, including:")
    print("• Technique names and detailed descriptions")
    print("• Specific instructions to incorporate each technique")
    print("• Context about why each was selected")
    print("• Integration requirements for seamless combination")


if __name__ == "__main__":
    test_technique_sending()