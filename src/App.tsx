import {
  Box,
  Container,
  Flex,
  Heading,
  Text,
  useColorModeValue,
  IconButton,
  HStack,
  Button,
  Badge,
  useDisclosure,
} from '@chakra-ui/react'
import { ViewIcon, ViewOffIcon, SettingsIcon } from '@chakra-ui/icons'
import PromptConfigurationForm from './components/PromptConfigurationForm'
import PromptDisplay from './components/PromptDisplay'
import PromptHistoryPanel from './components/PromptHistoryPanel'
import ApiKeyModal from './components/ApiKeyModal'
import { usePromptStore } from './store/promptStore'

function App() {
  const { isHistoryPanelVisible, setHistoryPanelVisible, hasApiKey } = usePromptStore()
  const { isOpen: isApiKeyModalOpen, onOpen: onApiKeyModalOpen, onClose: onApiKeyModalClose } = useDisclosure()

  const bg = useColorModeValue('gray.50', 'gray.900')
  const headerBg = useColorModeValue('white', 'gray.800')
  const borderColor = useColorModeValue('gray.200', 'gray.700')

  return (
    <Box minH="100vh" bg={bg}>
      {/* Header */}
      <Box
        bg={headerBg}
        borderBottom="1px"
        borderColor={borderColor}
        shadow="sm"
      >
        <Container maxW="full" px={6}>
          <Flex justify="space-between" align="center" py={4}>
            <HStack spacing={4}>
              <IconButton
                size="sm"
                variant="ghost"
                icon={isHistoryPanelVisible ? <ViewOffIcon /> : <ViewIcon />}
                onClick={() => setHistoryPanelVisible(!isHistoryPanelVisible)}
                aria-label="Toggle history panel"
              />
              <Heading size="lg" color={useColorModeValue('gray.900', 'white')}>
                Intelligent Prompt Generator
              </Heading>
            </HStack>
            <HStack spacing={3}>
              <Button
                size="sm"
                variant="outline"
                leftIcon={<SettingsIcon />}
                onClick={onApiKeyModalOpen}
                colorScheme={hasApiKey() ? 'green' : 'red'}
              >
                {hasApiKey() ? 'API Key Set' : 'Set API Key'}
                {hasApiKey() && <Badge ml={2} colorScheme="green" fontSize="xs">●</Badge>}
              </Button>
              <Text
                fontSize="sm"
                color={useColorModeValue('gray.500', 'gray.400')}
              >
                Powered by OpenRouter
              </Text>
            </HStack>
          </Flex>
        </Container>
      </Box>

      {/* Main 3-Panel Layout */}
      <Flex h="calc(100vh - 80px)">
        {/* Left Panel - History (optional) */}
        {isHistoryPanelVisible && <PromptHistoryPanel />}

        {/* Middle Panel - Configuration Form */}
        <Box
          flex={isHistoryPanelVisible ? "0 0 400px" : "0 0 50%"}
          borderRight="1px"
          borderColor={borderColor}
          bg={useColorModeValue('white', 'gray.800')}
          overflowY="auto"
        >
          <Box p={6}>
            <Heading
              size="md"
              mb={4}
              color={useColorModeValue('gray.900', 'white')}
            >
              Prompt Configuration
            </Heading>
            <PromptConfigurationForm />
          </Box>
        </Box>

        {/* Right Panel - Prompt Display */}
        <Box
          flex={1}
          bg={useColorModeValue('gray.50', 'gray.900')}
          overflowY="auto"
        >
          <Box p={6}>
            <Heading
              size="md"
              mb={4}
              color={useColorModeValue('gray.900', 'white')}
            >
              Generated Prompt
            </Heading>
            <PromptDisplay />
          </Box>
        </Box>
      </Flex>

      {/* API Key Modal */}
      <ApiKeyModal isOpen={isApiKeyModalOpen} onClose={onApiKeyModalClose} />
    </Box>
  )
}

export default App