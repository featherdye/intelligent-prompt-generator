#!/usr/bin/env python3
"""
Technique Selection Engine

This module implements intelligent technique selection based on the
Ultimate LLM Prompt Engineering Guide principles.
"""

from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
from enum import Enum


class Technique(Enum):
    """Available prompt engineering techniques"""
    ZERO_SHOT = "zero_shot"
    FEW_SHOT = "few_shot"
    CHAIN_OF_THOUGHT = "chain_of_thought"
    SELF_CONSISTENCY = "self_consistency"
    GENERATE_KNOWLEDGE = "generate_knowledge"
    RETRIEVAL_AUGMENTED = "retrieval_augmented"
    REACT = "react"
    REFLEXION = "reflexion"
    META_PROMPTING = "meta_prompting"
    STRUCTURED_OUTPUT = "structured_output"
    ROLE_BASED = "role_based"
    SAFETY_CONSTRAINTS = "safety_constraints"
    DOMAIN_EXPERTISE = "domain_expertise"
    MODEL_SPECIFIC = "model_specific"
    CREATIVE_STIMULUS = "creative_stimulus"
    QUALITY_CONTROLS = "quality_controls"


@dataclass
class TechniqueInfo:
    """Information about a technique"""
    name: str
    description: str
    best_for: List[str]
    model_compatibility: List[str]
    complexity_requirement: str
    token_cost: str  # low, medium, high
    combines_well_with: List[str]


class TechniqueDatabase:
    """Database of technique information from the Ultimate Guide"""
    
    def __init__(self):
        self.techniques = {
            Technique.ZERO_SHOT: TechniqueInfo(
                name="Zero-Shot Prompting",
                description="Direct instruction without examples, relies on model's pre-trained knowledge",
                best_for=["simple", "general", "quick"],
                model_compatibility=["any"],
                complexity_requirement="simple",
                token_cost="low",
                combines_well_with=["role_based", "structured_output"]
            ),
            
            Technique.FEW_SHOT: TechniqueInfo(
                name="Few-Shot Prompting",
                description="Provides examples to guide model behavior and output format",
                best_for=["standardized", "specific_format", "pattern_recognition"],
                model_compatibility=["any"],
                complexity_requirement="simple",
                token_cost="medium",
                combines_well_with=["structured_output", "domain_expertise"]
            ),
            
            Technique.CHAIN_OF_THOUGHT: TechniqueInfo(
                name="Chain-of-Thought Reasoning",
                description="Breaks down complex problems into step-by-step reasoning",
                best_for=["reasoning", "analysis", "complex", "mathematical"],
                model_compatibility=["gpt-4", "claude-3", "large_models"],
                complexity_requirement="moderate",
                token_cost="medium",
                combines_well_with=["self_consistency", "structured_output"]
            ),
            
            Technique.SELF_CONSISTENCY: TechniqueInfo(
                name="Self-Consistency",
                description="Generates multiple reasoning paths and selects most consistent answer",
                best_for=["reasoning", "complex", "high_accuracy"],
                model_compatibility=["gpt-4", "claude-3"],
                complexity_requirement="complex",
                token_cost="high",
                combines_well_with=["chain_of_thought"]
            ),
            
            Technique.GENERATE_KNOWLEDGE: TechniqueInfo(
                name="Generate Knowledge Prompting",
                description="Generates relevant background knowledge before making predictions",
                best_for=["analysis", "research", "knowledge_intensive"],
                model_compatibility=["any"],
                complexity_requirement="moderate",
                token_cost="medium",
                combines_well_with=["chain_of_thought", "retrieval_augmented"]
            ),
            
            Technique.RETRIEVAL_AUGMENTED: TechniqueInfo(
                name="Retrieval Augmented Generation",
                description="Enhances responses with external knowledge sources",
                best_for=["knowledge_intensive", "factual", "research"],
                model_compatibility=["any"],
                complexity_requirement="moderate",
                token_cost="high",
                combines_well_with=["generate_knowledge", "structured_output"]
            ),
            
            Technique.REACT: TechniqueInfo(
                name="ReAct (Reasoning and Acting)",
                description="Combines reasoning traces with external tool interactions",
                best_for=["tool_use", "dynamic", "interactive"],
                model_compatibility=["gpt-4", "claude-3"],
                complexity_requirement="complex",
                token_cost="high",
                combines_well_with=["chain_of_thought"]
            ),
            
            Technique.STRUCTURED_OUTPUT: TechniqueInfo(
                name="Structured Output Formatting",
                description="Ensures consistent, well-formatted responses",
                best_for=["json", "structured", "markdown", "standardized"],
                model_compatibility=["any"],
                complexity_requirement="simple",
                token_cost="low",
                combines_well_with=["few_shot", "quality_controls"]
            ),
            
            Technique.ROLE_BASED: TechniqueInfo(
                name="Role-Based Prompting",
                description="Assigns specific expertise roles to guide responses",
                best_for=["domain_specific", "expert_level", "professional"],
                model_compatibility=["any"],
                complexity_requirement="simple",
                token_cost="low",
                combines_well_with=["domain_expertise", "quality_controls"]
            ),
            
            Technique.SAFETY_CONSTRAINTS: TechniqueInfo(
                name="Safety and Ethical Guidelines",
                description="Implements safety measures and ethical considerations",
                best_for=["healthcare", "legal", "sensitive_domains"],
                model_compatibility=["any"],
                complexity_requirement="simple",
                token_cost="low",
                combines_well_with=["domain_expertise", "quality_controls"]
            ),
            
            Technique.DOMAIN_EXPERTISE: TechniqueInfo(
                name="Domain-Specific Optimization",
                description="Tailors prompts for specific professional domains",
                best_for=["healthcare", "legal", "finance", "technical"],
                model_compatibility=["any"],
                complexity_requirement="moderate",
                token_cost="medium",
                combines_well_with=["role_based", "safety_constraints"]
            ),
            
            Technique.MODEL_SPECIFIC: TechniqueInfo(
                name="Model-Specific Adaptations",
                description="Optimizes prompts for specific model architectures",
                best_for=["performance", "efficiency", "model_optimization"],
                model_compatibility=["specific"],
                complexity_requirement="simple",
                token_cost="low",
                combines_well_with=["any"]
            ),
            
            Technique.CREATIVE_STIMULUS: TechniqueInfo(
                name="Creative Stimulus Techniques",
                description="Encourages innovative and creative responses",
                best_for=["creative", "brainstorming", "innovative"],
                model_compatibility=["any"],
                complexity_requirement="moderate",
                token_cost="medium",
                combines_well_with=["few_shot", "structured_output"]
            ),
            
            Technique.QUALITY_CONTROLS: TechniqueInfo(
                name="Quality Control Measures",
                description="Implements verification and quality assurance steps",
                best_for=["high_accuracy", "professional", "critical"],
                model_compatibility=["any"],
                complexity_requirement="moderate",
                token_cost="medium",
                combines_well_with=["any"]
            ),
            
            Technique.REFLEXION: TechniqueInfo(
                name="Reflexion",
                description="Self-reflection and iterative improvement of responses",
                best_for=["complex", "iterative", "self_improvement"],
                model_compatibility=["gpt-4", "claude-3"],
                complexity_requirement="complex",
                token_cost="high",
                combines_well_with=["chain_of_thought", "self_consistency"]
            ),
            
            Technique.META_PROMPTING: TechniqueInfo(
                name="Meta-Prompting",
                description="Uses prompts to generate or improve other prompts",
                best_for=["prompt_optimization", "recursive", "meta_tasks"],
                model_compatibility=["gpt-4", "claude-3"],
                complexity_requirement="complex",
                token_cost="high",
                combines_well_with=["self_consistency", "quality_controls"]
            )
        }


