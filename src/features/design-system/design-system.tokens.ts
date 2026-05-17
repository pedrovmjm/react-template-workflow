export const colorTokens = [
  { name: "primary", value: "#e60023", usage: "CTA principal e foco de acao" },
  { name: "canvas", value: "#ffffff", usage: "Fundo principal" },
  { name: "surface-card", value: "#f6f6f3", usage: "Superficie discreta" },
  { name: "hairline", value: "#dadad3", usage: "Bordas e divisores" },
  { name: "ink-soft", value: "#211922", usage: "Texto principal" },
  { name: "mute", value: "#62625b", usage: "Texto secundario" },
] as const

export const architectureLayers = [
  {
    name: "pages",
    description: "Rotas e composicao de layout. Nao concentram regra de negocio.",
  },
  {
    name: "features",
    description: "UI e regras de dominio, com components, hooks, services, schemas e types.",
  },
  {
    name: "services",
    description: "Clientes de API e integracoes sem dependencia de React.",
  },
  {
    name: "workflow",
    description: "Fluxo de validacao, gates e padroes de entrega do frontend.",
  },
] as const
