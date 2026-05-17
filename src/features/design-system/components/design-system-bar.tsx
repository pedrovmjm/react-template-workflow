import { Badge } from "@/components/ui/badge"
import { Card, CardContent } from "@/components/ui/card"
import { Separator } from "@/components/ui/separator"

export function DesignSystemBar() {
  return (
    <Card className="overflow-hidden">
      <CardContent className="flex flex-col gap-4 p-4 md:flex-row md:items-center">
        <div className="min-w-0">
          <p className="text-sm font-semibold">Design System</p>
          <p className="text-sm text-muted-foreground">
            Tokens, estrutura feature-first e shadcn/ui prontos para a primeira tela.
          </p>
        </div>
        <Separator className="hidden h-8 md:block" orientation="vertical" />
        <div className="flex flex-wrap gap-2 md:ml-auto">
          <Badge>primary #e60023</Badge>
          <Badge variant="secondary">radius 16px</Badge>
          <Badge variant="outline">Inter</Badge>
        </div>
      </CardContent>
    </Card>
  )
}
