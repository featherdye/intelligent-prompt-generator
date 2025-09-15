#!/usr/bin/env python3
"""
Debug the LLM technique selector to see what it's actually returning
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_technique_selector import LLMTechniqueSelector


def debug_llm_response():
    """Debug what the LLM is actually returning"""
    
    print("🔍 DEBUGGING LLM TECHNIQUE SELECTOR")
    print("=" * 50)
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="simple",  # Start with simple
        audience="general",
        output_format="structured", 
        creativity="balanced",
        safety_level="medium",
        specific_needs="Test what the LLM returns",
        session_id="debug"
    )
    
    selector = LLMTechniqueSelector(OPENAI_API_KEY)
    
    if selector.llm_available:
        try:
            techniques, reasoning = selector.select_techniques(requirements)
            print("✅ SUCCESS! LLM selection worked")
            print(f"Selected: {[t.value for t in techniques]}")
            print("Reasoning:", reasoning)
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("❌ LLM not available")


if __name__ == "__main__":
    debug_llm_response()