import { DownloadIcon, FileIcon, FileTextIcon, ImageIcon, XIcon } from "lucide-react"

import { Button } from "@/components/ui/button"

import { type ChatAttachment } from "./chat-types"
import { formatFileSize } from "./markdown-utils"

type AttachmentPreviewKind = "image" | "pdf" | "file"

const imageExtensions = [".png", ".jpg", ".jpeg", ".webp"]

function hasKnownExtension(name: string, extensions: string[]) {
  const normalizedName = name.toLowerCase()

  return extensions.some((extension) => normalizedName.endsWith(extension))
}

function getAttachmentPreviewKind(attachment: ChatAttachment): AttachmentPreviewKind {
  if (attachment.type.startsWith("image/") || hasKnownExtension(attachment.name, imageExtensions)) {
    return "image"
  }

  if (attachment.type === "application/pdf" || hasKnownExtension(attachment.name, [".pdf"])) {
    return "pdf"
  }

  return "file"
}

function getAttachmentLabel(kind: AttachmentPreviewKind) {
  if (kind === "image") {
    return "Imagem"
  }

  if (kind === "pdf") {
    return "PDF"
  }

  return "Arquivo"
}

function AttachmentVisualPreview({
  attachment,
  kind,
}: {
  attachment: ChatAttachment
  kind: AttachmentPreviewKind
}) {
  if (kind === "image") {
    return (
      <a
        href={attachment.url}
        target="_blank"
        rel="noreferrer"
        aria-label={`Abrir preview de ${attachment.name}`}
        className="block focus-visible:outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50"
      >
        <img
          src={attachment.url}
          alt={`Preview de ${attachment.name}`}
          className="h-36 w-full bg-background object-cover"
          loading="lazy"
        />
      </a>
    )
  }

  if (kind === "pdf") {
    return (
      <div className="h-44 overflow-hidden bg-background">
        <iframe
          src={`${attachment.url}#toolbar=0&navpanes=0&scrollbar=0`}
          title={`Preview de ${attachment.name}`}
          className="h-full w-full border-0"
          loading="lazy"
          tabIndex={-1}
        />
      </div>
    )
  }

  return (
    <div className="flex h-28 flex-col items-center justify-center gap-2 bg-background text-muted-foreground">
      <FileIcon className="size-8" aria-hidden="true" />
      <span className="text-xs font-medium">Sem preview</span>
    </div>
  )
}

export function AttachmentChips({
  attachments,
  onRemove,
}: {
  attachments: ChatAttachment[]
  onRemove?: (attachment: ChatAttachment) => void
}) {
  if (attachments.length === 0) {
    return null
  }

  return (
    <div className="grid gap-2 sm:grid-cols-2" aria-live="polite">
      {attachments.map((attachment) => {
        const kind = getAttachmentPreviewKind(attachment)
        const label = getAttachmentLabel(kind)
        const Icon = kind === "image" ? ImageIcon : kind === "pdf" ? FileTextIcon : FileIcon

        return (
          <article
            key={attachment.id}
            className="min-w-0 animate-in overflow-hidden rounded-lg border bg-muted/60 text-sm shadow-sm fade-in-0 zoom-in-95"
            aria-label={`${label}: ${attachment.name}`}
          >
            <div data-clipboard-exclude className="relative">
              <AttachmentVisualPreview attachment={attachment} kind={kind} />
              {onRemove ? (
                <Button
                  data-clipboard-exclude
                  type="button"
                  size="icon-xs"
                  variant="secondary"
                  className="absolute right-2 top-2 shadow-sm"
                  aria-label={`Remover ${attachment.name}`}
                  onClick={() => onRemove(attachment)}
                >
                  <XIcon aria-hidden="true" />
                </Button>
              ) : null}
            </div>
            <div className="flex min-w-0 items-center gap-2 p-3">
              <Icon className="size-4 shrink-0 text-muted-foreground" aria-hidden="true" />
              <div className="min-w-0 flex-1">
                <a
                  href={attachment.url}
                  download={attachment.name}
                  className="block truncate font-medium underline-offset-4 hover:underline"
                >
                  {attachment.name}
                </a>
                <p className="truncate text-xs text-muted-foreground">
                  {label} - {formatFileSize(attachment.size)}
                </p>
              </div>
              <Button data-clipboard-exclude asChild type="button" size="icon-xs" variant="ghost">
                <a href={attachment.url} download={attachment.name} aria-label={`Baixar ${attachment.name}`}>
                  <DownloadIcon aria-hidden="true" />
                </a>
              </Button>
            </div>
          </article>
        )
      })}
    </div>
  )
}
