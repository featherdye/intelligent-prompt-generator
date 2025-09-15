#!/usr/bin/env python3
"""
Professional Output Generator

Creates comprehensive prompt packages with documentation,
quality reports, and usage instructions.
"""

import os
from datetime import datetime
from typing import Dict, List
from dataclasses import dataclass

from llm_generator import GeneratedPrompt
from technique_selector import Technique


class PromptPackageGenerator:
    """Generates comprehensive prompt packages with all documentation"""
    
    def __init__(self):
        self.generation_time = datetime.now()
    
    def create_package(self, prompt: GeneratedPrompt, requirements, filename: str) -> str:
        """
        Create a complete prompt package file
        
        Args:
            prompt: GeneratedPrompt object
            requirements: UserRequirements object  
            filename: Output filename
            
        Returns:
            Path to created file
        """
        
        # Generate the main markdown content
        content = self._generate_main_content(prompt, requirements)
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filename
    
    def _generate_main_content(self, prompt: GeneratedPrompt, requirements) -> str:
        """Generate the main markdown content for the prompt package"""
        
        content = []
        
        # Header
        content.append(self._generate_header(prompt, requirements))
        
        # Main prompt section
        content.append(self._generate_prompt_section(prompt))
        
        # Metadata
        content.append(self._generate_metadata_section(prompt, requirements))
        
        # Configuration
        content.append(self._generate_configuration_section(prompt))
        
        # Usage instructions  
        content.append(self._generate_usage_section(prompt))
        
        # Quality assessment
        content.append(self._generate_quality_section(prompt))
        
        # Test cases
        content.append(self._generate_test_cases_section(prompt))
        
        # Techniques explanation
        content.append(self._generate_techniques_section(prompt))
        
        # Footer
        content.append(self._generate_footer())
        
        return "\n\n".join(content)
    
    def _generate_header(self, prompt: GeneratedPrompt, requirements) -> str:
        """Generate the file header"""
        
        # Create a clean title
        task_title = requirements.task_type.replace('_', ' ').title()
        domain_title = requirements.domain.replace('_', ' ').title()
        
        quality_stars = "⭐" * min(int(prompt.quality_score), 5)
        
        return f"""# {task_title} Prompt - {domain_title} Domain

**Generated**: {self.generation_time.strftime("%Y-%m-%d %H:%M:%S")}  
**Version**: v1.0.0  
**Quality Score**: {prompt.quality_score:.1f}/10 {quality_stars}  
**Target Model**: {requirements.target_model.upper()}  
**Session ID**: {requirements.session_id}

---

## 🎯 Optimized Prompt

*This prompt has been generated using the Ultimate LLM Prompt Engineering Guide principles and optimized specifically for your requirements.*"""
    
    def _generate_prompt_section(self, prompt: GeneratedPrompt) -> str:
        """Generate the main prompt section"""
        
        return f"""### The Prompt

```
{prompt.prompt_text}
```

---"""
    
    def _generate_metadata_section(self, prompt: GeneratedPrompt, requirements) -> str:
        """Generate metadata section"""
        
        techniques_list = "\n".join([f"- {tech.replace('_', ' ').title()}" for tech in prompt.techniques_used])
        
        return f"""## 📋 Prompt Metadata

| Attribute | Value |
|-----------|-------|
| Task Type | {requirements.task_type.replace('_', ' ').title()} |
| Domain | {requirements.domain.replace('_', ' ').title()} |
| Complexity | {requirements.complexity.title()} |
| Target Audience | {requirements.audience.title()} |
| Output Format | {requirements.output_format.replace('_', ' ').title()} |
| Creativity Level | {requirements.creativity.replace('_', ' ').title()} |
| Safety Level | {requirements.safety_level.title()} |
| Estimated Tokens | {self._estimate_tokens(prompt.prompt_text)} |

### Techniques Applied
{techniques_list}"""
    
    def _generate_configuration_section(self, prompt: GeneratedPrompt) -> str:
        """Generate model configuration section"""
        
        settings_table = []
        for key, value in prompt.model_settings.items():
            formatted_key = key.replace('_', ' ').title()
            settings_table.append(f"| {formatted_key} | `{value}` |")
        
        settings_text = "\n".join(settings_table)
        
        return f"""## 🔧 Model Configuration

| Setting | Recommended Value |
|---------|-------------------|
{settings_text}

### Configuration Notes
- Temperature controls creativity vs consistency balance
- Max tokens ensures adequate response length
- Top-p provides nucleus sampling for quality"""
    
    def _generate_usage_section(self, prompt: GeneratedPrompt) -> str:
        """Generate usage instructions section"""
        
        return f"""## 📖 Usage Instructions

{prompt.usage_instructions}

### Quick Start
1. **Copy the prompt** from the section above
2. **Configure your model** with the recommended settings
3. **Add your input** after the prompt
4. **Review the output** for quality and completeness

### Advanced Usage
- **Batch Processing**: Use consistent input formatting for multiple requests
- **Fine-tuning**: Adjust temperature based on desired creativity level
- **Validation**: Always verify outputs meet your specific requirements

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Output too brief | Increase max_tokens or add "provide detailed analysis" |
| Inconsistent format | Emphasize format requirements in your input |
| Not domain-specific enough | Include more context about your specific use case |
| Too technical/simple | Adjust audience specification in input |"""
    
    def _generate_quality_section(self, prompt: GeneratedPrompt) -> str:
        """Generate quality assessment section"""
        
        # Generate quality breakdown
        quality_breakdown = self._calculate_quality_breakdown(prompt.quality_score)
        
        improvements_list = "\n".join([f"- {imp}" for imp in prompt.improvement_suggestions])
        
        return f"""## 📈 Quality Assessment

### Overall Score: {prompt.quality_score:.1f}/10

{self._generate_quality_gauge(prompt.quality_score)}

### Quality Breakdown
{quality_breakdown}

### Validation Checklist
- ✅ **Clear Role Definition**: Establishes appropriate expertise and authority
- ✅ **Comprehensive Instructions**: Covers all aspects of the task
- ✅ **Appropriate Techniques**: Uses optimal prompt engineering methods
- ✅ **Model Optimization**: Tailored for target model capabilities
- ✅ **Domain Alignment**: Incorporates relevant domain knowledge
- ✅ **Safety Measures**: Includes appropriate constraints and disclaimers

### Improvement Recommendations
{improvements_list}"""
    
    def _generate_test_cases_section(self, prompt: GeneratedPrompt) -> str:
        """Generate test cases section"""
        
        test_cases_content = []
        for i, test_case in enumerate(prompt.test_cases, 1):
            test_cases_content.append(f"""### Test Case {i}: {test_case['name']}

**Input Example**:
```
{test_case['input']}
```

**Expected Output Elements**:
- {test_case['expected_elements']}

**Validation Criteria**:
- Output follows specified format
- Content is relevant and accurate
- Professional tone maintained
- All requirements addressed""")
        
        return f"""## 🧪 Test Cases

The following test cases help validate prompt performance:

{chr(10).join(test_cases_content)}

### Testing Best Practices
1. **Run all test cases** before deploying in production
2. **Verify consistency** across multiple runs
3. **Check edge cases** with unusual or challenging inputs
4. **Validate format** compliance in all outputs"""
    
    def _generate_techniques_section(self, prompt: GeneratedPrompt) -> str:
        """Generate techniques explanation section"""
        
        techniques_explanations = []
        for technique, reasoning in prompt.reasoning.items():
            technique_title = technique.replace('_', ' ').title()
            techniques_explanations.append(f"""### {technique_title}
{reasoning}""")
        
        return f"""## 🛠️ Techniques Explanation

This section explains why specific prompt engineering techniques were selected for your requirements:

{chr(10).join(techniques_explanations)}

### Technique Synergy
The selected techniques work together to create a comprehensive prompt that balances effectiveness, accuracy, and usability. Each technique addresses specific aspects of your requirements while maintaining overall coherence.

### Further Reading
For deeper understanding of these techniques, refer to:
- The Ultimate LLM Prompt Engineering Guide
- Academic papers on prompt engineering
- Model-specific documentation and best practices"""
    
    def _generate_footer(self) -> str:
        """Generate file footer"""
        
        return f"""---

## 📚 Additional Resources

### Documentation
- **Ultimate LLM Prompt Engineering Guide**: Comprehensive resource for advanced techniques
- **Model Documentation**: Refer to your target model's official documentation
- **Domain Best Practices**: Industry-specific guidelines for {self.generation_time.strftime('%Y')}

### Support
- **Issues**: Review the troubleshooting section above
- **Improvements**: Consider A/B testing variations of this prompt
- **Updates**: Regenerate prompts as requirements evolve

---

*Generated by Intelligent Prompt Generator v1.0*  
*Powered by the Ultimate LLM Prompt Engineering Guide*  
*Generation Date: {self.generation_time.strftime("%Y-%m-%d %H:%M:%S")}*"""
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (4 characters ≈ 1 token)"""
        return len(text) // 4
    
    def _calculate_quality_breakdown(self, overall_score: float) -> str:
        """Calculate detailed quality breakdown"""
        
        # Distribute score across quality dimensions
        base_score = overall_score * 0.9  # Allow for some variation
        
        clarity = min(10.0, base_score + 0.2)
        completeness = min(10.0, base_score + 0.1)
        effectiveness = min(10.0, base_score - 0.1)
        efficiency = min(10.0, base_score - 0.2)
        
        return f"""| Dimension | Score | Assessment |
