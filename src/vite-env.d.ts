/// <reference types="vite/client" />

type AppEnvironment = "local" | "development" | "staging" | "production"

interface ImportMetaEnv {
  readonly VITE_APP_ENV?: AppEnvironment
  readonly VITE_APP_NAME?: string
  readonly VITE_API_BASE_URL?: string
  readonly VITE_ENABLE_MOCKS?: string
  readonly VITE_DEV_HOST?: string
  readonly VITE_DEV_PORT?: string
  readonly VITE_PREVIEW_PORT?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare const __APP_ENV__: AppEnvironment
