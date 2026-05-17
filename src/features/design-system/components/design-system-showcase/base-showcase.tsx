import { SettingsIcon, SparklesIcon } from "lucide-react"

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
