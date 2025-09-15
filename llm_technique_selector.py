#!/usr/bin/env python3
"""
LLM-Based Technique Selection Engine

Uses OpenAI GPT-4 to intelligently select optimal prompt engineering techniques
based on user requirements and the Ultimate LLM Prompt Engineering Guide.
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from technique_selector import IntelligentTechniqueSelector, Technique, TechniqueDatabase


class LLMTechniqueSelector:
    """Uses LLM to select optimal techniques based on requirements"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.technique_db = TechniqueDatabase()
        self.fallback_selector = IntelligentTechniqueSelector()  # Fallback to rule-based
        
        # Initialize OpenAI client if available
        if OPENAI_AVAILABLE and self.api_key and self.api_key != "your-openai-api-key-here":
            self.client = openai.OpenAI(api_key=self.api_key)
            self.llm_available = True
            print("✓ LLM Technique Selector initialized with OpenAI GPT-4")
        else:
            self.client = None
            self.llm_available = False
            print("⚠️  LLM Technique Selector falling back to rule-based selection")
    
    def select_techniques(self, requirements) -> Tuple[List[Technique], Dict[str, str]]:
        """
        Select optimal techniques using LLM intelligence
        
        Args:
            requirements: UserRequirements object
            
        Returns:
            Tuple of (selected_techniques, reasoning_explanations)
        """
        
        if self.llm_available:
            try:
                return self._llm_select_techniques(requirements)
            except Exception as e:
                print(f"❌ LLM technique selection failed: {e}")
                print("🔄 Falling back to rule-based selection...")
                return self.fallback_selector.select_techniques(requirements)
        else:
            return self.fallback_selector.select_techniques(requirements)
    
    def _llm_select_techniques(self, requirements) -> Tuple[List[Technique], Dict[str, str]]:
        """Use LLM to select techniques"""
        
        print("🧠 Using GPT-4 to select optimal techniques...")
        
        # Create the technique selection prompt
        selection_prompt = self._create_technique_selection_prompt(requirements)
        
        # Call OpenAI API
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are the world's leading expert in prompt engineering and the Ultimate LLM Prompt Engineering Guide. Your task is to select the optimal combination of prompt engineering techniques based on user requirements. You must respond with valid JSON only."
                },
                {
                    "role": "user", 
                    "content": selection_prompt
                }
            ],
            temperature=0.2,  # Lower temperature for more consistent selection
            max_tokens=1500
        )
        
        # Parse the response
        raw_response = response.choices[0].message.content.strip()
        print(f"🔍 Raw LLM response: {raw_response[:200]}...")
        
        try:
            result = json.loads(raw_response)
            return self._parse_llm_response(result)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse LLM response: {e}")
            print(f"Raw response: {raw_response}")
            raise Exception("Invalid JSON response from LLM")
    
    def _create_technique_selection_prompt(self, requirements) -> str:
        """Create the prompt for LLM technique selection"""
        
        # Get all available techniques with descriptions
        techniques_info = []
        for technique in Technique:
            info = self.technique_db.techniques[technique]
            techniques_info.append({
                "id": technique.value,
                "name": info.name,
                "description": info.description,
                "best_for": info.best_for,
                "complexity_requirement": info.complexity_requirement,
                "token_cost": info.token_cost,
                "model_compatibility": info.model_compatibility
            })
        
        prompt = f"""You are an expert in prompt engineering following the Ultimate LLM Prompt Engineering Guide principles.

TASK: Select ALL optimal prompt engineering techniques for the following requirements (no limits on quantity):

## User Requirements Analysis
- **Task Type**: {requirements.task_type} (What the user wants to accomplish)
- **Target Model**: {requirements.target_model} (The LLM that will use this prompt)  
- **Domain**: {requirements.domain} (Subject area/industry)
- **Complexity**: {requirements.complexity} (Task difficulty level)
- **Target Audience**: {requirements.audience} (Who will use the output)
- **Output Format**: {requirements.output_format} (How results should be structured)
- **Creativity Level**: {requirements.creativity} (Conservative to highly creative)
- **Safety Level**: {requirements.safety_level} (Risk tolerance)
- **Specific Needs**: {requirements.specific_needs or "None specified"}

## Available Techniques
{json.dumps(techniques_info, indent=2)}

## Selection Guidelines
1. **Consider synergies**: Choose techniques that work well together
2. **Match complexity**: Simple tasks don't need complex techniques
3. **Domain requirements**: High-stakes domains (healthcare, legal) need safety measures
4. **Model optimization**: Consider target model capabilities
5. **Token efficiency**: Balance effectiveness with cost
6. **Quality vs Speed**: Match user's priority

## Required Response Format
Respond with ONLY valid JSON in this exact format:

{{
    "selected_techniques": ["technique_id_1", "technique_id_2", "technique_id_3"],
    "reasoning": {{
        "technique_id_1": "Why this technique was selected for these requirements",
        "technique_id_2": "Why this technique was selected for these requirements", 
        "technique_id_3": "Why this technique was selected for these requirements"
    }},
    "technique_synergy": "Brief explanation of how these techniques work together",
    "confidence_score": 0.95
}}

Select ALL techniques that will enhance prompt effectiveness for these specific requirements. Don't limit the number - use as many as are beneficial for maximum quality and comprehensive coverage."""
        
        return prompt
    
    def _parse_llm_response(self, result: dict) -> Tuple[List[Technique], Dict[str, str]]:
        """Parse LLM response into techniques and reasoning"""
        
        # Extract selected technique IDs
        selected_ids = result.get("selected_techniques", [])
        
        # Convert to Technique enums with better error handling
        selected_techniques = []
        valid_technique_values = [t.value for t in Technique]
        
        for tech_id in selected_ids:
            try:
                if tech_id in valid_technique_values:
                    technique = Technique(tech_id)
                    selected_techniques.append(technique)
                else:
                    print(f"⚠️  Unknown technique ID: {tech_id}")
                    # Try to find a close match
                    close_match = self._find_closest_technique(tech_id)
                    if close_match:
                        print(f"   Using close match: {close_match.value}")
                        selected_techniques.append(close_match)
            except (ValueError, AttributeError) as e:
                print(f"⚠️  Error parsing technique {tech_id}: {e}")
        
        # Extract reasoning
        reasoning = result.get("reasoning", {})
        
        # Add synergy explanation
        if "technique_synergy" in result:
            reasoning["_synergy"] = result["technique_synergy"]
        
        # Add confidence score
        confidence = result.get("confidence_score", 0.0)
        reasoning["_llm_confidence"] = f"LLM Confidence: {confidence:.1%}"
        
        print(f"✓ LLM selected {len(selected_techniques)} techniques with {confidence:.1%} confidence")
        
        return selected_techniques, reasoning
    
    def _find_closest_technique(self, tech_id: str) -> Optional[Technique]:
        """Find the closest matching technique for invalid IDs"""
        
        # Common mapping of likely LLM outputs to actual techniques
        mappings = {
            "role_assignment": Technique.ROLE_BASED,
            "role_playing": Technique.ROLE_BASED,
            "step_by_step": Technique.CHAIN_OF_THOUGHT,
            "reasoning": Technique.CHAIN_OF_THOUGHT,
            "examples": Technique.FEW_SHOT,
            "formatting": Technique.STRUCTURED_OUTPUT,
            "safety": Technique.SAFETY_CONSTRAINTS,
            "domain": Technique.DOMAIN_EXPERTISE,
            "quality": Technique.QUALITY_CONTROLS,
            "creative": Technique.CREATIVE_STIMULUS,
            "model_adaptation": Technique.MODEL_SPECIFIC,
            "retrieval": Technique.RETRIEVAL_AUGMENTED,
            "knowledge": Technique.GENERATE_KNOWLEDGE,
            "consistency": Technique.SELF_CONSISTENCY,
            "react_pattern": Technique.REACT,
            "reflection": Technique.REFLEXION,
            "meta": Technique.META_PROMPTING
        }
        
        # Try exact matches in mappings
        if tech_id.lower() in mappings:
            return mappings[tech_id.lower()]
        
        # Try partial matches
        for key, technique in mappings.items():
            if key in tech_id.lower() or tech_id.lower() in key:
                return technique
        
        return None
    
    def get_technique_info(self, technique: Technique):
        """Get technique info (same interface as rule-based selector)"""
        return self.technique_db.techniques[technique]


