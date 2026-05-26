---
name: react-best-practices
description: Revisa codigo React + TypeScript, componentes, hooks, efeitos, TanStack Query, Zustand, formularios, tipos, organizacao de exports e performance basica. Use apos implementacoes ou quando uma feature introduzir estado, hooks, queries, forms, lazy loading ou renderizacao relevante.
---

# Skill: react-best-practices

## Nome

react-best-practices

## Proposito

Revisar componentes, hooks, estado, efeitos, queries, forms, tipos, exports e performance basica em codigo React + TypeScript.

## Quando usar

- Apos a implementacao.
- Antes da revisao final.
- Quando uma feature introduz hooks, queries, forms, estado compartilhado, lazy loading ou renderizacao relevante.

## Entradas

- Plano de componentes.
- Codigo implementado.
- Testes existentes.
- Regras tecnicas complementares em `.github/skills/shadcn/rules/react-vite-typescript.md`.

## Saidas

- Revisao de boas praticas React.
- Achados por severidade.
- Ajustes obrigatorios e opcionais.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/react-review.template.md` | Use em revisoes tecnicas antes do fechamento ou quando precisar padronizar achados por severidade. | Modelo de saida para achados, impacto, recomendacoes, testes, riscos e conclusao da revisao React/TypeScript. |
| `references/oficiais.md` | Use quando precisar confirmar comportamento atual de React, Vite, TypeScript, TanStack Query, React Hook Form ou Zod. | Referencias oficiais para validar decisoes tecnicas e evitar recomendacoes baseadas em memoria desatualizada. |
| `references/performance.md` | Use quando a mudanca envolver renderizacao custosa, bundle, lazy loading, listas grandes, imagens ou Core Web Vitals. | Guia de performance basica dentro do escopo React, sem criar revisao separada desnecessaria. |

## Procedimento

1. Revise composicao de componentes.
2. Procure estado desnecessario e efeitos sem motivo.
3. Verifique TanStack Query para dados remotos.
4. Verifique Zustand somente para estado de cliente compartilhado.
5. Verifique React Hook Form + Zod em formularios.
6. Revise tipos TypeScript.
7. Revise imports, exports e organizacao.
8. Revise performance basica: renders desnecessarios, imports pesados, imagens, lazy loading e listas grandes.
9. Registre achados por severidade.

## Checklist

- [ ] Componentes tem responsabilidade unica.
- [ ] Logica complexa esta em hooks.
- [ ] Nao ha chamada de API em JSX.
- [ ] Cada feature usa cliente HTTP proprio (`createApiClient` + `config.ts`); versoes de API nao sao compartilhadas entre dominios.
- [ ] Hooks de dominio estao em `src/features/<feature>/hooks/`, nao em `src/hooks/` global.
- [ ] Efeitos tem dependencias corretas.
- [ ] Forms tem validacao.
- [ ] Tipos evitam `any`.
- [ ] Exports sao limpos e previsiveis.
- [ ] Performance basica foi revisada sem criar otimizacao prematura.

## Referencias

- Consulte `references/oficiais.md` quando precisar confirmar comportamento atual de React, Vite, TypeScript, TanStack Query, React Hook Form ou Zod.
- Consulte `references/performance.md` quando a mudanca envolver renderizacao custosa, bundle, lazy loading, listas grandes, imagens ou Core Web Vitals.

## Exemplos

- Use `useQuery` para leitura remota.
- Use `useMutation` para escrita remota.
- Use schema Zod como fonte de validacao de formulario.

## Anti-patterns

- Cliente HTTP global compartilhado entre features com `X-API-Version` diferente.
- Hooks de dominio em `src/hooks/` ou services na raiz `src/services/`.
- Duplicar server state em store global.
- `useEffect` para calcular valor derivado simples.
- Componentes com responsabilidades de API, validacao e layout ao mesmo tempo.
- Exports circulares.
- Criar agente/skill separado de performance quando a revisao React ja cobre o risco comum.
