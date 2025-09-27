import React from 'react'
import { useForm, useWatch } from 'react-hook-form'
import {
  VStack,
  FormControl,
  FormLabel,
  FormErrorMessage,
  Textarea,
  Select,
  Button,
  Text,
  useToast,
  HStack,
  Radio,
  RadioGroup,
  Alert,
  AlertIcon,
  AlertDescription,
} from '@chakra-ui/react'
import { usePromptStore, PromptFormData } from '../store/promptStore'
import { createOpenRouterClient } from '../lib/openrouter-client'

const PromptConfigurationForm: React.FC = () => {
  const toast = useToast()
  const {
    updateFormData,
    setGeneratedPrompt,
    setIsGenerating,
    isGenerating,
    apiKey,
    hasApiKey
  } = usePromptStore()

  const {
    register,
    handleSubmit,
    control,
    formState: { errors, isValid }
  } = useForm<PromptFormData>({
    mode: 'onChange',
    defaultValues: {
      model: 'openai/gpt-4-turbo',
      domain: 'general',
      complexity: 'moderate',
      promptType: 'text',
      imageModel: 'dall-e-3',
      imageStyle: 'photorealistic',
      composition: 'centered',
      artMedium: 'digital-art'
    }
  })

  const promptType = useWatch({ control, name: 'promptType' })

  const calculateMetrics = (content: string) => {
    const characterCount = content.length
    const wordCount = content.trim().split(/\s+/).filter(word => word.length > 0).length
    const estimatedCost = (characterCount / 1000) * 0.02 // Rough estimate
    const qualityScore = Math.min(100, Math.max(50, 70 + (wordCount > 50 ? 10 : 0) + (characterCount > 200 ? 10 : 0)))

    return { characterCount, wordCount, estimatedCost, qualityScore }
  }

  const onSubmit = async (data: PromptFormData) => {
    // Check if API key is set
    if (!hasApiKey()) {
      toast({
        title: 'API Key Required',
        description: 'Please set your OpenRouter API key in the header to generate prompts.',
        status: 'warning',
        duration: 4000,
        isClosable: true,
      })
      return
    }

    try {
      setIsGenerating(true)
      updateFormData(data)

      // Create OpenRouter client
      const client = createOpenRouterClient(apiKey)

      // Generate prompt using OpenRouter with intelligent technique selection
      const promptResult = await client.generatePrompt(data.task, {
        model: data.model,
        domain: data.domain,
        complexity: data.complexity,
        requirements: data.requirements,
        examples: data.examples,
        promptType: data.promptType,
        imageModel: data.imageModel,
        imageStyle: data.imageStyle,
        composition: data.composition,
        artMedium: data.artMedium
      })

      // Calculate metrics from the generated prompt
      const metrics = calculateMetrics(promptResult.prompt)

      // Create the generated prompt object with real techniques
      const generatedPrompt = {
        id: '', // Will be generated in store
        content: promptResult.prompt,
        originalTask: data.task,
        promptType: data.promptType || 'text',
        formData: data,
        qualityScore: metrics.qualityScore,
        estimatedCost: metrics.estimatedCost,
        wordCount: metrics.wordCount,
        characterCount: metrics.characterCount,
        techniques: promptResult.techniques,
        createdAt: new Date()
      }

      console.log('Technique reasoning:', promptResult.reasoning)

      // Update store with generated prompt
      setGeneratedPrompt(generatedPrompt)

      toast({
        title: 'Prompt generated successfully!',
        description: 'Your optimized prompt is ready.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      })

    } catch (error) {
      console.error('Error generating prompt:', error)
      toast({
        title: 'Error generating prompt',
        description: error instanceof Error ? error.message : 'Failed to generate prompt. Please check your API key and try again.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      })
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <VStack spacing={5} align="stretch">
        {/* API Key Status Alert */}
        {!hasApiKey() && (
          <Alert status="warning" borderRadius="md">
            <AlertIcon />
            <AlertDescription>
              Please set your OpenRouter API key in the header to generate prompts.
            </AlertDescription>
          </Alert>
        )}

        {/* Prompt Type Selector */}
        <FormControl>
          <FormLabel>Prompt Type</FormLabel>
          <RadioGroup>
            <HStack spacing={6}>
              <Radio {...register('promptType')} value="text">
                Text Generation
              </Radio>
              <Radio {...register('promptType')} value="image">
                Image Generation
              </Radio>
            </HStack>
          </RadioGroup>
        </FormControl>

        {/* Task Description */}
        <FormControl isInvalid={!!errors.task} isRequired>
          <FormLabel>
            {promptType === 'image' ? 'Image Description' : 'Task Description'}
          </FormLabel>
          <Textarea
            {...register('task', {
              required: promptType === 'image' ? 'Image description is required' : 'Task description is required',
              minLength: {
                value: 10,
                message: promptType === 'image' ? 'Image description must be at least 10 characters' : 'Task description must be at least 10 characters'
              }
            })}
            rows={3}
            placeholder={
              promptType === 'image'
                ? "Describe the image you want to generate (e.g., 'A serene mountain landscape at sunset with a lake reflecting the colors')"
                : "Describe what you want the AI to help you with..."
            }
            resize="vertical"
          />
          <FormErrorMessage>
            {errors.task && errors.task.message}
          </FormErrorMessage>
        </FormControl>

        {/* AI Model Selection */}
        <FormControl>
          <FormLabel>Target AI Model</FormLabel>
          <Select {...register('model')}>
            <option value="openai/gpt-4-turbo">GPT-4 Turbo</option>
            <option value="openai/gpt-4">GPT-4</option>
            <option value="openai/gpt-3.5-turbo">GPT-3.5 Turbo</option>
            <option value="anthropic/claude-3-opus">Claude 3 Opus</option>
            <option value="anthropic/claude-3-sonnet">Claude 3 Sonnet</option>
            <option value="anthropic/claude-3-haiku">Claude 3 Haiku</option>
            <option value="google/gemini-pro">Gemini Pro</option>
            <option value="meta-llama/llama-2-70b-chat">Llama 2 70B</option>
            <option value="mistralai/mixtral-8x7b-instruct">Mixtral 8x7B</option>
          </Select>
        </FormControl>

        {/* Image-specific fields */}
        {promptType === 'image' && (
          <>
            {/* Image Model Selection */}
            <FormControl>
              <FormLabel>Target Image Model</FormLabel>
              <Select {...register('imageModel')}>
                <option value="dall-e-3">DALL-E 3</option>
                <option value="gemini-flash-image">Gemini 2.5 Flash Image (nano-banana)</option>
                <option value="midjourney-v7">Midjourney V7</option>
                <option value="flux-1-kontext">FLUX.1 Kontext</option>
                <option value="stable-diffusion">Stable Diffusion</option>
              </Select>
            </FormControl>

            {/* Image Style */}
            <FormControl>
              <FormLabel>Image Style</FormLabel>
              <Select {...register('imageStyle')}>
                <option value="photorealistic">Photorealistic</option>
                <option value="artistic">Artistic</option>
                <option value="digital-art">Digital Art</option>
                <option value="oil-painting">Oil Painting</option>
                <option value="watercolor">Watercolor</option>
                <option value="cartoon">Cartoon</option>
                <option value="sketch">Sketch</option>
                <option value="ui-mock">UI Mock</option>
              </Select>
            </FormControl>

            {/* Composition */}
            <FormControl>
              <FormLabel>Composition</FormLabel>
              <Select {...register('composition')}>
                <option value="centered">Centered</option>
                <option value="rule-of-thirds">Rule of Thirds</option>
                <option value="portrait">Portrait</option>
                <option value="landscape">Landscape</option>
                <option value="close-up">Close-up</option>
                <option value="wide-shot">Wide Shot</option>
                <option value="birds-eye-view">Bird's Eye View</option>
                <option value="low-angle">Low Angle</option>
              </Select>
            </FormControl>

            {/* Art Medium */}
            <FormControl>
              <FormLabel>Art Medium</FormLabel>
              <Select {...register('artMedium')}>
                <option value="digital-art">Digital Art</option>
                <option value="photography">Photography</option>
                <option value="oil-painting">Oil Painting</option>
                <option value="watercolor">Watercolor</option>
                <option value="pencil-sketch">Pencil Sketch</option>
                <option value="ink-drawing">Ink Drawing</option>
                <option value="acrylic">Acrylic</option>
                <option value="3d-render">3D Render</option>
              </Select>
            </FormControl>
          </>
        )}

        {/* Domain Selection */}
        <FormControl>
          <FormLabel>Domain</FormLabel>
          <Select {...register('domain')}>
            <option value="general">General</option>
            <option value="business">Business</option>
            <option value="technical">Technical</option>
            <option value="creative">Creative</option>
            <option value="academic">Academic</option>
            <option value="data-analysis">Data Analysis</option>
            <option value="coding">Coding</option>
          </Select>
        </FormControl>

        {/* Complexity Level */}
        <FormControl>
          <FormLabel>Complexity Level</FormLabel>
          <Select {...register('complexity')}>
            <option value="simple">Simple</option>
            <option value="moderate">Moderate</option>
            <option value="complex">Complex</option>
            <option value="expert">Expert</option>
          </Select>
        </FormControl>

        {/* Additional Requirements */}
        <FormControl>
          <FormLabel>Additional Requirements</FormLabel>
          <Textarea
            {...register('requirements')}
            rows={2}
            placeholder="Any specific instructions, constraints, or requirements..."
            resize="vertical"
          />
        </FormControl>

        {/* Examples */}
        <FormControl>
          <FormLabel>
            Examples <Text as="span" color="gray.500" fontSize="sm">(Optional)</Text>
          </FormLabel>
          <Textarea
            {...register('examples')}
            rows={3}
            placeholder="Provide examples of inputs/outputs if available..."
            resize="vertical"
          />
        </FormControl>

        {/* Submit Button */}
        <Button
          type="submit"
          colorScheme="blue"
          size="lg"
          width="full"
          isDisabled={!isValid || isGenerating}
          isLoading={isGenerating}
          loadingText="Generating..."
        >
          Generate Prompt
        </Button>
      </VStack>
    </form>
  )
}

export default PromptConfigurationForm