class HybridTechniqueSelector:
    """Hybrid selector that uses LLM when available, falls back to rules"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.llm_selector = LLMTechniqueSelector(api_key)
        self.rule_selector = IntelligentTechniqueSelector()
    
    def select_techniques(self, requirements) -> Tuple[List[Technique], Dict[str, str]]:
        """Select techniques using best available method"""
        
        if self.llm_selector.llm_available:
            print("🧠 Using AI-powered technique selection...")
            return self.llm_selector.select_techniques(requirements)
        else:
            print("📏 Using rule-based technique selection...")  
            return self.rule_selector.select_techniques(requirements)
    
    def get_technique_info(self, technique: Technique):
        """Get technique info"""
        return self.rule_selector.get_technique_info(technique)
    
    def compare_selections(self, requirements) -> dict:
        """Compare LLM vs rule-based selections for analysis"""
        
        if not self.llm_selector.llm_available:
            return {"error": "LLM not available for comparison"}
        
        try:
            llm_techniques, llm_reasoning = self.llm_selector.select_techniques(requirements)
            rule_techniques, rule_reasoning = self.rule_selector.select_techniques(requirements)
            
            return {
                "llm_selection": {
                    "techniques": [t.value for t in llm_techniques],
                    "count": len(llm_techniques),
                    "reasoning": llm_reasoning
                },
                "rule_selection": {
                    "techniques": [t.value for t in rule_techniques], 
                    "count": len(rule_techniques),
                    "reasoning": rule_reasoning
                },
                "overlap": list(set(llm_techniques) & set(rule_techniques)),
                "llm_unique": list(set(llm_techniques) - set(rule_techniques)),
                "rule_unique": list(set(rule_techniques) - set(llm_techniques))
            }
        except Exception as e:
            return {"error": f"Comparison failed: {e}"}