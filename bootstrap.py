#!/usr/bin/env python3
"""Bootstrap do starter frontend para projetos React/Vite.

Use `init-app` para criar a base da aplicacao React/Vite no diretorio alvo.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

SHADCN_STARTER_COMPONENTS = (
    "accordion",
    "alert",
    "alert-dialog",
    "aspect-ratio",
    "avatar",
    "badge",
    "breadcrumb",
    "button",
    "button-group",
    "calendar",
    "card",
    "carousel",
    "chart",
    "checkbox",
    "collapsible",
    "combobox",
    "command",
    "context-menu",
    "dialog",
    "direction",
    "drawer",
    "dropdown-menu",
    "empty",
    "field",
    "form",
    "hover-card",
    "input",
    "input-group",
    "input-otp",
    "item",
    "kbd",
    "label",
    "menubar",
    "native-select",
    "navigation-menu",
    "pagination",
    "popover",
    "progress",
    "radio-group",
    "resizable",
    "scroll-area",
    "select",
    "separator",
    "sheet",
    "sidebar",
    "slider",
    "skeleton",
    "sonner",
    "switch",
    "table",
    "tabs",
    "textarea",
    "tooltip",
    "toggle",
    "toggle-group",
)


APP_EXPECTED_FILES = (
    Path(".env.development"),
    Path(".env.production"),
    Path(".env.example"),
    Path("index.html"),
    Path("package.json"),
    Path("vite.config.ts"),
    Path("components.json"),
    Path("src/main.tsx"),
    Path("src/App.tsx"),
    Path("src/index.css"),
    Path("src/vite-env.d.ts"),
    Path("src/config/app-env.ts"),
    Path("src/lib/api/types.ts"),
    Path("src/lib/api/api-errors.ts"),
    Path("src/lib/api/read-helpers.ts"),
    Path("src/lib/api/create-api-client.ts"),
    Path("src/features/example/config.ts"),
    Path("src/features/example/services/api-client.ts"),
    Path("src/features/example/services/index.ts"),
    Path("src/features/example/hooks/use-query.ts"),
    Path("src/features/example/hooks/use-mutation.ts"),
    Path("src/features/example/hooks/index.ts"),
    Path("src/components/layout/data-state.tsx"),
    Path("src/components/layout/app-shell.tsx"),
    Path("src/components/layout/page-header.tsx"),
    Path("src/components/ui/file-upload-dropzone.tsx"),
    Path("src/pages/index.ts"),
    Path("src/pages/home/HomePage.tsx"),
    Path("src/pages/design-system/DesignSystemPage.tsx"),
    Path("src/pages/not-found/NotFoundPage.tsx"),
    Path("src/pages/chat/ChatPage.tsx"),
    Path("src/pages/chat/rich-message.tsx"),
    Path("src/pages/chat/plantuml-renderer.ts"),
    Path("src/pages/chat/markdown-utils.ts"),
    Path("src/pages/chat/markdown-table.tsx"),
    Path("src/pages/chat/diagram-block.tsx"),
    Path("src/pages/chat/copyable-code-block.tsx"),
    Path("src/pages/chat/attachment-chips.tsx"),
    Path("src/pages/chat/chat-composer.tsx"),
    Path("src/pages/chat/chat-bubble.tsx"),
    Path("src/pages/chat/chat-utils.ts"),
    Path("src/pages/chat/chat-types.ts"),
    Path("src/pages/workflow/WorkflowPage.tsx"),
    Path("src/features/design-system/design-system.tokens.ts"),
    Path("src/features/design-system/shadcn-components.ts"),
    Path("src/features/design-system/components/design-system-catalog.tsx"),
    Path("src/features/design-system/components/design-system-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/showcase-data.ts"),
    Path("src/features/design-system/components/design-system-showcase/showcase-card.tsx"),
    Path("src/features/design-system/components/design-system-showcase/overlays-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/navigation-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/forms-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/feedback-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/data-showcase.tsx"),
    Path("src/features/design-system/components/design-system-showcase/base-showcase.tsx"),
)

APP_EXPECTED_DIRS = (
    Path("src/components/ui"),
    Path("src/config"),
    Path("src/features"),
    Path("src/features/example"),
    Path("src/features/example/services"),
    Path("src/features/example/hooks"),
    Path("src/hooks"),
    Path("src/lib"),
    Path("src/lib/api"),
    Path("src/pages"),
)

SHADCN_STARTER_REQUIRED_FILES = (
    *(Path(f"src/components/ui/{component}.tsx") for component in SHADCN_STARTER_COMPONENTS),
    Path("src/hooks/use-mobile.ts"),
)

APP_FILE_TEMPLATES: dict[Path, str] = {
    Path("package.json"): """{
  "name": "react-template-workflow-app",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite --mode development",
    "dev:local": "vite --mode local",
    "build": "tsc -b && vite build --mode production",
    "build:development": "tsc -b && vite build --mode development",
    "build:staging": "tsc -b && vite build --mode staging",
    "preview": "vite preview --mode production",
    "preview:development": "vite preview --mode development",
    "typecheck": "tsc -b"
  },
  "dependencies": {
    "@radix-ui/react-slot": "latest",
    "class-variance-authority": "latest",
    "clsx": "latest",
    "lucide-react": "latest",
    "mermaid": "latest",
    "next-themes": "latest",
    "react": "latest",
    "react-dom": "latest",
    "react-markdown": "latest",
    "rehype-sanitize": "latest",
    "remark-gfm": "latest",
    "tailwind-merge": "latest",
    "type-fest": "latest"
  },
  "devDependencies": {
    "@tailwindcss/vite": "latest",
    "@types/node": "latest",
    "@types/react": "latest",
    "@types/react-dom": "latest",
    "@vitejs/plugin-react": "latest",
    "typescript": "latest",
    "tw-animate-css": "latest",
    "vite": "latest"
  }
}
""",
    Path("index.html"): """<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Template Workflow</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
""",
    Path(".env.development"): """VITE_APP_ENV=development
VITE_APP_NAME=React Template Workflow
VITE_API_BASE_URL=/api
VITE_API_PROXY_TARGET=http://localhost:8000
VITE_API_VERSION=v1
VITE_ENABLE_MOCKS=false
VITE_DEV_HOST=0.0.0.0
VITE_DEV_PORT=5173
VITE_PREVIEW_PORT=4173
""",
    Path(".env.production"): """VITE_APP_ENV=production
VITE_APP_NAME=React Template Workflow
VITE_API_BASE_URL=/api
VITE_API_VERSION=v1
VITE_ENABLE_MOCKS=false
VITE_DEV_HOST=0.0.0.0
VITE_DEV_PORT=5173
VITE_PREVIEW_PORT=4173
""",
    Path(".env.example"): """# =============================================================================
# Ambiente da aplicacao
# =============================================================================
VITE_APP_ENV=development
VITE_APP_NAME=React Template Workflow

# =============================================================================
# API global (defaults) — usados por features que NAO definem override proprio
# =============================================================================
# URL que o browser chama (em dev o Vite faz proxy de /api para o backend real).
VITE_API_BASE_URL=/api

# Destino real do backend no desenvolvimento (somente usado pelo proxy do Vite).
VITE_API_PROXY_TARGET=http://localhost:8000

# Versao default enviada no header X-API-Version para features sem override.
VITE_API_VERSION=v1

# =============================================================================
# API por feature (override) — cada dominio pode ter versao/base proprias
# =============================================================================
# Padrao de nome: VITE_<FEATURE>_API_VERSION e VITE_<FEATURE>_API_BASE_URL
# O cliente HTTP da feature le isso em src/features/<feature>/config.ts
# e instancia createApiClient() em src/features/<feature>/services/api-client.ts.
#
# Exemplo: feature "example" (src/features/example/config.ts)
#   - Se VITE_EXAMPLE_API_VERSION nao existir → usa VITE_API_VERSION (v1)
#   - Se VITE_EXAMPLE_API_BASE_URL nao existir → usa VITE_API_BASE_URL (/api)
#
# Cenario A — duas features na mesma base e mesma versao (comum):
#   VITE_API_VERSION=v1
#   VITE_API_BASE_URL=/api
#   (nao precisa definir VITE_EXAMPLE_* nem VITE_PEDIDOS_*)
#
# Cenario B — feature legada em v1, feature nova em v2 (mesmo backend):
#   VITE_API_VERSION=v1
#   VITE_PEDIDOS_API_VERSION=v2
#   VITE_API_BASE_URL=/api
#
# Cenario C — feature apontando para outro gateway:
#   VITE_API_BASE_URL=/api
#   VITE_RELATORIOS_API_BASE_URL=https://relatorios.exemplo.com/api
#   VITE_RELATORIOS_API_VERSION=v1
#
# Descomente para testar overrides da feature example:
# VITE_EXAMPLE_API_VERSION=v1
# VITE_EXAMPLE_API_BASE_URL=/api

