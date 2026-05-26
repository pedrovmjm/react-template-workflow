import { appEnv } from "@/config/app-env"

/** Exemplo: cada feature pode definir versao e base URL proprias. */
export const exampleApiConfig = {
  apiVersion: import.meta.env.VITE_EXAMPLE_API_VERSION ?? appEnv.apiDefaultVersion,
  baseUrl: import.meta.env.VITE_EXAMPLE_API_BASE_URL ?? appEnv.apiBaseUrl,
} as const
