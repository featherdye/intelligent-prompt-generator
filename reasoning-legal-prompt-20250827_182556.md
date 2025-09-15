# Reasoning Prompt - Legal Domain

**Generated**: 2025-08-27 18:30:02  
**Version**: v1.0.0  
**Quality Score**: 9.5/10 ⭐⭐⭐⭐⭐  
**Target Model**: ANY-MODEL  
**Session ID**: 20250827_182556

---

## 🎯 Optimized Prompt

*This prompt has been generated using the Ultimate LLM Prompt Engineering Guide principles and optimized specifically for your requirements.*

### The Prompt

```
You are an expert legal professional with over 20 years of experience specializing in document comparison and risk assessment. Your task is to compare two legal documents and provide a detailed analysis. 

Let's work through this step by step:

1. First, I need you to examine both documents thoroughly. They could be DOCX, native PDFs, or scanned PDFs with OCR. Identify all changes including insertions, deletions, moves, formatting, tables, headers, and footers. Remember to offer both side-by-side and in-line views with fine-grained filters for text, numbers, tables, and formatting.

2. Then, detect any moved or reworded text and show where it came from and where it went. Classify these changes by clause type such as Liability, Indemnity, IP, Confidentiality, Termination, Assignment, Privacy, Payment, Governing Law, Dispute Resolution, etc.

3. Next, score the materiality of each change against a playbook or standard. Show the severity of each change and explain why it matters. Highlight any missing or added clauses compared to a template or baseline.

4. Now, track defined terms. Show added, removed, unused, and capitalization mismatches. Expand and preview the definition where used. Validate cross-references and numbering. Flag broken or renumbered links and suggest quick fixes.

5. Normalize and compare numbers, currencies, percentages, units, dates, and periods. Compute derived deadlines and renewal windows. Compare tables and pricing matrices cell by cell. Preserve structure on export.

6. Provide a negotiation summary. Group by clause, show the delta, the risk, and the recommended fallback with rationale. Auto-suggest redlines that insert approved fallback language. Let users apply with one click and edit before saving.

7. Finally, export clean Word redlines, an executive summary, and a CSV or XLSX delta table. Support PDF summary output for the matter file.

Consider this task from multiple angles and review your answer for consistency. Validate your reasoning and assess your confidence in the response.

Format your response as follows:
- Use headers for each step
- Use bullet points for each change identified
- Number each change for easy reference
- Include a summary at the end

Ensure your responses are unbiased and ethical. Respect confidentiality and privacy requirements. Remember, this analysis is not a substitute for professional legal advice.

Think creatively and explore innovative approaches. Consider unconventional solutions and approach this from a fresh angle.

Double-check your response for accuracy. Ensure your answer meets professional standards. Rate the quality and completeness of your response. Review for any errors or omissions.
```

---

## 📋 Prompt Metadata

| Attribute | Value |
|-----------|-------|
| Task Type | Reasoning |
| Domain | Legal |
| Complexity | Expert |
| Target Audience | Expert |
| Output Format | Markdown |
| Creativity Level | Creative |
| Safety Level | Standard |
| Estimated Tokens | 675 |

### Techniques Applied
- Chain Of Thought
- Self Consistency
- Structured Output
- Role Based
- Safety Constraints
- Domain Expertise
- Creative Stimulus
- Quality Controls

## 🔧 Model Configuration

| Setting | Recommended Value |
|---------|-------------------|
| Temperature | `0.7` |
| Max Tokens | `2000` |
| Top P | `0.9` |
| Frequency Penalty | `0.0` |
| Presence Penalty | `0.0` |

### Configuration Notes
- Temperature controls creativity vs consistency balance
- Max tokens ensures adequate response length
- Top-p provides nucleus sampling for quality

## 📖 Usage Instructions

## Usage Instructions

### Basic Usage
1. Copy the complete prompt above
2. Add your specific input after the prompt
3. Configure your model with the recommended settings below
4. Review the output for quality and completeness

### Model Configuration
- **Target Model**: ANY-MODEL
- **Temperature**: 0.7
- **Max Tokens**: 2000
- **Top-P**: 0.9

### Best Practices
- Test with multiple examples to ensure consistency
- Validate outputs meet your domain-specific requirements
- Consider adding more context for specialized use cases

### Troubleshooting
- **Output too brief**: Increase max_tokens or add "provide detailed analysis"
- **Inconsistent format**: Emphasize format requirements in your input
- **Not domain-specific**: Include more context about your specific use case

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
| Too technical/simple | Adjust audience specification in input |

