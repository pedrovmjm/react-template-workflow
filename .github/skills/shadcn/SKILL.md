---
name: shadcn
description: Gerencia componentes e projetos shadcn — adicionando, pesquisando, corrigindo, depurando, estilizando e compondo UI. Fornece contexto do projeto, documentação de componentes e exemplos de uso. Aplica-se ao trabalhar com shadcn/ui, registros de componentes, presets, códigos --preset ou qualquer projeto com um arquivo components.json. Também é acionado por "shadcn init", "create an app with --preset" ou "switch to --preset".
---

# shadcn/ui

Um framework para criar UI, componentes e design systems. Os componentes são adicionados como código-fonte ao projeto do usuário via CLI.

> **IMPORTANTE:** Execute todos os comandos da CLI usando o executor de pacotes do projeto: `npx shadcn@latest`, `pnpm dlx shadcn@latest` ou `bunx --bun shadcn@latest`, conforme o `packageManager` do projeto. Os exemplos abaixo usam `npx shadcn@latest`; substitua pelo executor correto quando necessario.

## Contexto Atual do Projeto

```json
!`npx shadcn@latest info --json`
```

O JSON acima contém a configuração do projeto e os componentes instalados. Use `npx shadcn@latest docs <component>` para obter documentação e URLs de exemplos de qualquer componente.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `cli.md` | Use ao executar ou orientar comandos `init`, `add`, `diff`, `docs`, `view`, `search`, `preset`, `info` ou ao lidar com templates/presets da CLI. | Referencia de comandos, flags, templates suportados, presets, saidas e fluxo operacional da CLI shadcn. |
| `customization.md` | Use quando a tarefa envolver tema, variaveis CSS, tokens, fontes, radius, cores, Tailwind ou extensao de componentes. | Guia para customizar shadcn sem quebrar tokens semanticos e variaveis do projeto. |
| `rules/styling.md` | Use em qualquer revisao de classes Tailwind, variantes, tokens, `className`, spacing, sizing, truncamento, dark mode, `cn()` ou z-index. | Regras de estilização com exemplos Incorreto/Correto. |
| `rules/forms.md` | Use quando houver formulario, input, textarea, select, checkbox, radio, switch, slider, validacao ou estado disabled/invalid. | Regras de composicao de formularios com `FieldGroup`, `Field`, `InputGroup`, labels e validacao acessivel. |
| `rules/composition.md` | Use quando houver Card, Dialog, Sheet, Drawer, Tabs, Avatar, Empty, Alert, Skeleton, Badge, Toast, grupos ou overlays. | Regras de composicao correta dos componentes shadcn/ui e seus subcomponentes. |
| `rules/base-vs-radix.md` | Use quando precisar decidir entre APIs `asChild` e `render`, ou quando o campo `base` do projeto afetar Select, ToggleGroup, Slider ou Accordion. | Diferencas operacionais entre componentes base e Radix. |
| `rules/icons.md` | Use quando houver icones em botoes, acoes iconicas, `data-icon`, tamanho de icone ou biblioteca configurada em `iconLibrary`. | Regras para iconografia consistente e acessivel dentro de componentes shadcn. |
| `rules/react-vite-typescript.md` | Use quando a composicao shadcn cruzar com React, Vite, TypeScript, TanStack Query, Zustand, lucide ou variaveis `VITE_`. | Regras tecnicas para integrar shadcn em projetos React + Vite + TypeScript. |
| `assets/shadcn.png` e `assets/shadcn-small.png` | Use somente quando a resposta ou documentacao precisar de imagem da skill ou referencia visual de marca. | Assets visuais da skill, nao sao fonte de regra tecnica. |
| `evals/evals.json` | Use apenas para manutencao/avaliacao da propria skill. | Casos de avaliacao da skill; nao deve orientar implementacao normal de produto. |

## Princípios

