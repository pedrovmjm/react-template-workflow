import { type ReactNode } from "react"
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
