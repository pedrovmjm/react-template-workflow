import { lazy, Suspense, useMemo, useState } from "react"
import { useForm } from "react-hook-form"

import { Spinner } from "@/components/ui/spinner"
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { operationalRows, type DemoForm } from "./design-system-showcase/showcase-data"

const BaseShowcase = lazy(() =>
  import("./design-system-showcase/base-showcase").then((module) => ({
    default: module.BaseShowcase,
  })),
)
const FormsShowcase = lazy(() =>
  import("./design-system-showcase/forms-showcase").then((module) => ({
    default: module.FormsShowcase,
  })),
)
const NavigationShowcase = lazy(() =>
  import("./design-system-showcase/navigation-showcase").then((module) => ({
    default: module.NavigationShowcase,
  })),
)
const OverlaysShowcase = lazy(() =>
  import("./design-system-showcase/overlays-showcase").then((module) => ({
    default: module.OverlaysShowcase,
  })),
)
const DataShowcase = lazy(() =>
  import("./design-system-showcase/data-showcase").then((module) => ({
    default: module.DataShowcase,
  })),
)
const FeedbackShowcase = lazy(() =>
  import("./design-system-showcase/feedback-showcase").then((module) => ({
    default: module.FeedbackShowcase,
  })),
)

type ShowcaseTab = "base" | "forms" | "navigation" | "overlays" | "data" | "feedback"

function ShowcaseLoader() {
  return (
    <div className="flex min-h-48 items-center justify-center gap-2 text-sm text-muted-foreground">
      <Spinner className="size-4" />
      Carregando secao
    </div>
  )
}

export function DesignSystemShowcase() {
  const [activeTab, setActiveTab] = useState<ShowcaseTab>("base")
  const [removedRowIds, setRemovedRowIds] = useState<string[]>([])
  const [tableQuery, setTableQuery] = useState("")
  const [statusFilter, setStatusFilter] = useState("all")
  const [categoryFilter, setCategoryFilter] = useState("all")
  const [uploadedFiles, setUploadedFiles] = useState<File[]>([])

  const form = useForm<DemoForm>({
    defaultValues: {
      cliente: "Cliente Demo",
    },
  })

  const tableRows = useMemo(
    () => operationalRows.filter((row) => !removedRowIds.includes(row.id)),
    [removedRowIds],
  )

  const filteredRows = useMemo(() => {
    const normalizedQuery = tableQuery.trim().toLowerCase()

    return tableRows.filter((row) => {
      const matchesQuery =
        normalizedQuery.length === 0 ||
        row.id.toLowerCase().includes(normalizedQuery) ||
        row.service.toLowerCase().includes(normalizedQuery) ||
        row.owner.toLowerCase().includes(normalizedQuery)
      const matchesStatus = statusFilter === "all" || row.status === statusFilter
      const matchesCategory = categoryFilter === "all" || row.category === categoryFilter

      return matchesQuery && matchesStatus && matchesCategory
    })
  }, [categoryFilter, statusFilter, tableQuery, tableRows])

  return (
    <section className="flex flex-col gap-6">
      <div className="flex flex-col gap-2">
        <h1 className="text-3xl font-semibold tracking-normal">Design System</h1>
        <p className="max-w-3xl text-sm text-muted-foreground">
          Galeria funcional dos componentes shadcn/ui materializados pelo bootstrap e estilizados
          pelos tokens do projeto.
        </p>
      </div>

      <Tabs value={activeTab} onValueChange={(value) => setActiveTab(value as ShowcaseTab)}>
        <TabsList className="flex h-auto w-full flex-wrap justify-start">
          <TabsTrigger value="base">Base</TabsTrigger>
          <TabsTrigger value="forms">Forms</TabsTrigger>
          <TabsTrigger value="navigation">Navigation</TabsTrigger>
          <TabsTrigger value="overlays">Overlays</TabsTrigger>
          <TabsTrigger value="data">Data</TabsTrigger>
          <TabsTrigger value="feedback">Feedback</TabsTrigger>
        </TabsList>

        <Suspense fallback={<ShowcaseLoader />}>
          {activeTab === "base" ? <BaseShowcase /> : null}
          {activeTab === "forms" ? (
            <FormsShowcase form={form} uploadedFiles={uploadedFiles} setUploadedFiles={setUploadedFiles} />
          ) : null}
          {activeTab === "navigation" ? <NavigationShowcase /> : null}
          {activeTab === "overlays" ? <OverlaysShowcase /> : null}
          {activeTab === "data" ? (
            <DataShowcase
              categoryFilter={categoryFilter}
              filteredRows={filteredRows}
              setCategoryFilter={setCategoryFilter}
              setRemovedRowIds={setRemovedRowIds}
              setStatusFilter={setStatusFilter}
              setTableQuery={setTableQuery}
              statusFilter={statusFilter}
              tableQuery={tableQuery}
              tableRows={tableRows}
            />
          ) : null}
          {activeTab === "feedback" ? <FeedbackShowcase /> : null}
        </Suspense>
      </Tabs>
    </section>
  )
}
