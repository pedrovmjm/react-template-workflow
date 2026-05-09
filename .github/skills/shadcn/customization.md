# Customização e Temas

Os componentes referenciam tokens semânticos de variáveis CSS. Altere as variáveis para alterar todos os componentes.

## Conteúdo

- Como funciona (variaveis CSS → utilitarios Tailwind → componentes)
- Variaveis de cor e formato OKLCH
- Configuracao de modo escuro
- Alterando o tema (presets, variaveis CSS)
- Adicionando cores customizadas (Tailwind v3 e v4)
- Border radius
- Customizando componentes (variantes, className, wrappers)
- Verificando atualizacoes

---

## Como Funciona

1. Variaveis CSS sao definidas em `:root` (claro) e `.dark` (modo escuro).
2. Tailwind mapeia essas variaveis para utilitarios: `bg-primary`, `text-muted-foreground`, etc.
3. Os componentes usam essas utilidades; alterar uma variável muda todos os componentes que a referenciam.

---

## Variáveis de Cor

Toda cor segue a convencao `name` / `name-foreground`. A variavel base serve para fundos; `-foreground` serve para texto/icones sobre esse fundo.

| Variável                                     | Finalidade                          |
| -------------------------------------------- | -------------------------------- |
| `--background` / `--foreground`              | Fundo da pagina e texto padrao   |
| `--card` / `--card-foreground`               | Card surfaces                    |
| `--primary` / `--primary-foreground`         | Botoes e acoes primarias         |
| `--secondary` / `--secondary-foreground`     | Acoes secundarias                |
| `--muted` / `--muted-foreground`             | Estados discretos/desabilitados  |
| `--accent` / `--accent-foreground`           | Estados de hover e destaque      |
| `--destructive` / `--destructive-foreground` | Erros e acoes destrutivas        |
| `--border`                                   | Cor padrao de borda              |
| `--input`                                    | Form input borders               |
| `--ring`                                     | Cor do anel de foco              |
| `--chart-1` a `--chart-5`                    | Graficos e visualizacao de dados |
| `--sidebar-*`                                | Cores especificas da sidebar     |
| `--surface` / `--surface-foreground`         | Secondary surface                |

Cores usam OKLCH: `--primary: oklch(0.205 0 0)`, onde os valores sao luminosidade (0 a 1), chroma (0 = cinza) e hue (0 a 360).

---

## Modo Escuro

Alternância baseada em classe via `.dark` no elemento raiz. No Next.js, use `next-themes`:

```tsx
import { ThemeProvider } from "next-themes"

<ThemeProvider attribute="class" defaultTheme="system" enableSystem>
  {children}
</ThemeProvider>
```

---

## Alterando o Tema

```bash
# Aplicar um preset code de ui.shadcn.com.
npx shadcn@latest apply --preset a2r6bw

# O atalho posicional tambem funciona.
npx shadcn@latest apply a2r6bw

# Troque para um preset nomeado e sobrescreva componentes existentes.
npx shadcn@latest apply --preset nova

# Preserve os componentes existentes.
npx shadcn@latest init --preset nova --force --no-reinstall

# Use uma URL de tema customizada.
npx shadcn@latest apply --preset "https://ui.shadcn.com/init?base=radix&style=nova&theme=blue&..."
```

Ou edite as variaveis CSS diretamente em `globals.css`.

---

## Adicionando Cores Customizadas

Adicione variaveis ao arquivo indicado por `tailwindCssFile` em `npx shadcn@latest info` (normalmente `globals.css`). Nunca crie um novo arquivo CSS para isso.

```css
/* 1. Defina no arquivo CSS global. */
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}
.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}
```

```css
/* 2a. Registre com Tailwind v4 (@theme inline). */
@theme inline {
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
}
```

Quando `tailwindVersion` for `"v3"` (verifique via `npx shadcn@latest info`), registre em `tailwind.config.js`:

```js
// 2b. Registre com Tailwind v3 (tailwind.config.js).
module.exports = {
  theme: {
    extend: {
      colors: {
        warning: "oklch(var(--warning) / <alpha-value>)",
        "warning-foreground":
          "oklch(var(--warning-foreground) / <alpha-value>)",
      },
    },
  },
}
```

```tsx
// 3. Use em componentes.
<div className="bg-warning text-warning-foreground">Aviso</div>
```

---

## Raio da Borda

`--radius` controla o raio de borda globalmente. Componentes derivam valores dele (`rounded-lg` = `var(--radius)`, `rounded-md` = `calc(var(--radius) - 2px)`).

---

## Customizando Componentes

Veja tambem [rules/styling.md](./rules/styling.md) para exemplos Incorreto/Correto.

Prefira estas abordagens nesta ordem:

### 1. Variantes embutidas

```tsx
<Button variant="outline" size="sm">
  Clique
</Button>
```

### 2. Classes Tailwind via `className`

```tsx
<Card className="mx-auto max-w-md">...</Card>
```

### 3. Adicionar uma nova variante

Edite o código-fonte do componente para adicionar uma variante via `cva`:

```tsx
// components/ui/button.tsx
warning: "bg-warning text-warning-foreground hover:bg-warning/90",
```

### 4. Componentes wrapper

Componha primitivas shadcn/ui em componentes de nível mais alto:

```tsx
export function ConfirmDialog({ title, description, onConfirm, children }) {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>{children}</AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>{title}</AlertDialogTitle>
          <AlertDialogDescription>{description}</AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancelar</AlertDialogCancel>
          <AlertDialogAction onClick={onConfirm}>Confirmar</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```

---

## Verificando Atualizacoes

```bash
npx shadcn@latest add button --diff
```

Para pre-visualizar exatamente o que mudaria antes de atualizar, use `--dry-run` e `--diff`:

```bash
npx shadcn@latest add button --dry-run        # ver todos os arquivos afetados
npx shadcn@latest add button --diff button.tsx # ver o diff de um arquivo especifico
```

Veja [Atualizando Componentes em SKILL.md](./SKILL.md#atualizando-componentes) para o fluxo completo de merge inteligente.
