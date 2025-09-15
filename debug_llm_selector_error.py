#!/usr/bin/env python3
"""
Debug the LLM technique selector parsing error
"""

import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_technique_selector import LLMTechniqueSelector
from technique_selector import Technique


def debug_llm_selector_error():
    """Debug what the LLM is actually returning that's causing the error"""
    
    print("🔍 DEBUGGING LLM TECHNIQUE SELECTOR ERROR")
    print("=" * 50)
    print()
    
    print("🧪 Available Techniques in Enum:")
    for tech in Technique:
        print(f"   • {tech.value}")
    print()
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="simple",
        audience="expert",
        output_format="structured", 
        creativity="balanced",
        safety_level="high",
        specific_needs="Simple test case",
        session_id="debug"
    )
    
    selector = LLMTechniqueSelector(OPENAI_API_KEY)
    
    if selector.llm_available:
        try:
            # Let's call the LLM directly to see what it returns
            selection_prompt = selector._create_technique_selection_prompt(requirements)
            
            print("📤 PROMPT BEING SENT TO LLM:")
            print("-" * 30)
            print(selection_prompt[:500] + "...")
            print("-" * 30)
            print()
            
            # Make the API call
            import openai
            client = openai.OpenAI(api_key=OPENAI_API_KEY)
            
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in prompt engineering. Respond with valid JSON only."
                    },
                    {
                        "role": "user", 
                        "content": selection_prompt
                    }
                ],
                temperature=0.2,
                max_tokens=1500
            )
            
            raw_response = response.choices[0].message.content.strip()
            print("📥 RAW LLM RESPONSE:")
            print("-" * 30)
            print(raw_response)
            print("-" * 30)
            print()
            
            # Try to parse
            try:
                parsed = json.loads(raw_response)
                print("✅ Valid JSON received")
                print(f"Selected techniques: {parsed.get('selected_techniques', [])}")
                
                # Check if techniques are valid
                invalid_techniques = []
                valid_technique_values = [t.value for t in Technique]
                
                for tech_id in parsed.get('selected_techniques', []):
                    if tech_id not in valid_technique_values:
                        invalid_techniques.append(tech_id)
                
                if invalid_techniques:
                    print(f"❌ INVALID TECHNIQUES FOUND: {invalid_techniques}")
                    print(f"   Valid options are: {valid_technique_values}")
                else:
                    print("✅ All techniques are valid")
                    
            except json.JSONDecodeError as e:
                print(f"❌ JSON parsing failed: {e}")
                
        except Exception as e:
            print(f"❌ API call failed: {e}")
    else:
        print("❌ LLM not available")


if __name__ == "__main__":
    debug_llm_selector_error()