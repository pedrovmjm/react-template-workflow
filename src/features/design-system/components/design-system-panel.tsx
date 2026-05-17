import { ArrowRightIcon } from "lucide-react"

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
