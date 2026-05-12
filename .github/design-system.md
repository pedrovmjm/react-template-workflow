---
version: alpha
name: Galeria Visual
description: |
  Sistema de descoberta visual centrado em fotografia, organizado por CTA primario vermelho, grade masonry de pins e chrome neutro creme que recua para deixar a imagem conduzir a experiencia. A home funciona como uma ferramenta de descoberta com linguagem editorial: manchetes display de 70px, tipografia Inter, botoes pill com raio de 16px, paleta neutra levemente creme e CTA fixo vermelho ancorando a navegacao. As imagens sao o elemento estrutural: pins quadrados, retrato e paisagem se distribuem em uma grade masonry baseada em colunas, com cards de raio 16px e gutters compactos de 8px. O chrome permanece discreto: cinzas quentes, branco real e um unico vermelho saturado, sem gradientes decorativos, fundos atmosfericos ou sombras alem do scrim modal suave.

colors:
  primary: "#e60023"
  on-primary: "#ffffff"
  primary-pressed: "#cc001f"
  ink: "#000000"
  ink-soft: "#211922"
  body: "#33332e"
  charcoal: "#262622"
  mute: "#62625b"
  ash: "#91918c"
  stone: "#c8c8c1"
  hairline: "#dadad3"
  hairline-soft: "#e5e5e0"
  on-secondary: "#000000"
  secondary-bg: "#e5e5e0"
  secondary-pressed: "#c8c8c1"
  canvas: "#ffffff"
  surface-soft: "#fbfbf9"
  surface-card: "#f6f6f3"
  surface-elevated: "#ffffff"
  on-dark: "#ffffff"
  on-dark-mute: "#b3b3b3"
  surface-dark: "#262622"
  focus-outer: "#435ee5"
  focus-inner: "#ffffff"
  accent-pressed-blue: "#617bff"
  accent-purple: "#7e238b"
  accent-purple-deep: "#6845ab"
  success-deep: "#103c25"
  success-pale: "#c7f0da"
  error: "#9e0a0a"
  error-deep: "#cc001f"

typography:
  display-xl:
    fontFamily: Inter
    fontSize: 70px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1.2px
  display-lg:
    fontFamily: Inter
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.8px
  heading-xl:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -1.2px
  heading-lg:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  heading-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-strong:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm-strong:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  caption-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  link-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  button-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0

rounded:
  none: 0px
  sm: 8px
  md: 16px
  lg: 32px
  full: 9999px

spacing:
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 6px 14px
    height: 40px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.secondary-bg}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 6px 14px
    height: 40px
  button-secondary-pressed:
    backgroundColor: "{colors.secondary-pressed}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
  button-icon-circular:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
  button-pill-on-image:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 14px
  button-disabled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ash}"
    rounded: "{rounded.md}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 11px 15px
    height: 48px
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 11px 15px
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  pin-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0px
  pin-card-large:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 0px
  pin-overlay-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.md}"
    padding: 16px
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-xl}"
    rounded: "{rounded.md}"
    padding: 32px
  feature-card-soft:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-xl}"
    rounded: "{rounded.md}"
    padding: 32px
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  hero-cta-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-xl}"
    rounded: "{rounded.none}"
    padding: 48px 32px
  primary-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    height: 64px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.mute}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 32px 24px
  link-inline:
    textColor: "{colors.ink-soft}"
    typography: "{typography.link-md}"
---

## Visao Geral

Este sistema visual e construido em torno de um principio simples: deixar a fotografia conduzir a experiencia. A interface usa uma paleta neutra quente e discreta (`{colors.surface-soft}`, `{colors.surface-card}`, `{colors.canvas}`), com tipografia sem serifa em **Inter** e o vermelho primario (`{colors.primary}` - `#e60023`) reservado para CTAs principais, indicadores ativos e ancoras importantes da navegacao. As demais superficies recuam para que imagens, miniaturas, cards de descoberta e retratos sejam o foco real do produto.

