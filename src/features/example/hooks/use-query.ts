import {
  type Dispatch,
  type SetStateAction,
  useCallback,
  useEffect,
  useRef,
  useState,
} from "react"

import { type ApiFailureKind, ApiRequestError } from "@/lib/api/api-errors"

export type QueryStatus = "idle" | "loading" | "success" | "error" | "retrying"

export type QueryState<T> = {
  data: T | undefined
  error: string
  failureKind: ApiFailureKind | null
  status: QueryStatus
  loading: boolean
  failed: boolean
  serverUnavailable: boolean
  isRetrying: boolean
  retryAttempt: number
  reload: () => Promise<void>
  cancel: () => void
  setData: Dispatch<SetStateAction<T | undefined>>
}

export type UseQueryOptions = {
  enabled?: boolean
  /** Tentativas extras apos a primeira falha (padrao: 2). Use 0 para nao repetir automaticamente. */
  maxRetries?: number
  /** Intervalo entre tentativas em ms (padrao: 3000). */
  retryDelayMs?: number
}

type RetrySignal = {
  cancelled: boolean
  timer?: number
}

function sleep(ms: number, signal: RetrySignal) {
  return new Promise<void>((resolve) => {
    signal.timer = window.setTimeout(() => {
      if (!signal.cancelled) {
        resolve()
      }
    }, ms)
  })
}

function readQueryError(error: unknown): { message: string; kind: ApiFailureKind; serverUnavailable: boolean } {
  if (error instanceof ApiRequestError) {
    return {
      message: error.message,
      kind: error.kind,
      serverUnavailable: error.kind === "server_unavailable" || error.kind === "network_error",
    }
  }

  return {
    message: error instanceof Error ? error.message : "Nao foi possivel carregar os dados.",
    kind: "request_failed",
    serverUnavailable: false,
  }
}

/**
 * Hook generico de leitura com retry controlado.
 * queryFn deve ser estavel (useCallback no caller) ou passada via ref interna — evita loop de requisicoes.
 */
export function useQuery<T>(
  queryFn: () => Promise<T>,
  deps: ReadonlyArray<unknown> = [],
  options: UseQueryOptions = {},
): QueryState<T> {
  const { enabled = true, maxRetries = 2, retryDelayMs = 3000 } = options

  const [data, setData] = useState<T>()
  const [error, setError] = useState("")
  const [failureKind, setFailureKind] = useState<ApiFailureKind | null>(null)
  const [status, setStatus] = useState<QueryStatus>("idle")
  const [loading, setLoading] = useState(enabled)
  const [failed, setFailed] = useState(false)
  const [serverUnavailable, setServerUnavailable] = useState(false)
  const [isRetrying, setIsRetrying] = useState(false)
  const [retryAttempt, setRetryAttempt] = useState(0)

  const queryFnRef = useRef(queryFn)
  const optionsRef = useRef({ enabled, maxRetries, retryDelayMs })
  const requestIdRef = useRef(0)
  const retrySignalRef = useRef<RetrySignal>({ cancelled: false })

  queryFnRef.current = queryFn
  optionsRef.current = { enabled, maxRetries, retryDelayMs }

  const cancel = useCallback(() => {
    retrySignalRef.current.cancelled = true
    if (retrySignalRef.current.timer !== undefined) {
      window.clearTimeout(retrySignalRef.current.timer)
      retrySignalRef.current.timer = undefined
    }
    requestIdRef.current += 1
  }, [])

  const runQuery = useCallback(async () => {
    cancel()
    const signal: RetrySignal = { cancelled: false }
    retrySignalRef.current = signal

    const requestId = requestIdRef.current + 1
    requestIdRef.current = requestId

    const { enabled: isEnabled, maxRetries: retriesLimit, retryDelayMs: delayMs } = optionsRef.current

    if (!isEnabled) {
      setLoading(false)
      setStatus("idle")
      setFailed(false)
      setServerUnavailable(false)
      setIsRetrying(false)
      return
    }

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
      if (signal.cancelled || requestIdRef.current !== requestId) {
        return
      }

      setRetryAttempt(attempt)
      setIsRetrying(attempt > 0)
      setStatus(attempt > 0 ? "retrying" : "loading")
      setLoading(true)

      try {
        const result = await queryFnRef.current()
        if (signal.cancelled || requestIdRef.current !== requestId) {
          return
        }

        setData(result)
        setError("")
        setFailureKind(null)
        setFailed(false)
        setServerUnavailable(false)
        setIsRetrying(false)
        setStatus("success")
        setLoading(false)
        return
      } catch (queryError) {
        if (signal.cancelled || requestIdRef.current !== requestId) {
          return
        }

        const parsed = readQueryError(queryError)
        const isLastAttempt = attempt >= totalAttempts - 1

        if (!isLastAttempt) {
          setError(`${parsed.message} Tentando novamente (${attempt + 1}/${retriesLimit})...`)
          setFailureKind(parsed.kind)
          setServerUnavailable(parsed.serverUnavailable)
          setStatus("retrying")
          setIsRetrying(true)
          await sleep(delayMs, signal)
          continue
        }

        setError(parsed.message)
        setFailureKind(parsed.kind)
        setFailed(true)
        setServerUnavailable(parsed.serverUnavailable)
        setIsRetrying(false)
        setStatus("error")
        setLoading(false)
        return
      }
    }
  }, [cancel])

  useEffect(() => {
    void runQuery()

    return () => {
      cancel()
    }
    // deps controlam quando refazer a leitura; queryFn vem via ref para nao gerar loop
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [runQuery, enabled, maxRetries, retryDelayMs, ...deps])

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
    reload: runQuery,
    cancel,
    setData,
  }
}
