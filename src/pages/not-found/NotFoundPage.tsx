import { HomeIcon, SearchXIcon } from "lucide-react"

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
