#!/usr/bin/env python3
"""
LLM-as-a-Judge Quality Assessment System

Advanced quality evaluation using GPT-4 to assess prompt quality
across multiple dimensions with domain-specific criteria.
"""

import sys
import os
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from prompt_generator import UserRequirements


@dataclass
class QualityAssessment:
    """Comprehensive quality assessment from LLM judge"""
    overall_score: float
    dimension_scores: Dict[str, float]
    strengths: List[str]
    weaknesses: List[str]
    specific_feedback: str
    recommendations: List[str]
    confidence: float


class LLMQualityJudge:
    """Advanced quality assessment using LLM-as-a-Judge methodology"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.available = OPENAI_AVAILABLE and self.api_key and self.api_key != "your-openai-api-key-here"
        
        if self.available:
            self.client = openai.OpenAI(api_key=self.api_key)
            print("✓ LLM Quality Judge initialized with GPT-4")
        else:
            print("⚠️  LLM Quality Judge unavailable - API key needed")
    
    def assess_prompt_quality(self, prompt_text: str, requirements: UserRequirements) -> QualityAssessment:
        """Comprehensive quality assessment of a generated prompt"""
        
        if not self.available:
            return self._fallback_assessment(prompt_text, requirements)
        
        try:
            # Create domain-specific evaluation criteria
            evaluation_prompt = self._create_evaluation_prompt(prompt_text, requirements)
            
            # Call GPT-4 for assessment
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": """You are an expert prompt engineering evaluator with deep knowledge of the Ultimate LLM Prompt Engineering Guide. Your task is to assess prompt quality across multiple dimensions and provide actionable feedback. You must respond with valid JSON only."""
                    },
                    {
                        "role": "user",
                        "content": evaluation_prompt
                    }
                ],
                temperature=0.2,  # Lower temperature for consistent evaluation
                max_tokens=2000
            )
            
            # Parse the assessment
            raw_assessment = response.choices[0].message.content.strip()
            assessment_data = json.loads(raw_assessment)
            
            return self._parse_assessment(assessment_data)
            
        except Exception as e:
            print(f"❌ LLM quality assessment failed: {e}")
            return self._fallback_assessment(prompt_text, requirements)
    
    def _create_evaluation_prompt(self, prompt_text: str, requirements: UserRequirements) -> str:
        """Create a comprehensive evaluation prompt for the LLM judge"""
        
        # Domain-specific criteria
        domain_criteria = self._get_domain_criteria(requirements.domain)
        
        evaluation_prompt = f"""Evaluate this generated prompt for quality and effectiveness according to advanced prompt engineering principles.

## PROMPT TO EVALUATE:
```
{prompt_text}
```

## CONTEXT & REQUIREMENTS:
- **Task Type**: {requirements.task_type}
- **Domain**: {requirements.domain}  
- **Complexity**: {requirements.complexity}
- **Target Audience**: {requirements.audience}
- **Safety Level**: {requirements.safety_level}
- **Specific Needs**: {requirements.specific_needs or "None specified"}

## EVALUATION DIMENSIONS:

### 1. Clarity & Structure (0-10)
- Are instructions clear and unambiguous?
- Is the prompt well-organized and logical?
- Would a user understand exactly what to do?

### 2. Completeness & Thoroughness (0-10) 
- Does it cover all aspects of the task?
- Are edge cases and constraints addressed?
- Is sufficient context provided?

### 3. Technique Implementation (0-10)
- Are prompt engineering techniques properly implemented?
- Is there evidence of Chain-of-Thought, role assignment, etc.?
- Do techniques work synergistically?

### 4. Domain Expertise (0-10)
- Does it demonstrate deep domain knowledge?
- Are domain-specific terms and practices correctly used?
- Would domain experts find it credible?

### 5. Safety & Ethics (0-10)
- Are appropriate safety measures included?
- Does it prevent harmful or biased outputs?
- Are ethical considerations addressed?

### 6. Effectiveness & Actionability (0-10)
- Would this prompt achieve the intended results?
- Is it actionable and specific enough?
- Does it guide the model effectively?

{domain_criteria}

## REQUIRED JSON RESPONSE FORMAT:
{{
    "overall_score": 0.0,
    "dimension_scores": {{
        "clarity_structure": 0.0,
        "completeness": 0.0, 
        "technique_implementation": 0.0,
        "domain_expertise": 0.0,
        "safety_ethics": 0.0,
        "effectiveness": 0.0
    }},
    "strengths": ["strength1", "strength2", "strength3"],
    "weaknesses": ["weakness1", "weakness2"],
    "specific_feedback": "Detailed analysis of the prompt's quality...",
    "recommendations": ["improvement1", "improvement2", "improvement3"],
    "confidence": 0.95
}}

Provide honest, constructive evaluation focusing on actionable improvements."""

        return evaluation_prompt
    
    def _get_domain_criteria(self, domain: str) -> str:
        """Get domain-specific evaluation criteria"""
        
        domain_criteria = {
            "healthcare": """
### Domain-Specific Criteria (Healthcare):
- Medical accuracy and appropriate disclaimers
- HIPAA compliance and patient privacy considerations
- Clinical workflow integration
- Evidence-based practice references
- Professional liability protections""",
            
            "legal": """
### Domain-Specific Criteria (Legal):
- Legal accuracy and jurisdiction awareness
- Citation and reference standards
- Professional ethics and confidentiality
- Regulatory compliance considerations
- Risk mitigation and disclaimers""",
            
            "finance": """
