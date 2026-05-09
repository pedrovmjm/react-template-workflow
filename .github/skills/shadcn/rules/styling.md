# Estilização e Customização

Veja [customization.md](../customization.md) para temas, variaveis CSS e cores customizadas.

## Conteúdo

- Cores semânticas
- Variantes embutidas primeiro
- className apenas para layout
- Sem `space-x-*` / `space-y-*`
- Prefira `size-*` em vez de `w-* h-*` quando forem iguais
- Prefira o atalho truncate
- Sem overrides manuais de cor dark:
- Use cn() para classes condicionais
- Sem z-index manual em componentes de overlay

---

## Cores semânticas

**Incorreto:**

```tsx
<div className="bg-blue-500 text-white">
  <p className="text-gray-600">Texto secundário</p>
</div>
```

**Correto:**

```tsx
<div className="bg-primary text-primary-foreground">
  <p className="text-muted-foreground">Texto secundário</p>
</div>
```

---

## Sem valores brutos de cor para indicadores de status

Para indicadores positivos, negativos ou de status, use variantes de `Badge`, tokens semanticos como `text-destructive` ou variaveis CSS customizadas. Evite cores brutas do Tailwind.

**Incorreto:**

```tsx
<span className="text-emerald-600">+20.1%</span>
<span className="text-green-500">Active</span>
<span className="text-red-600">-3.2%</span>
```

**Correto:**

```tsx
<Badge variant="secondary">+20.1%</Badge>
<Badge>Active</Badge>
<span className="text-destructive">-3.2%</span>
```

Se precisar de uma cor de sucesso/positiva que nao exista como token semantico, use uma variante de `Badge` ou proponha adicionar uma variavel CSS customizada ao tema (veja [customization.md](../customization.md)).

---

## Variantes embutidas primeiro

**Incorreto:**

```tsx
<Button className="border border-input bg-transparent hover:bg-accent">
  Clique aqui
</Button>
```

**Correto:**

```tsx
<Button variant="outline">Clique aqui</Button>
```

---

## className apenas para layout

Use `className` para layout (por exemplo, `max-w-md`, `mx-auto`, `mt-4`), **nao** para sobrescrever cores ou tipografia de componentes. Para alterar cores, use tokens semanticos, variantes embutidas ou variaveis CSS.

**Incorreto:**

```tsx
<Card className="bg-blue-100 text-blue-900 font-bold">
  <CardContent>Dashboard</CardContent>
</Card>
```

**Correto:**

```tsx
<Card className="max-w-md mx-auto">
  <CardContent>Dashboard</CardContent>
</Card>
```

Para customizar a aparencia de um componente, prefira estas abordagens nesta ordem:

1. **Variantes embutidas** — `variant="outline"`, `variant="destructive"`, etc.
2. **Tokens de cor semanticos** — `bg-primary`, `text-muted-foreground`.
3. **Variaveis CSS** — defina cores customizadas no arquivo CSS global (veja [customization.md](../customization.md)).

---

## Sem space-x-* / space-y-*

Use `gap-*` em vez disso. `space-y-4` → `flex flex-col gap-4`. `space-x-2` → `flex gap-2`.

```tsx
<div className="flex flex-col gap-4">
  <Input />
  <Input />
  <Button>Enviar</Button>
</div>
```

---

## Prefira size-* em vez de w-* h-* quando forem iguais

`size-10` não `w-10 h-10`. Aplica-se a ícones, avatares, skeletons etc.

---

## Prefira o atalho truncate

Use `truncate`, nao `overflow-hidden text-ellipsis whitespace-nowrap`.

---

## Sem overrides manuais de cor dark:

Use tokens semânticos; eles lidam com claro/escuro via variáveis CSS. `bg-background text-foreground` não `bg-white dark:bg-gray-950`.

---

## Use cn() para classes condicionais

Use a utilidade `cn()` do projeto para nomes de classe condicionais ou mesclados. Não escreva ternários manuais em strings de className.

**Incorreto:**

```tsx
<div className={`flex items-center ${isActive ? "bg-primary text-primary-foreground" : "bg-muted"}`}>
```

**Correto:**

```tsx
import { cn } from "@/lib/utils"

<div className={cn("flex items-center", isActive ? "bg-primary text-primary-foreground" : "bg-muted")}>
```

---

## Sem z-index manual em componentes de overlay

`Dialog`, `Sheet`, `Drawer`, `AlertDialog`, `DropdownMenu`, `Popover`, `Tooltip`, `HoverCard` gerenciam seu próprio empilhamento. Nunca adicione `z-50` ou `z-[999]`.
