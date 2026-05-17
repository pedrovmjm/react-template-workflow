import { useEffect, useRef, useState } from "react"

import { Card, CardContent } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"

import { ChatBubble } from "./chat-bubble"
import { ChatComposer } from "./chat-composer"
import { type BrowserSpeechRecognition, type ChatAttachment, type ChatMessage } from "./chat-types"
import {
  createAttachment,
  createMessageId,
  getSpeechRecognitionConstructor,
  runAssistantResponse,
} from "./chat-utils"

const initialMessages: ChatMessage[] = [
  {
    id: "welcome",
    role: "assistant",
    status: "done",
    content: [
      "Pronto para receber Markdown do usuario e da IA.",
      "",
      "- Listas, links e tabelas usam GitHub Flavored Markdown.",
      "- Tabelas, codigo e diagramas ganham acoes de leitura.",
      "- Mermaid e PlantUML podem ser expandidos, copiados e abertos em PNG/SVG.",
      "- PDFs e imagens anexadas exibem preview no composer e na conversa.",
      "- Respostas longas permanecem dentro da area da conversa.",
      "",
      "```mermaid",
      "flowchart LR",
      "  usuario[Usuario] --> chat[Chat]",
      "  chat --> backend[Backend]",
      "  backend --> resposta[IA]",
      "```",
    ].join("\n"),
  },
]

export function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>(initialMessages)
  const [input, setInput] = useState("")
  const [attachments, setAttachments] = useState<ChatAttachment[]>([])
  const [isResponding, setIsResponding] = useState(false)
  const [isListening, setIsListening] = useState(false)
  const [isSpeechSupported, setIsSpeechSupported] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const recognitionRef = useRef<BrowserSpeechRecognition | null>(null)
  const attachmentUrlsRef = useRef(new Set<string>())

  useEffect(() => {
    setIsSpeechSupported(Boolean(getSpeechRecognitionConstructor()))

    return () => {
      recognitionRef.current?.abort()
      attachmentUrlsRef.current.forEach((url) => URL.revokeObjectURL(url))
      attachmentUrlsRef.current.clear()
    }
  }, [])

  async function sendMessage() {
    const prompt = input.trim()

    if ((!prompt && attachments.length === 0) || isResponding) {
      return
    }

    const assistantId = createMessageId()
    const outgoingAttachments = attachments

    setInput("")
    setAttachments([])
    setError(null)
    setIsResponding(true)
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: createMessageId(),
        role: "user",
        content: prompt || "Referencias anexadas.",
        attachments: outgoingAttachments,
        status: "done",
      },
      { id: assistantId, role: "assistant", content: "", status: "streaming" },
    ])

    try {
      await runAssistantResponse({
        attachmentCount: outgoingAttachments.length,
        onChunk: (chunk) => {
          setMessages((currentMessages) =>
            currentMessages.map((message) =>
              message.id === assistantId
                ? { ...message, content: `${message.content}${chunk}` }
                : message,
            ),
          )
        },
      })

      setMessages((currentMessages) =>
        currentMessages.map((message) =>
          message.id === assistantId ? { ...message, status: "done" } : message,
        ),
      )
    } catch {
      setError("Nao foi possivel gerar a resposta agora.")
      setMessages((currentMessages) =>
        currentMessages.map((message) =>
          message.id === assistantId
            ? { ...message, content: "Falha ao gerar resposta.", status: "error" }
            : message,
        ),
      )
    } finally {
      setIsResponding(false)
    }
  }

  function handleFilesChange(files: FileList | null) {
    if (!files) {
      return
    }

    const availableSlots = Math.max(6 - attachments.length, 0)
    const selectedFiles = Array.from(files)
    const nextAttachments = selectedFiles
      .slice(0, availableSlots)
      .map((file) => {
        const attachment = createAttachment(file)

        attachmentUrlsRef.current.add(attachment.url)
        return attachment
      })

    if (selectedFiles.length > availableSlots) {
      setError("Limite de 6 anexos por mensagem.")
    } else {
      setError(null)
    }

    setAttachments((currentAttachments) => [...currentAttachments, ...nextAttachments])

    if (fileInputRef.current) {
      fileInputRef.current.value = ""
    }
  }

  function removeAttachment(attachment: ChatAttachment) {
    URL.revokeObjectURL(attachment.url)
    attachmentUrlsRef.current.delete(attachment.url)
    setAttachments((currentAttachments) =>
      currentAttachments.filter((currentAttachment) => currentAttachment.id !== attachment.id),
    )
  }

  function toggleSpeechInput() {
    if (isListening) {
      recognitionRef.current?.stop()
      setIsListening(false)
      return
    }

    const SpeechRecognition = getSpeechRecognitionConstructor()

    if (!SpeechRecognition) {
      setError("Este navegador nao oferece transcricao por voz.")
      return
    }

    const recognition = new SpeechRecognition()

    recognition.lang = navigator.language || "pt-BR"
    recognition.continuous = false
    recognition.interimResults = false
    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .slice(event.resultIndex)
        .map((result) => result[0]?.transcript.trim() ?? "")
        .filter(Boolean)
        .join(" ")

      if (transcript) {
        setInput((currentInput) => `${currentInput}${currentInput ? " " : ""}${transcript}`)
      }
    }
    recognition.onerror = () => {
      setError("Nao foi possivel transcrever o audio.")
      setIsListening(false)
    }
    recognition.onend = () => setIsListening(false)
    recognitionRef.current = recognition
    setError(null)
    setIsListening(true)
    recognition.start()
  }

  return (
    <div className="flex h-svh w-full min-w-0 flex-col overflow-hidden bg-background">
      <Card className="flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden rounded-none border-0 bg-background shadow-none">
        <CardContent className="flex min-h-0 min-w-0 flex-1 flex-col p-0">
          <ScrollArea className="min-h-0 min-w-0 flex-1">
            <div className="min-w-0 px-3 pb-6 pt-20 sm:px-6 md:px-8 md:pt-16" aria-live="polite">
              <div className="mx-auto flex w-full max-w-5xl flex-col gap-6">
                {messages.map((message) => (
                  <ChatBubble key={message.id} message={message} />
                ))}
              </div>
            </div>
          </ScrollArea>

          <ChatComposer
            attachments={attachments}
            error={error}
            fileInputRef={fileInputRef}
            input={input}
            isListening={isListening}
            isResponding={isResponding}
            isSpeechSupported={isSpeechSupported}
            onFilesChange={handleFilesChange}
            onInputChange={setInput}
            onRemoveAttachment={removeAttachment}
            onSubmit={() => void sendMessage()}
            onToggleSpeechInput={toggleSpeechInput}
          />
        </CardContent>
      </Card>
    </div>
  )
}
