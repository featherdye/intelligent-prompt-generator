#!/usr/bin/env python3
"""
Test the LLM-based technique selection vs rule-based selection
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_technique_selector import LLMTechniqueSelector, HybridTechniqueSelector
from technique_selector import IntelligentTechniqueSelector


def test_llm_vs_rules():
    """Compare LLM vs rule-based technique selection"""
    
    print("🧪 TESTING LLM vs RULE-BASED TECHNIQUE SELECTION")
    print("=" * 60)
    print()
    
    # Create test requirements
    test_cases = [
        {
            "name": "Healthcare Analysis",
            "requirements": UserRequirements(
                task_type="analysis",
                target_model="gpt-4",
                domain="healthcare", 
                complexity="moderate",
                audience="expert",
                output_format="structured",
                creativity="balanced",
                safety_level="high",
                specific_needs="Analyze patient symptoms and provide differential diagnosis",
                session_id="test1"
            )
        },
        {
            "name": "Creative Writing",
            "requirements": UserRequirements(
                task_type="creative",
                target_model="gpt-4",
                domain="creative",
                complexity="simple",
                audience="general",
                output_format="free_form", 
                creativity="highly_creative",
                safety_level="medium",
                specific_needs="Write engaging marketing copy",
                session_id="test2"
            )
        },
        {
            "name": "Complex Legal Research",
            "requirements": UserRequirements(
                task_type="reasoning",
                target_model="gpt-4",
                domain="legal",
                complexity="complex",
                audience="expert", 
                output_format="structured",
                creativity="conservative",
                safety_level="critical",
                specific_needs="Analyze contract clauses for compliance risks",
                session_id="test3"
            )
        }
    ]
    
    # Initialize selectors
    hybrid_selector = HybridTechniqueSelector(OPENAI_API_KEY)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"🎯 TEST CASE {i}: {test_case['name']}")
        print("-" * 50)
        
        # Get comparison
        comparison = hybrid_selector.compare_selections(test_case["requirements"])
        
        if "error" in comparison:
            print(f"❌ {comparison['error']}")
            continue
        
        print("🧠 LLM SELECTION:")
        print(f"   Techniques ({comparison['llm_selection']['count']}): {', '.join(comparison['llm_selection']['techniques'])}")
        
        print("\n📏 RULE-BASED SELECTION:")
        print(f"   Techniques ({comparison['rule_selection']['count']}): {', '.join(comparison['rule_selection']['techniques'])}")
        
        print(f"\n🔄 OVERLAP: {len(comparison['overlap'])} techniques")
        if comparison['overlap']:
            overlap_names = [t.value for t in comparison['overlap']]
            print(f"   Shared: {', '.join(overlap_names)}")
        
        if comparison['llm_unique']:
            llm_unique_names = [t.value for t in comparison['llm_unique']]
            print(f"   🧠 LLM only: {', '.join(llm_unique_names)}")
        
        if comparison['rule_unique']:
            rule_unique_names = [t.value for t in comparison['rule_unique']]
            print(f"   📏 Rules only: {', '.join(rule_unique_names)}")
        
        print()
    
    print("🎉 LLM TECHNIQUE SELECTION TEST COMPLETE!")
    print("\nThe LLM can now intelligently select techniques based on context!")


def test_individual_llm_selection():
    """Test individual LLM selection with detailed reasoning"""
    
    print("\n🔬 DETAILED LLM TECHNIQUE SELECTION TEST")
    print("=" * 60)
    
    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="moderate", 
        audience="expert",
        output_format="structured",
        creativity="balanced",
        safety_level="high",
        specific_needs="Analyze patient symptoms for emergency triage",
        session_id="detailed_test"
    )
    
    llm_selector = LLMTechniqueSelector(OPENAI_API_KEY)
    
    if llm_selector.llm_available:
        techniques, reasoning = llm_selector.select_techniques(requirements)
        
        print("🎯 REQUIREMENTS:")
        print(f"   Task: {requirements.task_type} in {requirements.domain}")
        print(f"   Complexity: {requirements.complexity} for {requirements.audience}")
        print(f"   Safety: {requirements.safety_level} level")
        print(f"   Specific: {requirements.specific_needs}")
        print()
        
        print("🧠 LLM SELECTED TECHNIQUES:")
        for i, technique in enumerate(techniques, 1):
            technique_name = technique.value.replace('_', ' ').title()
            print(f"   {i}. {technique_name}")
        print()
        
        print("🧾 LLM REASONING:")
        for tech_id, reason in reasoning.items():
            if not tech_id.startswith('_'):
                tech_name = tech_id.replace('_', ' ').title()
                print(f"   • {tech_name}: {reason}")
        
        if "_synergy" in reasoning:
            print(f"\n🔗 TECHNIQUE SYNERGY:")
            print(f"   {reasoning['_synergy']}")
        
        if "_llm_confidence" in reasoning:
            print(f"\n📊 {reasoning['_llm_confidence']}")
        
    else:
        print("❌ LLM not available - cannot test detailed selection")


if __name__ == "__main__":
    test_llm_vs_rules()
    test_individual_llm_selection()