class IntelligentTechniqueSelector:
    """Selects optimal techniques based on requirements using Ultimate Guide logic"""
    
    def __init__(self):
        self.db = TechniqueDatabase()
        self.selection_rules = self._build_selection_rules()
    
    def select_techniques(self, requirements) -> Tuple[List[Technique], Dict[str, str]]:
        """
        Select optimal techniques based on user requirements
        
        Returns:
            Tuple of (selected_techniques, reasoning_explanations)
        """
        selected = set()
        reasoning = {}
        
        # Core technique selection based on task type and complexity
        core_techniques = self._select_core_techniques(requirements)
        selected.update(core_techniques)
        reasoning.update(self._explain_core_selection(requirements, core_techniques))
        
        # Domain-specific additions
        domain_techniques = self._select_domain_techniques(requirements)
        selected.update(domain_techniques)
        reasoning.update(self._explain_domain_selection(requirements, domain_techniques))
        
        # Model-specific optimizations
        model_techniques = self._select_model_techniques(requirements)
        selected.update(model_techniques)
        reasoning.update(self._explain_model_selection(requirements, model_techniques))
        
        # Quality and safety enhancements
        quality_techniques = self._select_quality_techniques(requirements)
        selected.update(quality_techniques)
        reasoning.update(self._explain_quality_selection(requirements, quality_techniques))
        
        # Remove incompatible combinations
        selected = self._resolve_conflicts(selected)
        
        # No technique count limits - use all relevant techniques
        print(f"✓ Selected {len(selected)} techniques (unlimited mode)")
        
        return list(selected), reasoning
    
    def _select_core_techniques(self, req) -> Set[Technique]:
        """Select core techniques based on task type and complexity"""
        techniques = set()
        
        # Always include role-based prompting for clarity
        techniques.add(Technique.ROLE_BASED)
        
        # Complexity-based selection
        if req.complexity == "simple":
            techniques.add(Technique.ZERO_SHOT)
        elif req.complexity == "moderate":
            techniques.add(Technique.FEW_SHOT)
            if req.task_type in ["reasoning", "analysis"]:
                techniques.add(Technique.CHAIN_OF_THOUGHT)
        else:  # complex or expert
            techniques.add(Technique.CHAIN_OF_THOUGHT)
            if req.task_type in ["reasoning", "analysis"]:
                techniques.add(Technique.SELF_CONSISTENCY)
        
        # Task-type specific selections
        if req.task_type == "reasoning":
            techniques.add(Technique.CHAIN_OF_THOUGHT)
        elif req.task_type == "creative":
            techniques.add(Technique.CREATIVE_STIMULUS)
        elif req.task_type in ["analysis", "research"]:
            techniques.add(Technique.GENERATE_KNOWLEDGE)
        
        # Output format considerations
        if req.output_format in ["structured", "json", "markdown"]:
            techniques.add(Technique.STRUCTURED_OUTPUT)
        
        return techniques
    
    def _select_domain_techniques(self, req) -> Set[Technique]:
        """Select domain-specific techniques"""
        techniques = set()
        
        # High-stakes domains need safety and expertise
        if req.domain in ["healthcare", "legal", "finance"]:
            techniques.add(Technique.DOMAIN_EXPERTISE)
            techniques.add(Technique.SAFETY_CONSTRAINTS)
            techniques.add(Technique.QUALITY_CONTROLS)
        
        # Knowledge-intensive domains
        if req.domain in ["healthcare", "legal", "science", "education"]:
            techniques.add(Technique.RETRIEVAL_AUGMENTED)
        
        return techniques
    
    def _select_model_techniques(self, req) -> Set[Technique]:
        """Select model-specific optimizations"""
        techniques = set()
        
        # Always include model-specific adaptations
        techniques.add(Technique.MODEL_SPECIFIC)
        
        # Advanced techniques for capable models
        if req.target_model in ["gpt-4", "claude-3"]:
            if req.complexity in ["complex", "expert"]:
                techniques.add(Technique.REACT)
        
        return techniques
    
    def _select_quality_techniques(self, req) -> Set[Technique]:
        """Select quality and safety techniques"""
        techniques = set()
        
        # High safety requirements
        if req.safety_level in ["high", "critical"]:
            techniques.add(Technique.SAFETY_CONSTRAINTS)
            techniques.add(Technique.QUALITY_CONTROLS)
        
        # Expert audience needs quality controls
        if req.audience == "expert":
            techniques.add(Technique.QUALITY_CONTROLS)
        
        return techniques
    
    def _resolve_conflicts(self, techniques: Set[Technique]) -> Set[Technique]:
        """Remove conflicting technique combinations"""
        # Zero-shot conflicts with few-shot
        if Technique.ZERO_SHOT in techniques and Technique.FEW_SHOT in techniques:
            techniques.remove(Technique.ZERO_SHOT)  # Few-shot is more specific
        
        return techniques
    
    def _optimize_technique_count(self, techniques: Set[Technique], req) -> Set[Technique]:
        """Ensure optimal number of techniques (3-5)"""
        techniques_list = list(techniques)
        
        # If too few, add complementary techniques
        while len(techniques_list) < 3:
            missing = self._suggest_complementary_technique(techniques_list, req)
            if missing:
                techniques_list.append(missing)
            else:
                break
        
        # If too many, prioritize by importance
        if len(techniques_list) > 5:
            techniques_list = self._prioritize_techniques(techniques_list, req)[:5]
        
        return set(techniques_list)
    
    def _suggest_complementary_technique(self, current: List[Technique], req) -> Technique:
        """Suggest a complementary technique"""
        current_set = set(current)
        
        # Common useful additions
        if Technique.STRUCTURED_OUTPUT not in current_set:
            return Technique.STRUCTURED_OUTPUT
        if Technique.QUALITY_CONTROLS not in current_set and req.audience == "expert":
            return Technique.QUALITY_CONTROLS
        if Technique.DOMAIN_EXPERTISE not in current_set and req.domain != "general":
            return Technique.DOMAIN_EXPERTISE
        
        return None
    
    def _prioritize_techniques(self, techniques: List[Technique], req) -> List[Technique]:
        """Prioritize techniques by importance for the use case"""
        # Priority scoring based on requirements
        scores = {}
        
        for tech in techniques:
            score = 0
            
            # Core techniques get higher scores
            if tech in [Technique.ROLE_BASED, Technique.CHAIN_OF_THOUGHT, Technique.STRUCTURED_OUTPUT]:
                score += 10
            
            # Domain-specific needs
            if req.domain in ["healthcare", "legal", "finance"]:
                if tech in [Technique.SAFETY_CONSTRAINTS, Technique.DOMAIN_EXPERTISE]:
                    score += 8
            
            # Complexity needs
            if req.complexity in ["complex", "expert"]:
                if tech in [Technique.SELF_CONSISTENCY, Technique.QUALITY_CONTROLS]:
                    score += 6
            
            scores[tech] = score
        
        return sorted(techniques, key=lambda t: scores.get(t, 0), reverse=True)
    
    def _explain_core_selection(self, req, techniques: Set[Technique]) -> Dict[str, str]:
        """Generate explanations for core technique selection"""
        explanations = {}
        
        for tech in techniques:
            if tech == Technique.ROLE_BASED:
                explanations[tech.value] = "Provides clear expertise context and authority"
            elif tech == Technique.CHAIN_OF_THOUGHT:
                explanations[tech.value] = f"Essential for {req.task_type} tasks requiring step-by-step reasoning"
            elif tech == Technique.FEW_SHOT:
                explanations[tech.value] = f"Guides output format and style for {req.complexity} complexity"
            elif tech == Technique.ZERO_SHOT:
                explanations[tech.value] = "Efficient approach for straightforward tasks"
            elif tech == Technique.SELF_CONSISTENCY:
                explanations[tech.value] = "Improves accuracy for complex reasoning tasks"
        
        return explanations
    
    def _explain_domain_selection(self, req, techniques: Set[Technique]) -> Dict[str, str]:
        """Generate explanations for domain-specific selections"""
        explanations = {}
        
        for tech in techniques:
            if tech == Technique.DOMAIN_EXPERTISE:
                explanations[tech.value] = f"Incorporates {req.domain} domain knowledge and terminology"
            elif tech == Technique.SAFETY_CONSTRAINTS:
                explanations[tech.value] = f"Essential safety measures for {req.domain} applications"
            elif tech == Technique.RETRIEVAL_AUGMENTED:
                explanations[tech.value] = f"Enhances factual accuracy for knowledge-intensive {req.domain} tasks"
        
        return explanations
    
    def _explain_model_selection(self, req, techniques: Set[Technique]) -> Dict[str, str]:
        """Generate explanations for model-specific selections"""
        explanations = {}
        
        for tech in techniques:
            if tech == Technique.MODEL_SPECIFIC:
                explanations[tech.value] = f"Optimized specifically for {req.target_model} architecture"
            elif tech == Technique.REACT:
                explanations[tech.value] = f"Leverages {req.target_model}'s advanced reasoning capabilities"
        
        return explanations
    
    def _explain_quality_selection(self, req, techniques: Set[Technique]) -> Dict[str, str]:
        """Generate explanations for quality-related selections"""
        explanations = {}
        
        for tech in techniques:
            if tech == Technique.QUALITY_CONTROLS:
                explanations[tech.value] = f"Ensures high quality output for {req.audience} audience"
            elif tech == Technique.SAFETY_CONSTRAINTS:
                explanations[tech.value] = f"Meets {req.safety_level} safety requirements"
        
        return explanations
    
    def _build_selection_rules(self) -> Dict[str, any]:
        """Build the rule system for technique selection"""
        # This could be expanded into a more sophisticated rule engine
        return {
            "core_rules": "Select based on task type and complexity",
            "domain_rules": "Add safety and expertise for professional domains",
            "model_rules": "Optimize for specific model capabilities",
            "quality_rules": "Ensure appropriate quality controls"
        }
    
    def get_technique_info(self, technique: Technique) -> TechniqueInfo:
        """Get detailed information about a technique"""
        return self.db.techniques[technique]
    
    def explain_technique_combination(self, techniques: List[Technique]) -> str:
        """Explain why these techniques work well together"""
        if len(techniques) <= 1:
            return "Single technique approach for simplicity"
        
        explanations = []
        
        # Check for common powerful combinations
        if Technique.CHAIN_OF_THOUGHT in techniques and Technique.SELF_CONSISTENCY in techniques:
            explanations.append("Chain-of-Thought + Self-Consistency provides robust reasoning with error checking")
        
        if Technique.ROLE_BASED in techniques and Technique.DOMAIN_EXPERTISE in techniques:
            explanations.append("Role-based prompting with domain expertise ensures authoritative responses")
        
        if Technique.STRUCTURED_OUTPUT in techniques:
            explanations.append("Structured output ensures consistent, professional formatting")
        
        if not explanations:
            explanations.append("Selected techniques complement each other for optimal performance")
        
        return "; ".join(explanations)