O design system trabalha com dois modos de superficie: o **chrome de hero/CTA** (superficies claras, manchetes grandes de 70px e cards editoriais com fotografia alternando esquerda/direita) e o **masonry de conteudo** (grade em colunas com cards de 16px de raio em `{colors.surface-card}`, sem padding interno; a imagem e o card). Superficies editoriais podem inverter a grade para um layout mais tradicional, mas mantem as mesmas regras: tipografia Inter, chrome creme, CTA vermelho e pills de 16px.

O gesto visual mais reconhecivel do sistema e a **geometria de formas**: raio de 16px (`{rounded.md}`) para quase todas as superficies - botoes, inputs, pin cards e feature cards - e raio de 32px (`{rounded.lg}`) reservado para `pin-card-large` e cards modais. Na pratica, o vocabulario ativo usa 16px, 32px e pill (`9999px`). O sistema evita cantos secos em elementos interativos e nao cria valores intermediarios de raio sem necessidade.

**Caracteristicas principais:**
- CTA de acento unico: `{colors.primary}` conduz acoes primarias; o restante permanece majoritariamente monocromatico.
- Tipografia Inter em todos os papeis de texto, de `{typography.display-xl}` (70px) a `{typography.caption-sm}` (12px), sem serifas ou monospace na interface principal.
- Sistema de raio concentrado: `{rounded.md}` (16px) para a maioria dos componentes, `{rounded.lg}` (32px) para cards grandes e modais, `{rounded.full}` para elementos circulares.
- Grade masonry de pins como elemento visual estrutural, preservando a proporcao natural de cada imagem.
- Chrome neutro creme (`{colors.surface-card}` - `#f6f6f3`) que recua atras da imagem sem competir com ela.
- Navegacao superior fixa com CTA primario vermelho visivel nos principais breakpoints.
- Overlay modal de login/cadastro usando scrim suave sobre a pagina em vez de troca brusca de navegacao.

## Cores

> **Paginas de referencia:** home, resultados de busca, superficie editorial/de criacao e artigo editorial. A paleta de chrome deve permanecer consistente entre esses contextos.

### Marca e Acento
- **Vermelho primario** (`{colors.primary}` - `#e60023`): unica cor altamente saturada do sistema. Usado em CTAs principais, ancora da navegacao fixa, estado ativo em abas e marca/identidade visual.
- **Vermelho primario pressionado** (`{colors.primary-pressed}` - `#cc001f`): estado pressionado do botao primario, um passo mais profundo que o vermelho base.

### Superficie
- **Canvas** (`{colors.canvas}` - `#ffffff`): branco real. Superficie-base para navegacao primaria, modais, feature cards e corpo do conteudo.
- **Surface Soft** (`{colors.surface-soft}` - `#fbfbf9`): off-white levemente creme usado como banho de pagina no hero.
- **Surface Card** (`{colors.surface-card}` - `#f6f6f3`): fundo creme quente para cards e tiles. Sustenta category tiles, preenchimento padrao da search bar, botao secundario e pin cards.
- **Secondary BG** (`{colors.secondary-bg}` - `#e5e5e0`): cinza-creme para `{component.button-secondary}`, um passo mais profundo que `{colors.surface-card}`.
- **Secondary Pressed** (`{colors.secondary-pressed}` - `#c8c8c1`): estado pressionado do botao secundario.
- **Surface Dark** (`{colors.surface-dark}` - `#262622`): quase preto quente usado em faixas escuras de CTA.
- **Hairline** (`{colors.hairline}` - `#dadad3`): divisores de 1px, linhas de rodape e separadores discretos.
- **Hairline Soft** (`{colors.hairline-soft}` - `#e5e5e0`): divisor inline mais leve; tambem pode funcionar como fundo do botao secundario.

