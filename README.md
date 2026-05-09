# react-template-workflow

Workflow de agentes e skills para projetos React + Vite + shadcn/ui + TypeScript + Tailwind + lucide.

## Estrutura

- `.github/copilot-instructions.md`: instrucoes globais do repositorio para Copilot.
- `.github/agents/`: perfis de agentes do GitHub Copilot no formato `.agent.md`, com frontmatter `name`, `description` e `tools`.
- `.github/skills/`: skills de projeto no formato oficial do GitHub Copilot, cada uma em uma pasta propria com `SKILL.md`.
- `.github/design-system.md`: fonte obrigatoria de design system para tokens, componentes, estados, layouts e criterios visuais.

## Skills

- `feature-brief`: transformar pedido em escopo verificavel.
- `component-plan`: arquitetura frontend, componentes, props, estado e arquivos.
- `layout-system`: layout, hierarquia visual, responsividade e uso obrigatorio de `.github/design-system.md`.
- `shadcn`: skill operacional principal de shadcn/ui, CLI, regras locais e componentes instalados.
- `react-best-practices`: React, Vite, TypeScript, hooks, forms, estado, queries e performance basica.
- `testing-strategy`: planejamento de cobertura e definition of done.
- `frontend-accessibility`: WCAG, ARIA, teclado, foco e checklist de a11y.
- `security-review`, `content-renderer`, `responsive-review`: dominios especializados existentes.

## Agentes

Trilha principal:

1. `frontend-orchestrator`: coordena o fluxo completo.
2. `feature-brief-agent`: escopo, objetivos, nao objetivos e aceite.
3. `architecture-agent`: fronteiras, ownership e estrutura.
4. `ui-layout-agent`: layout, shadcn/ui, lucide e responsividade.
5. `component-planning-agent`: componentes, props, eventos e estado.
6. `react-implementer`: implementacao quando o workflow precisar editar codigo.
7. `react-best-practices-agent`: revisao React/TypeScript.
8. `api-state-agent`: dados remotos, query/cache, estado compartilhado e formularios persistidos.
9. `responsive-review-agent`, `accessibility-agent`, `security-agent`, `content-renderer-agent`: revisoes por dominio.
10. `testing-agent`: estrategia de testes e DoD.
11. `frontend-orchestrator`: consolida riscos, gates e decisao final.

## Matriz de sobreposicao

| Area | Dono principal | Pode apoiar | Nao deve fazer |
| --- | --- | --- | --- |
| Escopo e plano | `frontend-orchestrator` | `feature-brief-agent` | Implementar UI de producao |
| Design system | `ui-layout-agent` | `responsive-review-agent` | Ignorar `.github/design-system.md` |
| Componentes React | `react-implementer` | `component-planning-agent`, `react-best-practices-agent` | Criar tokens ou padroes visuais isolados |
| shadcn/ui | `ui-layout-agent` | `react-implementer` | Reimplementar primitivos existentes |
| Estado e formularios | `api-state-agent` | `react-implementer`, `react-best-practices-agent` | Misturar regra de negocio em componentes sem motivo |
| Acessibilidade | `accessibility-agent` | `ui-layout-agent`, `testing-agent` | Tratar a11y como checagem so no fim |
| Testes | `testing-agent` | `react-implementer` | Testar detalhes de implementacao quando comportamento basta |
| Performance | `react-best-practices-agent` | `react-implementer` | Criar agente separado sem necessidade |
| Revisao final | `frontend-orchestrator` | Todos | Reabrir arquitetura sem evidencia |

## Principios

- Agentes coordenam responsabilidade; skills guardam modo de trabalho reutilizavel.
- Referencias detalhadas ficam dentro de `references/` da skill ja existente correspondente.
- Toda alteracao visual deve consultar `.github/design-system.md`.
- Toda feature de UI deve sair com validacao minima: typecheck, lint, teste adequado e, quando houver tela, verificacao visual/responsiva.
- Quando duas skills parecem aplicaveis, use a skill mais especifica e consulte a outra apenas para checagens de borda.
