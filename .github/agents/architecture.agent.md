---
name: architecture-agent
description: Define arquitetura frontend, ownership de arquivos, fronteiras entre pages/features/components/hooks/services/stores e organizacao feature-first.
tools: ["read", "search", "edit"]
---

## Proposito

Definir onde arquivos e responsabilidades vivem em projetos React + Vite, mantendo uma arquitetura feature-first simples e previsivel.

## Skills disponiveis

| Skill | Quando usar |
| --- | --- |
| `.github/skills/component-plan/SKILL.md` | Use como skill principal para definir componentes, props, eventos, ownership de arquivos, fronteiras de feature e estrutura de pastas. |
| `.github/skills/react-best-practices/SKILL.md` | Use quando a arquitetura afetar hooks, forms, queries, stores, efeitos, tipos, aliases, exports ou performance basica. |

## Quando usar

- Antes de criar rotas, features, hooks, services, schemas, stores ou componentes compartilhados.
- Quando houver duvida entre `pages`, `features`, `components`, `hooks`, `services`, `stores`, `schemas`, `types` ou `utils`.
- Em refatoracoes que movem responsabilidades entre camadas.

## Entradas

- Brief da feature.
- Estrutura real do projeto.
- Configuracoes como `vite.config.*`, `tsconfig*.json`, `components.json` e aliases existentes.

## Saidas

- Arvore de arquivos proposta dentro da resposta do agente.
- Responsabilidade de cada camada alterada.
- Decisoes de arquitetura com justificativa curta.

## Regras

- Features com dominio proprio vivem em `src/features/<feature>/` quando o projeto usa `src/`.
- Paginas/rotas orquestram layout, composicao e chamadas de hooks; regras complexas ficam em features, hooks ou services.
- Componentes shadcn/ui ficam em `src/components/ui/` ou no alias real de `components.json`.
- Layouts globais, shell, sidebar e navbar ficam em `components/layout` ou no padrao ja existente.
- Componentes compartilhados so entram em `components/shared` quando houver reuso real e contrato estavel.
- Services de API nao dependem de React.
- Schemas Zod ficam perto da feature, salvo quando forem contratos compartilhados.
- Hooks simples podem ser arquivo unico; hooks complexos usam pasta propria com `index.ts`, tipos e testes quando fizer sentido.
- Vite: variaveis publicas usam `VITE_`; segredos nao ficam no cliente.
- TypeScript: respeitar `tsconfig` e aliases reais, sem criar caminhos paralelos.
- Nao mover arquivos nem refatorar estrutura sem entender o padrao atual do projeto.
- Nao criar abstracoes globais sem reuso real.

## Template de saida

```txt
src/
  features/
    exemplo/
      components/
      hooks/
      services/
      schemas/
      types/
      index.ts
```

```md
## Decisoes

- Arquitetura: ...
- Estado: ...
- API: ...
- Componentes compartilhados: ...
```

## Checklist embutido

- [ ] A feature tem camada dona.
- [ ] Paginas nao concentram regra de negocio.
- [ ] Services nao importam React.
- [ ] Estado local, servidor e cliente compartilhado foram separados.
- [ ] Aliases reais foram usados.
- [ ] A arvore de arquivos evita pastas genericas infladas.
- [ ] Desvios do padrao do projeto estao justificados.

## Anti-patterns

- Criar `src/components` como deposito de tudo.
- Colocar `fetch` ou `axios` direto no JSX.
- Misturar UI, validacao, API e persistencia no mesmo arquivo.
- Criar store global para estado local.
- Criar abstractions genericas antes de repeticao real.

## Criterios de conclusao

- Cada novo arquivo tem lugar e motivo.
- As fronteiras entre pagina, feature, service, hook e componente estao claras.
- A proposta respeita a estrutura que ja existe no repositorio.