### Texto
- **Ink** (`{colors.ink}` - `#000000`): titulos primarios, texto de botoes e links da navegacao principal.
- **Ink Soft** (`{colors.ink-soft}` - `#211922`): cor de links inline em texto corrido, um quase preto com leve calor.
- **Body** (`{colors.body}` - `#33332e`): texto padrao de paragrafos sobre `{colors.canvas}`.
- **Charcoal** (`{colors.charcoal}` - `#262622`): corpo de texto levemente mais suave quando preto puro pesa demais.
- **Mute** (`{colors.mute}` - `#62625b`): metadados, links de rodape e legendas secundarias.
- **Ash** (`{colors.ash}` - `#91918c`): texto desabilitado e placeholders de inputs.
- **Stone** (`{colors.stone}` - `#c8c8c1`): texto utilitario de menor enfase e bordas de estado desabilitado.
- **On Dark** (`{colors.on-dark}` - `#ffffff`): texto principal sobre `{colors.surface-dark}`.

### Semanticas
- **Error** (`{colors.error}` - `#9e0a0a`): mensagens de validacao e textos de confirmacao destrutiva.
- **Error Deep** (`{colors.error-deep}` - `#cc001f`): fundo de erro mais profundo quando o tom regular precisa de mais contraste.
- **Success Deep** (`{colors.success-deep}` - `#103c25`): mensagens de sucesso dentro do produto.
- **Success Pale** (`{colors.success-pale}` - `#c7f0da`): fundo claro para pills de sucesso.
- **Focus Outer** (`{colors.focus-outer}` - `#435ee5`): azul do anel de foco, aplicado como contorno externo de 2px em inputs e botoes focados.
- **Focus Inner** (`{colors.focus-inner}` - `#ffffff`): intervalo branco interno no stack do anel de foco.

### Acentos Editoriais
- **Accent Pressed Blue** (`{colors.accent-pressed-blue}` - `#617bff`): estado pressionado para badges informativos azuis e chips editoriais.
- **Accent Purple** (`{colors.accent-purple}` - `#7e238b`): badge de recomendacao editorial e chamadas especiais dentro do produto.
- **Accent Purple Deep** (`{colors.accent-purple-deep}` - `#6845ab`): par escuro para lockups roxos e iconografia de performance.

## Tipografia

### Familia Tipografica
**Inter** e a familia recomendada para todas as funcoes de texto. Use pesos 400 (regular), 500 (medium), 600 (semibold) e 700 (bold), com fallback para `-apple-system`, `system-ui`, `Segoe UI`, `Roboto`, `Helvetica Neue`, `Arial` e fallbacks de emoji. Em tamanhos de display, o tracking negativo em `{typography.display-xl}` e `{typography.heading-xl}` ajuda a criar manchetes densas, confiantes e amigaveis.

### Hierarquia

| Token | Tamanho | Peso | Altura de linha | Espacamento entre letras | Uso |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 70px | 600 | 1.1 | -1.2px | Manchete de hero de marketing |
| `{typography.display-lg}` | 44px | 700 | 1.15 | -0.8px | Hero editorial ou de criacao |
| `{typography.heading-xl}` | 28px | 700 | 1.2 | -1.2px | Titulo de secao |
| `{typography.heading-lg}` | 22px | 600 | 1.25 | 0 | Subtitulo de secao, titulo de modal |
| `{typography.heading-md}` | 18px | 600 | 1.3 | 0 | Titulo de card, rotulo em grade |
| `{typography.body-md}` | 16px | 400 | 1.4 | 0 | Corpo de texto, corpo de modal, paragrafo padrao |
| `{typography.body-strong}` | 16px | 600 | 1.4 | 0 | Enfase inline, link da navegacao, label de formulario |
| `{typography.body-sm}` | 14px | 400 | 1.4 | 0 | Texto de rodape, metadados em grade, helper text |
| `{typography.body-sm-strong}` | 14px | 700 | 1.4 | 0 | Contador de resultados, cabecalho de tabela |
| `{typography.caption-md}` | 12px | 500 | 1.5 | 0 | Legenda e metadados de link |
| `{typography.caption-sm}` | 12px | 400 | 1.4 | 0 | Menor texto utilitario, copyright |
| `{typography.link-md}` | 16px | 600 | 1.4 | 0 | Link inline em texto corrido |
| `{typography.button-md}` | 14px | 700 | 1 | 0 | Label padrao de botao primario/secundario |
| `{typography.button-sm}` | 12px | 700 | 1 | 0 | Chip compacto, botao dentro de card |