1. **Use componentes existentes primeiro.** Use `npx shadcn@latest search` para verificar registros antes de escrever UI customizada. Verifique tambem registros da comunidade.
2. **Componha, nao reinvente.** Pagina de configuracoes = Tabs + Card + controles de formulario. Dashboard = Sidebar + Card + Chart + Table.
3. **Use variantes embutidas antes de estilos customizados.** `variant="outline"`, `size="sm"`, etc.
4. **Use cores semanticas.** `bg-primary`, `text-muted-foreground`; nunca valores brutos como `bg-blue-500`.

## Regras Críticas

Estas regras são **sempre aplicadas**. Cada uma aponta para um arquivo com pares de código Incorreto/Correto.

### Estilização e Tailwind → [styling.md](./rules/styling.md)

- **`className` para layout, nao para estilização.** Nunca sobrescreva cores ou tipografia de componentes.
- **Sem `space-x-*` ou `space-y-*`.** Use `flex` com `gap-*`. Para pilhas verticais, `flex flex-col gap-*`.
- **Use `size-*` quando largura e altura forem iguais.** `size-10`, nao `w-10 h-10`.
- **Use o atalho `truncate`.** Nao use `overflow-hidden text-ellipsis whitespace-nowrap`.
- **Sem `dark:` overrides de cor.** Use tokens semânticos (`bg-background`, `text-muted-foreground`).
- **Use `cn()` para classes condicionais.** Nao escreva ternarios manuais em template literals.
- **Sem `z-index` manual em componentes de overlay.** Dialog, Sheet, Popover, etc. gerenciam seu próprio empilhamento.

### Formulários e Inputs → [forms.md](./rules/forms.md)

- **Formularios usam `FieldGroup` + `Field`.** Nunca use `div` bruto com `space-y-*` ou `grid gap-*` para layout de formulario.
- **`InputGroup` usa `InputGroupInput`/`InputGroupTextarea`.** Nunca coloque `Input`/`Textarea` bruto dentro de `InputGroup`.
- **Botoes dentro de inputs usam `InputGroup` + `InputGroupAddon`.**
- **Conjuntos de opcoes (2 a 7 opcoes) usam `ToggleGroup`.** Nao itere `Button` com estado ativo manual.
- **`FieldSet` + `FieldLegend` agrupam checkboxes/radios.** Nao use uma `div` com heading.
- **Validacao usa `data-invalid` + `aria-invalid`.** `data-invalid` fica no `Field`; `aria-invalid` fica no controle. Para desabilitado: `data-disabled` no `Field` e `disabled` no controle.

### Estrutura de Componentes → [composition.md](./rules/composition.md)

- **Itens sempre ficam dentro do grupo correto.** `SelectItem` → `SelectGroup`. `DropdownMenuItem` → `DropdownMenuGroup`. `CommandItem` → `CommandGroup`.
- **Use `asChild` (radix) ou `render` (base) para triggers customizados.** Verifique o campo `base` em `npx shadcn@latest info`. → [base-vs-radix.md](./rules/base-vs-radix.md)
- **Dialog, Sheet e Drawer sempre precisam de titulo.** `DialogTitle`, `SheetTitle`, `DrawerTitle` sao obrigatorios para acessibilidade. Use `className="sr-only"` se estiver visualmente oculto.
- **Use a composicao completa de Card.** `CardHeader`/`CardTitle`/`CardDescription`/`CardContent`/`CardFooter`. Nao despeje tudo em `CardContent`.
- **Button nao tem `isPending`/`isLoading`.** Componha com `Spinner` + `data-icon` + `disabled`.
- **`TabsTrigger` deve ficar dentro de `TabsList`.** Nunca renderize triggers diretamente em `Tabs`.
- **`Avatar` sempre precisa de `AvatarFallback`.** Para quando a imagem falhar ao carregar.

### Use Componentes, Nao Markup Customizado → [composition.md](./rules/composition.md)

