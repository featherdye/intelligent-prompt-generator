import React, { useState } from 'react'
import {
  Box,
  VStack,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Text,
  Badge,
  IconButton,
  Button,
  useColorModeValue,
  Tooltip,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  ModalCloseButton,
  useDisclosure,
} from '@chakra-ui/react'
import { SearchIcon, DeleteIcon, TimeIcon } from '@chakra-ui/icons'
import { usePromptStore } from '../store/promptStore'

const PromptHistoryPanel: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState('')
  const { isOpen, onOpen, onClose } = useDisclosure()

  const {
    promptHistory,
    loadPromptFromHistory,
    deleteFromHistory,
    clearHistory,
    searchHistory,
  } = usePromptStore()

  const bg = useColorModeValue('white', 'gray.800')
  const borderColor = useColorModeValue('gray.200', 'gray.700')
  const hoverBg = useColorModeValue('gray.50', 'gray.700')
  const textColor = useColorModeValue('gray.900', 'white')
  const mutedColor = useColorModeValue('gray.500', 'gray.400')

  const filteredHistory = searchQuery
    ? searchHistory(searchQuery)
    : promptHistory

  const formatDate = (date: Date) => {
    const now = new Date()
    const diffInHours = (now.getTime() - date.getTime()) / (1000 * 60 * 60)

    if (diffInHours < 24) {
      return `${Math.floor(diffInHours)}h ago`
    } else if (diffInHours < 24 * 7) {
      return `${Math.floor(diffInHours / 24)}d ago`
    } else {
      return date.toLocaleDateString()
    }
  }

  const truncateText = (text: string, maxLength: number = 80) => {
    if (text.length <= maxLength) return text
    return text.substring(0, maxLength) + '...'
  }

  const getPromptTypeBadgeColor = (type: 'text' | 'image') => {
    return type === 'image' ? 'purple' : 'blue'
  }

  const groupedHistory = React.useMemo(() => {
    const groups: { [key: string]: typeof filteredHistory } = {}

    filteredHistory.forEach(prompt => {
      const date = prompt.createdAt
      const now = new Date()
      const diffInDays = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24))

      let groupKey = ''
      if (diffInDays === 0) groupKey = 'Today'
      else if (diffInDays === 1) groupKey = 'Yesterday'
      else if (diffInDays < 7) groupKey = 'This Week'
      else if (diffInDays < 30) groupKey = 'This Month'
      else groupKey = 'Older'

      if (!groups[groupKey]) groups[groupKey] = []
      groups[groupKey].push(prompt)
    })

    return groups
  }, [filteredHistory])

  const groupOrder = ['Today', 'Yesterday', 'This Week', 'This Month', 'Older']

  return (
    <Box
      w="300px"
      h="full"
      bg={bg}
      borderRight="1px"
      borderColor={borderColor}
      overflowY="auto"
    >
      {/* Header */}
      <Box p={4} borderBottom="1px" borderColor={borderColor}>
        <HStack justify="space-between" mb={3}>
          <Text fontSize="lg" fontWeight="semibold" color={textColor}>
            History
          </Text>
          <Tooltip label="Clear all history">
            <IconButton
              size="sm"
              variant="ghost"
              icon={<DeleteIcon />}
              onClick={onOpen}
              aria-label="Clear history"
            />
          </Tooltip>
        </HStack>

        {/* Search */}
        <InputGroup size="sm">
          <InputLeftElement pointerEvents="none">
            <SearchIcon color={mutedColor} />
          </InputLeftElement>
          <Input
            placeholder="Search prompts..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            bg={useColorModeValue('white', 'gray.700')}
          />
        </InputGroup>
      </Box>

      {/* History List */}
      <Box flex={1}>
        {Object.keys(groupedHistory).length === 0 ? (
          <Box p={4} textAlign="center">
            <Text color={mutedColor} fontSize="sm">
              {searchQuery ? 'No matching prompts found' : 'No prompts yet'}
            </Text>
            {!searchQuery && (
              <Text color={mutedColor} fontSize="xs" mt={2}>
                Generate your first prompt to get started!
              </Text>
            )}
          </Box>
        ) : (
          <VStack spacing={0} align="stretch">
            {groupOrder.map(groupKey => {
              const groupPrompts = groupedHistory[groupKey]
              if (!groupPrompts || groupPrompts.length === 0) return null

              return (
                <Box key={groupKey}>
                  {/* Group Header */}
                  <Box p={3} pb={2}>
                    <Text fontSize="xs" fontWeight="medium" color={mutedColor} textTransform="uppercase">
                      {groupKey}
                    </Text>
                  </Box>

                  {/* Group Items */}
                  {groupPrompts.map((prompt) => (
                    <Box
                      key={prompt.id}
                      p={3}
                      mx={2}
                      mb={1}
                      borderRadius="md"
                      cursor="pointer"
                      _hover={{ bg: hoverBg }}
                      onClick={() => loadPromptFromHistory(prompt.id)}
                      role="group"
                    >
                      <HStack justify="space-between" align="start" spacing={2}>
                        <VStack align="start" spacing={1} flex={1} minW={0}>
                          {/* Task preview */}
                          <Text
                            fontSize="sm"
                            fontWeight="medium"
                            color={textColor}
                            noOfLines={2}
                            lineHeight="1.3"
                          >
                            {truncateText(prompt.originalTask)}
                          </Text>

                          {/* Metadata */}
                          <HStack spacing={2} wrap="wrap">
                            <Badge
                              size="sm"
                              colorScheme={getPromptTypeBadgeColor(prompt.promptType)}
                              variant="subtle"
                            >
                              {prompt.promptType}
                            </Badge>
                            <HStack spacing={1}>
                              <TimeIcon w={3} h={3} color={mutedColor} />
                              <Text fontSize="xs" color={mutedColor}>
                                {formatDate(prompt.createdAt)}
                              </Text>
                            </HStack>
                          </HStack>

                          {/* Quality score */}
                          <HStack spacing={1}>
                            <Text fontSize="xs" color={mutedColor}>
                              Quality: {prompt.qualityScore}%
                            </Text>
                          </HStack>
                        </VStack>

                        {/* Delete button */}
                        <IconButton
                          size="xs"
                          variant="ghost"
                          icon={<DeleteIcon />}
                          onClick={(e) => {
                            e.stopPropagation()
                            deleteFromHistory(prompt.id)
                          }}
                          aria-label="Delete prompt"
                          opacity={0}
                          _groupHover={{ opacity: 1 }}
                        />
                      </HStack>
                    </Box>
                  ))}
                </Box>
              )
            })}
          </VStack>
        )}
      </Box>

      {/* Clear History Confirmation Modal */}
      <Modal isOpen={isOpen} onClose={onClose} size="sm">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Clear History</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Text>Are you sure you want to clear all prompt history? This action cannot be undone.</Text>
          </ModalBody>
          <ModalFooter>
            <Button variant="ghost" mr={3} onClick={onClose}>
              Cancel
            </Button>
            <Button
              colorScheme="red"
              onClick={() => {
                clearHistory()
                onClose()
              }}
            >
              Clear All
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  )
}

export default PromptHistoryPanel