### Principios
O sistema tem um salto forte entre display e corpo: `{typography.display-xl}` (70px) pode cair diretamente para `{typography.body-md}` (16px) no hero, sem uma camada intermediaria obrigatoria. O tracking negativo nos maiores niveis (-1.2px / -0.8px) cria titulos mais compactos, enquanto o corpo em `1.4` de line-height preserva leitura confortavel em descricoes de varias linhas.

### Substitutos de Fonte
Inter e a fonte padrao recomendada. **Manrope** pode funcionar como substituta secundaria para display quando for preciso um desenho um pouco mais fechado. Mantenha o tracking de -1.2px em tamanhos grandes sempre que o substituto precisar preservar a mesma densidade visual.

## Layout

### Sistema de Espacamento
- **Unidade base:** 8px, com passos finos de 4/6/7px para gaps inline apertados em botoes pill e chips.
- **Tokens:** `{spacing.xxs}` (4px), `{spacing.xs}` (6px), `{spacing.sm}` (8px), `{spacing.md}` (12px), `{spacing.lg}` (16px), `{spacing.xl}` (24px), `{spacing.xxl}` (32px), `{spacing.section}` (64px).
- **Ritmo universal de secao:** use `{spacing.section}` (64px) como intervalo vertical entre blocos principais. Grades de pins usam gutters `{spacing.sm}` (8px), criando uma malha visual apertada para imagens.
- **Padding de modal:** `{component.modal-card}` usa 32px (`{spacing.xxl}`) em todos os lados.

### Grid e Container
- **Largura maxima:** area de conteudo de aproximadamente 1280px no desktop, com gutters de 24px e cerca de 48px em ultrawide.
- **Grade masonry de pins:** layout em colunas autoajustaveis - 5 a 6 colunas em ultrawide, 4 no desktop, 3 em tablet, 2 em mobile landscape e 1 em mobile. Cada tile preserva a proporcao natural (quadrado, 2:3, 3:4, 4:5). Gutters horizontais e verticais usam `{spacing.sm}` (8px).
- **Linha de feature do hero:** split assimetrico de 2 colunas, alternando texto e imagem entre esquerda/direita ao longo da pagina.
- **Rodape:** grade de links em 4 colunas no desktop, 2 colunas no tablet e 1 coluna no mobile.

### Filosofia de Espaco em Branco
O espaco e generoso em superficies de marketing e apertado em superficies de descoberta. A home separa secoes por 64px e usa 32px de padding interno nos cards editoriais, enquanto resultados de busca podem se condensar em uma grade masonry com gutter de 8px. O sistema deve parecer dois modos do mesmo produto: revista (hero, feature, CTA, rodape) e mecanismo de descoberta (nav, filtros, grade e carregar mais).

## Elevacao e Profundidade

| Nivel | Tratamento | Uso |
|---|---|---|
| 0 - Plano | Sem borda, sem sombra | Padrao para pin cards, feature cards e rodape |
| 1 - Borda hairline | `1px solid {colors.hairline}` | Inputs, divisores de rodape, linhas em listas |
| 2 - Scrim modal + sombra suave | Modal sobre scrim escuro com sombra ambiente de 16px | Modal de login/cadastro, preview de imagem |
| 3 - Lift de hover em pin | Nao documentado por politica do sistema | n/a |

O sistema praticamente nao usa sombra em superficies de conteudo. Pin cards ficam planos sobre o canvas; a elevacao aparece no layer modal, onde um scrim de 50% de opacidade e uma sombra ambiente de 16px colocam o card acima da pagina.

