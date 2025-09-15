#!/usr/bin/env python3
"""
Simple direct LLM test to see what's going wrong
"""

import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import OPENAI_API_KEY
import openai


def simple_llm_test():
    """Direct test of LLM technique selection"""
    
    print("🧪 SIMPLE LLM TEST")
    print("=" * 30)
    
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    simple_prompt = """Select ALL optimal prompt engineering techniques for analyzing patient symptoms in healthcare (no limits).

Available techniques: zero_shot, few_shot, chain_of_thought, self_consistency, role_based, structured_output, domain_expertise, safety_constraints.

Respond with ONLY valid JSON:
{
    "selected_techniques": ["technique1", "technique2", "technique3", "...as many as needed"],
    "reasoning": {
        "technique1": "why selected",
        "technique2": "why selected", 
        "technique3": "why selected"
    }
}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a prompt engineering expert. Respond only with valid JSON."},
                {"role": "user", "content": simple_prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        
        raw_response = response.choices[0].message.content.strip()
        print("Raw response:")
        print(raw_response)
        print()
        
        try:
            parsed = json.loads(raw_response)
            print("✅ Valid JSON!")
            print("Selected:", parsed.get("selected_techniques", []))
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            
    except Exception as e:
        print(f"❌ API Error: {e}")


if __name__ == "__main__":
    simple_llm_test()