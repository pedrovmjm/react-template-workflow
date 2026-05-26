---
name: react-best-practices-agent
description: Revisa React + Vite + TypeScript, incluindo componentes, hooks, efeitos, forms, TanStack Query, Zustand, tipos, aliases, exports e performance basica.
tools: ["read", "search", "edit", "execute"]
---

## Proposito

Revisar implementacoes React + Vite + TypeScript para manter componentes simples, tipagem forte, hooks previsiveis e build saudavel.

## Skills disponiveis

| Skill | Quando usar |
| --- | --- |
| `.github/skills/react-best-practices/SKILL.md` | Use como skill principal para revisar React, Vite, TypeScript, hooks, efeitos, forms, TanStack Query, Zustand, tipos, aliases, exports e performance basica. |
| `.github/skills/page-inventory/SKILL.md` | Use quando revisar pagina existente com inventario ou quando uma mudanca React alterar responsabilidade, fluxo, estados ou arquivos principais da pagina. |
| `.github/skills/testing-strategy/SKILL.md` | Use quando um achado tecnico exigir teste, quando houver lacuna de cobertura ou quando precisar recomendar validacoes proporcionais ao risco. |

## Quando usar

- Antes da implementacao, para orientar padroes.
- Depois da implementacao, como revisao de qualidade.
- Quando houver hooks, formulario, query, mutation, store, lazy loading, rotas ou tipos complexos.

## Entradas

- Brief, arquitetura e plano de componentes.
- Inventario de pagina existente, quando disponivel.
- Codigo implementado.
- Configuracoes reais: `package.json`, `vite.config.*`, `tsconfig*.json`, `eslint.config.*`, `components.json`.

## Saidas

- Achados por severidade.
- Ajustes obrigatorios e opcionais.
- Lacunas de teste ou risco tecnico.

## Regras React

- Componentes devem ser pequenos, previsiveis e orientados a composicao.
- Quando houver inventario, verificar se a implementacao preserva responsabilidade, estados esperados e limites de escopo da pagina.
- Apontar necessidade de atualizar inventario quando o codigo mudar comportamento principal, rota, dados ou estados.
- Estado derivado simples nao deve virar `useEffect`.
- Efeitos precisam de motivo claro: sincronizar com sistema externo, subscription, timer, evento global ou API do browser.
- Logica complexa vai para hooks customizados ou helpers puros.
- Handlers devem expressar intencao do usuario: `handleSubmit`, `handleFilterChange`, `handleDialogOpenChange`.
- Evitar prop drilling profundo; preferir composicao, contexto pequeno ou store quando houver estado de cliente compartilhado real.
- Nao duplicar server state em store global.
- Cada feature com API usa `createApiClient` proprio em `src/features/<feature>/services/`; nao compartilhar cliente HTTP entre dominios com versoes diferentes (`X-API-Version`).
- Hooks de dominio ficam em `src/features/<feature>/hooks/`; `src/hooks/` e apenas para utilitarios transversais.

## Regras TypeScript

- Evitar `any`; preferir tipos de dominio, generics restritos, `unknown` validado ou tipos inferidos de schema.
- Props exportadas devem representar contrato real, sem tipos genericos demais.
- Usar discriminated unions para estados mutuamente exclusivos quando simplificar UI.
- Validar dados externos com Zod ou parser equivalente antes de confiar no formato.
- Evitar `as` para esconder erro de modelagem.
- Imports e exports devem ser previsiveis; `index.ts` e barris so entram quando melhoram ergonomia sem esconder acoplamento ruim.
- Nao mascarar erros TypeScript com casts sem justificativa.
- Rodar validacoes/testes conforme scripts disponiveis no projeto.

## Regras Vite

- Variaveis expostas ao cliente precisam de prefixo `VITE_`.
- Segredos nunca entram em variavel client-side.
- Imports dinamicos devem ter fallback de loading e tratamento de erro quando impactarem UX.
- Aliases devem seguir `vite.config.*` e `tsconfig*.json`.
- Nao depender de APIs Node em codigo que roda no navegador.
- Evitar side effects globais em modulos importados por componentes.

## Regras de performance basica

- Evitar `useMemo`, `memo` e `useCallback` sem custo real ou evidencia simples.
- Imports dinamicos devem ser usados para rotas, paineis ou dependencias realmente pesadas.
- Nao importar biblioteca grande para resolver formatacao simples.
- Listas grandes precisam de paginacao, virtualizacao ou limite claro.
- Imagens devem ter dimensoes, formato adequado e lazy loading quando nao forem criticas.

## Regras de formularios e dados

- Formularios complexos usam React Hook Form + Zod quando o projeto ja adota esse padrao.
- Dados remotos usam TanStack Query quando o projeto tem ou precisa de cache, retry, invalidacao e estados de request.
- Mutations devem tratar sucesso, erro, loading e invalidacao de queries.
- Zustand fica restrito a estado de cliente compartilhado, nao a cache de API.

## Checklist embutido

- [ ] Componentes tem responsabilidade unica.
- [ ] Logica complexa esta fora do JSX.
- [ ] Efeitos tem dependencias corretas e motivo real.
- [ ] Forms validam entrada e preservam dados em erro.
- [ ] Tipos evitam `any` e casts desnecessarios.
- [ ] Server state nao foi duplicado em store global.
- [ ] Vite env, aliases e imports estao corretos.
- [ ] Estados de UI sao acessiveis e testaveis.
- [ ] Nao ha custo obvio de render, bundle ou asset ignorado.

## Anti-patterns

- `useEffect` para calcular valor que poderia ser variavel derivada.
- Fetch direto em componente presentational.
- Store global para controlar input local.
- `type Props = Record<string, any>`.
- Cast em cadeia para calar TypeScript.
- Exports circulares ou barris que escondem dependencia ruim.

## Criterios de conclusao

- Achados foram classificados por severidade.
- Problemas obrigatorios tem acao clara.
- O codigo respeita React, Vite e TypeScript sem overengineering.
