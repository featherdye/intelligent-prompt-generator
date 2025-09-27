import React, { useState, useEffect } from 'react'
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  Input,
  InputGroup,
  InputRightElement,
  VStack,
  HStack,
  Text,
  Alert,
  AlertIcon,
  AlertDescription,
  FormControl,
  FormLabel,
  FormErrorMessage,
  IconButton,
  useToast,
} from '@chakra-ui/react'
import { ViewIcon, ViewOffIcon, CheckIcon, DeleteIcon } from '@chakra-ui/icons'
import { usePromptStore } from '../store/promptStore'

interface ApiKeyModalProps {
  isOpen: boolean
  onClose: () => void
}

const ApiKeyModal: React.FC<ApiKeyModalProps> = ({ isOpen, onClose }) => {
  const toast = useToast()
  const { apiKey, setApiKey, clearApiKey, hasApiKey } = usePromptStore()

  const [inputValue, setInputValue] = useState('')
  const [showKey, setShowKey] = useState(false)
  const [isValid, setIsValid] = useState(true)
  const [isTesting, setIsTesting] = useState(false)

  useEffect(() => {
    if (isOpen) {
      setInputValue(apiKey)
      setShowKey(false)
      setIsValid(true)
    }
  }, [isOpen, apiKey])

  const validateApiKey = (key: string): boolean => {
    return key.length > 0 && key.startsWith('sk-or-v1-') && key.length > 20
  }

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value.trim()
    setInputValue(value)
    setIsValid(validateApiKey(value) || value === '')
  }

  const handleSave = () => {
    if (inputValue && !validateApiKey(inputValue)) {
      setIsValid(false)
      return
    }

    setApiKey(inputValue)
    toast({
      title: inputValue ? 'API Key saved successfully!' : 'API Key cleared',
      status: 'success',
      duration: 2000,
      isClosable: true,
    })
    onClose()
  }

  const handleClear = () => {
    setInputValue('')
    clearApiKey()
    toast({
      title: 'API Key cleared',
      status: 'info',
      duration: 2000,
      isClosable: true,
    })
    onClose()
  }

  const handleTestKey = async () => {
    if (!validateApiKey(inputValue)) {
      setIsValid(false)
      return
    }

    setIsTesting(true)
    try {
      // Simple test request to OpenRouter
      const response = await fetch('https://openrouter.ai/api/v1/models', {
        headers: {
          'Authorization': `Bearer ${inputValue}`,
          'HTTP-Referer': window.location.origin,
          'X-Title': 'Intelligent Prompt Generator'
        }
      })

      if (response.ok) {
        toast({
          title: 'API Key is valid!',
          description: 'Successfully connected to OpenRouter',
          status: 'success',
          duration: 3000,
          isClosable: true,
        })
      } else {
        throw new Error(`HTTP ${response.status}`)
      }
    } catch (error) {
      toast({
        title: 'API Key test failed',
        description: 'Unable to connect to OpenRouter. Please check your key.',
        status: 'error',
        duration: 4000,
        isClosable: true,
      })
    } finally {
      setIsTesting(false)
    }
  }

  const maskKey = (key: string) => {
    if (key.length <= 8) return key
    return key.substring(0, 8) + '...' + key.substring(key.length - 4)
  }

  return (
    <Modal isOpen={isOpen} onClose={onClose} size="md">
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>API Key Management</ModalHeader>
        <ModalCloseButton />

        <ModalBody>
          <VStack spacing={4} align="stretch">
            {/* Current Status */}
            {apiKey && (
              <Alert status={hasApiKey() ? 'success' : 'warning'} borderRadius="md">
                <AlertIcon />
                <AlertDescription>
                  {hasApiKey()
                    ? `Current key: ${maskKey(apiKey)}`
                    : 'Current key appears to be invalid'
                  }
                </AlertDescription>
              </Alert>
            )}

            {/* API Key Input */}
            <FormControl isInvalid={!isValid}>
              <FormLabel>OpenRouter API Key</FormLabel>
              <InputGroup>
                <Input
                  type={showKey ? 'text' : 'password'}
                  placeholder="sk-or-v1-..."
                  value={inputValue}
                  onChange={handleInputChange}
                  pr="4rem"
                />
                <InputRightElement>
                  <IconButton
                    size="sm"
                    variant="ghost"
                    icon={showKey ? <ViewOffIcon /> : <ViewIcon />}
                    onClick={() => setShowKey(!showKey)}
                    aria-label={showKey ? 'Hide key' : 'Show key'}
                  />
                </InputRightElement>
              </InputGroup>
              {!isValid && (
                <FormErrorMessage>
                  Please enter a valid OpenRouter API key (starts with sk-or-v1-)
                </FormErrorMessage>
              )}
            </FormControl>

            {/* Test Button */}
            {inputValue && validateApiKey(inputValue) && (
              <Button
                size="sm"
                variant="outline"
                leftIcon={<CheckIcon />}
                onClick={handleTestKey}
                isLoading={isTesting}
                loadingText="Testing..."
              >
                Test API Key
              </Button>
            )}

            {/* Help Text */}
            <Text fontSize="sm" color="gray.500">
              Get your API key from{' '}
              <Text as="span" color="blue.500" cursor="pointer" textDecoration="underline"
                onClick={() => window.open('https://openrouter.ai/keys', '_blank')}
              >
                OpenRouter.ai
              </Text>
              . Your key is stored securely in your browser's local storage.
            </Text>
          </VStack>
        </ModalBody>

        <ModalFooter>
          <HStack spacing={2}>
            {apiKey && (
              <Button
                variant="ghost"
                colorScheme="red"
                leftIcon={<DeleteIcon />}
                onClick={handleClear}
                size="sm"
              >
                Clear
              </Button>
            )}
            <Button variant="ghost" onClick={onClose}>
              Cancel
            </Button>
            <Button
              colorScheme="blue"
              onClick={handleSave}
              isDisabled={inputValue !== '' && !validateApiKey(inputValue)}
            >
              Save
            </Button>
          </HStack>
        </ModalFooter>
      </ModalContent>
    </Modal>
  )
}

export default ApiKeyModal