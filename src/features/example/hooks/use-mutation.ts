import { useCallback, useRef, useState } from "react"

import { type ApiFailureKind, ApiRequestError } from "@/lib/api/api-errors"

export type MutationStatus = "idle" | "loading" | "success" | "error" | "retrying"

export type MutationState<TData, TVariables> = {
  data: TData | undefined
  error: string
  failureKind: ApiFailureKind | null
  status: MutationStatus
  loading: boolean
  failed: boolean
  serverUnavailable: boolean
  isRetrying: boolean
  retryAttempt: number
  mutate: (variables: TVariables) => Promise<TData | undefined>
  reset: () => void
  cancel: () => void
}

export type UseMutationOptions<TData, TVariables> = {
  mutationFn: (variables: TVariables) => Promise<TData>
  maxRetries?: number
  retryDelayMs?: number
}

function sleep(ms: number) {
  return new Promise<void>((resolve) => {
    window.setTimeout(resolve, ms)
  })
}

function readMutationError(error: unknown): { message: string; kind: ApiFailureKind; serverUnavailable: boolean } {
  if (error instanceof ApiRequestError) {
    return {
      message: error.message,
      kind: error.kind,
      serverUnavailable: error.kind === "server_unavailable" || error.kind === "network_error",
    }
  }

  return {
    message: error instanceof Error ? error.message : "Nao foi possivel concluir a operacao.",
    kind: "request_failed",
    serverUnavailable: false,
  }
}

/** Hook para POST/PUT/DELETE com retry controlado e sem reexecucao automatica. */
export function useMutation<TData, TVariables = void>(
  options: UseMutationOptions<TData, TVariables>,
): MutationState<TData, TVariables> {
  const { mutationFn, maxRetries = 1, retryDelayMs = 3000 } = options

  const [data, setData] = useState<TData>()
  const [error, setError] = useState("")
  const [failureKind, setFailureKind] = useState<ApiFailureKind | null>(null)
  const [status, setStatus] = useState<MutationStatus>("idle")
  const [loading, setLoading] = useState(false)
  const [failed, setFailed] = useState(false)
  const [serverUnavailable, setServerUnavailable] = useState(false)
  const [isRetrying, setIsRetrying] = useState(false)
  const [retryAttempt, setRetryAttempt] = useState(0)

  const mutationFnRef = useRef(mutationFn)
  const optionsRef = useRef({ maxRetries, retryDelayMs })
  const requestIdRef = useRef(0)
  const cancelledRef = useRef(false)

  mutationFnRef.current = mutationFn
  optionsRef.current = { maxRetries, retryDelayMs }

  const cancel = useCallback(() => {
    cancelledRef.current = true
    requestIdRef.current += 1
  }, [])

  const reset = useCallback(() => {
    cancel()
    setData(undefined)
    setError("")
    setFailureKind(null)
    setStatus("idle")
    setLoading(false)
    setFailed(false)
    setServerUnavailable(false)
    setIsRetrying(false)
    setRetryAttempt(0)
    cancelledRef.current = false
  }, [cancel])

  const mutate = useCallback(
    async (variables: TVariables) => {
      cancel()
      cancelledRef.current = false

      const requestId = requestIdRef.current + 1
      requestIdRef.current = requestId

      const { maxRetries: retriesLimit, retryDelayMs: delayMs } = optionsRef.current
      const totalAttempts = retriesLimit + 1

      setError("")
      setFailureKind(null)
      setFailed(false)
      setServerUnavailable(false)
      setLoading(true)
      setStatus("loading")
      setIsRetrying(false)
      setRetryAttempt(0)

      for (let attempt = 0; attempt < totalAttempts; attempt += 1) {
        if (cancelledRef.current || requestIdRef.current !== requestId) {
          return undefined
        }

        setRetryAttempt(attempt)
        setIsRetrying(attempt > 0)
        setStatus(attempt > 0 ? "retrying" : "loading")

        try {
          const result = await mutationFnRef.current(variables)
          if (cancelledRef.current || requestIdRef.current !== requestId) {
            return undefined
          }

          setData(result)
          setStatus("success")
          setLoading(false)
          setIsRetrying(false)
          return result
        } catch (mutationError) {
          if (cancelledRef.current || requestIdRef.current !== requestId) {
            return undefined
          }

          const parsed = readMutationError(mutationError)
          const isLastAttempt = attempt >= totalAttempts - 1

          if (!isLastAttempt) {
            setError(`${parsed.message} Tentando novamente (${attempt + 1}/${retriesLimit})...`)
            setFailureKind(parsed.kind)
            setServerUnavailable(parsed.serverUnavailable)
            setStatus("retrying")
            setIsRetrying(true)
            await sleep(delayMs)
            continue
          }

          setError(parsed.message)
          setFailureKind(parsed.kind)
          setFailed(true)
          setServerUnavailable(parsed.serverUnavailable)
          setIsRetrying(false)
          setStatus("error")
          setLoading(false)
          return undefined
        }
      }

      return undefined
    },
    [cancel],
  )

  return {
    data,
    error,
    failureKind,
    status,
    loading,
    failed,
    serverUnavailable,
    isRetrying,
    retryAttempt,
    mutate,
    reset,
    cancel,
  }
}
