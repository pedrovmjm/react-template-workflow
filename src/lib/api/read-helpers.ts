export type UnknownRecord = Record<string, unknown>

export function readString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback
}

export function readOptionalString(value: unknown): string | undefined {
  return typeof value === "string" ? value : undefined
}

export function readNumber(value: unknown): number | undefined {
  return typeof value === "number" ? value : undefined
}

export function readRecord(value: unknown): UnknownRecord {
  return value && typeof value === "object" && !Array.isArray(value) ? (value as UnknownRecord) : {}
}

export function readArray(value: unknown): unknown[] {
  return Array.isArray(value) ? value : []
}
