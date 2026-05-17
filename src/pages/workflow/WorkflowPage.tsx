import { CheckCircle2Icon, GitPullRequestIcon, ShieldCheckIcon } from "lucide-react"

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
