import { lazy, Suspense, useEffect, useState } from "react"

import { AppShell, type AppPage } from "@/components/layout/app-shell"
import { Spinner } from "@/components/ui/spinner"

const ChatPage = lazy(() =>
  import("@/pages/chat/ChatPage").then((module) => ({ default: module.ChatPage })),
)
const DesignSystemPage = lazy(() =>
  import("@/pages/design-system/DesignSystemPage").then((module) => ({
    default: module.DesignSystemPage,
  })),
)
const HomePage = lazy(() =>
  import("@/pages/home/HomePage").then((module) => ({ default: module.HomePage })),
)
const NotFoundPage = lazy(() =>
  import("@/pages/not-found/NotFoundPage").then((module) => ({ default: module.NotFoundPage })),
)
const WorkflowPage = lazy(() =>
  import("@/pages/workflow/WorkflowPage").then((module) => ({ default: module.WorkflowPage })),
)

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

function PageLoader() {
  return (
    <div className="flex min-h-48 items-center justify-center gap-2 text-sm text-muted-foreground">
      <Spinner className="size-4" />
      Carregando pagina
    </div>
  )
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
      <Suspense fallback={<PageLoader />}>
        {currentPage === "chat" ? <ChatPage /> : null}
        {currentPage === "design-system" ? <DesignSystemPage /> : null}
        {currentPage === "home" ? <HomePage /> : null}
        {currentPage === "workflow" ? <WorkflowPage /> : null}
        {currentPage === "not-found" ? (
          <NotFoundPage onNavigateHome={() => handleNavigate("home")} />
        ) : null}
      </Suspense>
    </AppShell>
  )
}
