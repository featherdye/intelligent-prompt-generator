import React from 'react'
import {
  Box,
  VStack,
  HStack,
  Button,
  Text,
  Spinner,
  Alert,
  AlertIcon,
  AlertTitle,
  AlertDescription,
  useColorModeValue,
  useToast,
  SimpleGrid,
  Stat,
  StatLabel,
  StatNumber,
  Code,
} from '@chakra-ui/react'
import { CopyIcon, DownloadIcon } from '@chakra-ui/icons'
import { usePromptStore } from '../store/promptStore'

const PromptDisplay: React.FC = () => {
  const toast = useToast()
  const { generatedPrompt, isGenerating } = usePromptStore()

  const contentBg = useColorModeValue('white', 'gray.800')
  const borderColor = useColorModeValue('gray.200', 'gray.700')
  const statBg = useColorModeValue('gray.50', 'gray.800')

  // Placeholder prompt for demonstration
  const placeholderPrompt = `Welcome to the Intelligent Prompt Generator!

Your optimized prompt will appear here once you:
1. Fill out the configuration form on the left
2. Click "Generate Prompt"

The generated prompt will include:
• Optimized prompt engineering techniques
• Context-specific instructions
• Clear formatting and structure
• Best practices for your selected AI model`

  const handleCopy = async () => {
    const contentToCopy = generatedPrompt?.content || placeholderPrompt
    try {
      await navigator.clipboard.writeText(contentToCopy)
      toast({
        title: 'Copied!',
        description: 'Prompt has been copied to clipboard',
        status: 'success',
        duration: 2000,
        isClosable: true,
      })
    } catch (err) {
      console.error('Failed to copy prompt:', err)
      toast({
        title: 'Copy failed',
        description: 'Failed to copy prompt to clipboard',
        status: 'error',
        duration: 3000,
        isClosable: true,
      })
    }
  }

  const handleDownload = () => {
    const contentToDownload = generatedPrompt?.content || placeholderPrompt
    const element = document.createElement('a')
    const file = new Blob([contentToDownload], { type: 'text/plain' })
    element.href = URL.createObjectURL(file)
    element.download = 'generated-prompt.txt'
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)

    toast({
      title: 'Downloaded!',
      description: 'Prompt has been downloaded as a text file',
      status: 'success',
      duration: 2000,
      isClosable: true,
    })
  }

  return (
    <VStack spacing={4} align="stretch" h="full">
      {/* Action Buttons */}
      <HStack justify="flex-end" spacing={2}>
        <Button
          leftIcon={<CopyIcon />}
          size="sm"
          variant="outline"
          onClick={handleCopy}
        >
          Copy
        </Button>
        <Button
          leftIcon={<DownloadIcon />}
          size="sm"
          variant="outline"
          onClick={handleDownload}
        >
          Download
        </Button>
      </HStack>

      {/* Prompt Content Area */}
      <Box
        flex={1}
        bg={contentBg}
        borderRadius="lg"
        border="1px"
        borderColor={borderColor}
        shadow="sm"
        overflow="hidden"
      >
        {isGenerating ? (
          <VStack justify="center" h="full" spacing={3}>
            <Spinner size="lg" color="blue.500" />
            <Text color="gray.600">Generating prompt...</Text>
          </VStack>
        ) : (
          <Box h="full" p={4} overflowY="auto">
            <Code
              p={0}
              bg="transparent"
              fontSize="sm"
              fontFamily="mono"
              whiteSpace="pre-wrap"
              lineHeight="relaxed"
              display="block"
              w="full"
            >
              {generatedPrompt?.content || placeholderPrompt}
            </Code>
          </Box>
        )}
      </Box>

      {/* Prompt Quality Score */}
      {generatedPrompt && (
        <Alert status="info" borderRadius="md">
          <AlertIcon />
          <Box flex="1">
            <AlertTitle fontSize="sm">
              Prompt Quality Score: {generatedPrompt.qualityScore}/100
            </AlertTitle>
            <AlertDescription fontSize="xs">
              {generatedPrompt.qualityScore >= 80
                ? 'Excellent prompt structure with clear instructions and context.'
                : generatedPrompt.qualityScore >= 70
                ? 'Good prompt structure with clear instructions and context.'
                : 'Good prompt, consider adding more context for better results.'
              }
            </AlertDescription>
          </Box>
        </Alert>
      )}

      {/* Usage Statistics */}
      {generatedPrompt && (
        <SimpleGrid columns={3} spacing={3}>
          <Stat textAlign="center" p={3} bg={statBg} borderRadius="md">
            <StatNumber fontSize="lg">{generatedPrompt.characterCount}</StatNumber>
            <StatLabel fontSize="xs">Characters</StatLabel>
          </Stat>
          <Stat textAlign="center" p={3} bg={statBg} borderRadius="md">
            <StatNumber fontSize="lg">{generatedPrompt.wordCount}</StatNumber>
            <StatLabel fontSize="xs">Words</StatLabel>
          </Stat>
          <Stat textAlign="center" p={3} bg={statBg} borderRadius="md">
            <StatNumber fontSize="lg">~${generatedPrompt.estimatedCost.toFixed(3)}</StatNumber>
            <StatLabel fontSize="xs">Est. Cost</StatLabel>
          </Stat>
        </SimpleGrid>
      )}
    </VStack>
  )
}

export default PromptDisplay