- **Use componentes existentes antes de markup customizado.** Verifique se ja existe um componente antes de escrever uma `div` estilizada.
- **Callouts usam `Alert`.** Nao crie `div` estilizada.
- **Estados vazios usam `Empty`.** Nao crie markup customizado para empty state.
- **Toast via `sonner`.** Use `toast()` de `sonner`.
- **Use `Separator`** em vez de `<hr>` ou `<div className="border-t">`.
- **Use `Skeleton`** para placeholders de carregamento. Nao crie `div` customizada com `animate-pulse`.
- **Use `Badge`** em vez de `span` estilizado manualmente.

### Ícones → [icons.md](./rules/icons.md)

- **Icones em `Button` usam `data-icon`.** Use `data-icon="inline-start"` ou `data-icon="inline-end"` no icone.
- **Sem classes de tamanho em icones dentro de componentes.** Os componentes controlam o tamanho via CSS. Nao use `size-4` nem `w-4 h-4`.
- **Passe icones como componentes, nao como chaves string.** `icon={CheckIcon}`, nao lookup por string.

### React + Vite + TypeScript + lucide → [react-vite-typescript.md](./rules/react-vite-typescript.md)

- **Vite:** variaveis expostas ao cliente usam `VITE_`; segredos nunca entram no bundle.
- **TypeScript:** evite `any`, casts para esconder erro e contratos de props genericos demais.
- **React:** evite `useEffect` para estado derivado simples; use hooks para comportamento reutilizavel.
- **lucide:** quando `iconLibrary` for `lucide`, importe de `lucide-react` e use `data-icon` em botoes shadcn.

### CLI

- **Nunca decodifique preset codes nem monte URLs de preset manualmente.** Use `npx shadcn@latest preset decode <code>`, `preset url <code>` ou `preset open <code>`. Para detectar preset no contexto do projeto, use `npx shadcn@latest preset resolve`.
- **Aplique codigos de preset diretamente com a CLI.** Use `npx shadcn@latest apply <code>` para projetos existentes ou `npx shadcn@latest init --preset <code>` ao inicializar.

## Padrões Principais

Estes sao os padroes mais comuns para diferenciar codigo shadcn/ui correto. Para casos de borda, consulte os arquivos de regras vinculados acima.

```tsx
// Layout de formulario: FieldGroup + Field, nao div + Label.
<FieldGroup>
  <Field>
    <FieldLabel htmlFor="email">Email</FieldLabel>
    <Input id="email" />
  </Field>
</FieldGroup>

// Validacao: data-invalid no Field, aria-invalid no controle.
<Field data-invalid>
  <FieldLabel>Email</FieldLabel>
  <Input aria-invalid />
  <FieldDescription>Email invalido.</FieldDescription>
</Field>

// Icones em botoes: data-icon, sem classes de tamanho.
<Button>
  <SearchIcon data-icon="inline-start" />
  Pesquisar
</Button>

// Espacamento: gap-*, nao space-y-*.
<div className="flex flex-col gap-4">  // correto
<div className="space-y-4">           // errado

// Dimensoes iguais: size-*, nao w-* h-*.
<Avatar className="size-10">   // correto
<Avatar className="w-10 h-10"> // errado

// Cores de status: variantes de Badge ou tokens semanticos, nao cores brutas.
<Badge variant="secondary">+20.1%</Badge>    // correto
<span className="text-emerald-600">+20.1%</span> // errado
```

## Seleção de Componentes

