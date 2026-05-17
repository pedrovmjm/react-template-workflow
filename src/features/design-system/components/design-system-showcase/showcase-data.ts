import { type ChartConfig } from "@/components/ui/chart"

export const chartData = [
  { name: "Jan", volume: 42 },
  { name: "Fev", volume: 68 },
  { name: "Mar", volume: 54 },
  { name: "Abr", volume: 91 },
  { name: "Mai", volume: 76 },
]

export const chartConfig = {
  volume: {
    label: "Volume",
    color: "var(--primary)",
  },
} satisfies ChartConfig

export const services = [
  { name: "Conta digital", status: "ativo", value: "82%" },
  { name: "Pix", status: "ativo", value: "94%" },
  { name: "Cartoes", status: "revisao", value: "61%" },
]

export const operationalRows = [
  {
    id: "OPS-1024",
    service: "Conta digital",
    category: "Contas",
    status: "ativo",
    owner: "Squad Onboarding",
    conversion: 82,
  },
  {
    id: "OPS-1188",
    service: "Pix e transferencias",
    category: "Pagamentos",
    status: "ativo",
    owner: "Squad Pix",
    conversion: 94,
  },
  {
    id: "OPS-1302",
    service: "Cartoes",
    category: "Credito",
    status: "revisao",
    owner: "Squad Cartoes",
    conversion: 61,
  },
  {
    id: "OPS-1407",
    service: "Investimentos",
    category: "Wealth",
    status: "pausado",
    owner: "Squad Invest",
    conversion: 48,
  },
  {
    id: "OPS-1511",
    service: "Seguros",
    category: "Protecao",
    status: "revisao",
    owner: "Squad Seguros",
    conversion: 57,
  },
] as const

export type OperationalRow = (typeof operationalRows)[number]

export type DemoForm = {
  cliente: string
}