### Profundidade Decorativa
A profundidade vem das proprias imagens, nao de efeitos CSS:
- **Fotografia dos pins:** composicao, close-ups e cenas editoriais carregam profundidade visual; a interface deixa cada imagem falar.
- **Miniaturas de categoria:** linhas de feature usam composicoes fotograficas com um pequeno `{component.pin-overlay-pill}` no canto da imagem.
- **Scrim modal:** overlay escuro de 50% sobre a pagina inteira quando o modal abre, com sombra ambiente sob o card.

## Formas

### Escala de Border Radius

| Token | Valor | Uso |
|---|---|---|
| `{rounded.none}` | 0px | Rodape, navegacao primaria e secoes estruturais planas |
| `{rounded.sm}` | 8px | Superficie rara de raio medio, como tooltip editorial |
| `{rounded.md}` | 16px | Botoes, inputs, pin cards, feature cards e category tiles |
| `{rounded.lg}` | 32px | Pin cards grandes e modais, usado com parcimonia |
| `{rounded.full}` | 9999px | Search bar, filter chips, overlay pills, botoes circulares e avatares |

O vocabulario de raio se resume a 16px para a maioria dos componentes, 32px para cards grandes/modais e pill para elementos circulares. Botoes e pin cards nao devem usar cantos secos.

### Geometria de Fotografia
- **Imagens de pin:** proporcoes mistas - quadrado (1:1), retrato (3:4, 2:3, 4:5) e paisagem rara - preservadas em `{rounded.md}` (16px) nos tiles pequenos e `{rounded.lg}` (32px) em pins grandes.
- **Miniaturas de categoria:** quadradas (1:1) com cantos `{rounded.md}`.
- **Avatares circulares:** 32 a 48px com `{rounded.full}` para atribuicao e chips de perfil.
- **Imagens de feature card:** normalmente retrato 4:5 em cards de categoria, com foto ocupando cerca de 60% do card e titulo + CTA empilhados abaixo.

## Componentes

> **Estados de hover nao documentados** por politica do sistema. Cada especificacao cobre apenas Padrao e Ativo/Pressionado.

### Botoes

**`button-primary`** - CTA primario universal
- Fundo `{colors.primary}`, texto `{colors.on-primary}`, tipo `{typography.button-md}`, padding `6px 14px`, altura aproximada de 40px, raio `{rounded.md}` (16px).
- Usado para acoes como "Cadastrar", "Entrar gratuitamente" e "Comecar" em superficies principais.
- Estado pressionado em `button-primary-pressed`, com fundo `{colors.primary-pressed}` (`#cc001f`).

**`button-secondary`** - alternativa cinza-creme
- Fundo `{colors.secondary-bg}` (`#e5e5e0`), texto `{colors.on-secondary}`, tipo `{typography.button-md}`, padding `6px 14px`, altura aproximada de 40px, raio `{rounded.md}`.
- Usado para acoes de segundo nivel como "Ja tenho uma conta", "Continuar" e "Cancelar".
- Estado pressionado em `button-secondary-pressed`, com fundo `{colors.secondary-pressed}`.

**`button-tertiary`** - link fantasma
- Fundo transparente, texto `{colors.ink}`, tipo `{typography.button-md}`, raio `{rounded.md}`.
- Usado para acoes de baixa enfase em dialogs, como "Ler a documentacao" e "Saiba mais" com pequeno chevron.

**`button-icon-circular`** - botao circular com icone
- Fundo `{colors.surface-card}`, icone `{colors.ink}`, raio `{rounded.full}`, tamanho 40px.
- Setas de carrossel, botao de fechar modal e pequenas acoes flutuantes sobre imagem.

**`button-pill-on-image`** - pill pequena sobre fotografia
- Fundo `{colors.canvas}`, texto `{colors.ink}`, tipo `{typography.button-md}`, raio `{rounded.full}`, padding `8px 14px`.
- Pill de sobreposicao que ancora um termo ou rotulo no canto da imagem.

**`button-disabled`**
- Fundo `{colors.surface-card}`, texto `{colors.ash}`; visual plano em creme suave.

