---
name: testing-strategy
description: Define estrategia de testes frontend com Vitest, Testing Library e MSW, cobrindo criterios de aceite, componentes, hooks, formularios, API, acessibilidade, content renderer e riscos principais. Use no planejamento ou apos implementacao.
---

# Skill: testing-strategy

## Nome

testing-strategy

## Proposito

Definir testes uteis para a feature sem excesso de custo, usando Vitest, Testing Library e MSW quando aplicavel.

## Quando usar

- Depois da implementacao ou antes dela, para planejar cobertura.
- Quando houver logica de hook, formulario, API, estado, renderizacao rica ou comportamento responsivo relevante.

## Entradas

- Brief.
- Plano de componentes.
- Revisoes de React e seguranca.
- Codigo implementado.

## Saidas

- Plano de testes.
- Lacunas justificadas.
- Definition of done.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/testing-plan.template.md` | Use ao definir estrategia de testes, DoD, comandos de verificacao ou lacunas aceitas. | Modelo de saida para matriz de testes, criterios cobertos, automacao, QA manual, comandos, gaps e riscos residuais. |
| `references/oficiais.md` | Use quando precisar confirmar APIs ou boas praticas de Vitest, Testing Library, user-event, MSW ou Playwright. | Referencias oficiais para escolher ferramentas, comandos e padroes de teste. |
| `references/exemplos.md` | Use quando precisar de exemplos curtos de componente, hook, MSW, formulario ou E2E. | Exemplos prontos para orientar implementacao de testes sem inventar formato. |

## Procedimento

1. Mapeie criterios de aceite para testes.
2. Defina testes unitarios para helpers e schemas.
3. Defina testes de componentes para interacao.
4. Defina testes de hooks quando houver logica relevante.
5. Defina integracao com MSW quando houver API.
6. Inclua testes de acessibilidade basicos.
7. Inclua testes de content renderer quando aplicavel.
8. Registre definicao de pronto.

## Checklist

- [ ] Criterios de aceite tem teste ou QA manual justificado.
- [ ] Loading, empty, error e success foram considerados.
- [ ] Formularios testam validacao.
- [ ] API usa MSW quando util.
- [ ] Acessibilidade basica foi coberta.
- [ ] Seguranca tem teste quando ha risco concreto.

## Exemplos

- Hook de query: testar loading, sucesso e erro com wrapper de QueryClient.
- Formulario: testar erro Zod e submit valido.
- Renderer: testar HTML perigoso sanitizado.

## Referencias

- Consulte `references/oficiais.md` para Vitest, Testing Library, user-event, MSW e Playwright.
- Consulte `references/exemplos.md` para exemplos curtos de componente, MSW e E2E.

## Anti-patterns

- Snapshot grande como principal protecao.
- Testar detalhes internos irrelevantes.
- Mockar o componente sob teste.
- Ignorar regressoes de erro e vazio.
