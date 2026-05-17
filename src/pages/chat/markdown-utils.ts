import {
  Children,
  isValidElement,
  type ReactNode,
} from "react"

export type CodeChild = {
  code: string
  language: string
}

export function readCodeChild(children: ReactNode): CodeChild | null {
  const child = Children.toArray(children)[0]

  if (!isValidElement(child)) {
    return null
  }

  const props = child.props as { children?: ReactNode; className?: string }
  const language = /language-(\w+)/.exec(props.className ?? "")?.[1] ?? "text"
  const code = String(props.children ?? "").replace(/\n$/, "")

  return { code, language: language.toLowerCase() }
}

export async function copyText(text: string) {
  if (!navigator.clipboard) {
    return
  }

  await navigator.clipboard.writeText(text)
}

export function formatFileSize(size: number) {
  if (size < 1024) {
    return `${size} B`
  }

  if (size < 1024 * 1024) {
    return `${Math.round(size / 1024)} KB`
  }

  return `${(size / 1024 / 1024).toFixed(1)} MB`
}
