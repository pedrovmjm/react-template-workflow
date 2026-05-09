# shadcn Referência da CLI

A configuração é lida de `components.json`.

> **IMPORTANTE:** Sempre execute comandos usando o executor de pacotes do projeto: `npx shadcn@latest`, `pnpm dlx shadcn@latest` ou `bunx --bun shadcn@latest`. Verifique `packageManager` do contexto do projeto para escolher o correto. Os exemplos abaixo usam `npx shadcn@latest`; substitua pelo executor correto do projeto.

> **IMPORTANTE:** Use apenas as flags documentadas abaixo. Não invente nem adivinhe flags; se uma flag não estiver listada aqui, ela não existe. A CLI detecta automaticamente o gerenciador de pacotes pelo lockfile do projeto; não há flag `--package-manager`.

## Conteúdo

- Comandos: init, apply, add (dry-run, smart merge), search, view, docs, info, build
- Templates: next, vite, start, react-router, astro
- Presets: nomeados, code, URL e campos
- Trocando presets

---

## Comandos

### `init` — Inicializar ou criar um projeto

```bash
npx shadcn@latest init [components...] [options]
```

Inicializa shadcn/ui em um projeto existente ou cria um novo projeto (quando `--name` é fornecido). Opcionalmente instala componentes na mesma etapa.

| Flag                    | Curta | Descrição                                               | Padrão |
| ----------------------- | ----- | --------------------------------------------------------- | ------- |
| `--template <template>` | `-t`  | Template (next, start, vite, next-monorepo, react-router) | —       |
| `--preset [name]`       | `-p`  | Configuracao de preset (nomeado, code ou URL)             | —       |
| `--yes`                 | `-y`  | Pular prompt de confirmacao                               | `true`  |
| `--defaults`            | `-d`  | Usar padrões (`--template=next --preset=base-nova`)       | `false` |
| `--force`               | `-f`  | Forcar sobrescrita da configuracao existente              | `false` |
| `--cwd <cwd>`           | `-c`  | Diretorio de trabalho                                     | current |
| `--name <name>`         | `-n`  | Nome do novo projeto                                      | —       |
| `--silent`              | `-s`  | Mute output                                               | `false` |
| `--rtl`                 |       | Enable RTL support                                        | —       |
| `--reinstall`           |       | Reinstalar componentes de UI existentes                         | `false` |
| `--monorepo`            |       | Criar scaffold de projeto monorepo                        | —       |
| `--no-monorepo`         |       | Pular prompt de monorepo                                  | —       |

`npx shadcn@latest create` e um alias de `npx shadcn@latest init`.

### `apply` — Aplicar um preset a um projeto existente

```bash
npx shadcn@latest apply [preset] [options]
```

Aplica um preset a um projeto existente, sobrescrevendo configuração guiada por preset, fontes, variáveis CSS e componentes de UI detectados.

| Flag                | Curta | Descrição                                | Padrão |
| ------------------- | ----- | ------------------------------------------ | ------- |
| `--preset <preset>` | —     | Configuracao de preset (nomeado, code ou URL) | —       |
| `--yes`             | `-y`  | Pular prompt de confirmacao                   | `false` |
| `--cwd <cwd>`       | `-c`  | Diretorio de trabalho                         | current |
| `--silent`          | `-s`  | Mute output                                | `false` |

`[preset]` é um atalho para `--preset <preset>`. Se ambos forem fornecidos, eles devem corresponder.
Se nenhum preset for fornecido, a CLI oferece abrir o builder de preset customizado em `ui.shadcn.com/create`.

### `add` — Adicionar componentes

> **IMPORTANTE:** Para comparar componentes locais com o upstream ou pre-visualizar alteracoes, SEMPRE use `npx shadcn@latest add <component> --dry-run`, `--diff` ou `--view`. NUNCA busque arquivos brutos do GitHub ou de outras fontes manualmente. A CLI resolve registros, caminhos de arquivo e diffs de CSS automaticamente.

```bash
npx shadcn@latest add [components...] [options]
```

