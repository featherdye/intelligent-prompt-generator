# Extraction Prompt - Legal Domain

**Generated**: 2025-08-27 18:21:09  
**Version**: v1.0.0  
**Quality Score**: 9.5/10 ⭐⭐⭐⭐⭐  
**Target Model**: ANY-MODEL  
**Session ID**: 20250827_181938

---

## 🎯 Optimized Prompt

*This prompt has been generated using the Ultimate LLM Prompt Engineering Guide principles and optimized specifically for your requirements.*

### The Prompt

```
You are an expert legal professional with over 15 years of experience in preparing chronologies for court proceedings. Your task is to create a detailed chronology based on the following events, adhering strictly to the best practices and guidelines of the legal profession. 

Remember, you must:

1. List events in chronological order, with date and time, and one stated time zone.
2. Use neutral, concise language for each event.
3. Keep one event per line.
4. Pin-cite every entry to its source: exhibit ID, Bates/page, paragraph, or transcript line.
5. Mark status for each fact: agreed or disputed, and by whom.
6. Name the people involved, include roles where helpful.
7. Include location when it clarifies the event.
8. Use consistent formats for dates, times, names, and citations.
9. Add version metadata: prepared by, prepared on, proceeding or hearing.
10. Limit to material facts that move an issue, remove duplicates.
11. Note uncertainties clearly: “time unknown,” “evidence pending,” or “approx.”
12. Add issue tags for internal use so you can slice by claim, defense, or element.
13. Make it bundle-friendly: correct pagination, bookmarks, OCR, working internal links.
14. Provide translations or typed copies for hard-to-read or non-English sources.
15. Seek an agreed chronology with the other side for court-facing use.
16. Review for gaps, inconsistencies, and missing pin-cites before filing.
17. Update promptly as new documents or testimony arrive.

Avoid:

1. Arguing, embellishing, or adding legal submissions in the event text.
2. Including immaterial background or narrative filler.
3. Combining multiple facts in one entry.
4. Relying on memory or adding unpinned assertions.
5. Switching date or time formats, or time zones, mid-document.
6. Using vague terms like “soon” or “later” when a timestamp exists.
7. Introducing abbreviations without a legend.
8. Exceeding the record for court filings; keep to what is in evidence.
9. Using hyperlinks as a substitute for stable pin-cites.
10. Hiding disagreements; surface disputes explicitly.
11. Leaving key fields blank; mark “Unknown” if needed.
12. Exposing sensitive data; redact per rule or order.
13. Letting the chronology swell; shorter is better once material facts are captured.

Here are the events:

1. On July 1, 2020, John Doe was seen entering the premises of XYZ Corp. at 9:00 AM EST. (Source: CCTV footage, Exhibit A)
2. On July 2, 2020, a confidential document from XYZ Corp. was found in John Doe's possession. (Source: Police report, Exhibit B)
3. On July 3, 2020, John Doe was arrested on charges of corporate espionage. (Source: Arrest warrant, Exhibit C)

Format your response as:

```
1. [Date, Time, Time Zone] - [Event Description] (Source: [Source Description], Status: [Agreed/Disputed], By: [Who Agreed/Disputed])
```

For example:

```
1. July 1, 2020, 9:00 AM EST - John Doe was seen entering the premises of XYZ Corp. (Source: CCTV footage, Exhibit A, Status: Agreed, By: Both parties)
```

Ensure your responses are unbiased and ethical. Confidentiality and privacy must be maintained at all times. This task is for informational purposes only and should not replace professional legal consultation. 

After completing the task, double-check your response for accuracy. Ensure your answer meets professional standards. Review for any errors or omissions. Rate the quality and completeness of your response on a scale of 1-10. 

Think creatively and explore innovative approaches. Consider unconventional solutions and generate multiple creative alternatives. Approach this from a fresh angle. 

Remember, your expertise is critical in ensuring the accuracy and reliability of this chronology.
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
| Creativity Level | Highly Creative |
| Safety Level | Standard |
| Estimated Tokens | 925 |

### Techniques Applied
- Few Shot
- Structured Output
- Role Based
- Safety Constraints
- Domain Expertise
- Creative Stimulus
- Quality Controls

## 🔧 Model Configuration

| Setting | Recommended Value |
|---------|-------------------|
| Temperature | `0.9` |
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
- **Temperature**: 0.9
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
The task requires a specific format and structure. Few-shot prompting can provide examples to guide the model in generating the desired output.
### Structured Output
The output needs to be in markdown format, which can be achieved through structured output formatting.
### Role Based
The task is in the legal domain and requires expert-level knowledge. Role-based prompting can guide the model to generate responses as a legal expert.
### Safety Constraints
The task is in the legal domain which requires careful handling of sensitive information. Safety and ethical guidelines can ensure the model operates within these constraints.
### Domain Expertise
The task requires domain-specific knowledge in the legal field. Domain-specific optimization can tailor the prompts to this professional domain.
### Creative Stimulus
The task requires a high level of creativity. Creative stimulus techniques can encourage the model to generate innovative and creative responses.
### Quality Controls
The task requires high accuracy and professional-level output. Quality control measures can implement verification and quality assurance steps.
###  Synergy
These techniques work together to generate a highly accurate, creative, and domain-specific output in the required format. Few-shot and structured output formatting ensure the correct structure and format, while role-based prompting, safety constraints, and domain expertise ensure the content is accurate and appropriate for the legal domain. Creative stimulus techniques add a level of creativity, and quality controls ensure the overall quality of the output.
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
*Generation Date: 2025-08-27 18:21:09*