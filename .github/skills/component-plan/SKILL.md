---
name: component-plan
description: Planeja arquitetura frontend, rotas/URL, componentes React, contratos de props, estado, fluxo de dados, hooks, services e arvore de arquivos antes da implementacao. Use depois do brief e antes de alterar componentes.
---

# Skill: component-plan

## Nome

component-plan

## Proposito

Planejar arquitetura, rotas/URL, componentes, contratos de props, estado, fluxo de dados e estrutura de arquivos antes da implementacao.

## Quando usar

- Depois do brief.
- Antes de criar ou alterar componentes.
- Quando houver duvida sobre `pages`, `features`, `components`, `services`, `hooks`, `store`, `schemas`, `types` ou `utils`.
- Quando a feature criar pagina, mudar endereco, usar path params, query string, filtros compartilhaveis ou navegacao.

## Entradas

- Brief da feature.
- Estrutura atual do projeto.
- Componentes existentes.
- Regras shadcn em `.github/skills/shadcn`, quando a feature envolver UI shadcn.

## Saidas

- Plano de componentes e arquitetura.
- Plano de rotas, URL, path params, query string e navegacao.
- Arvore de arquivos proposta.
- Contratos de props, estado e dados.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/component-plan.template.md` | Use quando precisar entregar um plano de componentes completo e consistente antes da implementacao. | Modelo de saida para arvore de arquivos, componentes, contratos de props, eventos, dono de estado, dados, hooks, services e decisoes abertas. |

## Procedimento

1. Identifique rotas e paginas afetadas.
2. Defina path, path params, query string e comportamento de navegacao.
3. Defina se a logica pertence a feature, pagina, service, hook ou store.
4. Separe componentes de pagina, feature e compartilhados.
5. Defina props e eventos.
6. Defina dono do estado.
7. Defina hooks e services necessarios.
8. Planeje a arvore de arquivos.
9. Registre decisoes abertas.

## Checklist

- [ ] Organizacao feature-first foi aplicada.
- [ ] Rotas/URL foram planejadas quando houver pagina navegavel.
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
- `config.ts` da feature: `apiVersion` e `baseUrl` (com fallback em `appEnv`).
- Service: conversa com API via cliente da feature (`createApiClient`), nunca cliente global compartilhado.
- Hooks da feature: em `src/features/<feature>/hooks/` (dominio); `src/hooks/` so para transversal.
- Schema: valida payload e formulario.

### Cliente API por feature

```txt
src/lib/api/create-api-client.ts   # factory compartilhada
src/features/pedidos/config.ts     # apiVersion, baseUrl
src/features/pedidos/services/api-client.ts
src/features/pedidos/hooks/        # useQuery, usePedidos, etc.
```

## Anti-patterns

- Criar `components/shared` como destino padrao.
- Colocar logica de dominio em `pages`.
- Criar pagina sem rota/URL clara.
- Persistir em store aquilo que deve estar em path/query para refresh, compartilhamento ou historico.
- Criar store global para estado local.
- Usar `any` em contratos de props.
