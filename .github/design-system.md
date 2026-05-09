# Design System

Este arquivo e fonte obrigatoria para agentes que criam, alteram ou revisam UI.

## Produto

Padrao base: ferramenta web profissional, clara, eficiente e orientada a tarefas. A UI deve priorizar leitura, densidade controlada, estados previsiveis e acoes obvias.

## Tokens

Use tokens semanticos em vez de cores soltas:

- `background`, `foreground`
- `card`, `card-foreground`
- `popover`, `popover-foreground`
- `primary`, `primary-foreground`
- `secondary`, `secondary-foreground`
- `muted`, `muted-foreground`
- `accent`, `accent-foreground`
- `destructive`, `destructive-foreground`
- `border`, `input`, `ring`

Radius padrao:

- Controles e cards: ate `rounded-md`.
- Evite radius exagerado em dashboards, tabelas, formularios e ferramentas operacionais.

Spacing:

- Use escala Tailwind consistente.
- Em telas operacionais, prefira agrupamento compacto com `gap-2`, `gap-3`, `gap-4`.
- Evite secoes com cara de landing page quando a tarefa pede app, painel, editor ou ferramenta.

Tipografia:

- Headings compactos em paineis, cards, modais e sidebars.
- Hero-scale type apenas em paginas realmente hero.
- Nao use letter spacing negativo.
- Nao escale fonte com viewport width.

## Componentes

Preferencia:

- shadcn/ui para Button, Input, Select, Checkbox, Switch, Tabs, Dialog, Sheet, DropdownMenu, Tooltip, Table, Form, Alert, Badge, Separator e Skeleton.
- Radix quando for necessario comportamento acessivel de baixo nivel.
- lucide para icones de acoes.

Regras:

- Botoes de acao devem ter estado hover, focus-visible, disabled e loading quando a operacao for assincrona.
- Icon buttons devem ter `aria-label` e tooltip quando a acao nao for obvia.
- Formularios devem ter label, erro, descricao quando util e agrupamento visual claro.
- Tabelas devem priorizar leitura, ordenacao/filtro apenas quando a tarefa pedir ou o volume justificar.
- Modais devem ter titulo, descricao util e foco inicial coerente.

## Layout

- O primeiro viewport deve mostrar a experiencia principal quando o pedido for app, ferramenta, dashboard, jogo ou editor.
- Nao use cards dentro de cards.
- Nao transforme secoes de pagina em cards flutuantes sem necessidade.
- Defina dimensoes estaveis para grids, boards, toolbars, tiles e contadores.
- Em mobile, controles importantes devem permanecer acessiveis sem sobrepor conteudo.

## Cores

- Evite paletas dominadas por uma unica familia de cor.
- Evite interfaces inteiras em roxo/azul-roxo, bege/areia, slate/azul escuro ou marrom/laranja.
- Use cores de status somente para status: sucesso, alerta, erro, info.
- Contraste deve atender WCAG AA para texto normal sempre que possivel.

## Movimento

- Animacoes devem ajudar orientacao, feedback ou continuidade.
- Respeite `prefers-reduced-motion`.
- Evite movimento decorativo em ferramentas operacionais.

## Checklist antes de concluir UI

- A tela usa tokens semanticos do projeto.
- Componentes e estados seguem shadcn/ui ou padrao local.
- Nao ha texto sobreposto, truncado sem motivo ou botoes com texto quebrado de forma feia.
- Navegacao por teclado funciona nas interacoes principais.
- Estados vazio, carregando, erro e sucesso existem quando o fluxo depende de dados.
- Desktop e mobile mantem hierarquia, legibilidade e acoes principais.
