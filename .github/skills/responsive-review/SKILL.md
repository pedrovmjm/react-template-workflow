---
name: responsive-review
description: Revisa comportamento responsivo em mobile, tablet e desktop, incluindo overflow, app shell, sidebar, tabelas, cards, formularios, dialogs e sheets. Use no planejamento e na revisao final de UI.
---

# Skill: responsive-review

## Nome

responsive-review

## Proposito

Revisar comportamento responsivo em mobile, tablet e desktop, incluindo overflow e componentes complexos.

## Quando usar

- Depois do plano de layout.
- Antes da implementacao.
- Depois da implementacao, como gate de revisao.

## Entradas

- Plano de componentes.
- Plano de layout.
- Codigo implementado, quando disponivel.

## Saidas

- Revisao responsiva.
- Problemas, mitigacoes e riscos aceitos.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/responsive-review.template.md` | Use ao revisar mobile/tablet/desktop, app shell, sidebar, tabela, card, formulario, dialog, sheet ou conteudo dinamico. | Modelo de saida para viewports avaliados, problemas por breakpoint, overflow, mitigacoes, riscos aceitos e conclusao. |

## Procedimento

1. Defina breakpoints relevantes.
2. Revise mobile primeiro.
3. Revise tablet e desktop.
4. Procure overflow horizontal e vertical.
5. Revise tables, cards, forms, dialogs e sheets.
6. Revise comportamento dentro do app shell.
7. Registre problemas, mitigacao e status.

## Checklist

- [ ] Mobile tem fluxo utilizavel.
- [ ] Tablet nao fica como desktop comprimido.
- [ ] Desktop usa espaco sem exagero.
- [ ] Conteudo longo nao quebra layout.
- [ ] Dialogs e sheets cabem na viewport.
- [ ] Sidebar/app shell nao escondem conteudo.

## Exemplos

- Tabela larga pode virar cards em mobile.
- Sidebar fixa pode exigir `min-w-0` no conteudo principal.
- Dialog com formulario longo precisa de area rolavel.

## Anti-patterns

- Validar so no desktop.
- Esconder overflow sem resolver a causa.
- Usar `w-screen` dentro de app shell com sidebar.
- Ignorar teclado virtual em mobile.
