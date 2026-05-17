import { PageHeader } from "@/components/layout/page-header"
import { DesignSystemPanel } from "@/features/design-system/components/design-system-panel"

export function HomePage() {
  return (
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 md:px-6 lg:py-8">
      <PageHeader
        eyebrow="Bootstrap"
        title="Starter React com workflow pronto"
        description="Base operacional com sidebar, rotas, design system, componentes shadcn/ui e estados reutilizaveis para novas features."
      />
      <DesignSystemPanel />
    </div>
  )
}
