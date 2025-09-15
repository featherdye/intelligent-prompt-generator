# Quickstart Guide: Web-Based Prompt Generator

## Overview
This quickstart guide walks through the complete user journey from opening the application to generating and using an optimized prompt.

## Prerequisites
- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- OpenAI API key with GPT-4 or GPT-3.5-turbo access
- Internet connection for API requests

## User Journey: Generate Your First Prompt

### Step 1: Access the Application
1. Navigate to `https://prompt-generator.vercel.app` (or local development URL)
2. The application loads with a split-screen interface:
   - **Left Panel**: Configuration form
   - **Right Panel**: Empty prompt display area

**Expected Result**: Clean, responsive interface with empty form and placeholder text in prompt area.

### Step 2: Enter API Key
1. Locate the "API Key" field at the top of the left panel
2. Enter your OpenAI API key (starts with `sk-proj-` or `sk-`)
3. The application validates the key format and shows a green checkmark

**Expected Result**:
- Key validation feedback appears immediately
- Key is masked in the UI as `sk-proj-***...***XXX`
- Form fields become enabled once valid key is entered

### Step 3: Configure Your Prompt
Fill out the form with your requirements:

**Task Description** (required):
```
Write a comprehensive product review for a new smartphone that helps potential buyers make an informed decision about their purchase.
```

**Target Model**: Select "GPT-4" from dropdown

**Domain**: Select "General" from dropdown

**Complexity Level**: Select "Moderate" from dropdown

**Output Format**: Select "Structured" from dropdown

**Creativity Level**: Set slider to 6/10

**Specific Requirements** (optional):
```
Focus on camera quality, battery life, and user interface. Include both pros and cons. Target length: 300-400 words.
```

**Expected Result**: Form validates in real-time, showing validation messages for any errors.

### Step 4: Generate Prompt
1. Click the "Generate Prompt" button
2. Loading state appears with spinner and "Generating optimized prompt..." message
3. Generation typically takes 3-8 seconds

**Expected Result**:
- Button shows loading state
- Form is disabled during generation
- Progress indicator shows generation in progress

### Step 5: Review Generated Prompt
The right panel displays your optimized prompt with:

**Generated Prompt Content** (example):
```markdown
# Smartphone Review Prompt

You are an experienced technology reviewer who has tested hundreds of smartphones. Your reviews are trusted by consumers for their balanced, detailed analysis.

**Task**: Write a comprehensive review of the [SMARTPHONE_MODEL] that helps potential buyers make an informed purchasing decision.

**Review Structure**:
1. **Overview** (50 words): Brief introduction and first impressions
2. **Camera Performance** (100-120 words): Photo/video quality, features, comparison points
3. **Battery Life** (80-100 words): Usage patterns, charging speed, longevity
4. **User Interface** (80-100 words): Software experience, ease of use, notable features
5. **Pros & Cons** (60-80 words): Balanced list of strengths and weaknesses
6. **Verdict** (30-50 words): Final recommendation and ideal user profile

**Guidelines**:
- Be objective and evidence-based
- Include specific examples and scenarios
- Consider different user types (casual, power user, photographer)
- Target total length: 300-400 words
- Use clear, accessible language
```

**Quality Assessment**:
- Overall Score: 9.2/10
- Clarity: 9.5/10
- Completeness: 9.0/10
- Effectiveness: 9.1/10

**Applied Techniques**:
- ✅ Role-based prompting (technology reviewer persona)
- ✅ Structured output formatting (clear sections)
- ✅ Domain expertise (tech review knowledge)
- ✅ Specific constraints (word count, requirements)

### Step 6: Use Your Prompt
1. Click the "Copy Prompt" button to copy the full prompt to clipboard
2. Or click "Download" to save as a markdown file
3. Use the prompt in your AI tool of choice

**Expected Result**:
- Prompt is copied to clipboard with success message
- Downloaded file named `smartphone_review_prompt_YYYYMMDD.md`

## Advanced Usage

### Regenerate with Modifications
1. Modify any form fields (e.g., change creativity level to 8/10)
2. Click "Generate Prompt" again
3. New prompt appears with updated characteristics

### View Generation History
- Previous prompts remain accessible via history panel (if implemented)
- Compare different versions for the same task

### Error Recovery
If generation fails:
1. Check error message in the right panel
2. Verify API key is still valid
3. Try again after a few seconds (may be temporary rate limiting)

## Validation Scenarios

### Test Case 1: Invalid API Key
**Given**: User enters invalid API key `sk-invalid-key`
**When**: User attempts to generate prompt
**Then**: Error message appears: "Invalid API key format. Please check your key and try again."

### Test Case 2: Empty Task Description
**Given**: User leaves task description empty
**When**: User clicks generate
**Then**: Form validation error: "Task description is required (minimum 10 characters)"

### Test Case 3: Successful Generation
**Given**: Valid API key and complete form
**When**: User clicks generate
**Then**: Optimized prompt appears with quality score 8.0+ and 2+ applied techniques

### Test Case 4: Network Error
**Given**: No internet connection or API unavailable
**When**: User attempts generation
**Then**: Error message: "Network error. Please check your connection and try again."

### Test Case 5: Rate Limit Error
**Given**: User has exceeded OpenAI rate limits
**When**: User attempts generation
**Then**: Error message: "Rate limit reached. Please try again in a few minutes."

## Performance Benchmarks

### Expected Response Times
- Form validation: <100ms
- API key validation: <200ms
- Prompt generation: 3-8 seconds
- UI updates: <50ms

### Quality Targets
- Generated prompts should score 8.0+ overall quality
- At least 2 prompt engineering techniques applied
- Word count accuracy within ±10% of target
- 95%+ user satisfaction with generated prompts

## Browser Compatibility

### Supported Browsers
- ✅ Chrome 90+ (recommended)
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Mobile Support
- Responsive design works on tablets (iPad, Android tablets)
- Phone support available but desktop recommended for optimal experience

## Troubleshooting

### Common Issues
1. **Prompt generation hangs**: Refresh page, check network connection
2. **API key not accepting**: Verify key format and permissions
3. **Form not submitting**: Check all required fields are filled
4. **Low quality scores**: Try increasing complexity level or adding specific requirements

### Getting Help
- Check browser console for detailed error messages
- Verify API key has sufficient credits and permissions
- Try with different configuration options
- Report persistent issues via project repository

---

**Quickstart Complete**: You're ready to generate professional-quality prompts!
**Next Step**: Explore advanced features and technique combinations for specialized use cases.