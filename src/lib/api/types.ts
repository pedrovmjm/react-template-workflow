export type ApiErrorEnvelope = {
  errors: Array<{
    code: string
    message: string
    title: string
  }>
}

export type ApiEnvelope<T> = {
  data: T
}

export type ApiListEnvelope<T> = {
  data: T[]
  links?: Record<string, string>
  meta?: {
    page?: number
    page_size?: number
    total?: number
    total_pages?: number
  }
}
