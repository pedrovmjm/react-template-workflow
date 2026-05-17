import {
  type ChangeEvent,
  type KeyboardEvent,
  type RefObject,
} from "react"
import { Loader2Icon, MicIcon, PaperclipIcon, SendIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

import { AttachmentChips } from "./attachment-chips"
import { type ChatAttachment } from "./chat-types"

type ChatComposerProps = {
  attachments: ChatAttachment[]
  error: string | null
  fileInputRef: RefObject<HTMLInputElement | null>
  input: string
  isListening: boolean
  isResponding: boolean
  isSpeechSupported: boolean
  onFilesChange: (files: FileList | null) => void
  onInputChange: (value: string) => void
  onRemoveAttachment: (attachment: ChatAttachment) => void
  onSubmit: () => void
  onToggleSpeechInput: () => void
}

export function ChatComposer({
  attachments,
  error,
  fileInputRef,
  input,
  isListening,
  isResponding,
  isSpeechSupported,
  onFilesChange,
  onInputChange,
  onRemoveAttachment,
  onSubmit,
  onToggleSpeechInput,
}: ChatComposerProps) {
  return (
    <form
      className="min-w-0 border-t bg-background/95 px-3 py-3 backdrop-blur md:px-8 md:py-4"
      onSubmit={(event) => {
        event.preventDefault()
        onSubmit()
      }}
    >
      <input
        ref={fileInputRef}
        type="file"
        multiple
        className="sr-only"
        accept=".pdf,.doc,.docx,.txt,.md,.json,.csv,.png,.jpg,.jpeg,.webp"
        onChange={(event) => onFilesChange(event.target.files)}
      />
      <div className="mx-auto flex w-full max-w-5xl flex-col gap-2">
        {error ? <p className="text-sm text-destructive">{error}</p> : null}
        <div className="min-w-0 rounded-lg border bg-background p-2 shadow-sm focus-within:ring-[3px] focus-within:ring-ring/50">
          <AttachmentChips attachments={attachments} onRemove={onRemoveAttachment} />
          <Textarea
            value={input}
            placeholder="Envie Markdown, cole codigo ou descreva uma tarefa..."
            className="field-sizing-fixed min-h-24 min-w-0 max-w-full resize-none overflow-x-hidden border-0 bg-transparent px-2 shadow-none [overflow-wrap:anywhere] focus-visible:ring-0 focus-visible:ring-offset-0"
            disabled={isResponding}
            aria-label="Mensagem"
            onChange={(event: ChangeEvent<HTMLTextAreaElement>) => onInputChange(event.target.value)}
            onKeyDown={(event: KeyboardEvent<HTMLTextAreaElement>) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault()
                onSubmit()
              }
            }}
          />
          <div className="mt-2 flex flex-col gap-2 border-t pt-2 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex flex-wrap gap-2">
              <Button
                type="button"
                size="sm"
                variant="secondary"
                onClick={() => fileInputRef.current?.click()}
                disabled={isResponding}
              >
                <PaperclipIcon data-icon="inline-start" />
                Anexar
              </Button>
              <Button
                type="button"
                size="sm"
                variant={isListening ? "default" : "secondary"}
                disabled={isResponding || !isSpeechSupported}
                onClick={onToggleSpeechInput}
              >
                {isListening ? (
                  <Loader2Icon className="animate-spin" data-icon="inline-start" />
                ) : (
                  <MicIcon data-icon="inline-start" />
                )}
                {isListening ? "Ouvindo" : "Falar com chat"}
              </Button>
            </div>
            <Button
              type="submit"
              size="sm"
              disabled={isResponding || (!input.trim() && attachments.length === 0)}
              className="sm:w-fit"
            >
              {isResponding ? (
                <Loader2Icon className="animate-spin" data-icon="inline-start" />
              ) : (
                <SendIcon data-icon="inline-start" />
              )}
              Enviar
            </Button>
          </div>
        </div>
      </div>
    </form>
  )
}