| Necessidade                       | Use                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Botao/acao              | `Button` com a variante apropriada                                                                   |
| Inputs de formulario                | `Input`, `Select`, `Combobox`, `Switch`, `Checkbox`, `RadioGroup`, `Textarea`, `InputOTP`, `Slider` |
| Alternar entre 2 a 5 opcoes | `ToggleGroup` + `ToggleGroupItem`                                                                   |
| Exibicao de dados               | `Table`, `Card`, `Badge`, `Avatar`                                                                  |
| Navegacao                 | `Sidebar`, `NavigationMenu`, `Breadcrumb`, `Tabs`, `Pagination`                                     |
| Overlays                   | `Dialog` (modal), `Sheet` (side panel), `Drawer` (bottom sheet), `AlertDialog` (confirmation)       |
| Feedback                   | `sonner` (toast), `Alert`, `Progress`, `Skeleton`, `Spinner`                                        |
| Paleta de comandos            | `Command` dentro de `Dialog`                                                                           |
| Graficos                     | `Chart` (encapsula Recharts)                                                                        |
| Layout                     | `Card`, `Separator`, `Resizable`, `ScrollArea`, `Accordion`, `Collapsible`                          |
| Estados vazios               | `Empty`                                                                                             |
| Menus                      | `DropdownMenu`, `ContextMenu`, `Menubar`                                                            |
| Tooltips/info              | `Tooltip`, `HoverCard`, `Popover`                                                                   |

## Campos Principais

O contexto de projeto injetado contém estes campos principais:

- **`aliases`** → use o prefixo de alias real para imports (e.g. `@/`, `~/`), nunca fixe no código.
- **`isRSC`** → quando `true`, componentes que usam `useState`, `useEffect`, event handlers ou APIs do navegador precisam de `"use client"` no topo do arquivo. Sempre consulte este campo ao orientar sobre a diretiva.
- **`tailwindVersion`** → `"v4"` usa blocos `@theme inline`; `"v3"` usa `tailwind.config.js`.
- **`tailwindCssFile`** → arquivo CSS global onde variaveis CSS customizadas sao definidas. Sempre edite este arquivo, nunca crie um novo.
- **`style`** → tratamento visual do componente (e.g. `nova`, `vega`).
- **`base`** → biblioteca primitiva (`radix` ou `base`). Afeta APIs de componentes e props disponiveis.
- **`iconLibrary`** → determina imports de icones. Use `lucide-react` para `lucide`, `@tabler/icons-react` para `tabler`, etc. Nunca assuma `lucide-react`.
- **`resolvedPaths`** → destinos exatos no sistema de arquivos para componentes, utils, hooks, etc.
- **`framework`** → convencoes de roteamento e arquivos (por exemplo, Next.js App Router vs Vite SPA).
- **`packageManager`** → use isto para instalacoes de dependencias nao shadcn (por exemplo, `pnpm add date-fns` vs `npm install date-fns`).
- **`preset`** → codigo e valores do preset resolvido para o projeto atual. Use `npx shadcn@latest preset resolve --json` quando precisar apenas de informacoes do preset.

Veja [cli.md — comando `info`](./cli.md) para a referencia completa de campos.

## Documentação, Exemplos e Uso de Componentes

Execute `npx shadcn@latest docs <component>` para obter as URLs da documentação, exemplos e referência de API de um componente. Busque essas URLs para obter o conteúdo real.

```bash
npx shadcn@latest docs button dialog select
```

**Ao criar, corrigir, depurar ou usar um componente, sempre execute `npx shadcn@latest docs` e busque as URLs primeiro.** Isso garante que você trabalhe com a API correta e padrões de uso corretos, em vez de adivinhar.

## Fluxo de Trabalho