# =============================================================================
# Dev server
# =============================================================================
VITE_ENABLE_MOCKS=false
VITE_DEV_HOST=0.0.0.0
VITE_DEV_PORT=5173
VITE_PREVIEW_PORT=4173
""",
    Path("vite.config.ts"): """import path from "node:path"
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
      proxy: {
        "/api": {
          changeOrigin: true,
          target: env.VITE_API_PROXY_TARGET || "http://localhost:8000",
          rewrite: (requestPath) => requestPath.replace(/^\\/api/, ""),
        },
      },
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
""",
    Path("tsconfig.json"): """{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
""",
    Path("tsconfig.app.json"): """{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "allowImportingTsExtensions": true,
    "module": "ESNext",
    "moduleDetection": "force",
    "moduleResolution": "bundler",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "ignoreDeprecations": "6.0",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}
""",
    Path("tsconfig.node.json"): """{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ESNext", "DOM"],
    "module": "ESNext",
    "moduleDetection": "force",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "types": ["node"],
    "ignoreDeprecations": "6.0",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}
""",
    Path("components.json"): """{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/index.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
""",
    Path("src/main.tsx"): """import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { ThemeProvider } from "next-themes"

import App from "./App"
import "./index.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      <App />
    </ThemeProvider>
  </StrictMode>,
)
""",
    Path("src/App.tsx"): """import { useEffect, useState } from "react"

import { AppShell, type AppPage } from "@/components/layout/app-shell"
import { ChatPage } from "@/pages/chat/ChatPage"
import { DesignSystemPage } from "@/pages/design-system/DesignSystemPage"
import { HomePage } from "@/pages/home/HomePage"
import { NotFoundPage } from "@/pages/not-found/NotFoundPage"
import { WorkflowPage } from "@/pages/workflow/WorkflowPage"

type RoutePage = AppPage | "not-found"

const appRoutes = {
  home: "/",
  chat: "/chat",
  "design-system": "/design-system",
  workflow: "/workflow",
} satisfies Record<AppPage, string>

const routeEntries = Object.entries(appRoutes) as Array<[AppPage, string]>

function readPageFromPath(): RoutePage {
  const path = window.location.pathname || "/"
  const route = routeEntries.find(([, routePath]) => routePath === path)

  return route?.[0] ?? "not-found"
}

function routeForPage(page: AppPage) {
  return appRoutes[page]
}

export default function App() {
  const [currentPage, setCurrentPage] = useState<RoutePage>(() => readPageFromPath())

  useEffect(() => {
    const handlePopState = () => setCurrentPage(readPageFromPath())

    window.addEventListener("popstate", handlePopState)
    return () => window.removeEventListener("popstate", handlePopState)
  }, [])

  function handleNavigate(page: AppPage) {
    const nextRoute = routeForPage(page)

    if (window.location.pathname === nextRoute) {
      setCurrentPage(page)
      return
    }

    window.history.pushState(null, "", nextRoute)
    setCurrentPage(page)
  }

  const shellPage = currentPage === "not-found" ? "home" : currentPage

  return (
    <AppShell currentPage={shellPage} onNavigate={handleNavigate}>
      {currentPage === "chat" ? <ChatPage /> : null}
      {currentPage === "design-system" ? <DesignSystemPage /> : null}
      {currentPage === "home" ? <HomePage /> : null}
      {currentPage === "workflow" ? <WorkflowPage /> : null}
      {currentPage === "not-found" ? (
        <NotFoundPage onNavigateHome={() => handleNavigate("home")} />
      ) : null}
    </AppShell>
  )
}
""",
    Path("src/vite-env.d.ts"): """/// <reference types="vite/client" />

type AppEnvironment = "local" | "development" | "staging" | "production"

interface ImportMetaEnv {
  readonly VITE_APP_ENV?: AppEnvironment
  readonly VITE_APP_NAME?: string
  readonly VITE_API_BASE_URL?: string
  readonly VITE_API_VERSION?: string
  readonly VITE_API_PROXY_TARGET?: string
  readonly VITE_ENABLE_MOCKS?: string
  readonly VITE_DEV_HOST?: string
  readonly VITE_DEV_PORT?: string
  readonly VITE_PREVIEW_PORT?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare const __APP_ENV__: AppEnvironment
""",
    Path("src/index.css"): """@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --radius-sm: calc(var(--radius) - 8px);
  --radius-md: calc(var(--radius) - 4px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 8px);
  --color-sidebar-ring: var(--sidebar-ring);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar: var(--sidebar);
}

:root {
  --radius: 1rem;
  --background: #ffffff;
  --foreground: #211922;
  --card: #ffffff;
  --card-foreground: #211922;
  --popover: #ffffff;
  --popover-foreground: #211922;
  --primary: #e60023;
  --primary-foreground: #ffffff;
  --secondary: #e5e5e0;
  --secondary-foreground: #000000;
  --muted: #f6f6f3;
  --muted-foreground: #62625b;
  --accent: #f6f6f3;
  --accent-foreground: #211922;
  --destructive: #9e0a0a;
  --destructive-foreground: #ffffff;
  --border: #dadad3;
  --input: #dadad3;
  --ring: #435ee5;
  --sidebar: #fbfbf9;
  --sidebar-foreground: #211922;
  --sidebar-primary: #e60023;
  --sidebar-primary-foreground: #ffffff;
  --sidebar-accent: #f6f6f3;
  --sidebar-accent-foreground: #211922;
  --sidebar-border: #dadad3;
  --sidebar-ring: #435ee5;
}

.dark {
  --background: #181815;
  --foreground: #f7f7f2;
  --card: #211f1d;
  --card-foreground: #f7f7f2;
  --popover: #211f1d;
  --popover-foreground: #f7f7f2;
  --primary: #e60023;
  --primary-foreground: #ffffff;
  --secondary: #33332e;
  --secondary-foreground: #f7f7f2;
  --muted: #262622;
  --muted-foreground: #b3b3b3;
  --accent: #33332e;
  --accent-foreground: #f7f7f2;
  --destructive: #cc001f;
  --destructive-foreground: #ffffff;
  --border: #3f3f38;
  --input: #3f3f38;
  --ring: #617bff;
  --sidebar: #211f1d;
  --sidebar-foreground: #f7f7f2;
  --sidebar-primary: #e60023;
  --sidebar-primary-foreground: #ffffff;
  --sidebar-accent: #33332e;
  --sidebar-accent-foreground: #f7f7f2;
  --sidebar-border: #3f3f38;
  --sidebar-ring: #617bff;
}

* {
  border-color: var(--border);
}

body {
  min-width: 320px;
  margin: 0;
  background: var(--background);
  color: var(--foreground);
  font-family:
    Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
}
""",
    Path("src/lib/utils.ts"): """import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
""",
    Path("src/config/app-env.ts"): """export type AppEnvironment = "local" | "development" | "staging" | "production"

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
""",
    Path("src/components/layout/app-shell.tsx"): """import { type ReactNode } from "react"
import {
  HomeIcon,
  Layers3Icon,
  MessageSquareTextIcon,
  MoonIcon,
  PaletteIcon,
  SparklesIcon,
  SunIcon,
  WorkflowIcon,
} from "lucide-react"
import { useTheme } from "next-themes"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInset,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import { appEnv } from "@/config/app-env"
import { cn } from "@/lib/utils"

type AppShellProps = {
  children: ReactNode
  currentPage: AppPage
  onNavigate: (page: AppPage) => void
}

export type AppPage = "home" | "chat" | "design-system" | "workflow"

type NavigationItem = {
  id: AppPage
  label: string
  description: string
  icon: typeof HomeIcon
}

const navigationGroups: Array<{ label: string; items: NavigationItem[] }> = [
  {
    label: "Template",
    items: [
      {
        id: "home",
        label: "Inicio",
        description: "Resumo operacional",
        icon: HomeIcon,
      },
      {
        id: "design-system",
        label: "Design System",
        description: "Componentes e tokens",
        icon: PaletteIcon,
      },
    ],
  },
  {
    label: "Construcao",
    items: [
      {
        id: "chat",
        label: "Assistente",
        description: "Markdown e IA",
        icon: MessageSquareTextIcon,
      },
      {
        id: "workflow",
        label: "Workflow",
        description: "Gates e agentes",
        icon: WorkflowIcon,
      },
    ],
  },
]

const navigationItems: NavigationItem[] = navigationGroups.flatMap((group) => group.items)

function ThemeToggleButton({ className }: { className?: string }) {
  const { resolvedTheme, setTheme } = useTheme()
  const isDark = resolvedTheme === "dark"
  const label = isDark ? "Ativar modo claro" : "Ativar modo escuro"
  const Icon = isDark ? SunIcon : MoonIcon

  return (
    <Button
      type="button"
      aria-label={label}
      className={className}
      size="icon"
      title={label}
      variant="outline"
      onClick={() => setTheme(isDark ? "light" : "dark")}
    >
      <Icon aria-hidden="true" />
      <span className="sr-only">{label}</span>
    </Button>
  )
}

export function AppShell({ children, currentPage, onNavigate }: AppShellProps) {
  const currentItem = navigationItems.find((item) => item.id === currentPage) ?? navigationItems[0]
  const brandLogoUrl = appEnv.brandLogoUrl
  const isChatPage = currentPage === "chat"

  return (
    <SidebarProvider defaultOpen>
      <Sidebar collapsible="icon" variant="inset">
        <SidebarHeader className="gap-3 p-3 group-data-[collapsible=icon]:items-center">
          <SidebarMenu>
            <SidebarMenuItem>
              <SidebarMenuButton
                aria-label={`${appEnv.brandName} - Design system ativo`}
                className="h-12 justify-start group-data-[collapsible=icon]:size-10! group-data-[collapsible=icon]:justify-center group-data-[collapsible=icon]:p-0!"
                size="lg"
                tooltip={appEnv.brandName}
              >
                <span className="flex size-10 shrink-0 items-center justify-center overflow-hidden rounded-md border bg-background p-1 group-data-[collapsible=icon]:size-8">
                  {brandLogoUrl ? (
                    <img
                      src={brandLogoUrl}
                      alt=""
                      aria-hidden="true"
                      className="size-7 shrink-0 object-contain group-data-[collapsible=icon]:size-6"
                    />
                  ) : (
                    <SparklesIcon
                      aria-hidden="true"
                      className="size-5 shrink-0 text-primary group-data-[collapsible=icon]:size-4"
                    />
                  )}
                </span>
                <span className="grid min-w-0 flex-1 text-left text-sm leading-tight group-data-[collapsible=icon]:hidden">
                  <span className="truncate font-semibold">{appEnv.brandName}</span>
                  <span className="truncate text-xs text-sidebar-foreground/70">
                    Design system ativo
                  </span>
                </span>
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarHeader>

        <SidebarSeparator />

        <SidebarContent>
          {navigationGroups.map((group) => (
            <SidebarGroup key={group.label}>
              <SidebarGroupLabel>{group.label}</SidebarGroupLabel>
              <SidebarGroupContent>
                <SidebarMenu>
                  {group.items.map((item) => (
                    <SidebarMenuItem key={item.id}>
                      <SidebarMenuButton
                        aria-label={`${item.label}: ${item.description}`}
                        aria-current={currentPage === item.id ? "page" : undefined}
                        className="group-data-[collapsible=icon]:justify-center"
                        isActive={currentPage === item.id}
                        size="lg"
                        tooltip={item.label}
                        onClick={() => onNavigate(item.id)}
                      >
                        <item.icon />
                        <span className="grid min-w-0 flex-1 leading-tight group-data-[collapsible=icon]:hidden">
                          <span className="truncate font-medium">{item.label}</span>
                          <span className="truncate text-xs text-sidebar-foreground/70">
                            {item.description}
                          </span>
                        </span>
                      </SidebarMenuButton>
                    </SidebarMenuItem>
                  ))}
                </SidebarMenu>
              </SidebarGroupContent>
            </SidebarGroup>
          ))}
        </SidebarContent>

        <SidebarSeparator />

        <SidebarFooter className="gap-3 p-3 group-data-[collapsible=icon]:items-center">
          <div className="rounded-md border bg-background p-2 group-data-[collapsible=icon]:hidden">
            <div className="flex items-center gap-2">
              <Layers3Icon />
              <p className="truncate text-sm font-medium">Bootstrap pronto</p>
            </div>
            <p className="mt-1 text-xs text-sidebar-foreground/70">
              Rotas path e sidebar entram como default.
            </p>
          </div>
          <SidebarMenu className="hidden group-data-[collapsible=icon]:block">
            <SidebarMenuItem>
              <SidebarMenuButton
                aria-label="Bootstrap pronto"
                className="justify-center"
                tooltip="Bootstrap pronto"
              >
                <Layers3Icon />
              </SidebarMenuButton>
            </SidebarMenuItem>
          </SidebarMenu>
        </SidebarFooter>

        <SidebarRail />
      </Sidebar>

      <SidebarInset
        className={cn(
          "relative overflow-hidden",
          isChatPage &&
            "md:peer-data-[variant=inset]:m-0 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-none md:peer-data-[variant=inset]:shadow-none md:peer-data-[variant=inset]:peer-data-[state=collapsed]:ml-0",
        )}
      >
        {isChatPage ? (
          <div className="absolute left-3 top-3 z-30 flex items-center gap-2">
            <SidebarTrigger className="shadow-sm backdrop-blur" />
            <ThemeToggleButton className="shadow-sm backdrop-blur" />
          </div>
        ) : (
          <header className="sticky top-0 z-20 flex h-16 items-center gap-3 border-b bg-background/95 px-4 backdrop-blur md:px-6">
            <SidebarTrigger className="-ml-1" />
            <Separator className="h-6" orientation="vertical" />
            <div className="min-w-0">
              <p className="truncate text-sm font-semibold">{currentItem.label}</p>
              <p className="truncate text-xs text-muted-foreground">
                {appEnv.appName} - {appEnv.appEnv} - {appEnv.apiBaseUrl}
              </p>
            </div>
            <div className="ml-auto flex items-center gap-2">
              <ThemeToggleButton />
              <Badge className="hidden sm:inline-flex" variant="secondary">
                {currentItem.description}
              </Badge>
            </div>
          </header>
        )}

        <main className="flex-1">{children}</main>
      </SidebarInset>
    </SidebarProvider>
  )
}
""",
    Path("src/components/layout/page-header.tsx"): """import { type ReactNode } from "react"

import { Badge } from "@/components/ui/badge"
import { Separator } from "@/components/ui/separator"

type PageHeaderProps = {
  actions?: ReactNode
  description?: string
  eyebrow?: string
  title: string
}

export function PageHeader({ actions, description, eyebrow, title }: PageHeaderProps) {
  return (
    <section className="flex flex-col gap-4 rounded-lg border bg-card p-6 text-card-foreground md:flex-row md:items-start md:justify-between">
      <div className="min-w-0">
        {eyebrow ? (
          <Badge className="mb-3 w-fit" variant="secondary">
            {eyebrow}
          </Badge>
        ) : null}
        <div className="flex flex-col gap-2">
          <h1 className="text-2xl font-semibold tracking-normal md:text-3xl">{title}</h1>
          {description ? (
            <p className="max-w-3xl text-sm text-muted-foreground md:text-base">{description}</p>
          ) : null}
        </div>
      </div>

      {actions ? (
        <>
          <Separator className="md:hidden" />
          <div className="flex shrink-0 flex-wrap items-center gap-2">{actions}</div>
        </>
      ) : null}
    </section>
  )
}
""",
    Path("src/components/layout/data-state.tsx"): """import { type ReactNode } from "react"
import { AlertCircleIcon, InboxIcon, RefreshCwIcon } from "lucide-react"

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
import { Skeleton } from "@/components/ui/skeleton"

type DataStateProps = {
  actionLabel?: string
  children?: ReactNode
  description?: string
  onAction?: () => void
  state: "ready" | "loading" | "empty" | "error"
  title: string
}

export function DataState({
  actionLabel,
  children,
  description,
  onAction,
  state,
  title,
}: DataStateProps) {
  if (state === "ready") {
    return <>{children}</>
  }

  if (state === "loading") {
    return (
      <Card aria-busy="true" aria-live="polite">
        <CardHeader>
          <CardTitle>{title}</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-col gap-3">
          <Skeleton className="h-4 w-3/4" />
          <Skeleton className="h-4 w-full" />
          <Skeleton className="h-4 w-2/3" />
        </CardContent>
      </Card>
    )
  }

  if (state === "error") {
    return (
      <Alert variant="destructive">
        <AlertCircleIcon aria-hidden="true" />
        <AlertTitle>{title}</AlertTitle>
        {description ? <AlertDescription>{description}</AlertDescription> : null}
        {actionLabel && onAction ? (
          <Button className="mt-3 w-fit" variant="secondary" onClick={onAction}>
            <RefreshCwIcon data-icon="inline-start" />
            {actionLabel}
          </Button>
        ) : null}
      </Alert>
    )
  }

  return (
    <Empty className="min-h-64 border bg-card">
      <EmptyHeader>
        <EmptyMedia variant="icon">
          <InboxIcon aria-hidden="true" />
        </EmptyMedia>
        <EmptyTitle>{title}</EmptyTitle>
        {description ? <EmptyDescription>{description}</EmptyDescription> : null}
      </EmptyHeader>
      {actionLabel && onAction ? (
        <EmptyContent>
          <Button onClick={onAction}>{actionLabel}</Button>
        </EmptyContent>
      ) : null}
    </Empty>
  )
}
""",
    Path("src/components/ui/file-upload-dropzone.tsx"): """import * as React from "react"
import { FileIcon, UploadCloudIcon, XIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

type FileUploadDropzoneProps = Omit<
  React.ComponentProps<"input">,
  "className" | "files" | "onChange" | "type" | "value"
> & {
  className?: string
  description?: string
  files?: File[]
  label?: string
  maxFiles?: number
  onFilesChange?: (files: File[]) => void
}

function fileKey(file: File) {
  return `${file.name}-${file.size}`
}

function partitionIncomingFiles(incoming: File[], existing: File[]) {
  const existingKeys = new Set(existing.map(fileKey))
  const seenIncoming = new Set<string>()
  const accepted: File[] = []
  const duplicateNames: string[] = []

  for (const file of incoming) {
    const key = fileKey(file)

    if (existingKeys.has(key) || seenIncoming.has(key)) {
      if (!duplicateNames.includes(file.name)) {
        duplicateNames.push(file.name)
      }
      continue
    }

    seenIncoming.add(key)
    accepted.push(file)
  }

  return { accepted, duplicateNames }
}

function formatFileSize(size: number) {
  if (size < 1024) {
    return `${size} B`
  }

  if (size < 1024 * 1024) {
    return `${Math.round(size / 1024)} KB`
  }

  return `${(size / 1024 / 1024).toFixed(1)} MB`
}

function FileUploadDropzone({
  accept,
  className,
  description = "Arraste arquivos para ca ou selecione no computador.",
  disabled,
  files,
  id,
  label = "Upload de arquivos",
  maxFiles = 4,
  multiple = true,
  onFilesChange,
  ...props
}: FileUploadDropzoneProps) {
  const generatedId = React.useId()
  const inputId = id ?? generatedId
  const inputRef = React.useRef<HTMLInputElement>(null)
  const errorId = `${inputId}-error`
  const [isDragging, setIsDragging] = React.useState(false)
  const [internalFiles, setInternalFiles] = React.useState<File[]>([])
  const [validationError, setValidationError] = React.useState<string | null>(null)
  const selectedFiles = files ?? internalFiles

  const updateFiles = React.useCallback(
    (nextFiles: File[]) => {
      const limitedFiles = nextFiles.slice(0, multiple ? maxFiles : 1)

      if (!files) {
        setInternalFiles(limitedFiles)
      }

      onFilesChange?.(limitedFiles)
    },
    [files, maxFiles, multiple, onFilesChange],
  )

  function handleFiles(fileList: FileList | null) {
    if (!fileList) {
      return
    }

    const incoming = Array.from(fileList)
    const messages: string[] = []

    if (!multiple) {
      const { accepted, duplicateNames } = partitionIncomingFiles(
        incoming.slice(0, 1),
        selectedFiles,
      )

      if (duplicateNames.length > 0) {
        messages.push(`O arquivo "${duplicateNames[0]}" já foi adicionado.`)
      }

      if (accepted.length > 0) {
        updateFiles(accepted)
      }

      setValidationError(messages.length > 0 ? messages.join(" ") : null)

      if (inputRef.current) {
        inputRef.current.value = ""
      }
      return
    }

    const { accepted, duplicateNames } = partitionIncomingFiles(incoming, selectedFiles)

    if (duplicateNames.length > 0) {
      messages.push(
        duplicateNames.length === 1
          ? `O arquivo "${duplicateNames[0]}" já foi adicionado.`
          : `Estes arquivos já foram adicionados: ${duplicateNames.join(", ")}.`,
      )
    }

    const availableSlots = Math.max(maxFiles - selectedFiles.length, 0)
    const filesToAdd = accepted.slice(0, availableSlots)

    if (accepted.length > availableSlots) {
      messages.push(`Limite de ${maxFiles} arquivos.`)
    }

    if (filesToAdd.length > 0) {
      updateFiles([...selectedFiles, ...filesToAdd])
    }

    setValidationError(messages.length > 0 ? messages.join(" ") : null)

    if (inputRef.current) {
      inputRef.current.value = ""
    }
  }

  function removeFile(fileName: string) {
    setValidationError(null)
    updateFiles(selectedFiles.filter((file) => file.name !== fileName))
  }

  return (
    <div className={cn("flex flex-col gap-3", className)}>
      <input
        ref={inputRef}
        id={inputId}
        type="file"
        accept={accept}
        disabled={disabled}
        multiple={multiple}
        className="sr-only"
        onChange={(event) => handleFiles(event.target.files)}
        {...props}
      />
      <div
        aria-disabled={disabled}
        aria-describedby={validationError ? errorId : undefined}
        aria-invalid={validationError ? true : undefined}
        onDragEnter={(event) => {
          event.preventDefault()
          if (!disabled) {
            setIsDragging(true)
          }
        }}
        onDragLeave={(event) => {
          event.preventDefault()
          setIsDragging(false)
        }}
        onDragOver={(event) => {
          event.preventDefault()
        }}
        onDrop={(event) => {
          event.preventDefault()
          setIsDragging(false)

          if (!disabled) {
            handleFiles(event.dataTransfer.files)
          }
        }}
        className={cn(
          "flex min-h-48 flex-col items-center justify-center gap-3 rounded-lg border border-dashed bg-muted p-6 text-center transition-colors",
          isDragging && "border-primary bg-primary/5",
          validationError && "border-destructive ring-destructive/20",
          disabled && "pointer-events-none opacity-50",
        )}
      >
        <span className="flex size-11 items-center justify-center rounded-full bg-background text-primary">
          <UploadCloudIcon aria-hidden="true" />
        </span>
        <div className="flex max-w-md flex-col gap-1">
          <label htmlFor={inputId} className="text-sm font-semibold">
            {label}
          </label>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
        <Button
          type="button"
          variant="secondary"
          disabled={disabled}
          onClick={() => inputRef.current?.click()}
        >
          <UploadCloudIcon data-icon="inline-start" />
          Selecionar arquivos
        </Button>
      </div>

      {validationError ? (
        <p id={errorId} role="alert" className="text-sm text-destructive">
          {validationError}
        </p>
      ) : null}

      {selectedFiles.length > 0 ? (
        <div className="flex flex-col gap-2" aria-live="polite">
          {selectedFiles.map((file) => (
            <div
              key={fileKey(file)}
              className="flex items-center gap-3 rounded-md border bg-background px-3 py-2"
            >
              <FileIcon aria-hidden="true" />
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium">{file.name}</p>
                <p className="text-xs text-muted-foreground">{formatFileSize(file.size)}</p>
              </div>
              <Button
                type="button"
                size="icon-sm"
                variant="ghost"
                aria-label={`Remover ${file.name}`}
                onClick={() => removeFile(file.name)}
              >
                <XIcon />
              </Button>
            </div>
          ))}
        </div>
      ) : null}
    </div>
  )
}

export { FileUploadDropzone }
""",
    Path("src/pages/home/HomePage.tsx"): """import { PageHeader } from "@/components/layout/page-header"
import { DesignSystemPanel } from "@/features/design-system/components/design-system-panel"

export function HomePage() {
  return (
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 md:px-6 lg:py-8">
      <PageHeader
        eyebrow="Bootstrap"
        title="Starter React com workflow pronto"
        description="Base operacional com sidebar, rotas, design system, componentes shadcn/ui e estados reutilizaveis para novas features."
      />
      <DesignSystemPanel />
    </div>
  )
}
""",
    Path("src/pages/chat/ChatPage.tsx"): r"""import { useEffect, useRef, useState } from "react"

import { Card, CardContent } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"

import { ChatBubble } from "./chat-bubble"
import { ChatComposer } from "./chat-composer"
import { type BrowserSpeechRecognition, type ChatAttachment, type ChatMessage } from "./chat-types"
import {
  createAttachment,
  createMessageId,
  getSpeechRecognitionConstructor,
  runAssistantResponse,
} from "./chat-utils"

const initialMessages: ChatMessage[] = [
  {
    id: "welcome",
    role: "assistant",
    status: "done",
    content: [
      "Pronto para receber Markdown do usuario e da IA.",
      "",
      "- Listas, links e tabelas usam GitHub Flavored Markdown.",
      "- Tabelas, codigo e diagramas ganham acoes de leitura.",
      "- Mermaid e PlantUML podem ser expandidos, copiados e abertos em PNG/SVG.",
      "- PDFs e imagens anexadas exibem preview no composer e na conversa.",
      "- Respostas longas permanecem dentro da area da conversa.",
      "",
      "```mermaid",
      "flowchart LR",
      "  usuario[Usuario] --> chat[Chat]",
      "  chat --> backend[Backend]",
      "  backend --> resposta[IA]",
      "```",
    ].join("\n"),
  },
]

export function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>(initialMessages)
  const [input, setInput] = useState("")
  const [attachments, setAttachments] = useState<ChatAttachment[]>([])
  const [isResponding, setIsResponding] = useState(false)
  const [isListening, setIsListening] = useState(false)
  const [isSpeechSupported, setIsSpeechSupported] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const recognitionRef = useRef<BrowserSpeechRecognition | null>(null)
  const attachmentUrlsRef = useRef(new Set<string>())

  useEffect(() => {
    setIsSpeechSupported(Boolean(getSpeechRecognitionConstructor()))

    return () => {
      recognitionRef.current?.abort()
      attachmentUrlsRef.current.forEach((url) => URL.revokeObjectURL(url))
      attachmentUrlsRef.current.clear()
    }
  }, [])

  async function sendMessage() {
    const prompt = input.trim()

    if ((!prompt && attachments.length === 0) || isResponding) {
      return
    }

    const assistantId = createMessageId()
    const outgoingAttachments = attachments

    setInput("")
    setAttachments([])
    setError(null)
    setIsResponding(true)
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: createMessageId(),
        role: "user",
        content: prompt || "Referencias anexadas.",
        attachments: outgoingAttachments,
        status: "done",
      },
      { id: assistantId, role: "assistant", content: "", status: "streaming" },
    ])

    try {
      await runAssistantResponse({
        attachmentCount: outgoingAttachments.length,
        onChunk: (chunk) => {
          setMessages((currentMessages) =>
            currentMessages.map((message) =>
              message.id === assistantId
                ? { ...message, content: `${message.content}${chunk}` }
                : message,
            ),
          )
        },
      })

      setMessages((currentMessages) =>
        currentMessages.map((message) =>
          message.id === assistantId ? { ...message, status: "done" } : message,
        ),
      )
    } catch {
      setError("Nao foi possivel gerar a resposta agora.")
      setMessages((currentMessages) =>
        currentMessages.map((message) =>
          message.id === assistantId
            ? { ...message, content: "Falha ao gerar resposta.", status: "error" }
            : message,
        ),
      )
    } finally {
      setIsResponding(false)
    }
  }

  function handleFilesChange(files: FileList | null) {
    if (!files) {
      return
    }

    const availableSlots = Math.max(6 - attachments.length, 0)
    const selectedFiles = Array.from(files)
    const nextAttachments = selectedFiles
      .slice(0, availableSlots)
      .map((file) => {
        const attachment = createAttachment(file)

        attachmentUrlsRef.current.add(attachment.url)
        return attachment
      })

    if (selectedFiles.length > availableSlots) {
      setError("Limite de 6 anexos por mensagem.")
    } else {
      setError(null)
    }

    setAttachments((currentAttachments) => [...currentAttachments, ...nextAttachments])

    if (fileInputRef.current) {
      fileInputRef.current.value = ""
    }
  }

  function removeAttachment(attachment: ChatAttachment) {
    URL.revokeObjectURL(attachment.url)
    attachmentUrlsRef.current.delete(attachment.url)
    setAttachments((currentAttachments) =>
      currentAttachments.filter((currentAttachment) => currentAttachment.id !== attachment.id),
    )
  }

  function toggleSpeechInput() {
    if (isListening) {
      recognitionRef.current?.stop()
      setIsListening(false)
      return
    }

    const SpeechRecognition = getSpeechRecognitionConstructor()

    if (!SpeechRecognition) {
      setError("Este navegador nao oferece transcricao por voz.")
      return
    }

    const recognition = new SpeechRecognition()

    recognition.lang = navigator.language || "pt-BR"
    recognition.continuous = false
    recognition.interimResults = false
    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .slice(event.resultIndex)
        .map((result) => result[0]?.transcript.trim() ?? "")
        .filter(Boolean)
        .join(" ")

      if (transcript) {
        setInput((currentInput) => `${currentInput}${currentInput ? " " : ""}${transcript}`)
      }
    }
    recognition.onerror = () => {
      setError("Nao foi possivel transcrever o audio.")
      setIsListening(false)
    }
    recognition.onend = () => setIsListening(false)
    recognitionRef.current = recognition
    setError(null)
    setIsListening(true)
    recognition.start()
  }

  return (
    <div className="flex h-svh w-full min-w-0 flex-col overflow-hidden bg-background">
      <Card className="flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden rounded-none border-0 bg-background shadow-none">
        <CardContent className="flex min-h-0 min-w-0 flex-1 flex-col p-0">
          <ScrollArea className="min-h-0 min-w-0 flex-1">
            <div className="min-w-0 px-3 pb-6 pt-20 sm:px-6 md:px-8 md:pt-16" aria-live="polite">
              <div className="mx-auto flex w-full max-w-5xl flex-col gap-6">
                {messages.map((message) => (
                  <ChatBubble key={message.id} message={message} />
                ))}
              </div>
            </div>
          </ScrollArea>

          <ChatComposer
            attachments={attachments}
            error={error}
            fileInputRef={fileInputRef}
            input={input}
            isListening={isListening}
            isResponding={isResponding}
            isSpeechSupported={isSpeechSupported}
            onFilesChange={handleFilesChange}
            onInputChange={setInput}
            onRemoveAttachment={removeAttachment}
            onSubmit={() => void sendMessage()}
            onToggleSpeechInput={toggleSpeechInput}
          />
        </CardContent>
      </Card>
    </div>
  )
}
""",
    Path("src/pages/chat/chat-types.ts"): r"""export type ChatRole = "assistant" | "user"

