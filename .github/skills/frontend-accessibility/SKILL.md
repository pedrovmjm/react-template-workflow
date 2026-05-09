---
name: frontend-accessibility
description: Use para implementar ou revisar acessibilidade frontend: WCAG, ARIA, HTML semantico, teclado, foco, formularios, dialogs, menus, contrastes e testes de a11y.
---

# Acessibilidade Frontend

Use esta skill quando uma mudanca envolver UI interativa, formulario, navegacao, conteudo dinamico ou revisao visual.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `references/oficiais.md` | Use quando precisar confirmar WCAG, ARIA, HTML semantico, teclado, foco ou padroes de componentes acessiveis. | Referencias oficiais para embasar decisoes de acessibilidade. |
| `references/checklist.md` | Use em revisoes praticas de tela, componente, formulario, dialog, menu ou fluxo dinamico. | Checklist operacional para nao esquecer labels, roles, teclado, foco, contraste, mensagens e testes. |

## Processo

1. Prefira HTML semantico e componentes acessiveis existentes.
2. Garanta nome acessivel para todo controle.
3. Verifique teclado: Tab, Shift+Tab, Enter, Space, Escape e setas quando aplicavel.
4. Verifique foco visivel e ordem de foco.
5. Verifique contraste e estados visuais.
6. Use ARIA somente para complementar semantica, nunca para mascarar HTML incorreto.
7. Adicione testes quando a acessibilidade for contrato do comportamento.

## Componentes criticos

- Dialog: foco preso, Escape, titulo, descricao e retorno de foco.
- Menu/Combobox/Select: teclado, aria-expanded, aria-controls quando aplicavel.
- Tabs: roles e setas quando implementado manualmente; prefira Radix/shadcn.
- Form: label, erro associado e `aria-invalid` quando houver erro.
- Alert/status: `role="alert"` ou regiao adequada para mensagens importantes.

## Referencias

- Leia `references/oficiais.md`.
- Leia `references/checklist.md`.
