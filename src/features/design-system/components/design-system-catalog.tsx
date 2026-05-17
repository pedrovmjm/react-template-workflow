import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  shadcnComponentGroups,
  starterComponentNames,
} from "@/features/design-system/shadcn-components"

export function DesignSystemCatalog() {
  return (
    <section className="flex flex-col gap-4">
      <div className="flex justify-end">
        <Badge variant="secondary">{totalRequiredComponents}/{totalComponents} obrigatorios</Badge>
      </div>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {shadcnComponentGroups.map((group) => (
          <Card key={group.name}>
            <CardHeader>
              <CardTitle>{group.name}</CardTitle>
              <CardDescription>{group.components.length} componentes</CardDescription>
            </CardHeader>
            <CardContent className="flex flex-wrap gap-2">
              {group.components.map((component) => {
                const required = (starterComponentNames as readonly string[]).includes(component)

                return (
                  <Badge key={component} variant={required ? "default" : "outline"}>
                    {required ? "OK " : "Padrao "}
                    {component}
                  </Badge>
                )
              })}
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  )
}

const totalComponents = shadcnComponentGroups.reduce(
  (total, group) => total + group.components.length,
  0,
)

const totalRequiredComponents = starterComponentNames.length