### Domain-Specific Criteria (Finance):
- Financial regulation compliance
- Risk disclosure and disclaimers
- Market volatility considerations
- Fiduciary responsibility awareness
- Data security and privacy""",
            
            "technology": """
### Domain-Specific Criteria (Technology):
- Technical accuracy and best practices
- Security and privacy considerations
- Scalability and performance factors
- Industry standards compliance
- Innovation and forward-thinking""",
        }
        
        return domain_criteria.get(domain, """
### Domain-Specific Criteria (General):
- Industry best practices adherence
- Professional standards compliance
- Appropriate terminology usage
- Contextual relevance and accuracy""")
    
    def _parse_assessment(self, assessment_data: dict) -> QualityAssessment:
        """Parse the LLM assessment into structured format"""
        
        return QualityAssessment(
            overall_score=assessment_data.get("overall_score", 7.0),
            dimension_scores=assessment_data.get("dimension_scores", {}),
            strengths=assessment_data.get("strengths", []),
            weaknesses=assessment_data.get("weaknesses", []),
            specific_feedback=assessment_data.get("specific_feedback", ""),
            recommendations=assessment_data.get("recommendations", []),
            confidence=assessment_data.get("confidence", 0.8)
        )
    
    def _fallback_assessment(self, prompt_text: str, requirements: UserRequirements) -> QualityAssessment:
        """Fallback assessment when LLM judge is unavailable"""
        
        # Basic rule-based assessment
        score = 7.0
        strengths = ["Generated prompt available"]
        weaknesses = ["LLM judge unavailable for detailed assessment"]
        
        if len(prompt_text) > 100:
            score += 0.5
            strengths.append("Adequate prompt length")
        
        if any(word in prompt_text.lower() for word in ["you are", "task", "format"]):
            score += 0.5
            strengths.append("Basic structure elements present")
        
        return QualityAssessment(
            overall_score=min(score, 10.0),
            dimension_scores={
                "clarity_structure": score,
                "completeness": score - 1.0,
                "technique_implementation": score - 0.5,
                "domain_expertise": score - 1.0,
                "safety_ethics": score - 0.5,
                "effectiveness": score
            },
            strengths=strengths,
            weaknesses=weaknesses,
            specific_feedback="Fallback assessment - LLM judge unavailable for detailed analysis",
            recommendations=["Consider enabling LLM judge for comprehensive assessment"],
            confidence=0.6
        )
    
    def format_assessment_report(self, assessment: QualityAssessment, requirements: UserRequirements) -> str:
        """Format assessment into a readable report"""
        
        report = f"""
🎯 LLM QUALITY JUDGE ASSESSMENT
{'=' * 50}

📊 OVERALL SCORE: {assessment.overall_score:.1f}/10.0
🎖️  CONFIDENCE: {assessment.confidence:.1%}

📈 DIMENSION BREAKDOWN:
"""
        
        dimension_names = {
            "clarity_structure": "Clarity & Structure",
            "completeness": "Completeness",
            "technique_implementation": "Technique Implementation", 
            "domain_expertise": f"{requirements.domain.title()} Expertise",
            "safety_ethics": "Safety & Ethics",
            "effectiveness": "Effectiveness"
        }
        
        for dim_key, score in assessment.dimension_scores.items():
            name = dimension_names.get(dim_key, dim_key.replace('_', ' ').title())
            bars = "█" * int(score) + "░" * (10 - int(score))
            report += f"   {name:<20} [{bars}] {score:.1f}/10\n"
        
        report += f"""
✅ STRENGTHS:
{chr(10).join(['   • ' + strength for strength in assessment.strengths])}

⚠️  AREAS FOR IMPROVEMENT:
{chr(10).join(['   • ' + weakness for weakness in assessment.weaknesses])}

🔍 DETAILED FEEDBACK:
   {assessment.specific_feedback}

💡 RECOMMENDATIONS:
{chr(10).join(['   • ' + rec for rec in assessment.recommendations])}

{'=' * 50}
"""
        return report


def test_llm_quality_judge():
    """Test the LLM Quality Judge system"""
    
    print("🧪 TESTING LLM QUALITY JUDGE")
    print("=" * 50)
    
    # Create test prompt and requirements
    test_prompt = """As an expert healthcare professional with over 15 years of clinical experience, analyze the following patient symptoms and provide a systematic differential diagnosis.

Let me work through this step by step:

Step 1: Review the presenting symptoms and patient history
Step 2: Categorize symptoms by system and severity
Step 3: Generate differential diagnosis list
Step 4: Rank diagnoses by likelihood
Step 5: Recommend next steps and follow-up

Please ensure your response is:
- Formatted with clear medical terminology
- Includes appropriate disclaimers about professional consultation
- Structured with numbered sections and bullet points
- Based on evidence-based medical practices

Remember: This analysis is for educational purposes only and should not replace professional medical advice."""

    requirements = UserRequirements(
        task_type="analysis",
        target_model="gpt-4",
        domain="healthcare",
        complexity="moderate",
        audience="expert",
        output_format="structured",
        creativity="balanced", 
        safety_level="high",
        specific_needs="Medical differential diagnosis with systematic analysis",
        session_id="test"
    )
    
    # Test the judge
    from prompt_generator import OPENAI_API_KEY
    judge = LLMQualityJudge(OPENAI_API_KEY)
    
    print("🔍 Assessing prompt quality...")
    assessment = judge.assess_prompt_quality(test_prompt, requirements)
    
    # Display results
    report = judge.format_assessment_report(assessment, requirements)
    print(report)
    
    return assessment


if __name__ == "__main__":
    test_llm_quality_judge()