1. **Obter contexto do projeto** — ja injetado acima. Execute `npx shadcn@latest info` novamente se precisar atualizar.
2. **Verifique os componentes instalados primeiro** — antes de executar `add`, sempre verifique a lista `components` do contexto do projeto ou liste o diretorio `resolvedPaths.ui`. Nao importe componentes que ainda nao foram adicionados e nao adicione novamente os que ja estao instalados.
3. **Encontrar componentes** — `npx shadcn@latest search`.
4. **Obter documentacao e exemplos** — execute `npx shadcn@latest docs <component>` para obter URLs, depois busque-as. Use `npx shadcn@latest view` para navegar por itens de registro que voce ainda nao instalou. Para pre-visualizar alteracoes em componentes instalados, use `npx shadcn@latest add --diff`.
5. **Instalar ou atualizar** — `npx shadcn@latest add`. Ao atualizar componentes existentes, use `--dry-run` e `--diff` para pre-visualizar as alteracoes primeiro (veja [Atualizando Componentes](#atualizando-componentes)).
6. **Corrigir imports em componentes de terceiros** — Depois de adicionar componentes de registros da comunidade (por exemplo, `@bundui`, `@magicui`), verifique os arquivos adicionados nao UI em busca de caminhos de import fixos como `@/components/ui/...`. Eles nao corresponderao aos aliases reais do projeto. Use `npx shadcn@latest info` para obter o alias `ui` correto (por exemplo, `@workspace/ui/components`) e reescreva os imports conforme necessario. A CLI reescreve imports para seus proprios arquivos de UI, mas componentes de registros de terceiros podem usar caminhos padrao que nao correspondem ao projeto.
7. **Revisar componentes adicionados** — Depois de adicionar um componente ou bloco de qualquer registro, **sempre leia os arquivos adicionados e verifique se estao corretos**. Procure subcomponentes ausentes (por exemplo, `SelectItem` sem `SelectGroup`), imports ausentes, composicao incorreta ou violacoes das [Regras Criticas](#regras-criticas). Substitua imports de icones pela `iconLibrary` do contexto do projeto quando necessario. Corrija todos os problemas antes de prosseguir.
8. **O registro deve ser explicito** — Quando o usuario pedir para adicionar um bloco ou componente, **nao adivinhe o registro**. Se nenhum registro for especificado (por exemplo, se o usuario disser "adicione um bloco de login" sem especificar `@shadcn`, `@tailark` etc.), pergunte qual registro usar. Nunca escolha um registro padrao em nome do usuario.
9. **Trocando presets** — Pergunte primeiro ao usuario: **sobrescrever**, **parcial**, **mesclar** ou **pular**?
   - **Inspecionar preset atual**: `npx shadcn@latest preset resolve`. Use `--json` quando precisar de valores estruturados.
   - **Inspecionar preset recebido**: `npx shadcn@latest preset decode <code>`. Use `preset url <code>` ou `preset open <code>` para compartilhar ou abrir o preset builder.
   - **Sobrescrever**: `npx shadcn@latest apply <code>`. Sobrescreve componentes detectados, fontes e variaveis CSS.
   - **Parcial**: `npx shadcn@latest apply <code> --only theme,font`. Atualiza apenas as partes selecionadas do preset sem reinstalar componentes de UI. Os valores suportados sao `theme` e `font`; combinacoes separadas por virgula sao permitidas. `icon` nao e suportado intencionalmente, porque alteracoes de icone podem exigir reinstalacao completa dos componentes e transforms.
   - **Mesclar**: `npx shadcn@latest init --preset <code> --force --no-reinstall`; depois execute `npx shadcn@latest info` para listar componentes instalados. Para cada componente instalado, use `--dry-run` e `--diff` para fazer [merge inteligente](#atualizando-componentes) individualmente.
   - **Pular**: `npx shadcn@latest init --preset <code> --force --no-reinstall`. Atualiza apenas configuracao e CSS; deixa os componentes como estao.
   - **Importante**: Sempre execute comandos de preset dentro do diretorio do projeto do usuario. `apply` so funciona em um projeto existente com `components.json`. A CLI preserva automaticamente a base atual (`base` vs `radix`) a partir de `components.json`. Se precisar usar um diretorio temporario (por exemplo, para comparacoes `--dry-run`), passe `--base <current-base>` explicitamente; codigos de preset nao codificam a base.

## Atualizando Componentes

Quando o usuario pedir para atualizar um componente do upstream mantendo alteracoes locais, use `--dry-run` e `--diff` para mesclar de forma inteligente. **NUNCA busque arquivos brutos do GitHub manualmente — sempre use a CLI.**

1. Execute `npx shadcn@latest add <component> --dry-run` para ver todos os arquivos que seriam afetados.
2. Para cada arquivo, execute `npx shadcn@latest add <component> --diff <file>` para ver o que mudou no upstream em comparacao com o local.
3. Decida por arquivo com base no diff:
   - Sem alteracoes locais → seguro sobrescrever.
   - Tem alteracoes locais → leia o arquivo local, analise o diff e aplique atualizacoes do upstream preservando modificacoes locais.
   - Usuario diz "pode atualizar tudo" → use `--overwrite`, mas confirme primeiro.
4. **Nunca use `--overwrite` sem aprovacao explicita do usuario.**

## Referência Rápida

```bash
# Criar um novo projeto.
npx shadcn@latest init --name my-app --preset base-nova
npx shadcn@latest init --name my-app --preset a2r6bw --template vite

# Criar um projeto monorepo.
npx shadcn@latest init --name my-app --preset base-nova --monorepo
npx shadcn@latest init --name my-app --preset base-nova --template next --monorepo

# Inicializar projeto existente.
npx shadcn@latest init --preset base-nova
npx shadcn@latest init --defaults  # atalho: --template=next --preset=nova (estilo base implicito)

# Aplicar um preset a um projeto existente.
npx shadcn@latest apply a2r6bw
npx shadcn@latest apply a2r6bw --only theme
npx shadcn@latest apply a2r6bw --only font
npx shadcn@latest apply a2r6bw --only theme,font

# Inspecionar preset codes e estado de preset do projeto.
npx shadcn@latest preset decode a2r6bw
npx shadcn@latest preset url a2r6bw
npx shadcn@latest preset open a2r6bw
npx shadcn@latest preset resolve
npx shadcn@latest preset resolve --json

# Adicionar componentes.
npx shadcn@latest add button card dialog
npx shadcn@latest add @magicui/shimmer-button
npx shadcn@latest add --all

# Pre-visualizar alteracoes antes de adicionar/atualizar.
npx shadcn@latest add button --dry-run
npx shadcn@latest add button --diff button.tsx
npx shadcn@latest add @acme/form --view button.tsx

# Pesquisar registros.
npx shadcn@latest search @shadcn -q "sidebar"
npx shadcn@latest search @tailark -q "stats"

# Obter documentação de componentes e URLs de exemplos.
npx shadcn@latest docs button dialog select

# Ver detalhes de item do registro (para itens ainda não instalados).
npx shadcn@latest view @shadcn/button
```

**Presets nomeados:** `nova`, `vega`, `maia`, `lyra`, `mira`, `luma`
**Templates:** `next`, `vite`, `start`, `react-router`, `astro` (todos suportam `--monorepo`) e `laravel` (nao suporta monorepo)
**Preset codes:** strings base62 prefixadas por versao (por exemplo, `a2r6bw` ou `b0`), vindas de [ui.shadcn.com](https://ui.shadcn.com).

## Referências Detalhadas

- [rules/forms.md](./rules/forms.md) — FieldGroup, Field, InputGroup, ToggleGroup, FieldSet, estados de validacao
- [rules/composition.md](./rules/composition.md) — Grupos, overlays, Card, Tabs, Avatar, Alert, Empty, Toast, Separator, Skeleton, Badge, carregamento de Button
- [rules/icons.md](./rules/icons.md) — data-icon, tamanho de icones, icones passados como componentes
- [rules/styling.md](./rules/styling.md) — Cores semânticas, variants, className, spacing, size, truncate, dark mode, cn(), z-index
- [rules/base-vs-radix.md](./rules/base-vs-radix.md) — asChild vs render, Select, ToggleGroup, Slider, Accordion
- [rules/react-vite-typescript.md](./rules/react-vite-typescript.md) — React, Vite, TypeScript, TanStack Query, Zustand e lucide
- [cli.md](./cli.md) — Comandos, flags, presets, templates
- [customization.md](./customization.md) — Temas, variáveis CSS, extensão de componentes