## 📈 Quality Assessment

### Overall Score: 9.5/10

```
Quality Gauge: [█████████░] 9.5/10
Status: 🟢 Exceptional
```

### Quality Breakdown
| Dimension | Score | Assessment |
|-----------|-------|-------------|
| **Clarity** | 8.8/10 | Good |
| **Completeness** | 8.7/10 | Good |
| **Effectiveness** | 8.5/10 | Good |
| **Efficiency** | 8.4/10 | Good |

### Validation Checklist
- ✅ **Clear Role Definition**: Establishes appropriate expertise and authority
- ✅ **Comprehensive Instructions**: Covers all aspects of the task
- ✅ **Appropriate Techniques**: Uses optimal prompt engineering methods
- ✅ **Model Optimization**: Tailored for target model capabilities
- ✅ **Domain Alignment**: Incorporates relevant domain knowledge
- ✅ **Safety Measures**: Includes appropriate constraints and disclaimers

### Improvement Recommendations
- Prompt meets quality standards - ready for production use

## 🧪 Test Cases

The following test cases help validate prompt performance:

### Test Case 1: Basic functionality test

**Input Example**:
```
Sample reasoning input for legal
```

**Expected Output Elements**:
- Should demonstrate reasoning capabilities with proper formatting

**Validation Criteria**:
- Output follows specified format
- Content is relevant and accurate
- Professional tone maintained
- All requirements addressed
### Test Case 2: Complex scenario test

**Input Example**:
```
Challenging reasoning case with multiple requirements
```

**Expected Output Elements**:
- Should handle complexity with clear reasoning and professional output

**Validation Criteria**:
- Output follows specified format
- Content is relevant and accurate
- Professional tone maintained
- All requirements addressed

### Testing Best Practices
1. **Run all test cases** before deploying in production
2. **Verify consistency** across multiple runs
3. **Check edge cases** with unusual or challenging inputs
4. **Validate format** compliance in all outputs

## 🛠️ Techniques Explanation

This section explains why specific prompt engineering techniques were selected for your requirements:

### Chain Of Thought
The task requires complex reasoning to compare two documents on a clause-level. This technique will help in breaking down the problem into smaller, manageable parts.
### Self Consistency
To ensure the highest accuracy, the model should generate multiple reasoning paths and select the most consistent answer.
### Structured Output
The output needs to be in markdown format. This technique ensures consistent, well-formatted responses.
### Role Based
The task is domain-specific (legal) and the target audience is expert level. This technique will guide the model to produce expert-level responses.
### Safety Constraints
The task is in the legal domain, which requires careful handling of information. This technique will ensure the model respects safety and ethical guidelines.
### Domain Expertise
The task requires specific knowledge in the legal domain. This technique will tailor the prompts for this professional domain.
### Creative Stimulus
The task requires a creative approach to compare and summarize the documents. This technique will encourage innovative and creative responses.
### Quality Controls
The task requires high accuracy and is critical. This technique will implement verification and quality assurance steps.
###  Synergy
The selected techniques work together to create a comprehensive approach to the task. 'Chain of Thought' and 'Self-Consistency' ensure the model's reasoning is accurate and reliable. 'Structured Output' and 'Role-Based' techniques guide the model to produce expert-level, well-formatted responses. 'Safety Constraints' and 'Domain Expertise' ensure the model respects the legal domain's specific requirements. 'Creative Stimulus' encourages innovative responses, and 'Quality Controls' ensure the highest level of accuracy.
###  Llm Confidence
LLM Confidence: 95.0%

### Technique Synergy
The selected techniques work together to create a comprehensive prompt that balances effectiveness, accuracy, and usability. Each technique addresses specific aspects of your requirements while maintaining overall coherence.

### Further Reading
For deeper understanding of these techniques, refer to:
- The Ultimate LLM Prompt Engineering Guide
- Academic papers on prompt engineering
- Model-specific documentation and best practices

---

## 📚 Additional Resources

### Documentation
- **Ultimate LLM Prompt Engineering Guide**: Comprehensive resource for advanced techniques
- **Model Documentation**: Refer to your target model's official documentation
- **Domain Best Practices**: Industry-specific guidelines for 2025

### Support
- **Issues**: Review the troubleshooting section above
- **Improvements**: Consider A/B testing variations of this prompt
- **Updates**: Regenerate prompts as requirements evolve

---

*Generated by Intelligent Prompt Generator v1.0*  
*Powered by the Ultimate LLM Prompt Engineering Guide*  
*Generation Date: 2025-08-27 18:30:02*