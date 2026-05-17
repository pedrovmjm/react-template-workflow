export type ChatRole = "assistant" | "user"

export type ChatAttachment = {
  id: string
  name: string
  size: number
  type: string
  url: string
}

export type ChatMessage = {
  id: string
  role: ChatRole
  content: string
  attachments?: ChatAttachment[]
  status?: "streaming" | "done" | "error"
}

export type BrowserSpeechRecognitionEvent = Event & {
  resultIndex: number
  results: SpeechRecognitionResultList
}

export type BrowserSpeechRecognition = {
  continuous: boolean
  interimResults: boolean
  lang: string
  onend: (() => void) | null
  onerror: (() => void) | null
  onresult: ((event: BrowserSpeechRecognitionEvent) => void) | null
  abort: () => void
  start: () => void
  stop: () => void
}

export type BrowserSpeechRecognitionConstructor = new () => BrowserSpeechRecognition

export type WindowWithSpeechRecognition = Window &
  typeof globalThis & {
    SpeechRecognition?: BrowserSpeechRecognitionConstructor
    webkitSpeechRecognition?: BrowserSpeechRecognitionConstructor
  }
