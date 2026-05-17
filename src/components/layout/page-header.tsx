import { type ReactNode } from "react"

import { Badge } from "@/components/ui/badge"
import { Separator } from "@/components/ui/separator"

type PageHeaderProps = {
  actions?: ReactNode
  description?: string
  eyebrow?: string
  title: string
}

export function PageHeader({ actions, description, eyebrow, title }: PageHeaderProps) {
  return (
    <section className="flex flex-col gap-4 rounded-lg border bg-card p-6 text-card-foreground md:flex-row md:items-start md:justify-between">
      <div className="min-w-0">
        {eyebrow ? (
          <Badge className="mb-3 w-fit" variant="secondary">
            {eyebrow}
          </Badge>
        ) : null}
        <div className="flex flex-col gap-2">
          <h1 className="text-2xl font-semibold tracking-normal md:text-3xl">{title}</h1>
          {description ? (
            <p className="max-w-3xl text-sm text-muted-foreground md:text-base">{description}</p>
          ) : null}
        </div>
      </div>

      {actions ? (
        <>
          <Separator className="md:hidden" />
          <div className="flex shrink-0 flex-wrap items-center gap-2">{actions}</div>
        </>
      ) : null}
    </section>
  )
}
