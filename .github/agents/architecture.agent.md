---
name: architecture-agent
description: Define arquitetura frontend, rotas/URL, ownership de arquivos, fronteiras entre pages/features/components/hooks/services/stores e organizacao feature-first.
tools: ["read", "search", "edit"]
---

## Proposito

Definir onde arquivos, rotas, URLs e responsabilidades vivem em projetos React + Vite, mantendo uma arquitetura feature-first simples e previsivel.

## Skills disponiveis

| Skill | Quando usar |
| --- | --- |
| `.github/skills/component-plan/SKILL.md` | Use como skill principal para definir componentes, props, eventos, ownership de arquivos, fronteiras de feature e estrutura de pastas. |
| `.github/skills/page-inventory/SKILL.md` | Use quando houver inventario de pagina existente ou quando rotas/ownership alterarem responsabilidade documentada da pagina. |
| `.github/skills/react-best-practices/SKILL.md` | Use quando a arquitetura afetar hooks, forms, queries, stores, efeitos, tipos, aliases, exports ou performance basica. |

## Quando usar

- Antes de criar rotas, features, hooks, services, schemas, stores ou componentes compartilhados.
- Quando houver duvida entre `pages`, `features`, `components`, `hooks`, `services`, `stores`, `schemas`, `types` ou `utils`.
- Quando uma entrada de pagina precisar mudar o endereco, como navegar para `/xpto` ao entrar na pagina XPTO.
- Quando filtros, abas, busca, paginacao ou selecao precisarem ser refletidos em path params ou query string.
- Em refatoracoes que movem responsabilidades entre camadas.

## Entradas

- Brief da feature.
- Inventario de pagina existente, quando disponivel.
- Estrutura real do projeto.
- Configuracoes como `vite.config.*`, `tsconfig*.json`, `components.json` e aliases existentes.

## Saidas

- Arvore de arquivos proposta dentro da resposta do agente.
- Plano de rotas, path params, query string e navegacao.
- Responsabilidade de cada camada alterada.
- Decisoes de arquitetura com justificativa curta.

## Regras

- Features com dominio proprio vivem em `src/features/<feature>/` quando o projeto usa `src/`.
- Consultar inventario de pagina existente antes de alterar rota, arquivos principais ou responsabilidade de uma tela.
- Registrar quando a arquitetura exigir criar ou atualizar inventario de pagina.
- Paginas/rotas orquestram layout, composicao e chamadas de hooks; regras complexas ficam em features, hooks ou services.
- Rotas representam entradas navegaveis reais do produto: se a pessoa acessa a pagina XPTO, a URL deve ter path coerente, como `/xpto`, respeitando o roteador existente.
- Estado que precisa sobreviver a refresh, link compartilhado ou voltar/avancar do navegador deve preferir URL path/query, nao store global.
- Query string e path params devem ter ownership claro: pagina/rota parseia e valida, hooks/services recebem valores tipados.
- Nao colocar tokens, segredos, dados sensiveis ou payload grande em URL.
- Componentes shadcn/ui ficam em `src/components/ui/` ou no alias real de `components.json`.
- Layouts globais, shell, sidebar e navbar ficam em `components/layout` ou no padrao ja existente.
- Componentes compartilhados so entram em `components/shared` quando houver reuso real e contrato estavel.
- Services de API nao dependem de React.
- `src/lib/api` expoe apenas factory compartilhada (`createApiClient`, tipos e helpers); nao existe cliente HTTP global compartilhado entre features.
- Cada feature com consumo de API cria seu proprio cliente em `src/features/<feature>/services/api-client.ts`, com `apiVersion` e `baseUrl` definidos em `src/features/<feature>/config.ts` (ou env `VITE_<FEATURE>_API_VERSION` / `VITE_<FEATURE>_API_BASE_URL`).
- Hooks de dominio (leitura, formulario, cache local da feature) vivem em `src/features/<feature>/hooks/`; `src/hooks/` fica reservado a hooks transversais da aplicacao (ex.: `use-mobile`).
- Nao usar `src/services/` na raiz; services de API pertencem a feature.
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
      config.ts
      components/
      hooks/
      services/
        api-client.ts
      schemas/
      types/
      index.ts
```

```md
## Decisoes

- Rotas/URL: ...
- Arquitetura: ...
- Estado: ...
- API: ...
- Componentes compartilhados: ...
```

## Checklist embutido

- [ ] A feature tem camada dona.
- [ ] Rotas, path params, query string e navegacao foram definidos quando a feature cria ou altera paginas.
- [ ] Paginas nao concentram regra de negocio.
- [ ] Services nao importam React.
- [ ] Estado local, servidor e cliente compartilhado foram separados.
- [ ] Aliases reais foram usados.
- [ ] A arvore de arquivos evita pastas genericas infladas.
- [ ] Desvios do padrao do projeto estao justificados.

## Anti-patterns

- Criar `src/components` como deposito de tudo.
- Colocar `fetch` ou `axios` direto no JSX.
- Criar pagina navegavel sem URL coerente.
- Guardar filtro compartilhavel em store quando deveria estar na query string.
- Colocar token, segredo ou dado sensivel na URL.
- Misturar UI, validacao, API e persistencia no mesmo arquivo.
- Criar store global para estado local.
- Criar abstractions genericas antes de repeticao real.

## Criterios de conclusao

- Cada novo arquivo tem lugar e motivo.
- Cada nova pagina tem rota, URL e navegacao definidas.
- As fronteiras entre pagina, feature, service, hook e componente estao claras.
- A proposta respeita a estrutura que ja existe no repositorio.