Aceita nomes de componentes, nomes prefixados por registro (`@magicui/shimmer-button`), URLs ou caminhos locais.

| Flag            | Curta | Descrição                                                                                                          | Padrão |
| --------------- | ----- | -------------------------------------------------------------------------------------------------------------------- | ------- |
| `--yes`         | `-y`  | Pular prompt de confirmacao                                                                                          | `false` |
| `--overwrite`   | `-o`  | Sobrescrever arquivos existentes                                                                                     | `false` |
| `--cwd <cwd>`   | `-c`  | Diretorio de trabalho                                                                                                | current |
| `--all`         | `-a`  | Adicionar todos os componentes disponíveis                                                                                         | `false` |
| `--path <path>` | `-p`  | Caminho de destino do componente                                                                                        | —       |
| `--silent`      | `-s`  | Mute output                                                                                                          | `false` |
| `--dry-run`     |       | Pré-visualizar todas as alterações sem gravar arquivos                                                                            | `false` |
| `--diff [path]` |       | Mostra diffs. Sem path, mostra os 5 primeiros arquivos. Com path, mostra apenas esse arquivo (implica `--dry-run`)   | —       |
| `--view [path]` |       | Mostra conteudo. Sem path, mostra os 5 primeiros arquivos. Com path, mostra apenas esse arquivo (implica `--dry-run`) | —       |

#### Modo dry-run

Use `--dry-run` para pre-visualizar o que `add` faria sem gravar arquivos. `--diff` e `--view` ambos implicam `--dry-run`.

```bash
# Pre-visualizar todas as alteracoes.
npx shadcn@latest add button --dry-run

# Mostrar diffs dos arquivos principais (top 5).
npx shadcn@latest add button --diff

# Mostrar o diff de um arquivo especifico.
npx shadcn@latest add button --diff button.tsx

# Mostrar conteudo dos arquivos principais (top 5).
npx shadcn@latest add button --view

# Mostrar o conteudo completo de um arquivo especifico.
npx shadcn@latest add button --view button.tsx

# Também funciona com URLs.
npx shadcn@latest add https://api.npoint.io/abc123 --dry-run

# CSS diffs.
npx shadcn@latest add button --diff globals.css
```

**Quando usar dry-run:**

- Quando o usuário perguntar "quais arquivos isso vai adicionar?" ou "o que isso vai alterar?", use `--dry-run`.
- Antes de sobrescrever componentes existentes, use `--diff` para pré-visualizar as alterações.
- Quando o usuário quiser inspecionar o código-fonte do componente sem instalar, use `--view`.
- Ao verificar quais alterações de CSS seriam feitas em `globals.css`, use `--diff globals.css`.
- Quando o usuário pedir revisão ou auditoria de código de registro de terceiros antes da instalação, use `--view` para inspecionar o código-fonte.

> **`npx shadcn@latest add --dry-run` vs `npx shadcn@latest view`:** Prefira `npx shadcn@latest add --dry-run/--diff/--view` em vez de `npx shadcn@latest view` quando o usuário quiser pré-visualizar alterações no projeto. `npx shadcn@latest view` mostra apenas metadados brutos do registro. `npx shadcn@latest add --dry-run` mostra exatamente o que aconteceria no projeto do usuário: caminhos de arquivos resolvidos, diffs contra arquivos existentes e atualizações de CSS. Use `npx shadcn@latest view` apenas quando o usuário quiser navegar por informações do registro sem contexto do projeto.

#### Mesclar Inteligente do Upstream

