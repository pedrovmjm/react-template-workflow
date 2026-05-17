function escapeXml(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

function parsePlantUmlLines(source: string) {
  return source
    .split("\n")
    .map((line) => line.trim())
    .filter(
      (line) =>
        line &&
        !line.startsWith("'") &&
        !/^@(start|end)\w+/i.test(line) &&
        !/^(skinparam|title|hide|show)\b/i.test(line),
    )
}

const diagramSurfaceColor = "var(--muted)"
const diagramBorderColor = "var(--border)"
const diagramTextColor = "var(--foreground)"

function renderSequenceDiagram(lines: string[]) {
  const participants: string[] = []
  const messages = lines
    .map((line) => {
      const declaration = /^(actor|participant|boundary|control|entity|database)\s+("?[^"]+"?|\w+)/i.exec(line)

      if (declaration) {
        const name = declaration[2].replaceAll('"', "")

        if (!participants.includes(name)) {
          participants.push(name)
        }

        return null
      }

      const message = /^(.+?)\s*[-.]+[->]+\s*(.+?)(?:\s*:\s*(.*))?$/i.exec(line)

      if (!message) {
        return null
      }

      const from = message[1].replaceAll('"', "").trim()
      const to = message[2].replaceAll('"', "").trim()

      for (const name of [from, to]) {
        if (!participants.includes(name)) {
          participants.push(name)
        }
      }

      return { from, to, label: message[3]?.trim() ?? "" }
    })
    .filter((message): message is { from: string; to: string; label: string } => Boolean(message))

  const gap = 180
  const headerHeight = 72
  const rowHeight = 58
  const width = Math.max(360, participants.length * gap + 80)
  const height = Math.max(220, headerHeight + messages.length * rowHeight + 72)
  const xFor = (name: string) => participants.indexOf(name) * gap + 80
  const header = participants
    .map((name) => {
      const x = xFor(name)

      return `<g><rect x="${x - 56}" y="18" width="112" height="36" rx="12" fill="${diagramSurfaceColor}" stroke="${diagramBorderColor}"/><text x="${x}" y="41" text-anchor="middle" font-size="13" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(name)}</text><line x1="${x}" y1="54" x2="${x}" y2="${height - 24}" stroke="${diagramBorderColor}" stroke-dasharray="4 4"/></g>`
    })
    .join("")
  const arrows = messages
    .map((message, index) => {
      const y = headerHeight + index * rowHeight
      const fromX = xFor(message.from)
      const toX = xFor(message.to)
      const direction = toX >= fromX ? 1 : -1
      const labelX = (fromX + toX) / 2

      return `<g><line x1="${fromX}" y1="${y}" x2="${toX - direction * 10}" y2="${y}" stroke="${diagramTextColor}" stroke-width="1.5"/><path d="M ${toX - direction * 10} ${y - 5} L ${toX} ${y} L ${toX - direction * 10} ${y + 5}" fill="none" stroke="${diagramTextColor}" stroke-width="1.5"/><text x="${labelX}" y="${y - 10}" text-anchor="middle" font-size="12" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(message.label)}</text></g>`
    })
    .join("")

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">${header}${arrows}</svg>`
}

function renderClassDiagram(lines: string[]) {
  const classNames: string[] = []
  const relations: Array<{ from: string; to: string; label: string }> = []

  lines.forEach((line) => {
    const classMatch = /^(abstract\s+)?(class|interface|enum)\s+("?[^"{]+"?|\w+)/i.exec(line)

    if (classMatch) {
      const name = classMatch[3].replaceAll('"', "").trim()

      if (!classNames.includes(name)) {
        classNames.push(name)
      }
    }

    const relation = /^("?[^"]+"?|\w+)\s+[-.]+(?:\|>|>|o|x|\*)?[-.]*\s+("?[^"]+"?|\w+)(?:\s*:\s*(.*))?$/i.exec(line)

    if (relation) {
      const from = relation[1].replaceAll('"', "").trim()
      const to = relation[2].replaceAll('"', "").trim()

      for (const name of [from, to]) {
        if (!classNames.includes(name)) {
          classNames.push(name)
        }
      }

      relations.push({ from, to, label: relation[3]?.trim() ?? "" })
    }
  })

  if (classNames.length === 0) {
    classNames.push("PlantUML")
  }

  const columns = Math.min(3, classNames.length)
  const cardWidth = 150
  const cardHeight = 72
  const gapX = 80
  const gapY = 72
  const width = columns * cardWidth + (columns - 1) * gapX + 80
  const rows = Math.ceil(classNames.length / columns)
  const height = rows * cardHeight + (rows - 1) * gapY + 96
  const positionFor = (name: string) => {
    const index = classNames.indexOf(name)
    const column = index % columns
    const row = Math.floor(index / columns)

    return {
      x: 40 + column * (cardWidth + gapX),
      y: 40 + row * (cardHeight + gapY),
    }
  }
  const boxes = classNames
    .map((name) => {
      const position = positionFor(name)

      return `<g><rect x="${position.x}" y="${position.y}" width="${cardWidth}" height="${cardHeight}" rx="14" fill="${diagramSurfaceColor}" stroke="${diagramBorderColor}"/><text x="${position.x + cardWidth / 2}" y="${position.y + 40}" text-anchor="middle" font-size="14" font-weight="600" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(name)}</text></g>`
    })
    .join("")
  const edges = relations
    .map((relation) => {
      const from = positionFor(relation.from)
      const to = positionFor(relation.to)
      const fromX = from.x + cardWidth / 2
      const fromY = from.y + cardHeight
      const toX = to.x + cardWidth / 2
      const toY = to.y
      const labelX = (fromX + toX) / 2
      const labelY = (fromY + toY) / 2 - 6

      return `<g><line x1="${fromX}" y1="${fromY}" x2="${toX}" y2="${toY}" stroke="${diagramTextColor}" stroke-width="1.5"/><text x="${labelX}" y="${labelY}" text-anchor="middle" font-size="12" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(relation.label)}</text></g>`
    })
    .join("")

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">${edges}${boxes}</svg>`
}

export function normalizePlantUmlSource(source: string) {
  return /@start\w+/i.test(source) ? source : `@startuml\n${source}\n@enduml`
}

export function renderPlantUmlToSvg(source: string) {
  const lines = parsePlantUmlLines(source)
  const hasSequenceMessages = lines.some((line) => /^.+?\s*[-.]+[->]+\s*.+?(?:\s*:\s*.*)?$/i.test(line))

  return hasSequenceMessages ? renderSequenceDiagram(lines) : renderClassDiagram(lines)
}
