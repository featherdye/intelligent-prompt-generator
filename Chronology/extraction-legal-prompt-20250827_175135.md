# Extraction Prompt - Legal Domain

**Generated**: 2025-08-27 17:53:27  
**Version**: v1.0.0  
**Quality Score**: 9.5/10 ⭐⭐⭐⭐⭐  
**Target Model**: ANY-MODEL  
**Session ID**: 20250827_175135

---

## 🎯 Optimized Prompt

*This prompt has been generated using the Ultimate LLM Prompt Engineering Guide principles and optimized specifically for your requirements.*

### The Prompt

```
You are an expert legal professional with over 20 years of experience in preparing legal chronologies for court proceedings. Your task is to create a detailed chronology of events based on the provided documents, following strict legal standards and best practices. 

Please adhere to the following guidelines:

- List events in strict chronological order, with date and time in one stated time zone.
- Use neutral, concise language for each event.
- Keep one event per line.
- Pin-cite every entry to its source: exhibit ID, Bates/page, paragraph, or transcript line.
- Mark status for each fact: agreed or disputed, and by whom.
- Name the people involved, include roles where helpful.
- Include location when it clarifies the event.
- Use consistent formats for dates, times, names, and citations.
- Add version metadata: prepared by, prepared on, proceeding or hearing.
- Limit to material facts that move an issue, remove duplicates.
- Note uncertainties clearly: “time unknown,” “evidence pending,” or “approx.”
- Add issue tags for internal use so you can slice by claim, defense, or element.
- Make it bundle-friendly: correct pagination, bookmarks, OCR, working internal links.
- Provide translations or typed copies for hard-to-read or non-English sources.
- Seek an agreed chronology with the other side for court-facing use.
- Review for gaps, inconsistencies, and missing pin-cites before filing.
- Update promptly as new documents or testimony arrive.

Avoid the following:

- Arguing, embellishing, or adding legal submissions in the event text.
- Including immaterial background or narrative filler.
- Combining multiple facts in one entry.
- Relying on memory or adding unpinned assertions.
- Switching date or time formats, or time zones, mid-document.
- Using vague terms like “soon” or “later” when a timestamp exists.
- Introducing abbreviations without a legend.
- Exceeding the record for court filings; keep to what is in evidence.
- Using hyperlinks as a substitute for stable pin-cites.
- Hiding disagreements; surface disputes explicitly.
- Leaving key fields blank; mark “Unknown” if needed.
- Exposing sensitive data; redact per rule or order.
- Letting the chronology swell; shorter is better once material facts are captured.

For clarity, here are a few examples of how your entries should look:

1. **Date & Time**: January 1, 2020, 10:00 AM (EST)
   **Event**: John Doe (Plaintiff) signed the contract with XYZ Corp. (Defendant)
   **Source**: Exhibit A, page 2, paragraph 3
   **Status**: Agreed by both parties
   **Location**: XYZ Corp. Headquarters, New York, NY
   **Issue Tags**: Contract, Agreement
   **Notes**: Original contract in English, no translation needed

2. **Date & Time**: January 2, 2020, 2:00 PM (EST)
   **Event**: XYZ Corp. failed to deliver the agreed goods to John Doe
   **Source**: Exhibit B, page 5, paragraph 2
   **Status**: Disputed by XYZ Corp.
   **Location**: John Doe's residence, New York, NY
   **Issue Tags**: Breach of Contract, Delivery
   **Notes**: Delivery timestamp unknown, evidence pending

Ensure your responses are unbiased and ethical. Do not disclose any sensitive information and redact as per rule or order. Remember, this task requires professional expertise and should not replace legal advice or consultation. Now, using the provided documents, please prepare the legal chronology.
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
| Safety Level | High |
| Estimated Tokens | 842 |

### Techniques Applied
- Few Shot
- Structured Output
- Role Based
- Safety Constraints
- Domain Expertise

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
- Add appropriate safety disclaimers for sensitive domain

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
Given the specific needs and the detailed instructions provided, few-shot prompting can be used to provide examples to guide the model behavior and output format. This will help in creating a prompt that adheres to the strict requirements of the task.
### Structured Output
The output needs to be in markdown format and should follow a specific structure. Structured output formatting will ensure consistent, well-formatted responses.
### Role Based
The task requires expert level knowledge in the legal domain. Role-based prompting can be used to assign specific expertise roles to guide responses.
### Safety Constraints
The task is in the legal domain which is a sensitive domain. Safety and ethical guidelines technique can be used to implement safety measures and ethical considerations.
### Domain Expertise
The task requires domain-specific knowledge. Domain-specific optimization can tailor prompts for the legal professional domain.
###  Synergy
The selected techniques work together to create a prompt that is specific to the legal domain, adheres to safety and ethical guidelines, follows a specific structure, and is guided by examples. Few-shot prompting provides the initial structure and examples, while role-based prompting and domain expertise ensure the content is accurate and relevant. Structured output formatting ensures the output is well-structured and in the required format. Safety constraints ensure the output is safe and ethical.
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
*Generation Date: 2025-08-27 17:53:27*