Veja [Atualizando Componentes em SKILL.md](./SKILL.md#updating-components) para o fluxo completo.

### `search` — Pesquisar registros

```bash
npx shadcn@latest search <registries...> [options]
```

Pesquisa fuzzy entre registros. Também tem alias `npx shadcn@latest list`. Sem `-q`, lista todos os itens.

| Flag                | Curta | Descrição            | Padrão |
| ------------------- | ----- | ---------------------- | ------- |
| `--query <query>`   | `-q`  | Pesquisar query           | —       |
| `--limit <number>`  | `-l`  | Máx. de itens por registro | `100`   |
| `--offset <number>` | `-o`  | Items to skip          | `0`     |
| `--cwd <cwd>`       | `-c`  | Diretorio de trabalho  | current |

### `view` — Ver detalhes do item

```bash
npx shadcn@latest view <items...> [options]
```

Exibe informações do item, incluindo conteúdo dos arquivos. Exemplo: `npx shadcn@latest view @shadcn/button`.

### `docs` — Obter URLs da documentação de componentes

```bash
npx shadcn@latest docs <components...> [options]
```

Emite URLs resolvidas para documentação, exemplos e referências de API do componente. Aceita um ou mais nomes de componente. Busque as URLs para obter o conteúdo real.

Exemplo de saida para `npx shadcn@latest docs input button`:

```
base  radix

input
  docs      https://ui.shadcn.com/docs/components/radix/input
  examples  https://raw.githubusercontent.com/.../examples/input-example.tsx

button
  docs      https://ui.shadcn.com/docs/components/radix/button
  examples  https://raw.githubusercontent.com/.../examples/button-example.tsx
```

Alguns componentes incluem um link `api` para a biblioteca subjacente (por exemplo, `cmdk` para o componente Command).

### `diff` — Verificar atualizações

Não use este comando. Use `npx shadcn@latest add --diff` em vez disso.

### `info` — Informações do projeto

```bash
npx shadcn@latest info [options]
```

Exibe informações do projeto e a configuração de `components.json`. Execute isto primeiro para descobrir o framework, aliases, versão do Tailwind e caminhos resolvidos do projeto.

| Flag          | Curta | Descrição       | Padrão |
| ------------- | ----- | ----------------- | ------- |
| `--cwd <cwd>` | `-c`  | Diretorio de trabalho | current |

**Campos de Informações do Projeto:**

| Campo                | Tipo      | Significado                                                            |
| -------------------- | --------- | ------------------------------------------------------------------ |
| `framework`          | `string`  | Detected framework (`next`, `vite`, `react-router`, `start`, etc.) |
| `frameworkVersion`   | `string`  | Framework version (e.g. `15.2.4`)                                  |
| `isSrcDir`           | `boolean` | Se o projeto usa diretorio `src/`                                  |
| `isRSC`              | `boolean` | Se React Server Components estao habilitados                       |
| `isTsx`              | `boolean` | Se o projeto usa TypeScript                                        |
| `tailwindVersion`    | `string`  | `"v3"` ou `"v4"`                                                   |
| `tailwindConfigFile` | `string`  | Caminho do arquivo de configuracao Tailwind                        |
| `tailwindCssFile`    | `string`  | Caminho do arquivo CSS global                                      |
| `aliasPrefix`        | `string`  | Import alias prefix (e.g. `@`, `~`, `@/`)                          |
| `packageManager`     | `string`  | Detected package manager (`npm`, `pnpm`, `yarn`, `bun`)            |

**Campos de components.json:**

| Campo                | Tipo      | Significado                                                                                    |
| -------------------- | --------- | ------------------------------------------------------------------------------------------ |
| `base`               | `string`  | Biblioteca primitiva (`radix` ou `base`) — determina APIs de componentes e props disponíveis      |
| `style`              | `string`  | Visual style (e.g. `nova`, `vega`)                                                         |
| `rsc`                | `boolean` | Flag RSC da configuracao                                                                   |
| `tsx`                | `boolean` | TypeScript flag                                                                            |
| `tailwind.config`    | `string`  | Tailwind config path                                                                       |
| `tailwind.css`       | `string`  | Caminho do CSS global; e aqui que variaveis CSS customizadas entram                         |
| `iconLibrary`        | `string`  | Biblioteca de icones; determina o pacote de import (ex.: `lucide-react`)                    |
| `aliases.components` | `string`  | Alias de import de componentes (e.g. `@/components`)                                               |
| `aliases.utils`      | `string`  | Utils import alias (e.g. `@/lib/utils`)                                                    |
| `aliases.ui`         | `string`  | Alias de import de componentes de UI (e.g. `@/components/ui`)                                                |
| `aliases.lib`        | `string`  | Lib alias (e.g. `@/lib`)                                                                   |
| `aliases.hooks`      | `string`  | Hooks alias (e.g. `@/hooks`)                                                               |
| `resolvedPaths`      | `object`  | Caminhos absolutos no sistema de arquivos para cada alias                                  |
| `registries`         | `object`  | Registros customizados configurados                                                               |

**Links fields:**

A saída de `info` inclui uma seção **Links** com URLs em template para documentação, código-fonte e exemplos de componentes. Para URLs resolvidas, use `npx shadcn@latest docs <component>`.

### `build` — Criar um registro customizado

```bash
npx shadcn@latest build [registry] [options]
```

Gera arquivos JSON individuais a partir de `registry.json` para distribuição. Entrada padrão: `./registry.json`; saída padrão: `./public/r`.

| Flag              | Curta | Descrição       | Padrão      |
| ----------------- | ----- | ----------------- | ------------ |
| `--output <path>` | `-o`  | Diretorio de saida     | `./public/r` |
| `--cwd <cwd>`     | `-c`  | Diretorio de trabalho  | current      |

---

## Templates

| Value          | Framework      | Monorepo support |
| -------------- | -------------- | ---------------- |
| `next`         | Next.js        | Yes              |
| `vite`         | Vite           | Yes              |
| `start`        | TanStack Start | Yes              |
| `react-router` | React Router   | Yes              |
| `astro`        | Astro          | Yes              |
| `laravel`      | Laravel        | No               |

Todos os templates suportam scaffold de monorepo via flag `--monorepo`. Quando passada, a CLI usa um diretório de template específico de monorepo (por exemplo, `next-monorepo`, `vite-monorepo`). Quando nem `--monorepo` nem `--no-monorepo` são passados, a CLI pergunta interativamente. Laravel não suporta scaffold de monorepo.

---

## Presets

Three ways to specify a preset via `--preset`:

1. **Nomeado:** `--preset nova` ou `--preset lyra`
2. **Code:** `--preset a2r6bw` (string base62 prefixada por versao, por exemplo `a2r6bw` ou `b0`)
3. **URL:** `--preset "https://ui.shadcn.com/init?base=radix&style=nova&..."`

> **IMPORTANTE:** Nunca tente decodificar, buscar ou resolver preset codes manualmente. Preset codes sao opacos: passe diretamente para `npx shadcn@latest init --preset <code>` e deixe a CLI resolver.
> Use `npx shadcn@latest apply --preset <code>` ao sobrescrever o preset de um projeto existente.

## Trocando Presets

Pergunte primeiro ao usuário: **sobrescrever**, **mesclar** ou **pular** componentes existentes?

- **Sobrescrever / Reinstalar** → `npx shadcn@latest apply --preset <code>`. Sobrescreve todos os arquivos de componentes detectados com os novos estilos do preset. Use quando o usuário não tiver customizado componentes.
- **Mesclar** → `npx shadcn@latest init --preset <code> --force --no-reinstall`, depois execute `npx shadcn@latest info` para obter a lista de componentes instalados e use o [fluxo de merge inteligente](./SKILL.md#atualizando-componentes) para atualiza-los um por um, preservando alteracoes locais. Use quando o usuario tiver customizado componentes.
- **Pular** → `npx shadcn@latest init --preset <code> --force --no-reinstall`. Atualiza apenas configuração e variáveis CSS; deixa os componentes existentes como estão.

Sempre execute comandos de preset dentro do diretorio do projeto do usuario. `apply` so funciona em um projeto existente com `components.json`. A CLI preserva automaticamente a base atual (`base` vs `radix`) a partir de `components.json`. Se precisar usar um diretorio temporario (por exemplo, para comparacoes `--dry-run`), passe `--base <current-base>` explicitamente; codigos de preset nao codificam a base.
