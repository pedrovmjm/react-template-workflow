import { useEffect, useState } from "react"

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
