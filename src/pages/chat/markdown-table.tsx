import { type ComponentProps, useRef, useState } from "react"
import { CheckIcon, CopyIcon, ExpandIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { cn } from "@/lib/utils"

import { copyText } from "./markdown-utils"

export function MarkdownTable({ children, className, ...props }: ComponentProps<"table">) {
  const tableRef = useRef<HTMLTableElement>(null)
  const [copied, setCopied] = useState(false)
  const tableClassName = cn("w-full min-w-max table-auto border-collapse text-sm", className)

  async function handleCopy() {
    const table = tableRef.current

    if (!table) {
      return
    }

    const rows = Array.from(table.querySelectorAll("tr")).map((row) =>
      Array.from(row.querySelectorAll("th,td"))
        .map((cell) => cell.textContent?.trim() ?? "")
        .join("\t"),
    )

    await copyText(rows.join("\n"))
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  const table = (
    <table ref={tableRef} className={tableClassName} {...props}>
      {children}
    </table>
  )

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-background">
      <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 border-b px-3 py-2">
        <span className="text-xs font-medium text-muted-foreground">Tabela</span>
        <Button type="button" size="sm" variant="ghost" className="ml-auto" onClick={handleCopy}>
          {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
          {copied ? "Copiada" : "Copiar"}
        </Button>
        <Dialog>
          <DialogTrigger asChild>
            <Button type="button" size="sm" variant="ghost">
              <ExpandIcon data-icon="inline-start" />
              Expandir
            </Button>
          </DialogTrigger>
          <DialogContent className="max-h-[calc(100svh-2rem)] max-w-[calc(100vw-2rem)] overflow-auto p-4 sm:max-w-[calc(100vw-2rem)] lg:max-w-6xl xl:max-w-7xl">
            <DialogHeader>
              <DialogTitle>Tabela</DialogTitle>
            </DialogHeader>
            <div className="h-[min(78svh,900px)] w-full overflow-auto rounded-md border">
              <table className={tableClassName} {...props}>
                {children}
              </table>
            </div>
          </DialogContent>
        </Dialog>
      </div>
      <div className="w-full overflow-x-auto">{table}</div>
    </div>
  )
}
