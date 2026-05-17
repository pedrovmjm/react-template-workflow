import {
  type ChatAttachment,
  type ChatMessage,
  type WindowWithSpeechRecognition,
} from "./chat-types"

export function createMessageId() {
  return crypto.randomUUID?.() ?? `message-${Date.now()}-${Math.random().toString(16).slice(2)}`
}

function wait(ms: number) {
  return new Promise((resolve) => {
    window.setTimeout(resolve, ms)
  })
}

export function createAttachment(file: File): ChatAttachment {
  return {
    id: createMessageId(),
    name: file.name,
    size: file.size,
    type: file.type || "application/octet-stream",
    url: URL.createObjectURL(file),
  }
}

export function getSpeechRecognitionConstructor() {
  const speechWindow = window as WindowWithSpeechRecognition

  return speechWindow.SpeechRecognition ?? speechWindow.webkitSpeechRecognition
}

function createAssistantMarkdown(attachmentCount: number) {
  return [
    "Recebi sua mensagem em Markdown e mantive uma estrutura pronta para integrar com uma API real.",
    attachmentCount > 0
      ? `Tambem recebi ${attachmentCount} referencia(s) anexada(s) para o backend processar.`
      : "",
    "",
    "| Capacidade | Status |",
    "| --- | --- |",
    "| Markdown do usuario | Ativo |",
    "| Markdown da IA | Ativo |",
    "| Tabelas com acoes | Ativo |",
    "| Mermaid no cliente | Ativo |",
    "| PlantUML no cliente | Ativo |",
    "| Anexos como referencia | Ativo |",
    "| Conteudo sanitizado | Ativo |",
    "",
    "```plantuml",
    "@startuml",
    "actor Usuario",
    "participant Chat",
    "participant Backend",
    "Usuario -> Chat: envia mensagem e anexos",
    "Chat -> Backend: referencias para IA",
    "Backend --> Chat: resposta renderizada",
    "@enduml",
    "```",
  ]
    .filter(Boolean)
    .join("\n")
}

export async function runAssistantResponse({
  attachmentCount,
  onChunk,
}: {
  attachmentCount: number
  onChunk: (chunk: string) => void
}) {
  const response = createAssistantMarkdown(attachmentCount)
  const chunks = response.match(/.{1,28}(\s|$)/g) ?? [response]

  for (const chunk of chunks) {
    await wait(45)
    onChunk(chunk)
  }
}

export function formatMessageForCopy(message: ChatMessage) {
  const attachmentText = message.attachments
    ?.map((attachment) => `- ${attachment.name} (${attachment.type}, ${attachment.size} bytes)`)
    .join("\n")

  return [message.content, attachmentText ? `**Anexos**\n${attachmentText}` : ""]
    .filter(Boolean)
    .join("\n\n")
}

export function createClipboardHtml(contentElement: HTMLElement | null) {
  if (!contentElement) {
    return ""
  }

  const clonedContent = contentElement.cloneNode(true) as HTMLElement

  clonedContent
    .querySelectorAll("[data-clipboard-exclude], button")
    .forEach((element) => element.remove())

  return clonedContent.innerHTML.trim()
}
