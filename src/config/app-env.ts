export type AppEnvironment = "local" | "development" | "staging" | "production"

const fallbackMode = import.meta.env.MODE as AppEnvironment

function readBoolean(value: string | undefined, fallback: boolean) {
  if (value === undefined) {
    return fallback
  }

  return value === "true"
}

export const appEnv = {
  mode: import.meta.env.MODE,
  appEnv: import.meta.env.VITE_APP_ENV ?? fallbackMode,
  appName: import.meta.env.VITE_APP_NAME ?? "React Template Workflow",
  brandName: import.meta.env.VITE_BRAND_NAME ?? import.meta.env.VITE_APP_NAME ?? "React Template Workflow",
  brandLogoUrl: import.meta.env.VITE_BRAND_LOGO_URL ?? "",
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL ?? "/api",
  apiDefaultVersion: import.meta.env.VITE_API_VERSION ?? "v1",
  enableMocks: readBoolean(import.meta.env.VITE_ENABLE_MOCKS, false),
  isDevelopment: import.meta.env.DEV,
  isProduction: import.meta.env.PROD,
} as const
