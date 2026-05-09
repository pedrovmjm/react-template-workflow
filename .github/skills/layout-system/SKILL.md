---
name: layout-system
description: Planeja layouts consistentes com Tailwind CSS, shadcn/ui e .github/design-system.md, incluindo hierarquia visual, responsividade, estados de UI e composicao. Use antes de implementar telas, paineis, formularios, tabelas ou fluxos visuais.
---

# Skill: layout-system

## Nome

layout-system

## Proposito

Planejar layouts consistentes com Tailwind CSS, shadcn/ui e os padroes visuais do aplicativo.

Leia `.github/design-system.md` antes de decidir tokens, spacing, radius, densidade, estados ou comportamento responsivo.

## Quando usar

- Antes de implementar tela, pagina, painel, lista, formulario, tabela ou fluxo visual.
- Quando a feature precisa se adaptar a app shell, sidebar, navbar ou areas de conteudo.

## Entradas

- Brief da feature.
- Plano de componentes.
- Layouts existentes.
- `.github/design-system.md`.
- Regras shadcn em `.github/skills/shadcn`.

## Saidas

- Plano de layout.
- Hierarquia visual.
- Composicao shadcn/ui e convencoes Tailwind.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/layout-review.template.md` | Use ao planejar ou revisar tela, painel, formulario, tabela, dashboard, dialog ou fluxo visual. | Modelo de saida para padrao de layout, hierarquia, desktop/tablet/mobile, componentes shadcn/ui, Tailwind, tokens, estados e riscos visuais. |
| `references/oficiais.md` | Use quando precisar confirmar documentacao ou criterio externo sobre Tailwind, shadcn/ui, Radix, lucide ou design responsivo. | Lista de referencias oficiais que sustentam decisoes de layout e design system. |

## Procedimento

1. Leia `.github/design-system.md`.
2. Escolha o padrao de layout.
3. Defina hierarquia visual e ordem de leitura.
4. Mapeie componentes shadcn/ui usados.
5. Defina convencoes Tailwind de spacing, grid, largura e altura.
6. Planeje desktop, tablet e mobile.
7. Planeje empty, loading e error states.
8. Registre riscos visuais.

## Checklist

- [ ] O layout serve ao fluxo principal do usuario.
- [ ] Espacamento usa escala consistente.
- [ ] A UI nao depende de medidas fixas frageis.
- [ ] shadcn/ui e usado como base.
- [ ] Estados vazios, loading e erro foram desenhados.
- [ ] Nao ha cards dentro de cards sem necessidade.

## Exemplos

- Use `gap-*` em flex/grid para espacamento interno.
- Use `grid gap-4 md:grid-cols-2` para layouts que crescem progressivamente.
- Use `max-w-*` somente quando a leitura se beneficiar de largura limitada.

## Anti-patterns

- Layout de marketing para tela operacional.
- Classes Tailwind improvisadas sem padrao.
- Texto que depende de viewport para caber.
- Larguras fixas que quebram em mobile.
