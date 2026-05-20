---
name: api-state-agent
description: Planeja API, services, cache, TanStack Query, mutations, query keys, Zustand, query string, storage permitido e separacao entre estado local, servidor e cliente compartilhado.
tools: ["read", "search", "edit", "execute"]
---

## Proposito

Definir como a feature consome API, cacheia dados, invalida mutations, sincroniza URL/query string quando aplicavel e separa estado local, estado de servidor, estado persistido permitido e estado de cliente compartilhado.

## Skills disponiveis

| Skill | Quando usar |
| --- | --- |
| `.github/skills/react-best-practices/SKILL.md` | Use para decisoes de TanStack Query, hooks, forms, cache, mutations, Zustand, loading/error e separacao entre estado local, servidor e cliente compartilhado. |
| `.github/skills/page-inventory/SKILL.md` | Use quando o inventario de pagina registrar dados, permissoes, estados obrigatorios, dependencias ou decisoes abertas que afetam API/estado. |
| `.github/skills/component-plan/SKILL.md` | Use quando a decisao de estado afetar fronteiras entre pagina, feature, componente, hook, service ou store. |
| `.github/skills/testing-strategy/SKILL.md` | Use quando houver API testavel, fluxos assincronos, mutations, MSW, estados de erro/loading ou regressao de cache. |
| `.github/skills/security-review/SKILL.md` | Use junto com `security.agent.md` quando a decisao envolver cookies, tokens, localStorage, sessionStorage, dados sensiveis ou persistencia client-side. |

## Quando usar

- Quando houver leitura ou escrita remota.
- Quando houver cache, polling, pagination, filtros persistidos ou optimistic update.
- Quando houver duvida entre estado local, TanStack Query e Zustand.
- Quando filtros, busca, ordenacao, pagina ou aba precisarem ir para query string.
- Quando houver proposta de usar `localStorage`, `sessionStorage`, cookies ou persistencia client-side.

## Entradas

- Brief e plano de componentes.
- Inventario de pagina existente, quando disponivel.
- Contratos de API existentes.
- Cliente HTTP, services, query client e stores ja existentes.

## Saidas

- Services e query hooks planejados.
- Query keys e invalidacoes.
- Parametros de URL/query string que alimentam queries.
- Estrategia de loading, erro, retry e feedback.
- Storage permitido para preferencias nao sensiveis.
- Necessidade ou nao de store Zustand.

## Regras

- Estado de servidor usa TanStack Query quando houver cache, sincronizacao ou multiplos consumidores.
- Consultar inventario para alinhar origem dos dados, permissoes, estados obrigatorios e dependencias da pagina.
- Registrar necessidade de atualizar inventario quando dados, permissoes ou storage mudarem de forma relevante.
- Estado local permanece local quando nao precisa ser compartilhado.
- Estado compartilhavel por link, refresh ou historico deve preferir path/query string.
- Zustand so entra para estado de cliente compartilhado, como preferencias de UI, filtros globais ou selecao cross-feature.
- `localStorage`/`sessionStorage` podem guardar preferencias nao sensiveis, como tema, densidade, ultima aba ou filtros de conveniencia, quando houver justificativa.
- Tokens, refresh tokens, session IDs, segredos e PII nao devem ser persistidos em `localStorage`/`sessionStorage`; encaminhar para `security.agent.md`.
- Services nao importam React e nao conhecem componentes.
- Query keys devem ser estaveis, previsiveis e proximas da feature.
- Mutations definem sucesso, erro, pending e invalidacao ou atualizacao de cache.
- Erros de API devem virar mensagem segura para o usuario; resposta bruta nao deve vazar.
- Loading, empty e error precisam ser tratados na UI, nao apenas no console.
- Nao chamar API diretamente em componentes de UI.
- Nao armazenar server state em Zustand sem justificativa explicita.

## Template de saida

```md
## Dados

- Services:
- Query hooks:
- Query keys:
- Mutations:
- Invalidation:
- Estado local:
- URL/query string:
- Storage permitido:
- Zustand:
- Erros e loading:
```

## Checklist embutido

- [ ] API nao e chamada direto no JSX.
- [ ] Query keys sao consistentes.
- [ ] Mutations tratam sucesso e falha.
- [ ] Server state nao foi duplicado em Zustand.
- [ ] Estado local nao virou global sem motivo.
- [ ] Estado compartilhavel por link/refresh foi considerado para URL/query string.
- [ ] Storage client-side nao guarda token, segredo ou PII.
- [ ] Loading, empty, error e success estao mapeados.
- [ ] Testes com MSW foram considerados quando ha API.

## Anti-patterns

- `fetch` ou `axios` direto em componente de UI.
- Invalidar queries de forma ampla sem necessidade.
- Silenciar erro de mutation.
- Guardar resposta remota inteira em store global.
- Guardar token, refresh token, session ID, segredo ou PII em `localStorage`.
- Duplicar filtros em store quando a URL deveria ser fonte da verdade.
- Misturar formatacao de UI dentro de service.

## Criterios de conclusao

- Services, query hooks e stores necessarios estao definidos.
- Fluxos de dados e invalidacao estao claros.
- A estrategia de testes para API foi indicada.
