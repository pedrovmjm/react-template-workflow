import { type ReactNode } from "react"
import { AlertCircleIcon, InboxIcon, RefreshCwIcon } from "lucide-react"

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {
  Empty,
  EmptyContent,
  EmptyDescription,
  EmptyHeader,
  EmptyMedia,
  EmptyTitle,
} from "@/components/ui/empty"
import { Skeleton } from "@/components/ui/skeleton"

type DataStateProps = {
  actionLabel?: string
  children?: ReactNode
  description?: string
  onAction?: () => void
  state: "ready" | "loading" | "empty" | "error"
  title: string
}

export function DataState({
  actionLabel,
  children,
  description,
  onAction,
  state,
  title,
}: DataStateProps) {
  if (state === "ready") {
    return <>{children}</>
  }

  if (state === "loading") {
    return (
      <Card aria-busy="true" aria-live="polite">
        <CardHeader>
          <CardTitle>{title}</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-col gap-3">
          <Skeleton className="h-4 w-3/4" />
          <Skeleton className="h-4 w-full" />
          <Skeleton className="h-4 w-2/3" />
        </CardContent>
      </Card>
    )
  }

  if (state === "error") {
    return (
      <Alert variant="destructive">
        <AlertCircleIcon aria-hidden="true" />
        <AlertTitle>{title}</AlertTitle>
        {description ? <AlertDescription>{description}</AlertDescription> : null}
        {actionLabel && onAction ? (
          <Button className="mt-3 w-fit" variant="secondary" onClick={onAction}>
            <RefreshCwIcon data-icon="inline-start" />
            {actionLabel}
          </Button>
        ) : null}
      </Alert>
    )
  }

  return (
    <Empty className="min-h-64 border bg-card">
      <EmptyHeader>
        <EmptyMedia variant="icon">
          <InboxIcon aria-hidden="true" />
        </EmptyMedia>
        <EmptyTitle>{title}</EmptyTitle>
        {description ? <EmptyDescription>{description}</EmptyDescription> : null}
      </EmptyHeader>
      {actionLabel && onAction ? (
        <EmptyContent>
          <Button onClick={onAction}>{actionLabel}</Button>
        </EmptyContent>
      ) : null}
    </Empty>
  )
}
