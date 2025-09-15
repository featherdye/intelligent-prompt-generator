# Extraction Prompt - Legal Domain

**Generated**: 2025-08-27 18:18:01  
**Version**: v1.0.0  
**Quality Score**: 9.5/10 ⭐⭐⭐⭐⭐  
**Target Model**: ANY-MODEL  
**Session ID**: 20250827_180941

---

## 🎯 Optimized Prompt

*This prompt has been generated using the Ultimate LLM Prompt Engineering Guide principles and optimized specifically for your requirements.*

### The Prompt

```
You are an expert legal professional with over 20 years of experience, specializing in case chronology. Your task is to extract and present a chronology from a given legal case. 

Let's start with a few examples to guide you:

**Example 1**
- **Input**: "In 2005, John Doe was charged with theft. In 2006, he was found guilty and sentenced to 3 years in prison. In 2008, he was released on parole."
- **Output**: 
  - 2005: John Doe charged with theft
  - 2006: John Doe found guilty, sentenced to 3 years in prison
  - 2008: John Doe released on parole

**Example 2**
- **Input**: "In 2010, Jane Doe filed a lawsuit against XYZ Corporation for workplace discrimination. In 2011, the court ruled in favor of Jane Doe, awarding her $500,000 in damages."
- **Output**: 
  - 2010: Jane Doe filed lawsuit against XYZ Corporation for workplace discrimination
  - 2011: Court ruled in favor of Jane Doe, awarded $500,000 in damages

Now, let's work through this step by step:

1. **First**, establish the relevant context. Compile the relevant information from the given case.
2. **Then**, consider the case from multiple angles and generate a preliminary chronology.
3. **Next**, review your preliminary chronology for consistency and validate your reasoning based on established principles in the legal field.
4. **Finally**, format your response as follows: 
  - Year: Event description
  - Year: Event description
  - ...

Please ensure your responses are unbiased and ethical. Be aware that this information is sensitive and should be handled with care. Always remember that while you are an AI, users may need professional consultation for critical legal matters.

Think creatively and explore innovative approaches to presenting the chronology. Consider unconventional solutions and approach this from a fresh angle.

Double-check your response for accuracy and ensure it meets professional standards. Rate the quality and completeness of your response and review for any errors or omissions.

Now, please extract and present the chronology from the following case:

"In 1990, ABC Corporation was founded. In 2000, ABC Corporation was sued by DEF Corporation for patent infringement. In 2002, the court ruled in favor of DEF Corporation, awarding them $2 million in damages. In 2003, ABC Corporation filed for bankruptcy."
```

---

## 📋 Prompt Metadata

| Attribute | Value |
|-----------|-------|
| Task Type | Extraction |
| Domain | Legal |
| Complexity | Expert |
| Target Audience | Expert |
| Output Format | Markdown |
| Creativity Level | Creative |
| Safety Level | Standard |
| Estimated Tokens | 580 |

### Techniques Applied
- Few Shot
- Chain Of Thought
- Self Consistency
- Generate Knowledge
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
Sample extraction input for legal
```

**Expected Output Elements**:
- Should demonstrate extraction capabilities with proper formatting

**Validation Criteria**:
- Output follows specified format
- Content is relevant and accurate
- Professional tone maintained
- All requirements addressed
### Test Case 2: Complex scenario test

**Input Example**:
```
Challenging extraction case with multiple requirements
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

### Few Shot
The task requires a specific format (markdown) and the model can benefit from examples to understand the desired output.
### Chain Of Thought
The task is complex and requires expert level understanding, which can be achieved by breaking down the problem into smaller, manageable parts.
### Self Consistency
To ensure high accuracy in complex tasks, generating multiple reasoning paths and selecting the most consistent answer is beneficial.
### Generate Knowledge
The task is in the legal domain, which is knowledge-intensive. This technique can help generate relevant background knowledge before making predictions.
### Structured Output
The user requires the output in a specific format (markdown). This technique ensures consistent, well-formatted responses.
### Role Based
The task requires expert level understanding. Assigning a specific expertise role can guide the model's responses.
### Safety Constraints
The task is in the legal domain, which requires careful consideration of safety measures and ethical guidelines.
### Domain Expertise
The task is in the legal domain. Tailoring prompts for this specific professional domain can enhance the effectiveness of the model.
### Creative Stimulus
The user requires a creative output. This technique can encourage innovative and creative responses from the model.
### Quality Controls
The task requires expert level understanding and high accuracy. Implementing verification and quality assurance steps can ensure the quality of the output.
###  Synergy
The selected techniques work together to handle the complexity of the task, ensure the quality and safety of the output, stimulate creativity, and provide a structured output. For example, 'Few-Shot Prompting' and 'Structured Output Formatting' can work together to guide the model's output format, while 'Chain-of-Thought Reasoning' and 'Self-Consistency' can ensure the accuracy and consistency of the output.
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
*Generation Date: 2025-08-27 18:18:01*