### Filtros e Abas

**`filter-chip`** + **`filter-chip-active`**
- Padrao: fundo `{colors.surface-card}`, texto `{colors.ink}`, tipo `{typography.button-md}`, raio `{rounded.full}`, padding `8px 16px`.
- Ativo: fundo `{colors.ink}`, texto `{colors.on-dark}`; o chip inverte totalmente ao ser selecionado.
- Usado em faixas de filtro de resultados, como "Beleza", "Batom" e "Editorial".

### Inputs e Formularios

**`text-input`** + **`text-input-focused`**
- Padrao: fundo `{colors.canvas}`, texto `{colors.ink}`, borda `1px solid {colors.ash}`, tipo `{typography.body-md}`, padding `11px 15px`, altura aproximada de 44px, raio `{rounded.md}`.
- Focused: borda interna de 2px `{colors.ink}` + outline externo de 4px `{colors.focus-outer}`.
- Usado em campos de email, senha, data de nascimento, pais e outros formularios.

**`search-bar`** + **`search-bar-focused`**
- Padrao: fundo `{colors.surface-card}`, texto `{colors.ink}`, tipo `{typography.body-md}`, padding `11px 15px`, altura aproximada de 48px, raio `{rounded.full}`.
- Focused: mesmas dimensoes, fundo muda para `{colors.canvas}` com borda `1px solid {colors.ash}`.
- Ancorada no centro da navegacao primaria com icone de lupa a esquerda e placeholder contextual.

### Cards e Containers

**`pin-card`** - tile masonry padrao
- Container: fundo `{colors.surface-card}`, raio `{rounded.md}` (16px), padding 0.
- Layout: imagem full-bleed na proporcao natural do card, sem padding interno. Pode receber `{component.pin-overlay-pill}` em um canto e avatar circular de 32px com nome de perfil em `{typography.body-sm-strong}` sobreposto no canto inferior esquerdo.

**`pin-card-large`** - pin grande de feature
- Identico ao `pin-card`, mas com raio `{rounded.lg}` (32px), usado em pins editoriais maiores.

**`pin-overlay-pill`** - chip ancorado sobre imagem
- Fundo `{colors.canvas}`, texto `{colors.ink}`, tipo `{typography.button-sm}`, raio `{rounded.full}`, padding `6px 12px`.
- Flutua no canto inferior ou superior esquerdo de um pin com um termo de busca ou rotulo contextual.

**`category-tile`**
- Fundo `{colors.surface-card}`, raio `{rounded.md}`, padding 16px.
- Grade de 3 ou 4 colunas com miniaturas de categoria. Cada tile contem icone ou composicao fotografica e rotulo curto em `{typography.body-strong}`.

**`feature-card`** + **`feature-card-soft`**
- Padrao: fundo `{colors.canvas}`, raio `{rounded.md}`, padding 32px. Combina imagem retrato 4:5, titulo `{typography.heading-xl}`, texto de corpo e `{component.button-primary}`.
- Soft: fundo `{colors.surface-card}` para variantes alternadas que precisam quebrar a sequencia visual.

**`modal-card`** - overlay de login/cadastro
- Fundo `{colors.canvas}`, raio `{rounded.lg}` (32px), padding 32px.
- Layout: titulo em `{typography.heading-lg}`, subtitulo em `{typography.body-md}`, campos `{component.text-input}` empilhados, `{component.button-primary}` como acao principal e link secundario abaixo.
- Flutua sobre scrim de 50% de opacidade cobrindo a pagina, com sombra ambiente de 16px.

**`hero-cta-strip`** - faixa escura de CTA
- Fundo `{colors.surface-dark}`, texto `{colors.on-dark}`, tipo `{typography.heading-xl}`, padding `48px 32px`, raio `{rounded.none}`.
- Usada no topo de superficies editoriais ou institucionais, com um unico `{component.button-primary}` alinhado a direita quando houver espaco.

### Navegacao