export type ChatAttachment = {
  id: string
  name: string
  size: number
  type: string
  url: string
}

export type ChatMessage = {
  id: string
  role: ChatRole
  content: string
  attachments?: ChatAttachment[]
  status?: "streaming" | "done" | "error"
}

export type BrowserSpeechRecognitionEvent = Event & {
  resultIndex: number
  results: SpeechRecognitionResultList
}

export type BrowserSpeechRecognition = {
  continuous: boolean
  interimResults: boolean
  lang: string
  onend: (() => void) | null
  onerror: (() => void) | null
  onresult: ((event: BrowserSpeechRecognitionEvent) => void) | null
  abort: () => void
  start: () => void
  stop: () => void
}

export type BrowserSpeechRecognitionConstructor = new () => BrowserSpeechRecognition

export type WindowWithSpeechRecognition = Window &
  typeof globalThis & {
    SpeechRecognition?: BrowserSpeechRecognitionConstructor
    webkitSpeechRecognition?: BrowserSpeechRecognitionConstructor
  }
""",
    Path("src/pages/chat/chat-utils.ts"): r"""import {
  type ChatAttachment,
  type ChatMessage,
  type WindowWithSpeechRecognition,
} from "./chat-types"

export function createMessageId() {
  return crypto.randomUUID?.() ?? `message-${Date.now()}-${Math.random().toString(16).slice(2)}`
}

function wait(ms: number) {
  return new Promise((resolve) => {
    window.setTimeout(resolve, ms)
  })
}

export function createAttachment(file: File): ChatAttachment {
  return {
    id: createMessageId(),
    name: file.name,
    size: file.size,
    type: file.type || "application/octet-stream",
    url: URL.createObjectURL(file),
  }
}

export function getSpeechRecognitionConstructor() {
  const speechWindow = window as WindowWithSpeechRecognition

  return speechWindow.SpeechRecognition ?? speechWindow.webkitSpeechRecognition
}

function createAssistantMarkdown(attachmentCount: number) {
  return [
    "Recebi sua mensagem em Markdown e mantive uma estrutura pronta para integrar com uma API real.",
    attachmentCount > 0
      ? `Tambem recebi ${attachmentCount} referencia(s) anexada(s) para o backend processar.`
      : "",
    "",
    "| Capacidade | Status |",
    "| --- | --- |",
    "| Markdown do usuario | Ativo |",
    "| Markdown da IA | Ativo |",
    "| Tabelas com acoes | Ativo |",
    "| Mermaid no cliente | Ativo |",
    "| PlantUML no cliente | Ativo |",
    "| Anexos como referencia | Ativo |",
    "| Conteudo sanitizado | Ativo |",
    "",
    "```plantuml",
    "@startuml",
    "actor Usuario",
    "participant Chat",
    "participant Backend",
    "Usuario -> Chat: envia mensagem e anexos",
    "Chat -> Backend: referencias para IA",
    "Backend --> Chat: resposta renderizada",
    "@enduml",
    "```",
  ]
    .filter(Boolean)
    .join("\n")
}

export async function runAssistantResponse({
  attachmentCount,
  onChunk,
}: {
  attachmentCount: number
  onChunk: (chunk: string) => void
}) {
  const response = createAssistantMarkdown(attachmentCount)
  const chunks = response.match(/.{1,28}(\s|$)/g) ?? [response]

  for (const chunk of chunks) {
    await wait(45)
    onChunk(chunk)
  }
}

export function formatMessageForCopy(message: ChatMessage) {
  const attachmentText = message.attachments
    ?.map((attachment) => `- ${attachment.name} (${attachment.type}, ${attachment.size} bytes)`)
    .join("\n")

  return [message.content, attachmentText ? `**Anexos**\n${attachmentText}` : ""]
    .filter(Boolean)
    .join("\n\n")
}

export function createClipboardHtml(contentElement: HTMLElement | null) {
  if (!contentElement) {
    return ""
  }

  const clonedContent = contentElement.cloneNode(true) as HTMLElement

  clonedContent
    .querySelectorAll("[data-clipboard-exclude], button")
    .forEach((element) => element.remove())

  return clonedContent.innerHTML.trim()
}
""",
    Path("src/pages/chat/chat-bubble.tsx"): r"""import { useRef, useState } from "react"
import { BotIcon, CheckIcon, CopyIcon, Loader2Icon, UserIcon } from "lucide-react"

import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

import { AttachmentChips } from "./attachment-chips"
import { type ChatMessage } from "./chat-types"
import { createClipboardHtml, formatMessageForCopy } from "./chat-utils"
import { RichMarkdownMessage } from "./rich-message"

export function ChatBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === "user"
  const [copied, setCopied] = useState(false)
  const contentRef = useRef<HTMLDivElement>(null)

  async function handleCopyMessage() {
    if (!navigator.clipboard) {
      return
    }

    const plainText = formatMessageForCopy(message)
    const html = createClipboardHtml(contentRef.current)

    try {
      if (html && typeof ClipboardItem !== "undefined" && navigator.clipboard.write) {
        await navigator.clipboard.write([
          new ClipboardItem({
            "text/plain": new Blob([plainText], { type: "text/plain" }),
            "text/html": new Blob([html], { type: "text/html" }),
          }),
        ])
      } else {
        await navigator.clipboard.writeText(plainText)
      }
    } catch {
      await navigator.clipboard.writeText(plainText)
    }

    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <article className={cn("group flex w-full min-w-0 items-start gap-3", isUser && "justify-end")}>
      {!isUser ? (
        <Avatar className="mt-1 size-8 shrink-0 border">
          <AvatarFallback>
            <BotIcon className="size-4" aria-hidden="true" />
          </AvatarFallback>
        </Avatar>
      ) : null}

      {isUser ? (
        <Button
          type="button"
          size="icon-sm"
          variant="ghost"
          className="mt-1 opacity-100 sm:opacity-0 sm:transition-opacity sm:group-hover:opacity-100 sm:focus-visible:opacity-100"
          aria-label={copied ? "Mensagem copiada" : "Copiar mensagem"}
          onClick={handleCopyMessage}
        >
          {copied ? <CheckIcon /> : <CopyIcon />}
        </Button>
      ) : null}

      <div
        className={cn(
          "min-w-0 rounded-lg px-4 py-3 text-base leading-7",
          "overflow-hidden break-words [overflow-wrap:anywhere] [&_li]:ml-5 [&_ol]:list-decimal [&_p+p]:mt-3 [&_table]:border-collapse [&_ul]:list-disc",
          isUser
            ? "w-fit max-w-[min(42rem,82%)] border bg-muted text-foreground"
            : "w-full max-w-none bg-background text-foreground",
        )}
      >
        <div ref={contentRef} className="min-w-0 w-full max-w-full">
          <RichMarkdownMessage content={message.content || " "} />
          {message.attachments?.length ? (
            <div className="mt-3">
              <AttachmentChips attachments={message.attachments} />
            </div>
          ) : null}
        </div>
        {message.status === "streaming" ? (
          <span className="mt-3 inline-flex items-center gap-2 text-xs text-muted-foreground">
            <Loader2Icon className="size-3 animate-spin" aria-hidden="true" />
            Gerando resposta
          </span>
        ) : null}
      </div>

      {!isUser ? (
        <Button
          type="button"
          size="icon-sm"
          variant="ghost"
          className="mt-1 opacity-100 sm:opacity-0 sm:transition-opacity sm:group-hover:opacity-100 sm:focus-visible:opacity-100"
          aria-label={copied ? "Mensagem copiada" : "Copiar mensagem"}
          onClick={handleCopyMessage}
        >
          {copied ? <CheckIcon /> : <CopyIcon />}
        </Button>
      ) : null}

      {isUser ? (
        <Avatar className="mt-1 size-8 shrink-0 border">
          <AvatarFallback>
            <UserIcon className="size-4" aria-hidden="true" />
          </AvatarFallback>
        </Avatar>
      ) : null}
    </article>
  )
}
""",
    Path("src/pages/chat/chat-composer.tsx"): r"""import {
  type ChangeEvent,
  type KeyboardEvent,
  type RefObject,
} from "react"
import { Loader2Icon, MicIcon, PaperclipIcon, SendIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

import { AttachmentChips } from "./attachment-chips"
import { type ChatAttachment } from "./chat-types"

type ChatComposerProps = {
  attachments: ChatAttachment[]
  error: string | null
  fileInputRef: RefObject<HTMLInputElement | null>
  input: string
  isListening: boolean
  isResponding: boolean
  isSpeechSupported: boolean
  onFilesChange: (files: FileList | null) => void
  onInputChange: (value: string) => void
  onRemoveAttachment: (attachment: ChatAttachment) => void
  onSubmit: () => void
  onToggleSpeechInput: () => void
}

export function ChatComposer({
  attachments,
  error,
  fileInputRef,
  input,
  isListening,
  isResponding,
  isSpeechSupported,
  onFilesChange,
  onInputChange,
  onRemoveAttachment,
  onSubmit,
  onToggleSpeechInput,
}: ChatComposerProps) {
  return (
    <form
      className="min-w-0 border-t bg-background/95 px-3 py-3 backdrop-blur md:px-8 md:py-4"
      onSubmit={(event) => {
        event.preventDefault()
        onSubmit()
      }}
    >
      <input
        ref={fileInputRef}
        type="file"
        multiple
        className="sr-only"
        accept=".pdf,.doc,.docx,.txt,.md,.json,.csv,.png,.jpg,.jpeg,.webp"
        onChange={(event) => onFilesChange(event.target.files)}
      />
      <div className="mx-auto flex w-full max-w-5xl flex-col gap-2">
        {error ? <p className="text-sm text-destructive">{error}</p> : null}
        <div className="min-w-0 rounded-lg border bg-background p-2 shadow-sm focus-within:ring-[3px] focus-within:ring-ring/50">
          <AttachmentChips attachments={attachments} onRemove={onRemoveAttachment} />
          <Textarea
            value={input}
            placeholder="Envie Markdown, cole codigo ou descreva uma tarefa..."
            className="field-sizing-fixed min-h-24 min-w-0 max-w-full resize-none overflow-x-hidden border-0 bg-transparent px-2 shadow-none [overflow-wrap:anywhere] focus-visible:ring-0 focus-visible:ring-offset-0"
            disabled={isResponding}
            aria-label="Mensagem"
            onChange={(event: ChangeEvent<HTMLTextAreaElement>) => onInputChange(event.target.value)}
            onKeyDown={(event: KeyboardEvent<HTMLTextAreaElement>) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault()
                onSubmit()
              }
            }}
          />
          <div className="mt-2 flex flex-col gap-2 border-t pt-2 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex flex-wrap gap-2">
              <Button
                type="button"
                size="sm"
                variant="secondary"
                onClick={() => fileInputRef.current?.click()}
                disabled={isResponding}
              >
                <PaperclipIcon data-icon="inline-start" />
                Anexar
              </Button>
              <Button
                type="button"
                size="sm"
                variant={isListening ? "default" : "secondary"}
                disabled={isResponding || !isSpeechSupported}
                onClick={onToggleSpeechInput}
              >
                {isListening ? (
                  <Loader2Icon className="animate-spin" data-icon="inline-start" />
                ) : (
                  <MicIcon data-icon="inline-start" />
                )}
                {isListening ? "Ouvindo" : "Falar com chat"}
              </Button>
            </div>
            <Button
              type="submit"
              size="sm"
              disabled={isResponding || (!input.trim() && attachments.length === 0)}
              className="sm:w-fit"
            >
              {isResponding ? (
                <Loader2Icon className="animate-spin" data-icon="inline-start" />
              ) : (
                <SendIcon data-icon="inline-start" />
              )}
              Enviar
            </Button>
          </div>
        </div>
      </div>
    </form>
  )
}
""",
    Path("src/pages/chat/attachment-chips.tsx"): r"""import { DownloadIcon, FileIcon, FileTextIcon, ImageIcon, XIcon } from "lucide-react"

import { Button } from "@/components/ui/button"

import { type ChatAttachment } from "./chat-types"
import { formatFileSize } from "./markdown-utils"

type AttachmentPreviewKind = "image" | "pdf" | "file"

const imageExtensions = [".png", ".jpg", ".jpeg", ".webp"]

function hasKnownExtension(name: string, extensions: string[]) {
  const normalizedName = name.toLowerCase()

  return extensions.some((extension) => normalizedName.endsWith(extension))
}

function getAttachmentPreviewKind(attachment: ChatAttachment): AttachmentPreviewKind {
  if (attachment.type.startsWith("image/") || hasKnownExtension(attachment.name, imageExtensions)) {
    return "image"
  }

  if (attachment.type === "application/pdf" || hasKnownExtension(attachment.name, [".pdf"])) {
    return "pdf"
  }

  return "file"
}

function getAttachmentLabel(kind: AttachmentPreviewKind) {
  if (kind === "image") {
    return "Imagem"
  }

  if (kind === "pdf") {
    return "PDF"
  }

  return "Arquivo"
}

function AttachmentVisualPreview({
  attachment,
  kind,
}: {
  attachment: ChatAttachment
  kind: AttachmentPreviewKind
}) {
  if (kind === "image") {
    return (
      <a
        href={attachment.url}
        target="_blank"
        rel="noreferrer"
        aria-label={`Abrir preview de ${attachment.name}`}
        className="block focus-visible:outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50"
      >
        <img
          src={attachment.url}
          alt={`Preview de ${attachment.name}`}
          className="h-36 w-full bg-background object-cover"
          loading="lazy"
        />
      </a>
    )
  }

  if (kind === "pdf") {
    return (
      <div className="h-44 overflow-hidden bg-background">
        <iframe
          src={`${attachment.url}#toolbar=0&navpanes=0&scrollbar=0`}
          title={`Preview de ${attachment.name}`}
          className="h-full w-full border-0"
          loading="lazy"
          tabIndex={-1}
        />
      </div>
    )
  }

  return (
    <div className="flex h-28 flex-col items-center justify-center gap-2 bg-background text-muted-foreground">
      <FileIcon className="size-8" aria-hidden="true" />
      <span className="text-xs font-medium">Sem preview</span>
    </div>
  )
}

export function AttachmentChips({
  attachments,
  onRemove,
}: {
  attachments: ChatAttachment[]
  onRemove?: (attachment: ChatAttachment) => void
}) {
  if (attachments.length === 0) {
    return null
  }

  return (
    <div className="grid gap-2 sm:grid-cols-2" aria-live="polite">
      {attachments.map((attachment) => {
        const kind = getAttachmentPreviewKind(attachment)
        const label = getAttachmentLabel(kind)
        const Icon = kind === "image" ? ImageIcon : kind === "pdf" ? FileTextIcon : FileIcon

        return (
          <article
            key={attachment.id}
            className="min-w-0 animate-in overflow-hidden rounded-lg border bg-muted/60 text-sm shadow-sm fade-in-0 zoom-in-95"
            aria-label={`${label}: ${attachment.name}`}
          >
            <div data-clipboard-exclude className="relative">
              <AttachmentVisualPreview attachment={attachment} kind={kind} />
              {onRemove ? (
                <Button
                  data-clipboard-exclude
                  type="button"
                  size="icon-xs"
                  variant="secondary"
                  className="absolute right-2 top-2 shadow-sm"
                  aria-label={`Remover ${attachment.name}`}
                  onClick={() => onRemove(attachment)}
                >
                  <XIcon aria-hidden="true" />
                </Button>
              ) : null}
            </div>
            <div className="flex min-w-0 items-center gap-2 p-3">
              <Icon className="size-4 shrink-0 text-muted-foreground" aria-hidden="true" />
              <div className="min-w-0 flex-1">
                <a
                  href={attachment.url}
                  download={attachment.name}
                  className="block truncate font-medium underline-offset-4 hover:underline"
                >
                  {attachment.name}
                </a>
                <p className="truncate text-xs text-muted-foreground">
                  {label} - {formatFileSize(attachment.size)}
                </p>
              </div>
              <Button data-clipboard-exclude asChild type="button" size="icon-xs" variant="ghost">
                <a href={attachment.url} download={attachment.name} aria-label={`Baixar ${attachment.name}`}>
                  <DownloadIcon aria-hidden="true" />
                </a>
              </Button>
            </div>
          </article>
        )
      })}
    </div>
  )
}
""",
    Path("src/pages/chat/copyable-code-block.tsx"): r"""import { useState } from "react"
import { CheckIcon, CopyIcon } from "lucide-react"

import { Button } from "@/components/ui/button"

import { type CodeChild, copyText } from "./markdown-utils"

