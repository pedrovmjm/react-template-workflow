import { DesignSystemShowcase } from "@/features/design-system/components/design-system-showcase"

export function DesignSystemPage() {
  return (
    <div className="mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 md:px-6 lg:py-8">
      <DesignSystemShowcase />
    </div>
  )
}
