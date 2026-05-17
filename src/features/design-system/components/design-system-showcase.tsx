import { useMemo, useState } from "react"
import { useForm } from "react-hook-form"

import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { BaseShowcase } from "./design-system-showcase/base-showcase"
import { DataShowcase } from "./design-system-showcase/data-showcase"
import { FeedbackShowcase } from "./design-system-showcase/feedback-showcase"
import { FormsShowcase } from "./design-system-showcase/forms-showcase"
import { NavigationShowcase } from "./design-system-showcase/navigation-showcase"
import { OverlaysShowcase } from "./design-system-showcase/overlays-showcase"
import { operationalRows, type DemoForm } from "./design-system-showcase/showcase-data"

export function DesignSystemShowcase() {
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

      <Tabs defaultValue="base">
        <TabsList className="flex h-auto w-full flex-wrap justify-start">
          <TabsTrigger value="base">Base</TabsTrigger>
          <TabsTrigger value="forms">Forms</TabsTrigger>
          <TabsTrigger value="navigation">Navigation</TabsTrigger>
          <TabsTrigger value="overlays">Overlays</TabsTrigger>
          <TabsTrigger value="data">Data</TabsTrigger>
          <TabsTrigger value="feedback">Feedback</TabsTrigger>
        </TabsList>

        <BaseShowcase />
        <FormsShowcase form={form} uploadedFiles={uploadedFiles} setUploadedFiles={setUploadedFiles} />
        <NavigationShowcase />
        <OverlaysShowcase />
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
        <FeedbackShowcase />
      </Tabs>
    </section>
  )
}
