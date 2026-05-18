# Repository Instructions

Este repositorio usa um workflow de agentes para frontend React + Vite + TypeScript + shadcn/ui.

## Regra principal de roteamento

Envie o trabalho para o orquestrador quando o pedido envolver implementacao, alteracao de codigo, refatoracao, correcao, criacao de tela, criacao de componente, ajuste visual, teste, revisao tecnica, **briefing**, **planejamento sem edicao** ou qualquer trabalho que passe pelo workflow de agentes:

- `.github/agents/frontend-orchestrator.agent.md`

Briefing e planejamento sem edicao de arquivos tambem passam pelo orquestrador, mas **nao** exigem o workflow completo: o orquestrador deve usar o modo de escopo adequado (por exemplo **Brief-only** para "quero um briefing de uma tela") e acionar somente os especialistas necessarios.

Nao execute skills diretamente a partir destas instrucoes globais. O orquestrador e responsavel por decidir o modo de escopo, quais agentes especialistas acionar e quais skills cada um deve considerar.

## Design system obrigatorio

Toda implementacao ou revisao de UI deve usar:

- `.github/design-system.md`
- `.github/skills/layout-system/SKILL.md`
- `.github/skills/shadcn/SKILL.md`, quando houver shadcn/ui, Radix, Tailwind ou lucide

Nao crie nem altere UI sem consultar o design system. Tokens, componentes, estados, densidade, responsividade, foco, acessibilidade e padroes visuais devem seguir `.github/design-system.md`.

## Papel das skills

Skills em `.github/skills` sao material de apoio para os agentes especialistas. Elas nao sao o ponto de entrada do fluxo.

O ponto de entrada e sempre o `frontend-orchestrator`, que deve:

- coletar contexto real do projeto;
- repassar o trabalho para os agentes corretos;
- indicar quais skills cada agente deve considerar;
- exigir uso do design system quando houver UI;
- consolidar gates, riscos e pendencias.

## Regras de implementacao

Quando o orquestrador encaminhar uma implementacao, o agente implementador deve preservar os padroes existentes do projeto e usar as skills adequadas, especialmente:

- `react-best-practices` para React, Vite, TypeScript, hooks, estado, forms, queries e performance basica;
- `component-plan` para fronteiras, props, eventos e ownership de arquivos;
- `layout-system` para UI, responsividade e design system;
- `shadcn` para componentes shadcn/ui, Radix, Tailwind e lucide;
- `testing-strategy` para testes proporcionais ao risco;
- `frontend-accessibility` quando houver UI interativa, forms, dialogs, menus ou foco.

Ao finalizar uma mudanca, informe quais gates foram executados ou por que algum gate nao foi executado.
