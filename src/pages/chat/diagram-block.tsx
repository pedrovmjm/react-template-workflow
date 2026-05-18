import { type PointerEvent, useEffect, useId, useRef, useState } from "react"
type MermaidApi = typeof import("mermaid").default
import {
  CheckIcon,
  CopyIcon,
  DownloadIcon,
  ExpandIcon,
  ExternalLinkIcon,
  Loader2Icon,
  MinusIcon,
  PlusIcon,
  RotateCcwIcon,
} from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { cn } from "@/lib/utils"

import { normalizePlantUmlSource, renderPlantUmlToSvg } from "./plantuml-renderer"
import { type CodeChild, copyText } from "./markdown-utils"

const fallbackDiagramTextColor = "#211922"
const fallbackDiagramBackgroundColor = "#ffffff"
const fallbackDiagramSurfaceColor = "#f6f6f3"
const fallbackDiagramBorderColor = "#dadad3"
const fallbackDiagramMutedTextColor = "#62625b"
const defaultDiagramZoom = 1.2

function readCssColorVariable(name: string, fallback: string) {
  const value = window.getComputedStyle(document.documentElement).getPropertyValue(name).trim()

  return value || fallback
}

function getDiagramColors() {
  return {
    background: readCssColorVariable("--background", fallbackDiagramBackgroundColor),
    border: readCssColorVariable("--border", fallbackDiagramBorderColor),
    mutedForeground: readCssColorVariable("--muted-foreground", fallbackDiagramMutedTextColor),
    surface: readCssColorVariable("--muted", fallbackDiagramSurfaceColor),
    text: readCssColorVariable("--foreground", fallbackDiagramTextColor),
  }
}

function createDiagramThemeCss() {
  const colors = getDiagramColors()

  return [
    `svg{color:${colors.text};font-family:Inter,sans-serif;}`,
    `.nodeLabel,.edgeLabel,.label,text,tspan{color:${colors.text}!important;fill:${colors.text}!important;}`,
    `.edgeLabel,.label{background:${colors.background}!important;}`,
    `.edgeLabel rect,.labelBkg{fill:${colors.background}!important;opacity:1!important;}`,
    `.node rect,.node circle,.node ellipse,.node polygon{fill:${colors.surface}!important;stroke:${colors.border}!important;}`,
    `.cluster rect{fill:${colors.surface}!important;stroke:${colors.border}!important;}`,
    `.edgePath path,.flowchart-link{stroke:${colors.text}!important;}`,
    `marker path{fill:${colors.text}!important;stroke:${colors.text}!important;}`,
  ].join("")
}

let mermaidLoader: Promise<MermaidApi> | null = null

function loadMermaid() {
  mermaidLoader ??= import("mermaid").then((module) => module.default)
  return mermaidLoader
}

async function initializeMermaid() {
  const mermaid = await loadMermaid()
  const colors = getDiagramColors()

  mermaid.initialize({
    flowchart: {
      htmlLabels: false,
    },
    securityLevel: "strict",
    startOnLoad: false,
    theme: "base",
    themeVariables: {
      fontFamily: "Inter, sans-serif",
      background: colors.background,
      clusterBkg: colors.surface,
      clusterBorder: colors.border,
      edgeLabelBackground: colors.background,
      lineColor: colors.text,
      mainBkg: colors.surface,
      nodeBorder: colors.border,
      nodeTextColor: colors.text,
      primaryBorderColor: colors.border,
      primaryColor: colors.surface,
      primaryTextColor: colors.text,
      secondaryBorderColor: colors.border,
      secondaryColor: colors.background,
      secondaryTextColor: colors.text,
      tertiaryBorderColor: colors.border,
      tertiaryColor: colors.surface,
      tertiaryTextColor: colors.text,
      textColor: colors.text,
      titleColor: colors.text,
    },
    themeCSS: createDiagramThemeCss(),
  })
}

