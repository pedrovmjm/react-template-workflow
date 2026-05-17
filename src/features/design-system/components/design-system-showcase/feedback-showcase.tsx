import { BellIcon, CreditCardIcon } from "lucide-react"

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
