import { FileTextIcon, SearchIcon } from "lucide-react"

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