**`primary-nav`**
- Fundo `{colors.canvas}`, texto `{colors.ink}`, altura aproximada de 64px, tipo `{typography.body-strong}`, raio `{rounded.none}`, com regra inferior de `1px solid {colors.hairline}` em paginas internas.
- Layout desktop: marca/wordmark a esquerda + link principal, `{component.search-bar}` centralizada e cluster de links + `{component.button-primary}` a direita.
- Layout de resultados: icone/marca a esquerda, busca central com query ativa e cluster de login/CTA a direita.

**Navegacao Superior (Mobile)**
- Icone de menu a esquerda, marca central, lupa + CTA a direita. A search bar colapsa para icone de lupa e expande para overlay full-width ao toque.

### Rodape

**`footer-section`**
- Fundo `{colors.canvas}`, texto `{colors.mute}` em `{typography.body-sm}`, padding `32px 24px`, raio `{rounded.none}`, com regra superior `1px solid {colors.hairline}`.
- Layout: grade de links em 4 colunas (app, links rapidos, produto, sobre), com cabecalhos em `{typography.body-sm-strong}` e listas em `{typography.body-sm}` `{colors.mute}`.
- Linha inferior: wordmark/identidade + copyright em `{typography.caption-sm}` `{colors.mute}`.

### Inline

**`link-inline`** - ancora em texto corrido
- Texto `{colors.ink-soft}` sem underline por padrao. Use apenas para diferenciar links de corpo sem depender de uma cor saturada.

## Boas Praticas e Evitar

### Faca
- Reserve `{colors.primary}` para CTAs primarios, indicador ativo de abas e marca/wordmark. Ele nunca deve ser decorativo.
- Use `{rounded.md}` (16px) em todo elemento interativo e card padrao; reserve `{rounded.lg}` (32px) para pins grandes e modais; reserve `{rounded.full}` para elementos circulares.
- Coloque cada imagem de pin dentro de `{component.pin-card}` sem padding interno; a fotografia e o card.
- Empilhe secoes no ritmo de `{spacing.section}` (64px) e mantenha grades de pins com gutters `{spacing.sm}` (8px).
- Use `{component.pin-overlay-pill}` para ancorar uma tag contextual no canto da fotografia.
- Construa hierarquia com peso (400 -> 600 -> 700) e tamanho, nao com tintas de cor. O corpo permanece `{colors.body}`.
- Aplique letter-spacing de -1.2px em `{typography.display-xl}` e `{typography.heading-xl}`; esse tracking faz parte da voz visual.

### Nao Faca
- Nao use botoes ou cards com cantos secos. Elementos interativos nao usam `{rounded.none}`.
- Nao introduza sombras em cards. A unica sombra do sistema e a ambiente de 16px sob `{component.modal-card}`.
- Nao aplique padding interno em `{component.pin-card}`. A imagem e full-bleed; metadados ficam sobre a imagem como overlay pill.
- Nao substitua `{colors.primary}` por outro vermelho. O valor e preciso: `#e60023`.
- Nao use `{colors.ink-soft}` fora de links inline em texto corrido.
- Nao introduza um terceiro raio entre 16px e 32px. O sistema salta diretamente de md para lg.

## Comportamento Responsivo

### Breakpoints

| Nome | Largura | Mudancas principais |
|---|---|---|
| ultrawide | 1920px+ | Grade de pins expande para 5-6 colunas; conteudo segura max-width em ~1280px |
| desktop-large | 1440px | Padrao: grade de 4 colunas e navegacao completa |
| desktop | 1280px | Mesmo layout com gutters externos menores |
| desktop-small | 1024px | Grade de pins colapsa para 3 colunas; subnav permanece horizontal |
| tablet | 768px | Grade de pins colapsa para 2 colunas; nav vira drawer; busca vira icone |
| mobile | 480px | Grade de pins em 1 coluna; hero `{typography.display-xl}` reduz de 70px para ~44px |
| mobile-narrow | 320px | Hero reduz para ~36px; padding de secao aperta para 32px |