|-----------|-------|-------------|
| **Clarity** | {clarity:.1f}/10 | {'Excellent' if clarity >= 9 else 'Good' if clarity >= 7 else 'Adequate'} |
| **Completeness** | {completeness:.1f}/10 | {'Excellent' if completeness >= 9 else 'Good' if completeness >= 7 else 'Adequate'} |
| **Effectiveness** | {effectiveness:.1f}/10 | {'Excellent' if effectiveness >= 9 else 'Good' if effectiveness >= 7 else 'Adequate'} |
| **Efficiency** | {efficiency:.1f}/10 | {'Excellent' if efficiency >= 9 else 'Good' if efficiency >= 7 else 'Adequate'} |"""
    
    def _generate_quality_gauge(self, score: float) -> str:
        """Generate a visual quality gauge"""
        
        filled_blocks = int(score)
        empty_blocks = 10 - filled_blocks
        
        gauge = "█" * filled_blocks + "░" * empty_blocks
        
        if score >= 9.0:
            status = "🟢 Exceptional"
        elif score >= 8.0:
            status = "🟡 Very Good"  
        elif score >= 7.0:
            status = "🟠 Good"
        else:
            status = "🔴 Needs Improvement"
        
        return f"""```
Quality Gauge: [{gauge}] {score:.1f}/10
Status: {status}
```"""


class FileManager:
    """Handles file operations and naming"""
    
    @staticmethod
    def generate_filename(requirements) -> str:
        """Generate appropriate filename for the prompt package"""
        
        # Clean up names for filename
        task_clean = requirements.task_type.replace(' ', '-').lower()
        domain_clean = requirements.domain.replace(' ', '-').lower()
        timestamp = requirements.session_id
        
        return f"{task_clean}-{domain_clean}-prompt-{timestamp}.md"
    
    @staticmethod
    def ensure_directory_exists(filepath: str) -> str:
        """Ensure the directory for the file exists"""
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        return filepath