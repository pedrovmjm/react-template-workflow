import { ApiRequestError, classifyFetchError, isServerUnavailableStatus } from "./api-errors"
import { readRecord } from "./read-helpers"
import type { ApiErrorEnvelope } from "./types"

export type ApiClientConfig = {
  apiVersion: string
  baseUrl: string
}

export type ApiClient = ReturnType<typeof createApiClient>

export function createApiClient(config: ApiClientConfig) {
  const { apiVersion, baseUrl } = config

  function apiUrl(path: string, params?: Record<string, string | number | undefined>) {
    const normalizedBaseUrl = baseUrl.replace(/\/$/, "")
    const url = new URL(`${normalizedBaseUrl}${path}`, window.location.origin)

    Object.entries(params ?? {}).forEach(([key, value]) => {
      if (value !== undefined && String(value).trim()) {
        url.searchParams.set(key, String(value))
      }
    })

    return url.toString()
  }

  async function parseApiResponse<T>(response: Response): Promise<T> {
    if (response.status === 204) {
      throw new Error("O recurso solicitado nao esta disponivel.")
    }

    const body = (await response.json().catch(() => null)) as unknown

    if (!response.ok) {
      const errorBody = readRecord(body) as ApiErrorEnvelope
      const message = errorBody.errors?.[0]?.message ?? "A API nao conseguiu concluir a operacao."
      throw new ApiRequestError(
        message,
        isServerUnavailableStatus(response.status) ? "server_unavailable" : "request_failed",
        response.status,
      )
    }

    return body as T
  }

  function buildHeaders(extra?: HeadersInit): HeadersInit {
    return {
      Accept: "application/json",
      "X-API-Version": apiVersion,
      ...extra,
    }
  }

  async function request<T>(method: string, path: string, init?: RequestInit) {
    try {
      const response = await fetch(apiUrl(path), {
        ...init,
        headers: buildHeaders(init?.headers),
        method,
      })

      return parseApiResponse<T>(response)
    } catch (error) {
      throw classifyFetchError(error)
    }
  }

  async function get<T>(path: string, params?: Record<string, string | number | undefined>) {
    try {
      const response = await fetch(apiUrl(path, params), {
        headers: buildHeaders(),
      })

      return parseApiResponse<T>(response)
    } catch (error) {
      throw classifyFetchError(error)
    }
  }

  async function post<T>(path: string, payload: unknown) {
    return request<T>("POST", path, {
      body: JSON.stringify(payload),
      headers: { "Content-Type": "application/json" },
    })
  }

  async function postForm<T>(path: string, formData: FormData) {
    return request<T>("POST", path, { body: formData })
  }

  async function put<T>(path: string, payload: unknown) {
    return request<T>("PUT", path, {
      body: JSON.stringify(payload),
      headers: { "Content-Type": "application/json" },
    })
  }

  async function del(path: string) {
    try {
      const response = await fetch(apiUrl(path), {
        headers: buildHeaders(),
        method: "DELETE",
      })

      if (!response.ok) {
        await parseApiResponse<unknown>(response)
      }
    } catch (error) {
      throw classifyFetchError(error)
    }
  }

  return {
    apiUrl,
    del,
    get,
    post,
    postForm,
    put,
  }
}
