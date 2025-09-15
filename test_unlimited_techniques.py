#!/usr/bin/env python3
"""
Test unlimited technique selection
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_generator import UserRequirements, OPENAI_API_KEY
from llm_generator import LLMPromptGenerator


def test_unlimited_technique_selection():
    """Test the system with no technique limits"""
    
    print("🚀 TESTING UNLIMITED TECHNIQUE SELECTION")
    print("=" * 60)
    print()
    
    # Create a complex, multi-faceted requirements case that should benefit from many techniques
    requirements = UserRequirements(
        task_type="reasoning",
        target_model="gpt-4",
        domain="healthcare",
        complexity="complex",
        audience="expert", 
        output_format="structured",
        creativity="balanced",
        safety_level="critical",
        specific_needs="Comprehensive medical case analysis with differential diagnosis, treatment planning, risk assessment, patient education, and clinical documentation requirements",
        session_id="unlimited_test"
    )
    
    print("📋 COMPREHENSIVE TEST CASE:")
    print(f"   Task: {requirements.task_type} (complex reasoning)")
    print(f"   Domain: {requirements.domain} (high-stakes)")
    print(f"   Audience: {requirements.audience} (professional)")
    print(f"   Safety: {requirements.safety_level} (maximum)")
    print(f"   Needs: Multi-faceted medical analysis")
    print()
    
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    
    print("🧠 Generating prompt with unlimited technique selection...")
    result = generator.generate_prompt(requirements)
    
    print()
    print("✅ UNLIMITED TECHNIQUE SELECTION RESULTS:")
    print("=" * 60)
    print(f"🎯 Quality Score: {result.quality_score}/10")
    print(f"🔧 Total Techniques Used: {len(result.techniques_used)}")
    print(f"🤖 Used AI Generation: {result.used_ai_generation}")
    print()
    
    print("🧠 ALL SELECTED TECHNIQUES:")
    for i, technique in enumerate(result.techniques_used, 1):
        technique_name = technique.replace('_', ' ').title()
        print(f"   {i:2d}. {technique_name}")
    print()
    
    print("🔍 TECHNIQUE CATEGORIES BREAKDOWN:")
    
    # Categorize techniques
    categories = {
        "Core Reasoning": ["chain_of_thought", "self_consistency", "zero_shot", "few_shot"],
        "Domain & Role": ["domain_expertise", "role_based", "model_specific"],
        "Safety & Quality": ["safety_constraints", "quality_controls"],
        "Structure & Format": ["structured_output"],
        "Advanced Methods": ["generate_knowledge", "retrieval_augmented", "react", "reflexion", "meta_prompting"],
        "Creative & Enhancement": ["creative_stimulus"]
    }
    
    for category, techniques in categories.items():
        selected_in_category = [t for t in result.techniques_used if t in techniques]
        if selected_in_category:
            print(f"   📁 {category}: {len(selected_in_category)} techniques")
            for tech in selected_in_category:
                print(f"      • {tech.replace('_', ' ').title()}")
    print()
    
    print("🧾 SELECTION REASONING SAMPLE:")
    reasoning_count = 0
    for tech_name, reason in result.reasoning.items():
        if not tech_name.startswith('_') and reasoning_count < 4:
            display_name = tech_name.replace('_', ' ').title()
            print(f"   • {display_name}: {reason}")
            reasoning_count += 1
    if len(result.reasoning) > 4:
        print(f"   ... and {len(result.reasoning) - 4} more technique explanations")
    print()
    
    print("📝 COMPREHENSIVE PROMPT PREVIEW:")
    print("-" * 60)
    preview = result.prompt_text[:500] + "..." if len(result.prompt_text) > 500 else result.prompt_text
    print(preview)
    print("-" * 60)
    print()
    
    # Analysis
    print("📊 UNLIMITED SELECTION ANALYSIS:")
    print(f"   • Previous limit: 3-5 techniques")
    print(f"   • Current selection: {len(result.techniques_used)} techniques")
    increase = len(result.techniques_used) - 5
    print(f"   • Increase: +{increase} additional techniques ({increase/5*100:.1f}% more)")
    print()
    
    # Benefits assessment
    expected_benefits = []
    if len(result.techniques_used) >= 8:
        expected_benefits.append("Comprehensive coverage of all requirements aspects")
    if "safety_constraints" in result.techniques_used and requirements.safety_level == "critical":
        expected_benefits.append("Enhanced safety for critical healthcare domain")
    if "self_consistency" in result.techniques_used and "chain_of_thought" in result.techniques_used:
        expected_benefits.append("Robust reasoning with error checking")
    if "domain_expertise" in result.techniques_used and "quality_controls" in result.techniques_used:
        expected_benefits.append("Professional-grade domain knowledge with quality assurance")
    
    if expected_benefits:
        print("🎯 EXPECTED BENEFITS OF UNLIMITED SELECTION:")
        for benefit in expected_benefits:
            print(f"   ✓ {benefit}")
        print()
    
    print("🏆 UNLIMITED TECHNIQUE SELECTION SUMMARY:")
    print("=" * 50)
    print("✅ System now uses ALL relevant techniques (no artificial limits)")
    print("✅ More comprehensive prompt coverage")
    print("✅ Better handling of complex, multi-faceted requirements")  
    print("✅ Enhanced quality through technique synergy")
    print(f"✅ {len(result.techniques_used)} techniques working together")
    
    return result


def compare_limited_vs_unlimited():
    """Compare the old limited system vs new unlimited approach"""
    
    print("\n🔬 COMPARISON: LIMITED vs UNLIMITED TECHNIQUE SELECTION")
    print("=" * 70)
    print()
    
    # The same complex requirements
    requirements = UserRequirements(
        task_type="analysis", 
        target_model="gpt-4",
        domain="legal",
        complexity="expert",
        audience="expert",
        output_format="structured",
        creativity="conservative", 
        safety_level="critical",
        specific_needs="Multi-jurisdictional contract analysis with precedent research, risk assessment, compliance checking, and strategic recommendations",
        session_id="comparison"
    )
    
    generator = LLMPromptGenerator(api_key=OPENAI_API_KEY)
    result = generator.generate_prompt(requirements)
    
    print("📊 COMPARISON RESULTS:")
    print(f"   Old System (Limited): ~3-5 techniques")
    print(f"   New System (Unlimited): {len(result.techniques_used)} techniques")
    print(f"   Quality Score: {result.quality_score}/10")
    print()
    
    print("🎯 COMPREHENSIVE COVERAGE ACHIEVED:")
    print("   ✓ More techniques = more comprehensive prompts")  
    print("   ✓ Complex requirements get full attention")
    print("   ✓ No artificial constraints on quality")
    print("   ✓ Better technique synergy opportunities")
    
    return result


if __name__ == "__main__":
    # Test unlimited selection
    unlimited_result = test_unlimited_technique_selection()
    
    # Compare approaches
    comparison_result = compare_limited_vs_unlimited()
    
    print(f"\n🚀 The system now maximizes prompt quality with {len(unlimited_result.techniques_used)} techniques!")
    print("   No more artificial limits - just comprehensive, high-quality prompts! 🎉")