function sanitizeSvg(svg: string) {
  const document = new DOMParser().parseFromString(svg, "image/svg+xml")
  const svgElement = document.documentElement
  const style = document.createElementNS("http://www.w3.org/2000/svg", "style")
  const colors = getDiagramColors()

  style.textContent = createDiagramThemeCss()
  svgElement.prepend(style)
  document.querySelectorAll("foreignObject").forEach((node) => {
    const label = node.textContent?.trim()

    if (!label) {
      return
    }

    const x = Number(node.getAttribute("x") ?? 0)
    const y = Number(node.getAttribute("y") ?? 0)
    const width = Number(node.getAttribute("width") ?? 0)
    const height = Number(node.getAttribute("height") ?? 0)
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text")

    text.setAttribute("x", String(x + width / 2))
    text.setAttribute("y", String(y + height / 2))
    text.setAttribute("dominant-baseline", "middle")
    text.setAttribute("fill", colors.text)
    text.setAttribute("font-family", "Inter, sans-serif")
    text.setAttribute("font-size", "14")
    text.setAttribute("text-anchor", "middle")
    text.textContent = label
    node.parentNode?.insertBefore(text, node)
  })

  const blockedNodes = document.querySelectorAll("script, foreignObject, iframe, object, embed")

  blockedNodes.forEach((node) => node.remove())
  document.querySelectorAll("*").forEach((node) => {
    Array.from(node.attributes).forEach((attribute) => {
      const name = attribute.name.toLowerCase()
      const value = attribute.value.trim().toLowerCase()

      if (name.startsWith("on") || value.startsWith("javascript:")) {
        node.removeAttribute(attribute.name)
      }
    })
  })

  return new XMLSerializer().serializeToString(document.documentElement)
}

function downloadBlob(blob: Blob, filename: string) {
  const url = URL.createObjectURL(blob)
  const anchor = document.createElement("a")

  anchor.href = url
  anchor.download = filename
  anchor.click()
  URL.revokeObjectURL(url)
}

function openSvgInNewTab(svg: string) {
  const blob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" })
  const url = URL.createObjectURL(blob)
  const openedWindow = window.open(url, "_blank")

  if (!openedWindow) {
    URL.revokeObjectURL(url)
    downloadBlob(blob, "diagram.svg")
    return
  }

  openedWindow.opener = null
  window.setTimeout(() => URL.revokeObjectURL(url), 60_000)
}

async function downloadSvgAsPng(svg: string, filename: string) {
  const image = new Image()
  const svgBlob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" })
  const url = URL.createObjectURL(svgBlob)

  try {
    await new Promise<void>((resolve, reject) => {
      image.onload = () => resolve()
      image.onerror = () => reject(new Error("Nao foi possivel carregar o diagrama."))
      image.src = url
    })

    const svgDocument = new DOMParser().parseFromString(svg, "image/svg+xml")
    const svgElement = svgDocument.documentElement
    const viewBox = svgElement.getAttribute("viewBox")?.split(/\s+/).map(Number)
    const width = Number(svgElement.getAttribute("width")) || viewBox?.[2] || image.width || 1200
    const height = Number(svgElement.getAttribute("height")) || viewBox?.[3] || image.height || 800
    const canvas = document.createElement("canvas")
    const context = canvas.getContext("2d")

    canvas.width = Math.ceil(width)
    canvas.height = Math.ceil(height)
    context?.drawImage(image, 0, 0, canvas.width, canvas.height)

    const pngBlob = await new Promise<Blob | null>((resolve) => canvas.toBlob(resolve, "image/png"))

    if (pngBlob) {
      downloadBlob(pngBlob, filename)
    }
  } finally {
    URL.revokeObjectURL(url)
  }
}

function DiagramCanvas({ isExpanded = false, svg, zoom }: { isExpanded?: boolean; svg: string; zoom: number }) {
  const scrollRef = useRef<HTMLDivElement>(null)
  const dragRef = useRef<{
    left: number
    top: number
    x: number
    y: number
  } | null>(null)

  function handlePointerDown(event: PointerEvent<HTMLDivElement>) {
    const element = scrollRef.current

    if (!element) {
      return
    }

    dragRef.current = {
      left: element.scrollLeft,
      top: element.scrollTop,
      x: event.clientX,
      y: event.clientY,
    }
    element.setPointerCapture(event.pointerId)
  }

  function handlePointerMove(event: PointerEvent<HTMLDivElement>) {
    const element = scrollRef.current
    const drag = dragRef.current

    if (!element || !drag) {
      return
    }

    event.preventDefault()
    element.scrollLeft = drag.left - (event.clientX - drag.x)
    element.scrollTop = drag.top - (event.clientY - drag.y)
  }

  function handlePointerEnd(event: PointerEvent<HTMLDivElement>) {
    scrollRef.current?.releasePointerCapture(event.pointerId)
    dragRef.current = null
  }

  return (
    <div
      ref={scrollRef}
      onPointerDown={handlePointerDown}
      onPointerMove={handlePointerMove}
      onPointerUp={handlePointerEnd}
      onPointerCancel={handlePointerEnd}
      className={cn(
        "w-full min-w-0 cursor-grab select-none overflow-auto rounded-md bg-background p-4 active:cursor-grabbing",
        isExpanded ? "h-[calc(100svh-11rem)] w-full" : "max-h-[420px] min-h-72",
      )}
    >
      <div
        className="grid min-h-full min-w-full origin-center place-items-center transition-transform [&_svg]:h-auto [&_svg]:max-w-none"
        style={{ transform: `scale(${zoom})` }}
        dangerouslySetInnerHTML={{ __html: svg }}
      />
    </div>
  )
}

