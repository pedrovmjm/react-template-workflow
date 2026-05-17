import ReactMarkdown, { type Components } from "react-markdown"
import rehypeSanitize from "rehype-sanitize"
import remarkGfm from "remark-gfm"

import { cn } from "@/lib/utils"
import { CopyableCodeBlock } from "./copyable-code-block"
import { DiagramBlock } from "./diagram-block"
import { MarkdownTable } from "./markdown-table"
import { readCodeChild } from "./markdown-utils"

const markdownComponents: Components = {
  a({ children, href }) {
    return (
      <a
        href={href}
        target="_blank"
        rel="noreferrer"
        className="font-medium text-primary underline-offset-4 hover:underline"
      >
        {children}
      </a>
    )
  },
  code({ children, className }) {
    return (
      <code className={cn("rounded bg-muted px-1.5 py-0.5 text-sm", className)}>
        {children}
      </code>
    )
  },
  pre({ children }) {
    const codeChild = readCodeChild(children)

    if (!codeChild) {
      return (
        <pre className="w-full max-w-full overflow-x-auto rounded-md bg-muted p-4 [&_code]:block [&_code]:min-w-max [&_code]:whitespace-pre">
          {children}
        </pre>
      )
    }

    if (codeChild.language === "mermaid" || codeChild.language === "plantuml" || codeChild.language === "puml") {
      return <DiagramBlock {...codeChild} />
    }

    return <CopyableCodeBlock {...codeChild} />
  },
  table({ children, ...props }) {
    return <MarkdownTable {...props}>{children}</MarkdownTable>
  },
  td({ children, ...props }) {
    return (
      <td className="border p-2 align-top" {...props}>
        {children}
      </td>
    )
  },
  th({ children, ...props }) {
    return (
      <th className="border bg-muted p-2 text-left align-top font-semibold" {...props}>
        {children}
      </th>
    )
  },
}

export function RichMarkdownMessage({ content }: { content: string }) {
  return (
    <div className="min-w-0 w-full max-w-full">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeSanitize]}
        components={markdownComponents}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}
