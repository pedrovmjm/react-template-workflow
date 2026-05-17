import { useState } from "react"
import { CheckIcon, CopyIcon } from "lucide-react"

import { Button } from "@/components/ui/button"

import { type CodeChild, copyText } from "./markdown-utils"

export function CopyableCodeBlock({ code, language }: CodeChild) {
  const [copied, setCopied] = useState(false)

  async function handleCopy() {
    await copyText(code)
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-foreground text-background">
      <div data-clipboard-exclude className="flex min-h-10 min-w-0 items-center gap-2 border-b border-background/15 px-3">
        <span className="truncate text-xs font-medium text-background/70">{language}</span>
        <Button
          type="button"
          size="sm"
          variant="ghost"
          className="ml-auto h-8 text-background hover:bg-background/10 hover:text-background"
          onClick={handleCopy}
        >
          {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
          {copied ? "Copiado" : "Copiar"}
        </Button>
      </div>
      <pre className="max-w-full overflow-x-auto p-4 text-sm leading-6">
        <code className="block min-w-max whitespace-pre">{code}</code>
      </pre>
    </div>
  )
}
