import { useRef, useState } from "react"
import { BotIcon, CheckIcon, CopyIcon, Loader2Icon, UserIcon } from "lucide-react"

import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

import { AttachmentChips } from "./attachment-chips"
import { type ChatMessage } from "./chat-types"
import { createClipboardHtml, formatMessageForCopy } from "./chat-utils"
import { RichMarkdownMessage } from "./rich-message"

export function ChatBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === "user"
  const [copied, setCopied] = useState(false)
  const contentRef = useRef<HTMLDivElement>(null)

  async function handleCopyMessage() {
    if (!navigator.clipboard) {
      return
    }

    const plainText = formatMessageForCopy(message)
    const html = createClipboardHtml(contentRef.current)

    try {
      if (html && typeof ClipboardItem !== "undefined" && navigator.clipboard.write) {
        await navigator.clipboard.write([
          new ClipboardItem({
            "text/plain": new Blob([plainText], { type: "text/plain" }),
            "text/html": new Blob([html], { type: "text/html" }),
          }),
        ])
      } else {
        await navigator.clipboard.writeText(plainText)
      }
    } catch {
      await navigator.clipboard.writeText(plainText)
    }

    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <article className={cn("group flex w-full min-w-0 items-start gap-3", isUser && "justify-end")}>
      {!isUser ? (
        <Avatar className="mt-1 size-8 shrink-0 border">
          <AvatarFallback>
            <BotIcon className="size-4" aria-hidden="true" />
          </AvatarFallback>
        </Avatar>
      ) : null}

      {isUser ? (
        <Button
          type="button"
          size="icon-sm"
          variant="ghost"
          className="mt-1 opacity-100 sm:opacity-0 sm:transition-opacity sm:group-hover:opacity-100 sm:focus-visible:opacity-100"
          aria-label={copied ? "Mensagem copiada" : "Copiar mensagem"}
          onClick={handleCopyMessage}
        >
          {copied ? <CheckIcon /> : <CopyIcon />}
        </Button>
      ) : null}

      <div
        className={cn(
          "min-w-0 rounded-lg px-4 py-3 text-base leading-7",
          "overflow-hidden break-words [overflow-wrap:anywhere] [&_li]:ml-5 [&_ol]:list-decimal [&_p+p]:mt-3 [&_table]:border-collapse [&_ul]:list-disc",
          isUser
            ? "w-fit max-w-[min(42rem,82%)] border bg-muted text-foreground"
            : "w-full max-w-none bg-background text-foreground",
        )}
      >
        <div ref={contentRef} className="min-w-0 w-full max-w-full">
          <RichMarkdownMessage content={message.content || " "} />
          {message.attachments?.length ? (
            <div className="mt-3">
              <AttachmentChips attachments={message.attachments} />
            </div>
          ) : null}
        </div>
        {message.status === "streaming" ? (
          <span className="mt-3 inline-flex items-center gap-2 text-xs text-muted-foreground">
            <Loader2Icon className="size-3 animate-spin" aria-hidden="true" />
            Gerando resposta
          </span>
        ) : null}
      </div>

      {!isUser ? (
        <Button
          type="button"
          size="icon-sm"
          variant="ghost"
          className="mt-1 opacity-100 sm:opacity-0 sm:transition-opacity sm:group-hover:opacity-100 sm:focus-visible:opacity-100"
          aria-label={copied ? "Mensagem copiada" : "Copiar mensagem"}
          onClick={handleCopyMessage}
        >
          {copied ? <CheckIcon /> : <CopyIcon />}
        </Button>
      ) : null}

      {isUser ? (
        <Avatar className="mt-1 size-8 shrink-0 border">
          <AvatarFallback>
            <UserIcon className="size-4" aria-hidden="true" />
          </AvatarFallback>
        </Avatar>
      ) : null}
    </article>
  )
}
