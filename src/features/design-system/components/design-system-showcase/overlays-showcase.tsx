import { SearchIcon } from "lucide-react"

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