export function CopyableCodeBlock({ code, language }: CodeChild) {
  const [copied, setCopied] = useState(false)

  async function handleCopy() {
    await copyText(code)
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-foreground text-background">
      <div data-clipboard-exclude className="flex min-h-10 min-w-0 items-center gap-2 border-b border-background/15 px-3">
        <span className="truncate text-xs font-medium text-background/70">{language}</span>
        <Button
          type="button"
          size="sm"
          variant="ghost"
          className="ml-auto h-8 text-background hover:bg-background/10 hover:text-background"
          onClick={handleCopy}
        >
          {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
          {copied ? "Copiado" : "Copiar"}
        </Button>
      </div>
      <pre className="max-w-full overflow-x-auto p-4 text-sm leading-6">
        <code className="block min-w-max whitespace-pre">{code}</code>
      </pre>
    </div>
  )
}
""",
    Path("src/pages/chat/diagram-block.tsx"): r"""import { type PointerEvent, useEffect, useId, useRef, useState } from "react"
import mermaid from "mermaid"
import {
  CheckIcon,
  CopyIcon,
  DownloadIcon,
  ExpandIcon,
  ExternalLinkIcon,
  Loader2Icon,
  MinusIcon,
  PlusIcon,
  RotateCcwIcon,
} from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { cn } from "@/lib/utils"

import { normalizePlantUmlSource, renderPlantUmlToSvg } from "./plantuml-renderer"
import { type CodeChild, copyText } from "./markdown-utils"

const fallbackDiagramTextColor = "#211922"
const fallbackDiagramBackgroundColor = "#ffffff"
const fallbackDiagramSurfaceColor = "#f6f6f3"
const fallbackDiagramBorderColor = "#dadad3"
const fallbackDiagramMutedTextColor = "#62625b"
const defaultDiagramZoom = 1.2

function readCssColorVariable(name: string, fallback: string) {
  const value = window.getComputedStyle(document.documentElement).getPropertyValue(name).trim()

  return value || fallback
}

function getDiagramColors() {
  return {
    background: readCssColorVariable("--background", fallbackDiagramBackgroundColor),
    border: readCssColorVariable("--border", fallbackDiagramBorderColor),
    mutedForeground: readCssColorVariable("--muted-foreground", fallbackDiagramMutedTextColor),
    surface: readCssColorVariable("--muted", fallbackDiagramSurfaceColor),
    text: readCssColorVariable("--foreground", fallbackDiagramTextColor),
  }
}

function createDiagramThemeCss() {
  const colors = getDiagramColors()

  return [
    `svg{color:${colors.text};font-family:Inter,sans-serif;}`,
    `.nodeLabel,.edgeLabel,.label,text,tspan{color:${colors.text}!important;fill:${colors.text}!important;}`,
    `.edgeLabel,.label{background:${colors.background}!important;}`,
    `.edgeLabel rect,.labelBkg{fill:${colors.background}!important;opacity:1!important;}`,
    `.node rect,.node circle,.node ellipse,.node polygon{fill:${colors.surface}!important;stroke:${colors.border}!important;}`,
    `.cluster rect{fill:${colors.surface}!important;stroke:${colors.border}!important;}`,
    `.edgePath path,.flowchart-link{stroke:${colors.text}!important;}`,
    `marker path{fill:${colors.text}!important;stroke:${colors.text}!important;}`,
  ].join("")
}

function initializeMermaid() {
  const colors = getDiagramColors()

  mermaid.initialize({
    flowchart: {
      htmlLabels: false,
    },
    securityLevel: "strict",
    startOnLoad: false,
    theme: "base",
    themeVariables: {
      fontFamily: "Inter, sans-serif",
      background: colors.background,
      clusterBkg: colors.surface,
      clusterBorder: colors.border,
      edgeLabelBackground: colors.background,
      lineColor: colors.text,
      mainBkg: colors.surface,
      nodeBorder: colors.border,
      nodeTextColor: colors.text,
      primaryBorderColor: colors.border,
      primaryColor: colors.surface,
      primaryTextColor: colors.text,
      secondaryBorderColor: colors.border,
      secondaryColor: colors.background,
      secondaryTextColor: colors.text,
      tertiaryBorderColor: colors.border,
      tertiaryColor: colors.surface,
      tertiaryTextColor: colors.text,
      textColor: colors.text,
      titleColor: colors.text,
    },
    themeCSS: createDiagramThemeCss(),
  })
}

function sanitizeSvg(svg: string) {
  const document = new DOMParser().parseFromString(svg, "image/svg+xml")
  const svgElement = document.documentElement
  const style = document.createElementNS("http://www.w3.org/2000/svg", "style")
  const colors = getDiagramColors()

  style.textContent = createDiagramThemeCss()
  svgElement.prepend(style)
  document.querySelectorAll("foreignObject").forEach((node) => {
    const label = node.textContent?.trim()

    if (!label) {
      return
    }

    const x = Number(node.getAttribute("x") ?? 0)
    const y = Number(node.getAttribute("y") ?? 0)
    const width = Number(node.getAttribute("width") ?? 0)
    const height = Number(node.getAttribute("height") ?? 0)
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text")

    text.setAttribute("x", String(x + width / 2))
    text.setAttribute("y", String(y + height / 2))
    text.setAttribute("dominant-baseline", "middle")
    text.setAttribute("fill", colors.text)
    text.setAttribute("font-family", "Inter, sans-serif")
    text.setAttribute("font-size", "14")
    text.setAttribute("text-anchor", "middle")
    text.textContent = label
    node.parentNode?.insertBefore(text, node)
  })

  const blockedNodes = document.querySelectorAll("script, foreignObject, iframe, object, embed")

  blockedNodes.forEach((node) => node.remove())
  document.querySelectorAll("*").forEach((node) => {
    Array.from(node.attributes).forEach((attribute) => {
      const name = attribute.name.toLowerCase()
      const value = attribute.value.trim().toLowerCase()

      if (name.startsWith("on") || value.startsWith("javascript:")) {
        node.removeAttribute(attribute.name)
      }
    })
  })

  return new XMLSerializer().serializeToString(document.documentElement)
}

function downloadBlob(blob: Blob, filename: string) {
  const url = URL.createObjectURL(blob)
  const anchor = document.createElement("a")

  anchor.href = url
  anchor.download = filename
  anchor.click()
  URL.revokeObjectURL(url)
}

function openSvgInNewTab(svg: string) {
  const blob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" })
  const url = URL.createObjectURL(blob)
  const openedWindow = window.open(url, "_blank")

  if (!openedWindow) {
    URL.revokeObjectURL(url)
    downloadBlob(blob, "diagram.svg")
    return
  }

  openedWindow.opener = null
  window.setTimeout(() => URL.revokeObjectURL(url), 60_000)
}

async function downloadSvgAsPng(svg: string, filename: string) {
  const image = new Image()
  const svgBlob = new Blob([svg], { type: "image/svg+xml;charset=utf-8" })
  const url = URL.createObjectURL(svgBlob)

  try {
    await new Promise<void>((resolve, reject) => {
      image.onload = () => resolve()
      image.onerror = () => reject(new Error("Nao foi possivel carregar o diagrama."))
      image.src = url
    })

    const svgDocument = new DOMParser().parseFromString(svg, "image/svg+xml")
    const svgElement = svgDocument.documentElement
    const viewBox = svgElement.getAttribute("viewBox")?.split(/\s+/).map(Number)
    const width = Number(svgElement.getAttribute("width")) || viewBox?.[2] || image.width || 1200
    const height = Number(svgElement.getAttribute("height")) || viewBox?.[3] || image.height || 800
    const canvas = document.createElement("canvas")
    const context = canvas.getContext("2d")

    canvas.width = Math.ceil(width)
    canvas.height = Math.ceil(height)
    context?.drawImage(image, 0, 0, canvas.width, canvas.height)

    const pngBlob = await new Promise<Blob | null>((resolve) => canvas.toBlob(resolve, "image/png"))

    if (pngBlob) {
      downloadBlob(pngBlob, filename)
    }
  } finally {
    URL.revokeObjectURL(url)
  }
}

function DiagramCanvas({ isExpanded = false, svg, zoom }: { isExpanded?: boolean; svg: string; zoom: number }) {
  const scrollRef = useRef<HTMLDivElement>(null)
  const dragRef = useRef<{
    left: number
    top: number
    x: number
    y: number
  } | null>(null)

  function handlePointerDown(event: PointerEvent<HTMLDivElement>) {
    const element = scrollRef.current

    if (!element) {
      return
    }

    dragRef.current = {
      left: element.scrollLeft,
      top: element.scrollTop,
      x: event.clientX,
      y: event.clientY,
    }
    element.setPointerCapture(event.pointerId)
  }

  function handlePointerMove(event: PointerEvent<HTMLDivElement>) {
    const element = scrollRef.current
    const drag = dragRef.current

    if (!element || !drag) {
      return
    }

    event.preventDefault()
    element.scrollLeft = drag.left - (event.clientX - drag.x)
    element.scrollTop = drag.top - (event.clientY - drag.y)
  }

  function handlePointerEnd(event: PointerEvent<HTMLDivElement>) {
    scrollRef.current?.releasePointerCapture(event.pointerId)
    dragRef.current = null
  }

  return (
    <div
      ref={scrollRef}
      onPointerDown={handlePointerDown}
      onPointerMove={handlePointerMove}
      onPointerUp={handlePointerEnd}
      onPointerCancel={handlePointerEnd}
      className={cn(
        "w-full min-w-0 cursor-grab select-none overflow-auto rounded-md bg-background p-4 active:cursor-grabbing",
        isExpanded ? "h-[calc(100svh-11rem)] w-full" : "max-h-[420px] min-h-72",
      )}
    >
      <div
        className="grid min-h-full min-w-full origin-center place-items-center transition-transform [&_svg]:h-auto [&_svg]:max-w-none"
        style={{ transform: `scale(${zoom})` }}
        dangerouslySetInnerHTML={{ __html: svg }}
      />
    </div>
  )
}

export function DiagramBlock({ code, language }: CodeChild) {
  const renderId = useId().replace(/[^a-zA-Z0-9_-]/g, "")
  const [svg, setSvg] = useState("")
  const [error, setError] = useState<string | null>(null)
  const [zoom, setZoom] = useState(defaultDiagramZoom)
  const [copied, setCopied] = useState(false)
  const isPlantUml = language === "plantuml" || language === "puml"
  const label = isPlantUml ? "PlantUML" : "Mermaid"
  const zoomControls = (
    <>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom((value) => Math.max(0.3, value - 0.2))}>
        <MinusIcon />
        <span className="sr-only">Reduzir zoom</span>
      </Button>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom(defaultDiagramZoom)}>
        <RotateCcwIcon />
        <span className="sr-only">Resetar zoom</span>
      </Button>
      <Button type="button" size="icon-xs" variant="ghost" onClick={() => setZoom((value) => Math.min(4, value + 0.2))}>
        <PlusIcon />
        <span className="sr-only">Aumentar zoom</span>
      </Button>
    </>
  )

  useEffect(() => {
    let isMounted = true

    async function renderDiagram() {
      setError(null)
      setSvg("")

      try {
        const rawSvg = isPlantUml
          ? renderPlantUmlToSvg(normalizePlantUmlSource(code))
          : await renderMermaidDiagram(`diagram-${renderId}`, code)

        if (isMounted) {
          setSvg(sanitizeSvg(rawSvg))
        }
      } catch (renderError) {
        if (isMounted) {
          setError(renderError instanceof Error ? renderError.message : "Diagrama invalido.")
        }
      }
    }

    void renderDiagram()

    return () => {
      isMounted = false
    }
  }, [code, isPlantUml, renderId])

  async function handleCopy() {
    await copyText(code)
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-muted/40">
      <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 border-b bg-background px-3 py-2">
        <span className="text-xs font-medium text-muted-foreground">{label}</span>
        <div className="ml-auto flex flex-wrap items-center gap-1">
          {zoomControls}
          <Button type="button" size="sm" variant="ghost" onClick={handleCopy}>
            {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
            {copied ? "Copiado" : "Copiar"}
          </Button>
          <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => void downloadSvgAsPng(svg, `${label.toLowerCase()}-diagram.png`)}>
            <DownloadIcon data-icon="inline-start" />
            PNG
          </Button>
          <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => openSvgInNewTab(svg)}>
            <ExternalLinkIcon data-icon="inline-start" />
            SVG
          </Button>
          <Dialog>
            <DialogTrigger asChild>
              <Button type="button" size="sm" variant="ghost" disabled={!svg}>
                <ExpandIcon data-icon="inline-start" />
                Expandir
              </Button>
            </DialogTrigger>
            <DialogContent className="h-[calc(100svh-1rem)] max-h-[calc(100svh-1rem)] w-[calc(100vw-1rem)] max-w-none overflow-hidden p-4 sm:max-w-none">
              <DialogHeader className="pr-10">
                <DialogTitle>{label}</DialogTitle>
              </DialogHeader>
              <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 rounded-md border bg-background px-3 py-2">
                <span className="text-xs text-muted-foreground">{Math.round(zoom * 100)}%</span>
                <div className="ml-auto flex items-center gap-1">
                  {zoomControls}
                  <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => void downloadSvgAsPng(svg, `${label.toLowerCase()}-diagram.png`)}>
                    <DownloadIcon data-icon="inline-start" />
                    PNG
                  </Button>
                  <Button type="button" size="sm" variant="ghost" disabled={!svg} onClick={() => openSvgInNewTab(svg)}>
                    <ExternalLinkIcon data-icon="inline-start" />
                    SVG
                  </Button>
                </div>
              </div>
              {svg ? <DiagramCanvas isExpanded svg={svg} zoom={zoom} /> : null}
            </DialogContent>
          </Dialog>
        </div>
      </div>
      {error ? (
        <pre className="overflow-x-auto p-4 text-sm text-destructive">{error}</pre>
      ) : svg ? (
        <DiagramCanvas svg={svg} zoom={zoom} />
      ) : (
        <div className="flex min-h-72 items-center justify-center gap-2 text-sm text-muted-foreground">
          <Loader2Icon className="size-4 animate-spin" aria-hidden="true" />
          Renderizando diagrama
        </div>
      )}
    </div>
  )
}

async function renderMermaidDiagram(id: string, code: string) {
  initializeMermaid()

  return (await mermaid.render(id, code)).svg
}
""",
    Path("src/pages/chat/markdown-table.tsx"): r"""import { type ComponentProps, useRef, useState } from "react"
import { CheckIcon, CopyIcon, ExpandIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { cn } from "@/lib/utils"

import { copyText } from "./markdown-utils"

export function MarkdownTable({ children, className, ...props }: ComponentProps<"table">) {
  const tableRef = useRef<HTMLTableElement>(null)
  const [copied, setCopied] = useState(false)
  const tableClassName = cn("w-full min-w-max table-auto border-collapse text-sm", className)

  async function handleCopy() {
    const table = tableRef.current

    if (!table) {
      return
    }

    const rows = Array.from(table.querySelectorAll("tr")).map((row) =>
      Array.from(row.querySelectorAll("th,td"))
        .map((cell) => cell.textContent?.trim() ?? "")
        .join("\t"),
    )

    await copyText(rows.join("\n"))
    setCopied(true)
    window.setTimeout(() => setCopied(false), 1500)
  }

  const table = (
    <table ref={tableRef} className={tableClassName} {...props}>
      {children}
    </table>
  )

  return (
    <div className="my-3 w-full min-w-0 overflow-hidden rounded-md border bg-background">
      <div data-clipboard-exclude className="flex flex-wrap items-center gap-2 border-b px-3 py-2">
        <span className="text-xs font-medium text-muted-foreground">Tabela</span>
        <Button type="button" size="sm" variant="ghost" className="ml-auto" onClick={handleCopy}>
          {copied ? <CheckIcon data-icon="inline-start" /> : <CopyIcon data-icon="inline-start" />}
          {copied ? "Copiada" : "Copiar"}
        </Button>
        <Dialog>
          <DialogTrigger asChild>
            <Button type="button" size="sm" variant="ghost">
              <ExpandIcon data-icon="inline-start" />
              Expandir
            </Button>
          </DialogTrigger>
          <DialogContent className="max-h-[calc(100svh-2rem)] max-w-[calc(100vw-2rem)] overflow-auto p-4 sm:max-w-[calc(100vw-2rem)] lg:max-w-6xl xl:max-w-7xl">
            <DialogHeader>
              <DialogTitle>Tabela</DialogTitle>
            </DialogHeader>
            <div className="h-[min(78svh,900px)] w-full overflow-auto rounded-md border">
              <table className={tableClassName} {...props}>
                {children}
              </table>
            </div>
          </DialogContent>
        </Dialog>
      </div>
      <div className="w-full overflow-x-auto">{table}</div>
    </div>
  )
}
""",
    Path("src/pages/chat/markdown-utils.ts"): r"""import {
  Children,
  isValidElement,
  type ReactNode,
} from "react"

export type CodeChild = {
  code: string
  language: string
}

export function readCodeChild(children: ReactNode): CodeChild | null {
  const child = Children.toArray(children)[0]

  if (!isValidElement(child)) {
    return null
  }

  const props = child.props as { children?: ReactNode; className?: string }
  const language = /language-(\w+)/.exec(props.className ?? "")?.[1] ?? "text"
  const code = String(props.children ?? "").replace(/\n$/, "")

  return { code, language: language.toLowerCase() }
}

export async function copyText(text: string) {
  if (!navigator.clipboard) {
    return
  }

  await navigator.clipboard.writeText(text)
}

export function formatFileSize(size: number) {
  if (size < 1024) {
    return `${size} B`
  }

  if (size < 1024 * 1024) {
    return `${Math.round(size / 1024)} KB`
  }

  return `${(size / 1024 / 1024).toFixed(1)} MB`
}
""",
    Path("src/pages/chat/plantuml-renderer.ts"): r"""function escapeXml(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

function parsePlantUmlLines(source: string) {
  return source
    .split("\n")
    .map((line) => line.trim())
    .filter(
      (line) =>
        line &&
        !line.startsWith("'") &&
        !/^@(start|end)\w+/i.test(line) &&
        !/^(skinparam|title|hide|show)\b/i.test(line),
    )
}

const diagramSurfaceColor = "var(--muted)"
const diagramBorderColor = "var(--border)"
const diagramTextColor = "var(--foreground)"

function renderSequenceDiagram(lines: string[]) {
  const participants: string[] = []
  const messages = lines
    .map((line) => {
      const declaration = /^(actor|participant|boundary|control|entity|database)\s+("?[^"]+"?|\w+)/i.exec(line)

      if (declaration) {
        const name = declaration[2].replaceAll('"', "")

        if (!participants.includes(name)) {
          participants.push(name)
        }

        return null
      }

      const message = /^(.+?)\s*[-.]+[->]+\s*(.+?)(?:\s*:\s*(.*))?$/i.exec(line)

      if (!message) {
        return null
      }

      const from = message[1].replaceAll('"', "").trim()
      const to = message[2].replaceAll('"', "").trim()

      for (const name of [from, to]) {
        if (!participants.includes(name)) {
          participants.push(name)
        }
      }

      return { from, to, label: message[3]?.trim() ?? "" }
    })
    .filter((message): message is { from: string; to: string; label: string } => Boolean(message))

  const gap = 180
  const headerHeight = 72
  const rowHeight = 58
  const width = Math.max(360, participants.length * gap + 80)
  const height = Math.max(220, headerHeight + messages.length * rowHeight + 72)
  const xFor = (name: string) => participants.indexOf(name) * gap + 80
  const header = participants
    .map((name) => {
      const x = xFor(name)

      return `<g><rect x="${x - 56}" y="18" width="112" height="36" rx="12" fill="${diagramSurfaceColor}" stroke="${diagramBorderColor}"/><text x="${x}" y="41" text-anchor="middle" font-size="13" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(name)}</text><line x1="${x}" y1="54" x2="${x}" y2="${height - 24}" stroke="${diagramBorderColor}" stroke-dasharray="4 4"/></g>`
    })
    .join("")
  const arrows = messages
    .map((message, index) => {
      const y = headerHeight + index * rowHeight
      const fromX = xFor(message.from)
      const toX = xFor(message.to)
      const direction = toX >= fromX ? 1 : -1
      const labelX = (fromX + toX) / 2

      return `<g><line x1="${fromX}" y1="${y}" x2="${toX - direction * 10}" y2="${y}" stroke="${diagramTextColor}" stroke-width="1.5"/><path d="M ${toX - direction * 10} ${y - 5} L ${toX} ${y} L ${toX - direction * 10} ${y + 5}" fill="none" stroke="${diagramTextColor}" stroke-width="1.5"/><text x="${labelX}" y="${y - 10}" text-anchor="middle" font-size="12" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(message.label)}</text></g>`
    })
    .join("")

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">${header}${arrows}</svg>`
}

function renderClassDiagram(lines: string[]) {
  const classNames: string[] = []
  const relations: Array<{ from: string; to: string; label: string }> = []

  lines.forEach((line) => {
    const classMatch = /^(abstract\s+)?(class|interface|enum)\s+("?[^"{]+"?|\w+)/i.exec(line)

    if (classMatch) {
      const name = classMatch[3].replaceAll('"', "").trim()

      if (!classNames.includes(name)) {
        classNames.push(name)
      }
    }

    const relation = /^("?[^"]+"?|\w+)\s+[-.]+(?:\|>|>|o|x|\*)?[-.]*\s+("?[^"]+"?|\w+)(?:\s*:\s*(.*))?$/i.exec(line)

    if (relation) {
      const from = relation[1].replaceAll('"', "").trim()
      const to = relation[2].replaceAll('"', "").trim()

      for (const name of [from, to]) {
        if (!classNames.includes(name)) {
          classNames.push(name)
        }
      }

      relations.push({ from, to, label: relation[3]?.trim() ?? "" })
    }
  })

  if (classNames.length === 0) {
    classNames.push("PlantUML")
  }

  const columns = Math.min(3, classNames.length)
  const cardWidth = 150
  const cardHeight = 72
  const gapX = 80
  const gapY = 72
  const width = columns * cardWidth + (columns - 1) * gapX + 80
  const rows = Math.ceil(classNames.length / columns)
  const height = rows * cardHeight + (rows - 1) * gapY + 96
  const positionFor = (name: string) => {
    const index = classNames.indexOf(name)
    const column = index % columns
    const row = Math.floor(index / columns)

    return {
      x: 40 + column * (cardWidth + gapX),
      y: 40 + row * (cardHeight + gapY),
    }
  }
  const boxes = classNames
    .map((name) => {
      const position = positionFor(name)

      return `<g><rect x="${position.x}" y="${position.y}" width="${cardWidth}" height="${cardHeight}" rx="14" fill="${diagramSurfaceColor}" stroke="${diagramBorderColor}"/><text x="${position.x + cardWidth / 2}" y="${position.y + 40}" text-anchor="middle" font-size="14" font-weight="600" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(name)}</text></g>`
    })
    .join("")
  const edges = relations
    .map((relation) => {
      const from = positionFor(relation.from)
      const to = positionFor(relation.to)
      const fromX = from.x + cardWidth / 2
      const fromY = from.y + cardHeight
      const toX = to.x + cardWidth / 2
      const toY = to.y
      const labelX = (fromX + toX) / 2
      const labelY = (fromY + toY) / 2 - 6

      return `<g><line x1="${fromX}" y1="${fromY}" x2="${toX}" y2="${toY}" stroke="${diagramTextColor}" stroke-width="1.5"/><text x="${labelX}" y="${labelY}" text-anchor="middle" font-size="12" font-family="Inter, sans-serif" fill="${diagramTextColor}">${escapeXml(relation.label)}</text></g>`
    })
    .join("")

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}">${edges}${boxes}</svg>`
}

export function normalizePlantUmlSource(source: string) {
  return /@start\w+/i.test(source) ? source : `@startuml\n${source}\n@enduml`
}

export function renderPlantUmlToSvg(source: string) {
  const lines = parsePlantUmlLines(source)
  const hasSequenceMessages = lines.some((line) => /^.+?\s*[-.]+[->]+\s*.+?(?:\s*:\s*.*)?$/i.test(line))

  return hasSequenceMessages ? renderSequenceDiagram(lines) : renderClassDiagram(lines)
}
""",
    Path("src/pages/chat/rich-message.tsx"): r"""import ReactMarkdown, { type Components } from "react-markdown"
import rehypeSanitize from "rehype-sanitize"
import remarkGfm from "remark-gfm"

import { cn } from "@/lib/utils"
import { CopyableCodeBlock } from "./copyable-code-block"
import { DiagramBlock } from "./diagram-block"
import { MarkdownTable } from "./markdown-table"
import { readCodeChild } from "./markdown-utils"

const markdownComponents: Components = {
  a({ children, href }) {
    return (
      <a
        href={href}
        target="_blank"
        rel="noreferrer"
        className="font-medium text-primary underline-offset-4 hover:underline"
      >
        {children}
      </a>
    )
  },
  code({ children, className }) {
    return (
      <code className={cn("rounded bg-muted px-1.5 py-0.5 text-sm", className)}>
        {children}
      </code>
    )
  },
  pre({ children }) {
    const codeChild = readCodeChild(children)

    if (!codeChild) {
      return (
        <pre className="w-full max-w-full overflow-x-auto rounded-md bg-muted p-4 [&_code]:block [&_code]:min-w-max [&_code]:whitespace-pre">
          {children}
        </pre>
      )
    }

    if (codeChild.language === "mermaid" || codeChild.language === "plantuml" || codeChild.language === "puml") {
      return <DiagramBlock {...codeChild} />
    }

    return <CopyableCodeBlock {...codeChild} />
  },
  table({ children, ...props }) {
    return <MarkdownTable {...props}>{children}</MarkdownTable>
  },
  td({ children, ...props }) {
    return (
      <td className="border p-2 align-top" {...props}>
        {children}
      </td>
    )
  },
  th({ children, ...props }) {
    return (
      <th className="border bg-muted p-2 text-left align-top font-semibold" {...props}>
        {children}
      </th>
    )
  },
}

export function RichMarkdownMessage({ content }: { content: string }) {
  return (
    <div className="min-w-0 w-full max-w-full">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeSanitize]}
        components={markdownComponents}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}
""",
    Path("src/pages/workflow/WorkflowPage.tsx"): """import { CheckCircle2Icon, GitPullRequestIcon, ShieldCheckIcon } from "lucide-react"

import { DataState } from "@/components/layout/data-state"
import { PageHeader } from "@/components/layout/page-header"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Separator } from "@/components/ui/separator"