export function DiagramBlock({ code, language }: CodeChild) {
  const renderId = useId().replace(/[^a-zA-Z0-9_-]/g, "")
  const [svg, setSvg] = useState("")
  const [error, setError] = useState<string | null>(null)
  const [zoom, setZoom] = useState(defaultDiagramZoom)
  const [copied, setCopied] = useState(false)
  const isPlantUml = language === "plantuml" || language === "puml"
  const label = isPlantUml ? "PlantUML" : "Mermaid"
  const zoomControls = (
    <>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom((value) => Math.max(0.3, value - 0.2))}>
        <MinusIcon />
        <span className="sr-only">Reduzir zoom</span>
      </Button>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom(defaultDiagramZoom)}>
        <RotateCcwIcon />
        <span className="sr-only">Resetar zoom</span>
      </Button>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom((value) => Math.min(4, value + 0.2))}>
        <PlusIcon />
        <span className="sr-only">Aumentar zoom</span>
      </Button>
    </>
  )

  useEffect(() => {
    let isMounted = true

    async function renderDiagram() {
      setError(null)
      setSvg("")

      try {
        const rawSvg = isPlantUml
          ? renderPlantUmlToSvg(normalizePlantUmlSource(code))
          : await renderMermaidDiagram(`diagram-${renderId}`, code)

        if (isMounted) {
          setSvg(sanitizeSvg(rawSvg))
        }
      } catch (renderError) {
        if (isMounted) {
          setError(renderError instanceof Error ? renderError.message : "Diagrama invalido.")
        }
      }
    }

    void renderDiagram()

    return () => {
      isMounted = false
    }
  }, [code, isPlantUml, renderId])

  async function handleCopy() {
    await copyText(code)
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-muted/40">
      <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 border-b bg-background px-3 py-2">
        <span className="text-xs font-medium text-muted-foreground">{label}</span>
        <div className="ml-auto flex flex-wrap items-center gap-1">
          {zoomControls}
          <Button type="button" size="sm" variant="ghost" onClick={handleCopy}>
            {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
            {copied ? "Copiado" : "Copiar"}
          </Button>
          <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => void downloadSvgAsPng(svg, `${label.toLowerCase()}-diagram.png`)}>
            <DownloadIcon data-icon="inline-start" />
            PNG
          </Button>
          <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => openSvgInNewTab(svg)}>
            <ExternalLinkIcon data-icon="inline-start" />
            SVG
          </Button>
          <Dialog>
            <DialogTrigger asChild>
              <Button type="button" size="sm" variant="ghost" disabled={!svg}>
                <ExpandIcon data-icon="inline-start" />
                Expandir
              </Button>
            </DialogTrigger>
            <DialogContent className="h-[calc(100svh-1rem)] max-h-[calc(100svh-1rem)] w-[calc(100vw-1rem)] max-w-none overflow-hidden p-4 sm:max-w-none">
              <DialogHeader className="pr-10">
                <DialogTitle>{label}</DialogTitle>
              </DialogHeader>
              <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 rounded-md border bg-background px-3 py-2">
                <span className="text-xs text-muted-foreground">{Math.round(zoom * 100)}%</span>
                <div className="ml-auto flex items-center gap-1">
                  {zoomControls}
                  <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => void downloadSvgAsPng(svg, `${label.toLowerCase()}-diagram.png`)}>
                    <DownloadIcon data-icon="inline-start" />
                    PNG
                  </Button>
                  <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => openSvgInNewTab(svg)}>
                    <ExternalLinkIcon data-icon="inline-start" />
                    SVG
                  </Button>
                </div>
              </div>
              {svg ? <DiagramCanvas isExpanded svg={svg} zoom={zoom} /> : null}
            </DialogContent>
          </Dialog>
        </div>
      </div>
      {error ? (
        <pre className="overflow-x-auto p-4 text-sm text-destructive">{error}</pre>
      ) : svg ? (
        <DiagramCanvas svg={svg} zoom={zoom} />
      ) : (
        <div className="flex min-h-72 items-center justify-center gap-2 text-sm text-muted-foreground">
          <Loader2Icon className="size-4 animate-spin" aria-hidden="true" />
          Renderizando diagrama
        </div>
      )}
    </div>
  )
}

async function renderMermaidDiagram(id: string, code: string) {
  const mermaid = await loadMermaid()

  await initializeMermaid()

  return (await mermaid.render(id, code)).svg
}
