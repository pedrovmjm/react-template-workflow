export type ApiFailureKind = "network_error" | "server_unavailable" | "request_failed"

export class ApiRequestError extends Error {
  readonly kind: ApiFailureKind
  readonly statusCode?: number

  constructor(message: string, kind: ApiFailureKind, statusCode?: number) {
    super(message)
    this.name = "ApiRequestError"
    this.kind = kind
    this.statusCode = statusCode
  }
}

const SERVER_UNAVAILABLE_STATUSES = new Set([0, 502, 503, 504])

export function isServerUnavailableStatus(status?: number) {
  return status !== undefined && SERVER_UNAVAILABLE_STATUSES.has(status)
}

export function classifyFetchError(error: unknown, statusCode?: number): ApiRequestError {
  if (error instanceof ApiRequestError) {
    return error
  }

  if (isServerUnavailableStatus(statusCode)) {
    return new ApiRequestError(
      "O servidor esta indisponivel no momento. Tente novamente em instantes.",
      "server_unavailable",
      statusCode,
    )
  }

  if (error instanceof TypeError) {
    return new ApiRequestError(
      "Nao foi possivel conectar ao servidor. Verifique sua rede ou se o backend esta em execucao.",
      "network_error",
    )
  }

  const message = error instanceof Error ? error.message : "A requisicao falhou."
  return new ApiRequestError(message, "request_failed", statusCode)
}