const workflowSteps = [
  "Brief e fluxo",
  "Arquitetura",
  "Layout shadcn",
  "Implementacao React",
  "Revisoes e testes",
] as const

export function WorkflowPage() {
  return (
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 md:px-6 lg:py-8">
      <PageHeader
        eyebrow="Workflow"
        title="Gates de entrega frontend"
        description="Resumo visual do caminho esperado para transformar um pedido em uma entrega validada no starter."
        actions={<Badge variant="secondary">5 etapas</Badge>}
      />

      <section className="grid gap-6 lg:grid-cols-[minmax(0,1fr)_minmax(320px,0.85fr)]">
        <Card>
          <CardHeader>
            <CardTitle>Sequencia recomendada</CardTitle>
            <CardDescription>
              Cada etapa deixa uma decisao verificavel antes da proxima alteracao de codigo.
            </CardDescription>
          </CardHeader>
          <CardContent className="flex flex-col gap-4">
            <Progress value={60} aria-label="Progresso ilustrativo do workflow" />
            <div className="flex flex-col gap-3">
              {workflowSteps.map((step, index) => (
                <div key={step}>
                  <div className="flex items-center gap-3">
                    <span className="flex size-8 items-center justify-center rounded-full bg-muted text-sm font-semibold">
                      {index + 1}
                    </span>
                    <p className="text-sm font-medium">{step}</p>
                  </div>
                  {index < workflowSteps.length - 1 ? <Separator className="mt-3" /> : null}
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <div className="flex flex-col gap-6">
          <Alert>
            <ShieldCheckIcon aria-hidden="true" />
            <AlertTitle>Design system primeiro</AlertTitle>
            <AlertDescription>
              Toda UI nova deve consultar tokens, componentes shadcn/ui e estados responsivos antes
              da implementacao.
            </AlertDescription>
          </Alert>

          <Card>
            <CardHeader>
              <CardTitle>Fechamento</CardTitle>
              <CardDescription>O retorno final precisa citar gates executados e pendencias.</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-col gap-3">
              <div className="flex items-center gap-3">
                <CheckCircle2Icon aria-hidden="true" />
                <span className="text-sm">Typecheck ou build</span>
              </div>
              <div className="flex items-center gap-3">
                <GitPullRequestIcon aria-hidden="true" />
                <span className="text-sm">Riscos e revisoes registrados</span>
              </div>
            </CardContent>
          </Card>
        </div>
      </section>

      <DataState
        state="loading"
        title="Exemplo de estado de carregamento"
        description="Use DataState quando uma tela depender de dados remotos ou processamento local."
      />
    </div>
  )
}
""",
    Path("src/pages/not-found/NotFoundPage.tsx"): """import { HomeIcon, SearchXIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"

type NotFoundPageProps = {
  onNavigateHome: () => void
}

export function NotFoundPage({ onNavigateHome }: NotFoundPageProps) {
  return (
    <div className="mx-auto flex min-h-[calc(100svh-4rem)] w-full max-w-3xl items-center px-4 py-10 md:px-6">
      <Empty className="w-full border bg-card">
        <EmptyHeader>
          <EmptyMedia variant="icon">
            <SearchXIcon aria-hidden="true" />
          </EmptyMedia>
          <EmptyTitle>Pagina nao encontrada</EmptyTitle>
          <EmptyDescription>
            A rota acessada nao faz parte do bootstrap atual. Volte para o inicio e escolha uma
            entrada da sidebar.
          </EmptyDescription>
        </EmptyHeader>
        <EmptyContent>
          <Button onClick={onNavigateHome}>
            <HomeIcon data-icon="inline-start" />
            Voltar ao inicio
          </Button>
        </EmptyContent>
      </Empty>
    </div>
  )
}
""",
    Path("src/pages/design-system/DesignSystemPage.tsx"): """import { DesignSystemShowcase } from "@/features/design-system/components/design-system-showcase"

export function DesignSystemPage() {
  return (
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 md:px-6 lg:py-8">
      <DesignSystemShowcase />
    </div>
  )
}
""",
    Path("src/pages/index.ts"): """export { ChatPage } from "./chat/ChatPage"
export { DesignSystemPage } from "./design-system/DesignSystemPage"
export { HomePage } from "./home/HomePage"
export { NotFoundPage } from "./not-found/NotFoundPage"
export { WorkflowPage } from "./workflow/WorkflowPage"
""",
    Path("src/features/design-system/index.ts"): """export { DesignSystemBar } from "./components/design-system-bar"
export { DesignSystemCatalog } from "./components/design-system-catalog"
export { DesignSystemPanel } from "./components/design-system-panel"
export { DesignSystemShowcase } from "./components/design-system-showcase"
""",
    Path("src/features/design-system/design-system.tokens.ts"): """export const colorTokens = [
  { name: "primary", value: "#e60023", usage: "CTA principal e foco de acao" },
  { name: "canvas", value: "#ffffff", usage: "Fundo principal" },
  { name: "surface-card", value: "#f6f6f3", usage: "Superficie discreta" },
  { name: "hairline", value: "#dadad3", usage: "Bordas e divisores" },
  { name: "ink-soft", value: "#211922", usage: "Texto principal" },
  { name: "mute", value: "#62625b", usage: "Texto secundario" },
] as const

export const architectureLayers = [
  {
    name: "pages",
    description: "Rotas e composicao de layout. Nao concentram regra de negocio.",
  },
  {
    name: "features",
    description: "UI e regras de dominio, com components, hooks, services, schemas e types.",
  },
  {
    name: "services",
    description: "Clientes de API e integracoes sem dependencia de React.",
  },
  {
    name: "workflow",
    description: "Fluxo de validacao, gates e padroes de entrega do frontend.",
  },
] as const
""",
    Path("src/features/design-system/shadcn-components.ts"): """export const shadcnComponentGroups = [
  {
    name: "Base",
    components: [
      "accordion",
      "alert",
      "alert-dialog",
      "aspect-ratio",
      "avatar",
      "badge",
      "button",
      "button-group",
      "card",
      "collapsible",
      "separator",
    ],
  },
  {
    name: "Forms",
    components: [
      "calendar",
      "checkbox",
      "combobox",
      "field",
      "form",
      "input",
      "input-group",
      "input-otp",
      "label",
      "native-select",
      "radio-group",
      "select",
      "slider",
      "switch",
      "textarea",
      "toggle",
      "toggle-group",
    ],
  },
  {
    name: "Navigation",
    components: [
      "breadcrumb",
      "command",
      "menubar",
      "navigation-menu",
      "pagination",
      "sidebar",
      "tabs",
    ],
  },
  {
    name: "Overlays",
    components: [
      "context-menu",
      "dialog",
      "drawer",
      "dropdown-menu",
      "hover-card",
      "popover",
      "sheet",
      "tooltip",
    ],
  },
  {
    name: "Data",
    components: [
      "carousel",
      "chart",
      "item",
      "resizable",
      "scroll-area",
      "table",
    ],
  },
  {
    name: "Feedback",
    components: [
      "empty",
      "kbd",
      "progress",
      "skeleton",
      "sonner",
      "spinner",
    ],
  },
  {
    name: "Utilities",
    components: ["direction"],
  },
] as const

export const starterComponentNames = [
  "accordion",
  "alert",
  "alert-dialog",
  "aspect-ratio",
  "avatar",
  "badge",
  "breadcrumb",
  "button",
  "button-group",
  "calendar",
  "card",
  "carousel",
  "chart",
  "checkbox",
  "collapsible",
  "combobox",
  "command",
  "context-menu",
  "dialog",
  "direction",
  "drawer",
  "dropdown-menu",
  "empty",
  "field",
  "form",
  "hover-card",
  "input",
  "input-group",
  "input-otp",
  "item",
  "kbd",
  "label",
  "menubar",
  "native-select",
  "navigation-menu",
  "pagination",
  "popover",
  "progress",
  "radio-group",
  "resizable",
  "scroll-area",
  "select",
  "separator",
  "sheet",
  "sidebar",
  "slider",
  "skeleton",
  "sonner",
  "spinner",
  "switch",
  "table",
  "tabs",
  "textarea",
  "tooltip",
  "toggle",
  "toggle-group",
] as const
""",
    Path("src/features/design-system/components/design-system-bar.tsx"): """import { Badge } from "@/components/ui/badge"
import { Card, CardContent } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"

export function DesignSystemBar() {
  return (
    <Card className="overflow-hidden">
      <CardContent className="flex flex-col gap-4 p-4 md:flex-row md:items-center">
        <div className="min-w-0">
          <p className="text-sm font-semibold">Design System</p>
          <p className="text-sm text-muted-foreground">
            Tokens, estrutura feature-first e shadcn/ui prontos para a primeira tela.
          </p>
        </div>
        <Separator className="hidden h-8 md:block" orientation="vertical" />
        <div className="flex flex-wrap gap-2 md:ml-auto">
          <Badge>primary #e60023</Badge>
          <Badge variant="secondary">radius 16px</Badge>
          <Badge variant="outline">Inter</Badge>
        </div>
      </CardContent>
    </Card>
  )
}
""",
    Path("src/features/design-system/components/design-system-panel.tsx"): """import { ArrowRightIcon } from "lucide-react"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"
import { architectureLayers, colorTokens } from "@/features/design-system/design-system.tokens"

export function DesignSystemPanel() {
  return (
    <section className="flex flex-col gap-6">
      <Card>
        <CardHeader className="gap-4">
          <div className="flex flex-wrap items-center gap-2">
            <Badge>Boas-vindas</Badge>
            <Badge variant="secondary">React + Vite + TypeScript</Badge>
            <Badge variant="outline">shadcn/ui</Badge>
          </div>
          <div className="max-w-3xl space-y-3">
            <CardTitle className="text-3xl tracking-normal md:text-4xl">
              Bem-vindo ao template
            </CardTitle>
            <CardDescription className="text-base">
              Esta pagina inicial apresenta a base do projeto e mostra como o frontend deve crescer:
              com rotas organizadas, componentes consistentes, tokens visuais e um workflow de
              agentes para manter qualidade desde o primeiro ajuste.
            </CardDescription>
          </div>
        </CardHeader>
        <CardContent className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_minmax(280px,0.55fr)]">
          <div className="rounded-2xl bg-muted p-5">
            <p className="text-sm font-semibold">O que e esta pagina</p>
            <p className="mt-2 text-sm text-muted-foreground">
              A Home funciona como ponto de partida do template. Ela resume a estrutura principal,
              orienta a navegacao inicial e deixa claro quais convencoes guiam novas pages,
              features, services e componentes.
            </p>
          </div>
          <div className="rounded-2xl border bg-background p-5">
            <p className="text-sm font-semibold">O que e o design system</p>
            <p className="mt-2 text-sm text-muted-foreground">
              E o conjunto de tokens, componentes, estados, acessibilidade e regras de layout que
              mantem a interface coerente em telas diferentes.
            </p>
            <Button asChild className="mt-4" size="sm">
              <a href="/design-system">
                Ver catalogo
                <ArrowRightIcon />
              </a>
            </Button>
          </div>
        </CardContent>
      </Card>

      <div className="grid gap-6 lg:grid-cols-[minmax(0,1.15fr)_minmax(320px,0.85fr)]">
        <Card>
          <CardHeader>
            <CardTitle>Como este template se organiza</CardTitle>
            <CardDescription>
              Camadas praticas para separar composicao, dominio, integracoes e gates de entrega.
            </CardDescription>
          </CardHeader>
          <CardContent className="grid gap-3 sm:grid-cols-2">
            {architectureLayers.map((layer) => (
              <div key={layer.name} className="rounded-2xl bg-muted p-4">
                <p className="text-sm font-semibold">{layer.name}</p>
                <p className="mt-2 text-sm text-muted-foreground">{layer.description}</p>
              </div>
            ))}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Tokens principais</CardTitle>
            <CardDescription>Valores derivados dos tokens base do starter.</CardDescription>
          </CardHeader>
          <CardContent className="flex flex-col gap-3">
            {colorTokens.map((token, index) => (
              <div key={token.name}>
                <div className="flex items-center gap-3">
                  <span
                    className="size-10 rounded-full border"
                    style={{ backgroundColor: token.value }}
                    aria-hidden="true"
                  />
                  <div className="min-w-0">
                    <p className="truncate text-sm font-semibold">{token.name}</p>
                    <p className="truncate text-xs text-muted-foreground">
                      {token.value} - {token.usage}
                    </p>
                  </div>
                </div>
                {index < colorTokens.length - 1 ? <Separator className="mt-3" /> : null}
              </div>
            ))}
          </CardContent>
        </Card>
      </div>
    </section>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase.tsx"): r"""import { useMemo, useState } from "react"
import { useForm } from "react-hook-form"

import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { BaseShowcase } from "./design-system-showcase/base-showcase"
import { DataShowcase } from "./design-system-showcase/data-showcase"
import { FeedbackShowcase } from "./design-system-showcase/feedback-showcase"
import { FormsShowcase } from "./design-system-showcase/forms-showcase"
import { NavigationShowcase } from "./design-system-showcase/navigation-showcase"
import { OverlaysShowcase } from "./design-system-showcase/overlays-showcase"
import { operationalRows, type DemoForm } from "./design-system-showcase/showcase-data"

export function DesignSystemShowcase() {
  const [removedRowIds, setRemovedRowIds] = useState<string[]>([])
  const [tableQuery, setTableQuery] = useState("")
  const [statusFilter, setStatusFilter] = useState("all")
  const [categoryFilter, setCategoryFilter] = useState("all")
  const [uploadedFiles, setUploadedFiles] = useState<File[]>([])

  const form = useForm<DemoForm>({
    defaultValues: {
      cliente: "Cliente Demo",
    },
  })

  const tableRows = useMemo(
    () => operationalRows.filter((row) => !removedRowIds.includes(row.id)),
    [removedRowIds],
  )

  const filteredRows = useMemo(() => {
    const normalizedQuery = tableQuery.trim().toLowerCase()

    return tableRows.filter((row) => {
      const matchesQuery =
        normalizedQuery.length === 0 ||
        row.id.toLowerCase().includes(normalizedQuery) ||
        row.service.toLowerCase().includes(normalizedQuery) ||
        row.owner.toLowerCase().includes(normalizedQuery)
      const matchesStatus = statusFilter === "all" || row.status === statusFilter
      const matchesCategory = categoryFilter === "all" || row.category === categoryFilter

      return matchesQuery && matchesStatus && matchesCategory
    })
  }, [categoryFilter, statusFilter, tableQuery, tableRows])

  return (
    <section className="flex flex-col gap-6">
      <div className="flex flex-col gap-2">
        <h1 className="text-3xl font-semibold tracking-normal">Design System</h1>
        <p className="max-w-3xl text-sm text-muted-foreground">
          Galeria funcional dos componentes shadcn/ui materializados pelo bootstrap e estilizados
          pelos tokens do projeto.
        </p>
      </div>

      <Tabs defaultValue="base">
        <TabsList className="flex h-auto w-full flex-wrap justify-start">
          <TabsTrigger value="base">Base</TabsTrigger>
          <TabsTrigger value="forms">Forms</TabsTrigger>
          <TabsTrigger value="navigation">Navigation</TabsTrigger>
          <TabsTrigger value="overlays">Overlays</TabsTrigger>
          <TabsTrigger value="data">Data</TabsTrigger>
          <TabsTrigger value="feedback">Feedback</TabsTrigger>
        </TabsList>

        <BaseShowcase />
        <FormsShowcase form={form} uploadedFiles={uploadedFiles} setUploadedFiles={setUploadedFiles} />
        <NavigationShowcase />
        <OverlaysShowcase />
        <DataShowcase
          categoryFilter={categoryFilter}
          filteredRows={filteredRows}
          setCategoryFilter={setCategoryFilter}
          setRemovedRowIds={setRemovedRowIds}
          setStatusFilter={setStatusFilter}
          setTableQuery={setTableQuery}
          statusFilter={statusFilter}
          tableQuery={tableQuery}
          tableRows={tableRows}
        />
        <FeedbackShowcase />
      </Tabs>
    </section>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/base-showcase.tsx"): r"""import { SettingsIcon, SparklesIcon } from "lucide-react"

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { AspectRatio } from "@/components/ui/aspect-ratio"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { ButtonGroup } from "@/components/ui/button-group"
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible"
import { Kbd, KbdGroup } from "@/components/ui/kbd"
import { Separator } from "@/components/ui/separator"
import { TabsContent } from "@/components/ui/tabs"

import { ShowcaseCard } from "./showcase-card"

export function BaseShowcase() {
  return (
    <TabsContent value="base" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Acoes" description="button, button-group, badge, avatar, kbd e separator.">
        <div className="flex flex-wrap gap-3">
          <Button>
            <SparklesIcon data-icon="inline-start" />
            Acao primaria
          </Button>
          <Button variant="secondary">Secundaria</Button>
          <Button variant="outline">Outline</Button>
          <Button variant="ghost">Ghost</Button>
          <Button size="icon" variant="outline" aria-label="Configuracoes">
            <SettingsIcon />
          </Button>
        </div>
        <ButtonGroup>
          <Button variant="outline">Salvar</Button>
          <Button variant="outline">Publicar</Button>
          <Button variant="outline">Exportar</Button>
        </ButtonGroup>
        <Separator />
        <div className="flex flex-wrap items-center gap-3">
          <Badge>default</Badge>
          <Badge variant="secondary">secondary</Badge>
          <Badge variant="outline">outline</Badge>
          <Avatar>
            <AvatarFallback>BR</AvatarFallback>
          </Avatar>
          <KbdGroup>
            <Kbd>Ctrl</Kbd>
            <Kbd>K</Kbd>
          </KbdGroup>
        </div>
      </ShowcaseCard>

      <ShowcaseCard title="Conteudo base" description="accordion, alert, alert-dialog, aspect-ratio, card e collapsible.">
        <Alert>
          <SparklesIcon />
          <AlertTitle>Alert oficial</AlertTitle>
          <AlertDescription>Feedback inline usando tokens semanticos.</AlertDescription>
        </Alert>
        <AspectRatio ratio={16 / 9} className="overflow-hidden rounded-lg border bg-muted">
          <div className="flex size-full items-center justify-center text-sm text-muted-foreground">
            AspectRatio 16:9
          </div>
        </AspectRatio>
        <Accordion type="single" collapsible>
          <AccordionItem value="tokens">
            <AccordionTrigger>Como o tema chega no componente?</AccordionTrigger>
            <AccordionContent>
              Via variaveis CSS em src/index.css e classes semanticas como bg-primary.
            </AccordionContent>
          </AccordionItem>
        </Accordion>
        <Collapsible>
          <CollapsibleTrigger asChild>
            <Button variant="outline">Abrir collapsible</Button>
          </CollapsibleTrigger>
          <CollapsibleContent className="rounded-lg border bg-muted p-3 text-sm">
            Conteudo progressivo sem montar markup customizado.
          </CollapsibleContent>
        </Collapsible>
        <AlertDialog>
          <AlertDialogTrigger asChild>
            <Button variant="outline">Abrir alert-dialog</Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Confirmar acao</AlertDialogTitle>
              <AlertDialogDescription>
                Exemplo de confirmacao acessivel gerada pelo shadcn.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancelar</AlertDialogCancel>
              <AlertDialogAction>Confirmar</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/data-showcase.tsx"): r"""import { type Dispatch, type SetStateAction } from "react"
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
import { CreditCardIcon, EyeIcon, SearchIcon, Trash2Icon } from "lucide-react"

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Checkbox } from "@/components/ui/checkbox"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { Empty, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle } from "@/components/ui/empty"
import { InputGroup, InputGroupAddon, InputGroupInput } from "@/components/ui/input-group"
import { Item, ItemContent, ItemDescription, ItemGroup, ItemMedia, ItemTitle } from "@/components/ui/item"
import { NativeSelect, NativeSelectOption } from "@/components/ui/native-select"
import { Progress } from "@/components/ui/progress"
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { TabsContent } from "@/components/ui/tabs"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"

import { chartConfig, chartData, type OperationalRow, services } from "./showcase-data"
import { ShowcaseCard } from "./showcase-card"

type DataShowcaseProps = {
  categoryFilter: string
  filteredRows: OperationalRow[]
  setCategoryFilter: Dispatch<SetStateAction<string>>
  setRemovedRowIds: Dispatch<SetStateAction<string[]>>
  setStatusFilter: Dispatch<SetStateAction<string>>
  setTableQuery: Dispatch<SetStateAction<string>>
  statusFilter: string
  tableQuery: string
  tableRows: OperationalRow[]
}

export function DataShowcase({
  categoryFilter,
  filteredRows,
  setCategoryFilter,
  setRemovedRowIds,
  setStatusFilter,
  setTableQuery,
  statusFilter,
  tableQuery,
  tableRows,
}: DataShowcaseProps) {
  return (
    <TabsContent value="data" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard
        title="Tabela operacional"
        description="table, input-group, select, native-select, checkbox, dropdown-menu, badge, busca, filtros e estado vazio."
        className="lg:col-span-2"
      >
        <div className="grid gap-3 lg:grid-cols-[minmax(260px,1fr)_180px_180px_auto]">
          <InputGroup>
            <InputGroupAddon>
              <SearchIcon />
            </InputGroupAddon>
            <InputGroupInput
              value={tableQuery}
              onChange={(event) => setTableQuery(event.target.value)}
              placeholder="Buscar por ID, servico ou squad"
              aria-label="Buscar tabela operacional"
            />
          </InputGroup>

          <Select value={statusFilter} onValueChange={setStatusFilter}>
            <SelectTrigger className="w-full" aria-label="Filtrar status">
              <SelectValue placeholder="Status" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="all">Todos status</SelectItem>
                <SelectItem value="ativo">Ativo</SelectItem>
                <SelectItem value="revisao">Revisao</SelectItem>
                <SelectItem value="pausado">Pausado</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <NativeSelect
            value={categoryFilter}
            onChange={(event) => setCategoryFilter(event.target.value)}
            className="w-full"
            aria-label="Filtrar categoria"
          >
            <NativeSelectOption value="all">Todas categorias</NativeSelectOption>
            <NativeSelectOption value="Contas">Contas</NativeSelectOption>
            <NativeSelectOption value="Pagamentos">Pagamentos</NativeSelectOption>
            <NativeSelectOption value="Credito">Credito</NativeSelectOption>
            <NativeSelectOption value="Wealth">Wealth</NativeSelectOption>
            <NativeSelectOption value="Protecao">Protecao</NativeSelectOption>
          </NativeSelect>

          <Button
            variant="outline"
            onClick={() => {
              setTableQuery("")
              setStatusFilter("all")
              setCategoryFilter("all")
            }}
          >
            Limpar
          </Button>
        </div>

        <div className="flex flex-wrap items-center justify-between gap-3">
          <p className="text-sm text-muted-foreground">
            {filteredRows.length} de {tableRows.length} resultados
          </p>
          <div className="flex flex-wrap gap-2">
            <Badge variant="secondary">busca</Badge>
            <Badge variant="secondary">filtros</Badge>
            <Badge variant="secondary">acoes por linha</Badge>
          </div>
        </div>

        <div className="overflow-hidden rounded-lg border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="w-10">
                  <Checkbox aria-label="Selecionar todos" />
                </TableHead>
                <TableHead>ID</TableHead>
                <TableHead>Servico</TableHead>
                <TableHead>Categoria</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Squad</TableHead>
                <TableHead className="text-right">Conversao</TableHead>
                <TableHead className="w-16 text-right">Acoes</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredRows.length > 0 ? (
                filteredRows.map((row) => (
                  <TableRow key={row.id}>
                    <TableCell>
                      <Checkbox aria-label={`Selecionar ${row.service}`} />
                    </TableCell>
                    <TableCell className="font-medium">{row.id}</TableCell>
                    <TableCell>{row.service}</TableCell>
                    <TableCell>{row.category}</TableCell>
                    <TableCell>
                      <Badge variant={row.status === "ativo" ? "default" : "secondary"}>
                        {row.status}
                      </Badge>
                    </TableCell>
                    <TableCell>{row.owner}</TableCell>
                    <TableCell className="text-right">{row.conversion}%</TableCell>
                    <TableCell className="text-right">
                      <div className="flex justify-end gap-1">
                        <Dialog>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <DialogTrigger asChild>
                                <Button
                                  size="icon-sm"
                                  variant="ghost"
                                  aria-label={`Visualizar ${row.service}`}
                                >
                                  <EyeIcon />
                                </Button>
                              </DialogTrigger>
                            </TooltipTrigger>
                            <TooltipContent>Visualizar</TooltipContent>
                          </Tooltip>
                          <DialogContent>
                            <DialogHeader>
                              <DialogTitle>{row.service}</DialogTitle>
                              <DialogDescription>
                                {row.id} - {row.owner} - conversao de {row.conversion}%.
                              </DialogDescription>
                            </DialogHeader>
                          </DialogContent>
                        </Dialog>

                        <AlertDialog>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <AlertDialogTrigger asChild>
                                <Button
                                  size="icon-sm"
                                  variant="ghost"
                                  aria-label={`Deletar ${row.service}`}
                                >
                                  <Trash2Icon />
                                </Button>
                              </AlertDialogTrigger>
                            </TooltipTrigger>
                            <TooltipContent>Deletar</TooltipContent>
                          </Tooltip>
                          <AlertDialogContent>
                            <AlertDialogHeader>
                              <AlertDialogTitle>Deletar {row.service}?</AlertDialogTitle>
                              <AlertDialogDescription>
                                Esta acao remove {row.id} da tabela desta sessao de exemplo.
                              </AlertDialogDescription>
                            </AlertDialogHeader>
                            <AlertDialogFooter>
                              <AlertDialogCancel>Cancelar</AlertDialogCancel>
                              <AlertDialogAction
                                variant="destructive"
                                onClick={() =>
                                  setRemovedRowIds((currentIds) => [...currentIds, row.id])
                                }
                              >
                                Deletar
                              </AlertDialogAction>
                            </AlertDialogFooter>
                          </AlertDialogContent>
                        </AlertDialog>
                      </div>
                    </TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={8}>
                    <Empty className="min-h-40 border-0">
                      <EmptyHeader>
                        <EmptyMedia variant="icon">
                          <SearchIcon />
                        </EmptyMedia>
                        <EmptyTitle>Nenhum resultado</EmptyTitle>
                        <EmptyDescription>
                          Ajuste a busca ou remova filtros para voltar a ver os dados.
                        </EmptyDescription>
                      </EmptyHeader>
                    </Empty>
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </ShowcaseCard>

      <ShowcaseCard title="Graficos e tabela" description="chart, histogram/bar chart, table e progress.">
        <ChartContainer config={chartConfig} className="h-64 w-full">
          <BarChart data={chartData}>
            <CartesianGrid vertical={false} />
            <XAxis dataKey="name" tickLine={false} axisLine={false} />
            <ChartTooltip content={<ChartTooltipContent hideLabel />} />
            <Bar dataKey="volume" fill="var(--color-volume)" radius={6} />
          </BarChart>
        </ChartContainer>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Servico</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="text-right">Aderencia</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {services.map((service) => (
              <TableRow key={service.name}>
                <TableCell className="font-medium">{service.name}</TableCell>
                <TableCell>
                  <Badge variant={service.status === "ativo" ? "default" : "secondary"}>
                    {service.status}
                  </Badge>
                </TableCell>
                <TableCell className="text-right">{service.value}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Progress value={82} aria-label="Aderencia media dos servicos" />
      </ShowcaseCard>

      <ShowcaseCard title="Dados compostos" description="carousel, item, resizable e scroll-area.">
        <Carousel className="mx-auto w-full max-w-sm">
          <CarouselContent>
            {services.map((service) => (
              <CarouselItem key={service.name}>
                <Card>
                  <CardContent className="flex h-28 items-center justify-center p-6 text-sm font-medium">
                    {service.name}
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>
          <CarouselPrevious className="left-2" />
          <CarouselNext className="right-2" />
        </Carousel>
        <ItemGroup className="rounded-lg border">
          <Item>
            <ItemMedia variant="icon">
              <CreditCardIcon />
            </ItemMedia>
            <ItemContent>
              <ItemTitle>Item de dado</ItemTitle>
              <ItemDescription>Componente Item para listas densas e repetidas.</ItemDescription>
            </ItemContent>
          </Item>
        </ItemGroup>
        <ResizablePanelGroup orientation="horizontal" className="min-h-28 rounded-lg border">
          <ResizablePanel defaultSize={55} className="flex items-center justify-center text-sm">
            Painel A
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={45} className="flex items-center justify-center text-sm">
            Painel B
          </ResizablePanel>
        </ResizablePanelGroup>
        <ScrollArea className="h-28 rounded-lg border p-3">
          <div className="flex flex-col gap-2">
            {services.concat(services).map((service, index) => (
              <div key={`${service.name}-${index}`} className="rounded-md bg-muted px-3 py-2 text-sm">
                {service.name}
              </div>
            ))}
          </div>
        </ScrollArea>
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/feedback-showcase.tsx"): r"""import { BellIcon, CreditCardIcon } from "lucide-react"

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Button } from "@/components/ui/button"
import { DirectionProvider } from "@/components/ui/direction"
import { Empty, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle } from "@/components/ui/empty"
import { Skeleton } from "@/components/ui/skeleton"
import { Toaster } from "@/components/ui/sonner"
import { Spinner } from "@/components/ui/spinner"
import { TabsContent } from "@/components/ui/tabs"

import { ShowcaseCard } from "./showcase-card"

export function FeedbackShowcase() {
  return (
    <TabsContent value="feedback" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Estados" description="empty, skeleton, spinner, sonner e progress.">
        <Empty className="min-h-48 border">
          <EmptyHeader>
            <EmptyMedia variant="icon">
              <CreditCardIcon />
            </EmptyMedia>
            <EmptyTitle>Nenhum item selecionado</EmptyTitle>
            <EmptyDescription>Estado vazio renderizado com o componente oficial.</EmptyDescription>
          </EmptyHeader>
        </Empty>
        <div className="grid gap-3 sm:grid-cols-2">
          <Skeleton className="h-16" />
          <Skeleton className="h-16" />
        </div>
        <Button variant="secondary" disabled>
          <Spinner />
          Processando
        </Button>
        <Toaster />
      </ShowcaseCard>

      <ShowcaseCard title="Utilities" description="direction provider e componentes utilitarios.">
        <DirectionProvider dir="rtl">
          <div className="rounded-lg border bg-muted p-4 text-sm">Conteudo RTL via DirectionProvider</div>
        </DirectionProvider>
        <Alert>
          <BellIcon />
          <AlertTitle>Controle visual</AlertTitle>
          <AlertDescription>
            Todos os grupos acima renderizam componentes reais; o catalogo abaixo funciona como
            checklist de cobertura.
          </AlertDescription>
        </Alert>
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/forms-showcase.tsx"): r"""import { type Dispatch, type SetStateAction } from "react"
import { BoldIcon, ItalicIcon, SparklesIcon } from "lucide-react"
import { type UseFormReturn } from "react-hook-form"

import { Calendar } from "@/components/ui/calendar"
import { Checkbox } from "@/components/ui/checkbox"
import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxGroup,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
import { Field, FieldDescription, FieldGroup, FieldLabel } from "@/components/ui/field"
import { FileUploadDropzone } from "@/components/ui/file-upload-dropzone"
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { InputGroup, InputGroupAddon, InputGroupInput } from "@/components/ui/input-group"
import { InputOTP, InputOTPGroup, InputOTPSlot } from "@/components/ui/input-otp"
import { NativeSelect, NativeSelectOption } from "@/components/ui/native-select"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Slider } from "@/components/ui/slider"
import { Switch } from "@/components/ui/switch"
import { TabsContent } from "@/components/ui/tabs"
import { Textarea } from "@/components/ui/textarea"
import { Toggle } from "@/components/ui/toggle"
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"

import { type DemoForm } from "./showcase-data"
import { ShowcaseCard } from "./showcase-card"

type FormsShowcaseProps = {
  form: UseFormReturn<DemoForm>
  setUploadedFiles: Dispatch<SetStateAction<File[]>>
  uploadedFiles: File[]
}

export function FormsShowcase({ form, setUploadedFiles, uploadedFiles }: FormsShowcaseProps) {
  return (
    <TabsContent value="forms" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Campos" description="field, input, input-group, textarea, select, native-select e combobox.">
        <FieldGroup>
          <Field>
            <FieldLabel htmlFor="search">Busca</FieldLabel>
            <Input id="search" placeholder="Buscar componente" />
            <FieldDescription>Input shadcn estilizado pelos tokens globais.</FieldDescription>
          </Field>
          <Field>
            <FieldLabel htmlFor="amount">Valor</FieldLabel>
            <InputGroup>
              <InputGroupAddon>R$</InputGroupAddon>
              <InputGroupInput id="amount" placeholder="0,00" />
            </InputGroup>
          </Field>
          <Field>
            <FieldLabel>Categoria</FieldLabel>
            <Select defaultValue="contas">
              <SelectTrigger className="w-full" aria-label="Categoria">
                <SelectValue placeholder="Selecione" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectItem value="contas">Contas</SelectItem>
                  <SelectItem value="cartoes">Cartoes</SelectItem>
                  <SelectItem value="seguros">Seguros</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
          </Field>
          <Field>
            <FieldLabel htmlFor="native-payment-method">Native select</FieldLabel>
            <NativeSelect id="native-payment-method" defaultValue="pix" className="w-full">
              <NativeSelectOption value="pix">Pix</NativeSelectOption>
              <NativeSelectOption value="ted">TED</NativeSelectOption>
            </NativeSelect>
          </Field>
          <Field>
            <FieldLabel>Combobox</FieldLabel>
            <Combobox>
              <ComboboxInput aria-label="Servico" placeholder="Selecionar servico" />
              <ComboboxContent>
                <ComboboxList>
                  <ComboboxEmpty>Nenhum servico</ComboboxEmpty>
                  <ComboboxGroup>
                    <ComboboxItem value="Conta digital">Conta digital</ComboboxItem>
                    <ComboboxItem value="Cartoes">Cartoes</ComboboxItem>
                  </ComboboxGroup>
                </ComboboxList>
              </ComboboxContent>
            </Combobox>
          </Field>
          <Field>
            <FieldLabel htmlFor="notes">Observacoes</FieldLabel>
            <Textarea id="notes" placeholder="Descreva o caso de uso" />
          </Field>
        </FieldGroup>
      </ShowcaseCard>

      <ShowcaseCard title="Controles" description="calendar, checkbox, radio-group, switch, slider, toggle, toggle-group, input-otp e form.">
        <div className="grid gap-4 md:grid-cols-[260px_minmax(0,1fr)]">
          <Calendar mode="single" selected={new Date(2026, 4, 13)} />
          <FieldGroup>
            <Field orientation="horizontal">
              <Checkbox id="notifications" defaultChecked />
              <FieldLabel htmlFor="notifications">Receber novidades</FieldLabel>
            </Field>
            <Field orientation="horizontal">
              <Switch id="compact-mode" defaultChecked />
              <FieldLabel htmlFor="compact-mode">Modo compacto</FieldLabel>
            </Field>
            <RadioGroup defaultValue="app" className="flex gap-3">
              <Field orientation="horizontal">
                <RadioGroupItem id="channel-app" value="app" />
                <FieldLabel htmlFor="channel-app">App</FieldLabel>
              </Field>
              <Field orientation="horizontal">
                <RadioGroupItem id="channel-web" value="web" />
                <FieldLabel htmlFor="channel-web">Web</FieldLabel>
              </Field>
            </RadioGroup>
            <Slider aria-label="Valor de exemplo" defaultValue={[60]} max={100} step={10} />
            <ToggleGroup type="multiple" variant="outline">
              <ToggleGroupItem value="bold" aria-label="Negrito">
                <BoldIcon />
              </ToggleGroupItem>
              <ToggleGroupItem value="italic" aria-label="Italico">
                <ItalicIcon />
              </ToggleGroupItem>
            </ToggleGroup>
            <Toggle variant="outline" aria-label="Favorito">
              <SparklesIcon />
            </Toggle>
            <InputOTP aria-label="Codigo de exemplo" maxLength={4} value="2026" readOnly>
              <InputOTPGroup>
                <InputOTPSlot index={0} />
                <InputOTPSlot index={1} />
                <InputOTPSlot index={2} />
                <InputOTPSlot index={3} />
              </InputOTPGroup>
            </InputOTP>
          </FieldGroup>
        </div>
        <Form {...form}>
          <FormField
            control={form.control}
            name="cliente"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Form shadcn</FormLabel>
                <FormControl>
                  <Input {...field} />
                </FormControl>
                <FormDescription>Contrato react-hook-form integrado.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
        </Form>
      </ShowcaseCard>

      <ShowcaseCard
        title="Upload de arquivos"
        description="Componente pronto com input real, clique para selecionar e drag and drop."
        className="lg:col-span-2"
      >
        <FileUploadDropzone
          accept=".csv,.pdf,.png,.jpg,.jpeg"
          files={uploadedFiles}
          label="Enviar documentos"
          description="Solte arquivos aqui ou selecione CSV, PDF e imagens para anexar ao fluxo."
          onFilesChange={setUploadedFiles}
        />
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/navigation-showcase.tsx"): r"""import { FileTextIcon, SearchIcon } from "lucide-react"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList, CommandShortcut } from "@/components/ui/command"
import { Menubar, MenubarContent, MenubarItem, MenubarMenu, MenubarTrigger } from "@/components/ui/menubar"
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
import { Pagination, PaginationContent, PaginationItem, PaginationLink } from "@/components/ui/pagination"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

import { ShowcaseCard } from "./showcase-card"

export function NavigationShowcase() {
  return (
    <TabsContent value="navigation" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Navegacao" description="breadcrumb, menubar, navigation-menu, pagination e tabs.">
        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="#">Inicio</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Design System</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
        <Menubar>
          <MenubarMenu>
            <MenubarTrigger>Arquivo</MenubarTrigger>
            <MenubarContent>
              <MenubarItem>Novo</MenubarItem>
              <MenubarItem>Exportar</MenubarItem>
            </MenubarContent>
          </MenubarMenu>
        </Menubar>
        <NavigationMenu viewport={false}>
          <NavigationMenuList>
            <NavigationMenuItem>
              <NavigationMenuTrigger>Produtos</NavigationMenuTrigger>
            </NavigationMenuItem>
            <NavigationMenuItem>
              <NavigationMenuLink href="#">Atendimento</NavigationMenuLink>
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
        <Pagination>
          <PaginationContent>
            <PaginationItem>
              <PaginationLink href="#" isActive>
                1
              </PaginationLink>
            </PaginationItem>
            <PaginationItem>
              <PaginationLink href="#">2</PaginationLink>
            </PaginationItem>
          </PaginationContent>
        </Pagination>
      </ShowcaseCard>

      <ShowcaseCard title="Command e sidebar" description="command e sidebar aparecem renderizados na navegacao principal do app.">
        <Command className="rounded-lg border">
          <CommandInput placeholder="Buscar comando" />
          <CommandList>
            <CommandEmpty>Nenhum resultado.</CommandEmpty>
            <CommandGroup heading="Acoes">
              <CommandItem>
                <SearchIcon />
                Buscar cliente
                <CommandShortcut>⌘K</CommandShortcut>
              </CommandItem>
              <CommandItem>
                <FileTextIcon />
                Gerar relatorio
              </CommandItem>
            </CommandGroup>
          </CommandList>
        </Command>
        <Tabs defaultValue="sidebar">
          <TabsList>
            <TabsTrigger value="sidebar">Sidebar</TabsTrigger>
            <TabsTrigger value="tabs">Tabs</TabsTrigger>
          </TabsList>
          <TabsContent value="sidebar" className="rounded-lg border p-4 text-sm text-muted-foreground">
            A sidebar oficial shadcn esta no app shell e controla esta pagina.
          </TabsContent>
          <TabsContent value="tabs" className="rounded-lg border p-4 text-sm text-muted-foreground">
            Este painel demonstra Tabs dentro da propria galeria.
          </TabsContent>
        </Tabs>
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/overlays-showcase.tsx"): r"""import { SearchIcon } from "lucide-react"

import { Button } from "@/components/ui/button"
import { ContextMenu, ContextMenuContent, ContextMenuItem, ContextMenuTrigger } from "@/components/ui/context-menu"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { Drawer, DrawerContent, DrawerDescription, DrawerHeader, DrawerTitle, DrawerTrigger } from "@/components/ui/drawer"
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu"
import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card"
import { Popover, PopoverContent, PopoverDescription, PopoverHeader, PopoverTitle, PopoverTrigger } from "@/components/ui/popover"
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet"
import { TabsContent } from "@/components/ui/tabs"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"

import { ShowcaseCard } from "./showcase-card"

export function OverlaysShowcase() {
  return (
    <TabsContent value="overlays" className="grid gap-4 lg:grid-cols-2">
      <ShowcaseCard title="Overlays" description="dialog, drawer, dropdown-menu, popover, sheet e tooltip.">
        <div className="flex flex-wrap gap-3">
          <Dialog>
            <DialogTrigger asChild>
              <Button variant="outline">Dialog</Button>
            </DialogTrigger>
            <DialogContent>
              <DialogHeader>
                <DialogTitle>Dialog shadcn</DialogTitle>
                <DialogDescription>Overlay central estilizado pelo tema.</DialogDescription>
              </DialogHeader>
            </DialogContent>
          </Dialog>
          <Sheet>
            <SheetTrigger asChild>
              <Button variant="outline">Sheet</Button>
            </SheetTrigger>
            <SheetContent>
              <SheetHeader>
                <SheetTitle>Painel lateral</SheetTitle>
              </SheetHeader>
            </SheetContent>
          </Sheet>
          <Drawer>
            <DrawerTrigger asChild>
              <Button variant="outline">Drawer</Button>
            </DrawerTrigger>
            <DrawerContent>
              <DrawerHeader>
                <DrawerTitle>Drawer</DrawerTitle>
                <DrawerDescription>Overlay inferior do shadcn.</DrawerDescription>
              </DrawerHeader>
            </DrawerContent>
          </Drawer>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline">Menu</Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuItem>Editar</DropdownMenuItem>
              <DropdownMenuItem>Duplicar</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <Popover>
            <PopoverTrigger asChild>
              <Button variant="outline">Popover</Button>
            </PopoverTrigger>
            <PopoverContent>
              <PopoverHeader>
                <PopoverTitle>Resumo</PopoverTitle>
                <PopoverDescription>Conteudo contextual do popover.</PopoverDescription>
              </PopoverHeader>
            </PopoverContent>
          </Popover>
          <Tooltip>
            <TooltipTrigger asChild>
              <Button size="icon" variant="ghost" aria-label="Pesquisar">
                <SearchIcon />
              </Button>
            </TooltipTrigger>
            <TooltipContent>Tooltip shadcn</TooltipContent>
          </Tooltip>
        </div>
      </ShowcaseCard>

      <ShowcaseCard title="Interacao contextual" description="context-menu e hover-card.">
        <ContextMenu>
          <ContextMenuTrigger className="flex h-28 items-center justify-center rounded-lg border border-dashed bg-muted text-sm text-muted-foreground">
            Clique com o botao direito
          </ContextMenuTrigger>
          <ContextMenuContent>
            <ContextMenuItem>Editar</ContextMenuItem>
            <ContextMenuItem>Duplicar</ContextMenuItem>
          </ContextMenuContent>
        </ContextMenu>
        <HoverCard>
          <HoverCardTrigger asChild>
            <Button variant="link" className="w-fit px-0">
              Ver detalhes do componente
            </Button>
          </HoverCardTrigger>
          <HoverCardContent>
            HoverCard com conteudo de apoio e tokens do tema.
          </HoverCardContent>
        </HoverCard>
      </ShowcaseCard>
    </TabsContent>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/showcase-card.tsx"): r"""import { type ReactNode } from "react"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export function ShowcaseCard({
  title,
  description,
  className,
  children,
}: {
  title: string
  description: string
  className?: string
  children: ReactNode
}) {
  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent className="flex flex-col gap-4">{children}</CardContent>
    </Card>
  )
}
""",
    Path("src/features/design-system/components/design-system-showcase/showcase-data.ts"): r"""import { type ChartConfig } from "@/components/ui/chart"

export const chartData = [
  { name: "Jan", volume: 42 },
  { name: "Fev", volume: 68 },
  { name: "Mar", volume: 54 },
  { name: "Abr", volume: 91 },
  { name: "Mai", volume: 76 },
]

export const chartConfig = {
  volume: {
    label: "Volume",
    color: "var(--primary)",
  },
} satisfies ChartConfig

export const services = [
  { name: "Conta digital", status: "ativo", value: "82%" },
  { name: "Pix", status: "ativo", value: "94%" },
  { name: "Cartoes", status: "revisao", value: "61%" },
]

export const operationalRows = [
  {
    id: "OPS-1024",
    service: "Conta digital",
    category: "Contas",
    status: "ativo",
    owner: "Squad Onboarding",
    conversion: 82,
  },
  {
    id: "OPS-1188",
    service: "Pix e transferencias",
    category: "Pagamentos",
    status: "ativo",
    owner: "Squad Pix",
    conversion: 94,
  },
  {
    id: "OPS-1302",
    service: "Cartoes",
    category: "Credito",
    status: "revisao",
    owner: "Squad Cartoes",
    conversion: 61,
  },
  {
    id: "OPS-1407",
    service: "Investimentos",
    category: "Wealth",
    status: "pausado",
    owner: "Squad Invest",
    conversion: 48,
  },
  {
    id: "OPS-1511",
    service: "Seguros",
    category: "Protecao",
    status: "revisao",
    owner: "Squad Seguros",
    conversion: 57,
  },
] as const

export type OperationalRow = (typeof operationalRows)[number]

export type DemoForm = {
  cliente: string
}
""",
    Path("src/features/design-system/components/design-system-catalog.tsx"): """import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  shadcnComponentGroups,
  starterComponentNames,
} from "@/features/design-system/shadcn-components"

export function DesignSystemCatalog() {
  return (
    <section className="flex flex-col gap-4">
      <div className="flex justify-end">
        <Badge variant="secondary">{totalRequiredComponents}/{totalComponents} obrigatorios</Badge>
      </div>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {shadcnComponentGroups.map((group) => (
          <Card key={group.name}>
            <CardHeader>
              <CardTitle>{group.name}</CardTitle>
              <CardDescription>{group.components.length} componentes</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-wrap gap-2">
              {group.components.map((component) => {
                const required = (starterComponentNames as readonly string[]).includes(component)

                return (
                  <Badge key={component} variant={required ? "default" : "outline"}>
                    {required ? "OK " : "Padrao "}
                    {component}
                  </Badge>
                )
              })}
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  )
}

const totalComponents = shadcnComponentGroups.reduce(
  (total, group) => total + group.components.length,
  0,
)

const totalRequiredComponents = starterComponentNames.length
""",
    Path("src/lib/api/types.ts"): '''export type ApiErrorEnvelope = {
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
''',
    Path("src/lib/api/read-helpers.ts"): '''export type UnknownRecord = Record<string, unknown>

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
''',
    Path("src/lib/api/create-api-client.ts"): '''import { ApiRequestError, classifyFetchError, isServerUnavailableStatus } from "./api-errors"
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
',
    Path("src/features/example/config.ts"): '''import { appEnv } from "@/config/app-env"

/** Exemplo: cada feature pode definir versao e base URL proprias. */
export const exampleApiConfig = {
  apiVersion: import.meta.env.VITE_EXAMPLE_API_VERSION ?? appEnv.apiDefaultVersion,
  baseUrl: import.meta.env.VITE_EXAMPLE_API_BASE_URL ?? appEnv.apiBaseUrl,
} as const
''',
    Path("src/features/example/services/api-client.ts"): '''import { createApiClient } from "@/lib/api/create-api-client"

import { exampleApiConfig } from "../config"

export const exampleApi = createApiClient({
  apiVersion: exampleApiConfig.apiVersion,
  baseUrl: exampleApiConfig.baseUrl,
})
''',
    Path("src/features/example/services/index.ts"): '''export { exampleApi } from "./api-client"
''',
    Path("src/features/example/hooks/use-query.ts"): '''import {
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
',
    Path("src/features/example/hooks/use-mutation.ts"): '''import { useCallback, useRef, useState } from "react"

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
',
    Path("src/features/example/hooks/index.ts"): '''export { useMutation, type MutationState, type MutationStatus, type UseMutationOptions } from "./use-mutation"
export {
  useQuery,
  type QueryState,
  type QueryStatus,
  type UseQueryOptions,
} from "./use-query"
',
    Path("src/components/ui/.gitkeep"): "",
    Path("src/hooks/.gitkeep"): "",
    Path("src/features/.gitkeep"): "",
}


SHADCN_COMPONENT_REPLACEMENTS: dict[Path, tuple[tuple[str, str], ...]] = {
    Path("src/components/ui/button.tsx"): (
        (
            "inline-flex shrink-0 items-center justify-center gap-2 rounded-md text-sm font-medium whitespace-nowrap transition-all outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
            "inline-flex shrink-0 items-center justify-center gap-2 rounded-md text-sm font-medium whitespace-nowrap transition-all outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        ),
        (
            "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:bg-destructive/60 dark:focus-visible:ring-destructive/40",
            "bg-destructive text-destructive-foreground hover:bg-destructive/90 focus-visible:ring-destructive/20",
        ),
        (
            "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:border-input dark:bg-input/30 dark:hover:bg-input/50",
            "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground",
        ),
        (
            "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
            "hover:bg-accent hover:text-accent-foreground",
        ),
    ),
    Path("src/components/ui/badge.tsx"): (
        (
            "inline-flex w-fit shrink-0 items-center justify-center gap-1 overflow-hidden rounded-full border border-transparent px-2 py-0.5 text-xs font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 [&>svg]:pointer-events-none [&>svg]:size-3",
            "inline-flex w-fit shrink-0 items-center justify-center gap-1 overflow-hidden rounded-full border border-transparent px-2 py-0.5 text-xs font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 [&>svg]:pointer-events-none [&>svg]:size-3",
        ),
        (
            "bg-destructive text-white focus-visible:ring-destructive/20 dark:bg-destructive/60 dark:focus-visible:ring-destructive/40 [a&]:hover:bg-destructive/90",
            "bg-destructive text-destructive-foreground focus-visible:ring-destructive/20 [a&]:hover:bg-destructive/90",
        ),
    ),
    Path("src/components/ui/input.tsx"): (
        (
            "h-9 w-full min-w-0 rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none selection:bg-primary selection:text-primary-foreground file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm dark:bg-input/30",
            "h-9 w-full min-w-0 rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none selection:bg-primary selection:text-primary-foreground file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        ),
        (
            "aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40",
            "aria-invalid:border-destructive aria-invalid:ring-destructive/20",
        ),
    ),
    Path("src/components/ui/textarea.tsx"): (
        (
            "flex field-sizing-content min-h-16 w-full rounded-md border border-input bg-transparent px-3 py-2 text-base shadow-xs transition-[color,box-shadow] outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 md:text-sm dark:bg-input/30 dark:aria-invalid:ring-destructive/40",
            "flex field-sizing-content min-h-16 w-full rounded-md border border-input bg-transparent px-3 py-2 text-base shadow-xs transition-[color,box-shadow] outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 md:text-sm",
        ),
    ),
    Path("src/components/ui/select.tsx"): (
        (
            "flex w-fit items-center justify-between gap-2 rounded-md border border-input bg-transparent px-3 py-2 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[placeholder]:text-muted-foreground data-[size=default]:h-9 data-[size=sm]:h-8 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-2 dark:bg-input/30 dark:hover:bg-input/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg:not([class*='text-'])]:text-muted-foreground",
            "flex w-fit min-w-0 items-center justify-between gap-2 rounded-md border border-input bg-background px-3 py-2 text-sm font-normal whitespace-nowrap text-foreground shadow-xs transition-[color,box-shadow,background-color,border-color] outline-none hover:border-foreground/20 hover:bg-muted/50 focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 data-[state=open]:border-ring data-[state=open]:bg-background data-[state=open]:ring-[3px] data-[state=open]:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[placeholder]:text-muted-foreground data-[size=default]:h-10 data-[size=sm]:h-8 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-2 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg]:transition-transform [&_svg]:duration-200 [&_svg:not([class*='text-'])]:text-muted-foreground data-[state=open]:[&_svg]:rotate-180 data-[state=open]:[&_svg]:text-foreground",
        ),
        (
            '<ChevronDownIcon className="size-4 opacity-50" />',
            '<ChevronDownIcon className="size-4 opacity-70" />',
        ),
        (
            "relative z-50 max-h-(--radix-select-content-available-height) min-w-[8rem] origin-(--radix-select-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-md border bg-popover text-popover-foreground shadow-md",
            "relative z-50 max-h-(--radix-select-content-available-height) min-w-[8rem] origin-(--radix-select-content-transform-origin) overflow-hidden rounded-lg border border-border bg-popover text-popover-foreground shadow-lg",
        ),
        (
            '"p-1",',
            '"p-1.5",',
        ),
        (
            "relative flex w-full cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg:not([class*='text-'])]:text-muted-foreground *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2",
            "relative flex w-full cursor-default items-center gap-2 rounded-md py-2 pr-9 pl-3 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-[highlighted]:bg-accent data-[highlighted]:text-accent-foreground data-[state=checked]:bg-primary/10 data-[state=checked]:font-medium data-[state=checked]:text-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 [&_svg:not([class*='text-'])]:text-muted-foreground data-[state=checked]:[&_[data-slot=select-item-indicator]_svg]:text-primary *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2",
        ),
    ),
    Path("src/components/ui/native-select.tsx"): (
        (
            "h-9 w-full min-w-0 appearance-none rounded-md border border-input bg-transparent px-3 py-2 pr-9 text-sm shadow-xs transition-[color,box-shadow] outline-none selection:bg-primary selection:text-primary-foreground placeholder:text-muted-foreground disabled:pointer-events-none disabled:cursor-not-allowed data-[size=sm]:h-8 data-[size=sm]:py-1 dark:bg-input/30 dark:hover:bg-input/50",
            "h-10 w-full min-w-0 appearance-none rounded-md border border-input bg-background px-3 py-2 pr-9 text-sm font-normal text-foreground shadow-xs transition-[color,box-shadow,background-color,border-color] outline-none selection:bg-primary selection:text-primary-foreground placeholder:text-muted-foreground hover:border-foreground/20 hover:bg-muted/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 data-[size=sm]:h-8 data-[size=sm]:py-1",
        ),
        (
            "aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40",
            "aria-invalid:border-destructive aria-invalid:ring-destructive/20",
        ),
        (
            "right-3.5 size-4 -translate-y-1/2 text-muted-foreground opacity-50",
            "right-3 size-4 -translate-y-1/2 text-muted-foreground opacity-70",
        ),
    ),
    Path("src/components/ui/checkbox.tsx"): (
        (
            "peer size-4 shrink-0 rounded-[4px] border border-input shadow-xs transition-shadow outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[state=checked]:border-primary data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground dark:bg-input/30 dark:aria-invalid:ring-destructive/40 dark:data-[state=checked]:bg-primary",
            "peer size-4 shrink-0 rounded-[4px] border border-input shadow-xs transition-shadow outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[state=checked]:border-primary data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
        ),
    ),
    Path("src/components/ui/radio-group.tsx"): (
        (
            "aspect-square size-4 shrink-0 rounded-full border border-input text-primary shadow-xs transition-[color,box-shadow] outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 dark:bg-input/30 dark:aria-invalid:ring-destructive/40",
            "aspect-square size-4 shrink-0 rounded-full border border-input text-primary shadow-xs transition-[color,box-shadow] outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20",
        ),
    ),
    Path("src/components/ui/input-otp.tsx"): (
        (
            "relative flex h-9 w-9 items-center justify-center border-y border-r border-input text-sm shadow-xs transition-all outline-none first:rounded-l-md first:border-l last:rounded-r-md aria-invalid:border-destructive data-[active=true]:z-10 data-[active=true]:border-ring data-[active=true]:ring-[3px] data-[active=true]:ring-ring/50 data-[active=true]:aria-invalid:border-destructive data-[active=true]:aria-invalid:ring-destructive/20 dark:bg-input/30 dark:data-[active=true]:aria-invalid:ring-destructive/40",
            "relative flex h-9 w-9 items-center justify-center border-y border-r border-input text-sm shadow-xs transition-all outline-none first:rounded-l-md first:border-l last:rounded-r-md aria-invalid:border-destructive data-[active=true]:z-10 data-[active=true]:border-ring data-[active=true]:ring-[3px] data-[active=true]:ring-ring/50 data-[active=true]:aria-invalid:border-destructive data-[active=true]:aria-invalid:ring-destructive/20",
        ),
    ),
    Path("src/components/ui/input-group.tsx"): (
        (
            "group/input-group relative flex w-full items-center rounded-md border border-input shadow-xs transition-[color,box-shadow] outline-none dark:bg-input/30",
            "group/input-group relative flex w-full items-center rounded-md border border-input shadow-xs transition-[color,box-shadow] outline-none",
        ),
        (
            "has-[[data-slot][aria-invalid=true]]:border-destructive has-[[data-slot][aria-invalid=true]]:ring-destructive/20 dark:has-[[data-slot][aria-invalid=true]]:ring-destructive/40",
            "has-[[data-slot][aria-invalid=true]]:border-destructive has-[[data-slot][aria-invalid=true]]:ring-destructive/20",
        ),
        (
            "flex-1 rounded-none border-0 bg-transparent shadow-none focus-visible:ring-0 dark:bg-transparent",
            "flex-1 rounded-none border-0 bg-transparent shadow-none focus-visible:ring-0",
        ),
        (
            "flex-1 resize-none rounded-none border-0 bg-transparent py-3 shadow-none focus-visible:ring-0 dark:bg-transparent",
            "flex-1 resize-none rounded-none border-0 bg-transparent py-3 shadow-none focus-visible:ring-0",
        ),
    ),
    Path("src/components/ui/tabs.tsx"): (
        (
            "relative inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 text-sm font-medium whitespace-nowrap text-foreground/60 transition-all group-data-[orientation=vertical]/tabs:w-full group-data-[orientation=vertical]/tabs:justify-start hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 focus-visible:outline-ring disabled:pointer-events-none disabled:opacity-50 group-data-[variant=default]/tabs-list:data-[state=active]:shadow-sm group-data-[variant=line]/tabs-list:data-[state=active]:shadow-none dark:text-muted-foreground dark:hover:text-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
            "relative inline-flex h-[calc(100%-1px)] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 text-sm font-medium whitespace-nowrap text-foreground/60 transition-all group-data-[orientation=vertical]/tabs:w-full group-data-[orientation=vertical]/tabs:justify-start hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 focus-visible:outline-ring disabled:pointer-events-none disabled:opacity-50 group-data-[variant=default]/tabs-list:data-[state=active]:shadow-sm group-data-[variant=line]/tabs-list:data-[state=active]:shadow-none [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        ),
        (
            "group-data-[variant=line]/tabs-list:bg-transparent group-data-[variant=line]/tabs-list:data-[state=active]:bg-transparent dark:group-data-[variant=line]/tabs-list:data-[state=active]:border-transparent dark:group-data-[variant=line]/tabs-list:data-[state=active]:bg-transparent",
            "group-data-[variant=line]/tabs-list:bg-transparent group-data-[variant=line]/tabs-list:data-[state=active]:border-transparent group-data-[variant=line]/tabs-list:data-[state=active]:bg-transparent",
        ),
        (
            "data-[state=active]:bg-background data-[state=active]:text-foreground dark:data-[state=active]:border-input dark:data-[state=active]:bg-input/30 dark:data-[state=active]:text-foreground",
            "data-[state=active]:bg-background data-[state=active]:text-foreground",
        ),
    ),
    Path("src/components/ui/switch.tsx"): (
        (
            "peer group/switch inline-flex shrink-0 items-center rounded-full border border-transparent shadow-xs transition-all outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 data-[size=default]:h-[1.15rem] data-[size=default]:w-8 data-[size=sm]:h-3.5 data-[size=sm]:w-6 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input dark:data-[state=unchecked]:bg-input/80",
            "peer group/switch inline-flex shrink-0 items-center rounded-full border border-transparent shadow-xs transition-all outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 data-[size=default]:h-[1.15rem] data-[size=default]:w-8 data-[size=sm]:h-3.5 data-[size=sm]:w-6 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input",
        ),
        (
            "pointer-events-none block rounded-full bg-background ring-0 transition-transform group-data-[size=default]/switch:size-4 group-data-[size=sm]/switch:size-3 data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=unchecked]:translate-x-0 dark:data-[state=checked]:bg-primary-foreground dark:data-[state=unchecked]:bg-foreground",
            "pointer-events-none block rounded-full bg-background ring-0 transition-transform group-data-[size=default]/switch:size-4 group-data-[size=sm]/switch:size-3 data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=checked]:bg-primary-foreground data-[state=unchecked]:translate-x-0",
        ),
    ),
    Path("src/components/ui/slider.tsx"): (
        (
            "block size-4 shrink-0 rounded-full border border-primary bg-white shadow-sm ring-ring/50 transition-[color,box-shadow] hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50",
            "block size-4 shrink-0 rounded-full border border-primary bg-background shadow-sm ring-ring/50 transition-[color,box-shadow] hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50",
        ),
    ),
    Path("src/components/ui/calendar.tsx"): (
        (
            "data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground dark:hover:text-accent-foreground [&>span]:text-xs [&>span]:opacity-70",
            "data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground [&>span]:text-xs [&>span]:opacity-70",
        ),
    ),
    Path("src/components/ui/combobox.tsx"): (
        (
            "flex min-h-9 flex-wrap items-center gap-1.5 rounded-md border border-input bg-transparent bg-clip-padding px-2.5 py-1.5 text-sm shadow-xs transition-[color,box-shadow] focus-within:border-ring focus-within:ring-[3px] focus-within:ring-ring/50 has-aria-invalid:border-destructive has-aria-invalid:ring-[3px] has-aria-invalid:ring-destructive/20 has-data-[slot=combobox-chip]:px-1.5 dark:bg-input/30 dark:has-aria-invalid:border-destructive/50 dark:has-aria-invalid:ring-destructive/40",
            "flex min-h-9 flex-wrap items-center gap-1.5 rounded-md border border-input bg-transparent bg-clip-padding px-2.5 py-1.5 text-sm shadow-xs transition-[color,box-shadow] focus-within:border-ring focus-within:ring-[3px] focus-within:ring-ring/50 has-aria-invalid:border-destructive has-aria-invalid:ring-[3px] has-aria-invalid:ring-destructive/20 has-data-[slot=combobox-chip]:px-1.5",
        ),
    ),
    Path("src/components/ui/toggle.tsx"): (
        (
            "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium whitespace-nowrap transition-[color,box-shadow] outline-none hover:bg-muted hover:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
            "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium whitespace-nowrap transition-[color,box-shadow] outline-none hover:bg-muted hover:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
        ),
    ),
    Path("src/components/ui/field.tsx"): (
        (
            "has-data-[state=checked]:border-primary has-data-[state=checked]:bg-primary/5 dark:has-data-[state=checked]:bg-primary/10",
            "has-data-[state=checked]:border-primary has-data-[state=checked]:bg-primary/5",
        ),
    ),
    Path("src/components/ui/dropdown-menu.tsx"): (
        (
            "data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20",
            "data-[variant=destructive]:focus:text-destructive",
        ),
    ),
    Path("src/components/ui/context-menu.tsx"): (
        (
            "data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20",
            "data-[variant=destructive]:focus:text-destructive",
        ),
    ),
    Path("src/components/ui/menubar.tsx"): (
        (
            "data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20",
            "data-[variant=destructive]:focus:text-destructive",
        ),
    ),
    Path("src/components/ui/kbd.tsx"): (
        (
            "[[data-slot=tooltip-content]_&]:bg-background/20 [[data-slot=tooltip-content]_&]:text-background dark:[[data-slot=tooltip-content]_&]:bg-background/10",
            "[[data-slot=tooltip-content]_&]:bg-background/20 [[data-slot=tooltip-content]_&]:text-background",
        ),
    ),
    Path("src/components/ui/calendar.tsx"): (
        (
            '        table: "w-full border-collapse",',
            '        month_grid: cn("w-full border-collapse", defaultClassNames.month_grid),',
        ),
    ),
}


def create_file(relative_path: Path, content: str, target: Path, force: bool) -> str:
    output_path = target / relative_path
    if output_path.exists() and not force:
        return "skip"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return "create"


def create_app(target: Path, force: bool) -> tuple[list[str], list[str]]:
    created: list[str] = []
    skipped: list[str] = []

    for relative_path in APP_EXPECTED_DIRS:
        (target / relative_path).mkdir(parents=True, exist_ok=True)

    for relative_path, content in APP_FILE_TEMPLATES.items():
        result = create_file(relative_path, content, target, force)
        (created if result == "create" else skipped).append(str(relative_path))

    return created, skipped


def patch_shadcn_components(target: Path) -> list[str]:
    patched: list[str] = []

    for relative_path, replacements in SHADCN_COMPONENT_REPLACEMENTS.items():
        file_path = target / relative_path
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8")
        updated = content
        for old, new in replacements:
            updated = updated.replace(old, new)

        if updated != content:
            file_path.write_text(updated, encoding="utf-8")
            patched.append(str(relative_path))

    return patched


def relocate_misplaced_shadcn_files(target: Path) -> list[str]:
    relocated: list[str] = []
    mappings = (
        (Path("@/components/ui"), Path("src/components/ui")),
        (Path("@/hooks"), Path("src/hooks")),
    )

    for source_root, destination_root in mappings:
        absolute_source_root = target / source_root
        if not absolute_source_root.exists():
            continue

        for source_file in sorted(path for path in absolute_source_root.rglob("*") if path.is_file()):
            relative_file = source_file.relative_to(absolute_source_root)
            destination_file = target / destination_root / relative_file
            source_label = source_file.relative_to(target).as_posix()
            destination_label = destination_file.relative_to(target).as_posix()

            if destination_file.exists():
                if destination_file.read_bytes() == source_file.read_bytes():
                    source_file.unlink()
                    relocated.append(f"{source_label} duplicado em {destination_label}")
                else:
                    relocated.append(f"{source_label} mantido: conflito com {destination_label}")
                continue

            destination_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source_file), str(destination_file))
            relocated.append(f"{source_label} -> {destination_label}")

    remove_empty_directory_tree(target / "@")

    return relocated


def remove_empty_directory_tree(root: Path) -> None:
    if not root.exists():
        return

    for directory in sorted((path for path in root.rglob("*") if path.is_dir()), key=lambda path: len(path.parts), reverse=True):
        try:
            directory.rmdir()
        except OSError:
            pass

    try:
        root.rmdir()
    except OSError:
        pass


def run_shadcn_add_all(target: Path) -> int:
    command = ["npx", "shadcn@latest", "add", "--all", "--yes"]
    print("Materializando componentes shadcn oficiais:")
    print("  " + " ".join(command))

    completed = subprocess.run(command, cwd=target, check=False)
    if completed.returncode != 0:
        print()
        print("Falha ao executar shadcn add --all.")
        print("Rode manualmente dentro do projeto:")
        print("  npx shadcn@latest add --all")
        return completed.returncode

    relocated = relocate_misplaced_shadcn_files(target)
    print_status("componentes shadcn realocados", relocated)

    patched = patch_shadcn_components(target)
    print_status("componentes shadcn ajustados", patched)

    return 0


def init_app(target: Path, force: bool, with_shadcn: bool) -> int:
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)

    app_created, app_skipped = create_app(target, force)

    print(f"Starter React/Vite criado em: {target}")
    print_status("app criado", app_created)
    print_status("app mantido", app_skipped)
    print()

    if with_shadcn:
        shadcn_status = run_shadcn_add_all(target)
        if shadcn_status != 0:
            return shadcn_status
        print()
    else:
        print("Para materializar os componentes oficiais do shadcn usados pelo starter, rode:")
        print("  python3 bootstrap.py init-app . --with-shadcn")
        print("Ou execute manualmente dentro do projeto:")
        print("  npx shadcn@latest add --all")
        print()

    print("Componentes shadcn obrigatorios para este bootstrap:")
    print("  npx shadcn@latest add --all")
    print()
    return validate_app(target)


def validate_app(target: Path) -> int:
    target = target.resolve()

    missing_app = missing_paths(target, APP_EXPECTED_FILES + APP_EXPECTED_DIRS)
    missing_shadcn = missing_paths(target, SHADCN_STARTER_REQUIRED_FILES)
    misplaced_shadcn = misplaced_shadcn_paths(target)

    if missing_app:
        print("App React/Vite: pendente")
        print_status("faltando", missing_app)
    else:
        print("App React/Vite: ok")

    if missing_shadcn:
        print("Componentes shadcn do starter: pendente")
        print_status("faltando", missing_shadcn)
    else:
        print("Componentes shadcn do starter: ok")

    if misplaced_shadcn:
        print("Componentes shadcn fora do alias src: pendente")
        print_status("fora de src", misplaced_shadcn)

    if missing_app or missing_shadcn or misplaced_shadcn:
        print()
        print("Observacao: a base do app existe quando App React/Vite esta ok; rode shadcn add para materializar src/components/ui.")
        return 2

    return 0


def missing_paths(target: Path, paths: tuple[Path, ...]) -> list[str]:
    return [str(path) for path in paths if not (target / path).exists()]


def misplaced_shadcn_paths(target: Path) -> list[str]:
    literal_alias_root = target / "@"
    if not literal_alias_root.exists():
        return []

    return [
        path.relative_to(target).as_posix()
        for path in sorted(literal_alias_root.rglob("*"), key=lambda path: path.as_posix())
        if path.is_file()
    ]


def print_status(label: str, paths: list[str]) -> None:
    if not paths:
        return

    print(f"{label}:")
    for path in paths:
        print(f"  - {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cria ou valida o starter frontend em um projeto React/Vite."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    app_parser = subparsers.add_parser("init-app", help="cria apenas o starter React/Vite")
    app_parser.add_argument("target", nargs="?", default=".", help="diretorio do projeto alvo")
    app_parser.add_argument("--force", action="store_true", help="sobrescreve arquivos do starter")
    app_parser.add_argument(
        "--with-shadcn",
        action="store_true",
        help="executa npx shadcn@latest add --all para materializar componentes oficiais",
    )

    validate_app_parser = subparsers.add_parser("validate-app", help="valida apenas estrutura do app")
    validate_app_parser.add_argument("target", nargs="?", default=".", help="diretorio do projeto alvo")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "init-app":
        return init_app(Path(args.target), args.force, args.with_shadcn)

    if args.command == "validate-app":
        return validate_app(Path(args.target))

    return 1


if __name__ == "__main__":
    sys.exit(main())
