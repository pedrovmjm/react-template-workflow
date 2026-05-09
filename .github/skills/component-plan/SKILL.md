---
name: component-plan
description: Planeja arquitetura frontend, componentes React, contratos de props, estado, fluxo de dados, hooks, services e arvore de arquivos antes da implementacao. Use depois do brief e antes de alterar componentes.
---

# Skill: component-plan

## Nome

component-plan

## Proposito

Planejar arquitetura, componentes, contratos de props, estado, fluxo de dados e estrutura de arquivos antes da implementacao.

## Quando usar

- Depois do brief.
- Antes de criar ou alterar componentes.
- Quando houver duvida sobre `pages`, `features`, `components`, `services`, `hooks`, `store`, `schemas`, `types` ou `utils`.

## Entradas

- Brief da feature.
- Estrutura atual do projeto.
- Componentes existentes.
- Regras shadcn em `.github/skills/shadcn`, quando a feature envolver UI shadcn.

## Saidas

- Plano de componentes e arquitetura.
- Arvore de arquivos proposta.
- Contratos de props, estado e dados.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/component-plan.template.md` | Use quando precisar entregar um plano de componentes completo e consistente antes da implementacao. | Modelo de saida para arvore de arquivos, componentes, contratos de props, eventos, dono de estado, dados, hooks, services e decisoes abertas. |

## Procedimento

1. Identifique rotas e paginas afetadas.
2. Defina se a logica pertence a feature, pagina, service, hook ou store.
3. Separe componentes de pagina, feature e compartilhados.
4. Defina props e eventos.
5. Defina dono do estado.
6. Defina hooks e services necessarios.
7. Planeje a arvore de arquivos.
8. Registre decisoes abertas.

## Checklist

- [ ] Organizacao feature-first foi aplicada.
- [ ] Componentes de pagina apenas orquestram.
- [ ] Componentes de feature contem UI de dominio.
- [ ] Componentes compartilhados so existem com reuso real.
- [ ] Hooks complexos usam pasta propria.
- [ ] API fica em service ou query hook, nao em JSX.
- [ ] Estado de servidor usa TanStack Query quando aplicavel.
- [ ] Zustand so aparece se houver estado de cliente compartilhado.

## Exemplos

### Hook complexo

```txt
use-example-feature/
├── index.ts
├── use-example-feature.ts
├── use-example-feature.types.ts
└── use-example-feature.test.ts
```

### Separacao esperada

- Pagina: compoe layout e chama hooks.
- Feature component: exibe regra visual de dominio.
- Service: conversa com API.
- Schema: valida payload e formulario.

## Anti-patterns

- Criar `components/shared` como destino padrao.
- Colocar logica de dominio em `pages`.
- Criar store global para estado local.
- Usar `any` em contratos de props.