### Alvos de Toque
Todos os elementos interativos atendem WCAG AA (>= 44x44px). `{component.button-primary}` e `{component.button-secondary}` ficam em cerca de 40px de altura com 14px de padding horizontal, resultando em area tocavel efetiva ampla. `{component.search-bar}` tem 48px. `{component.text-input}` tem 44px. `{component.filter-chip}` tem cerca de 36-40px de altura com padding de 16px, estendido para alvo tocavel de 44px. `{component.button-icon-circular}` tem 40x40 com hit target estendido para 48x48 no container.

### Estrategia de Colapso
- **Navegacao primaria:** cluster horizontal no desktop -> drawer no tablet a 768px. O CTA vermelho permanece visivel nos principais breakpoints.
- **Search bar:** centralizada no desktop (~480px) -> comprimida no tablet (~320px) -> colapsa para lupa no mobile e expande em overlay full-width ao toque.
- **Grade masonry de pins:** 5/6 colunas -> 4 -> 3 -> 2 -> 1 em 1920, 1024, 768 e 480px. Gutters caem de 8px para 6px no mobile.
- **Feature row da home:** duas colunas alternando esquerda/direita no desktop -> stack vertical no tablet -> coluna unica no mobile com imagem full-bleed.
- **Modal:** card centralizado de ~480px no desktop -> sheet full-width no mobile com `{rounded.lg}` apenas no topo e CTA ancorado embaixo.
- **Padding de secao:** `{spacing.section}` (64px) no desktop -> 48px tablet -> 32px mobile.
- **Hero headline:** `{typography.display-xl}` (70px) no desktop, escalando para 56px / 44px / 36px nos breakpoints.
- **Rodape:** 4 colunas -> 2 no tablet -> accordion completo no mobile.

### Comportamento de Imagem
- Imagens de pin preservam proporcao natural em todos os breakpoints; muda a contagem de colunas, nao a proporcao.
- Miniaturas de categoria mantem 1:1 em todos os tamanhos.
- Imagens de feature usam cortes com art direction no mobile (retrato 4:5 -> quadrado) para manter o assunto centralizado.
- Imagens nao criticas devem usar lazy loading conforme entram na proxima linha da grade.

## Guia de Iteracao

1. Foque em UM componente por vez. Puxe sua entrada YAML e verifique se todas as propriedades resolvem.
2. Referencie nomes de componentes e tokens diretamente (`{colors.primary}`, `{component.button-primary-pressed}`, `{rounded.md}`); nao parafraseie tokens.
3. Rode `npx @google/design.md lint DESIGN.md` apos edicoes; avisos de `broken-ref`, `contrast-ratio` e `orphaned-tokens` apontam problemas automaticamente.
4. Adicione novas variantes como entradas de componente separadas (`-pressed`, `-disabled`, `-focused`); nao esconda variantes na prosa.
5. Use `{typography.body-md}` como corpo padrao; use `{typography.body-strong}` para enfase; reserve `{typography.display-xl}` para manchetes de topo de pagina.
6. Mantenha `{colors.primary}` escasso: no maximo um CTA vermelho por dobra, contando nav, hero e CTAs de feature card.
7. Ao introduzir um componente, pergunte se ele pode ser expresso com o vocabulario existente de pin-card + raio 16px + superficie creme antes de criar novos tokens.

## Lacunas Conhecidas

- **Screenshots mobile nao capturados:** o comportamento responsivo sintetiza padroes esperados de mobile (drawer, grade de 1 coluna, reducao do hero) a partir dos breakpoints documentados.
- **Estados de hover nao documentados** por politica do sistema.
- **Close-up de pin individual** nao esta no conjunto capturado; a view detalhada pode exigir componentes adicionais.
- **Chrome autenticado** (feed logado, paginas de colecao, perfis) nao esta nas superficies capturadas.
- **Telas mobile app** nao fazem parte deste sistema documentado; o escopo e web.
- **Estados de validacao de formulario** (sucesso/erro inline) nao estao documentados; apenas foco foi capturado.
