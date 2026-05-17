import path from "node:path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig, loadEnv } from "vite"

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "")
  const appEnv = env.VITE_APP_ENV || mode

  return {
    plugins: [react(), tailwindcss()],
    define: {
      __APP_ENV__: JSON.stringify(appEnv),
    },
    server: {
      host: env.VITE_DEV_HOST || "0.0.0.0",
      port: Number(env.VITE_DEV_PORT || 5173),
      strictPort: false,
    },
    preview: {
      host: env.VITE_DEV_HOST || "0.0.0.0",
      port: Number(env.VITE_PREVIEW_PORT || 4173),
      strictPort: false,
    },
    build: {
      sourcemap: appEnv !== "production",
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
  }
})
