# Base vs Radix

Diferenças de API entre `base` e `radix`. Verifique o campo `base` com `npx shadcn@latest info`.

## Conteúdo

- Composição: asChild vs render
- Button / trigger como elemento que não é botão
- Select (items prop, placeholder, positioning, multiple, object values)
- ToggleGroup (type vs multiple)
- Slider (scalar vs array)
- Accordion (`type` e `defaultValue`)

---

## Composição: asChild (radix) vs render (base)

Radix usa `asChild` para substituir o elemento padrao. Base usa `render`. Nao envolva triggers em elementos extras.

**Incorreto:**

```tsx
<DialogTrigger>
  <div>
    <Button>Abrir</Button>
  </div>
</DialogTrigger>
```

**Correto (radix):**

```tsx
<DialogTrigger asChild>
  <Button>Abrir</Button>
</DialogTrigger>
```

**Correto (base):**

```tsx
<DialogTrigger render={<Button />}>Abrir</DialogTrigger>
```

Isso se aplica a todos os componentes trigger e close: `DialogTrigger`, `SheetTrigger`, `AlertDialogTrigger`, `DropdownMenuTrigger`, `PopoverTrigger`, `TooltipTrigger`, `CollapsibleTrigger`, `DialogClose`, `SheetClose`, `NavigationMenuLink`, `BreadcrumbLink`, `SidebarMenuButton`, `Badge`, `Item`.

---

## Button / trigger como elemento que nao e botao (somente base)

Quando `render` transforma um elemento em algo que não é botão (`<a>`, `<span>`), adicione `nativeButton={false}`.

**Incorreto (base):** falta `nativeButton={false}`.

```tsx
<Button render={<a href="/docs" />}>Ler a documentação</Button>
```

**Correto (base):**

```tsx
<Button render={<a href="/docs" />} nativeButton={false}>
  Ler a documentação
</Button>
```

**Correto (radix):**

```tsx
<Button asChild>
  <a href="/docs">Ler a documentação</a>
</Button>
```

O mesmo vale para triggers cujo `render` não é um `Button`:

```tsx
// base.
<PopoverTrigger render={<InputGroupAddon />} nativeButton={false}>
  Escolher data
</PopoverTrigger>
```

---

## Select

**Prop `items` (somente base).** Base exige uma prop `items` no componente raiz. Radix usa apenas JSX inline.

**Incorreto (base):**

```tsx
<Select>
  <SelectTrigger><SelectValue placeholder="Select a fruit" /></SelectTrigger>
</Select>
```

**Correto (base):**

```tsx
const items = [
  { label: "Select a fruit", value: null },
  { label: "Apple", value: "apple" },
  { label: "Banana", value: "banana" },
]

<Select items={items}>
  <SelectTrigger>
    <SelectValue />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      {items.map((item) => (
        <SelectItem key={item.value} value={item.value}>{item.label}</SelectItem>
      ))}
    </SelectGroup>
  </SelectContent>
</Select>
```

**Correto (radix):**

```tsx
<Select>
  <SelectTrigger>
    <SelectValue placeholder="Select a fruit" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectItem value="apple">Apple</SelectItem>
      <SelectItem value="banana">Banana</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

**Placeholder.** Base usa um item `{ value: null }` no array `items`. Radix usa `<SelectValue placeholder="...">`.

**Posicionamento do conteudo.** Base usa `alignItemWithTrigger`. Radix usa `position`.

```tsx
// base.
<SelectContent alignItemWithTrigger={false} side="bottom">

// radix.
<SelectContent position="popper">
```

---

## Select — selecao multipla e valores de objeto (somente base)

Base suporta `multiple`, children como render function em `SelectValue` e valores de objeto com `itemToStringValue`. Radix e single-select apenas com valores string.

**Correto (base — multiple selection):**

```tsx
<Select items={items} multiple defaultValue={[]}>
  <SelectTrigger>
    <SelectValue>
      {(value: string[]) => value.length === 0 ? "Select fruits" : `${value.length} selected`}
    </SelectValue>
  </SelectTrigger>
  ...
</Select>
```

**Correto (base — object values):**

```tsx
<Select defaultValue={plans[0]} itemToStringValue={(plan) => plan.name}>
  <SelectTrigger>
    <SelectValue>{(value) => value.name}</SelectValue>
  </SelectTrigger>
  ...
</Select>
```

---

## ToggleGroup

Base usa a prop booleana `multiple`. Radix usa `type="single"` ou `type="multiple"`.

**Incorreto (base):**

```tsx
<ToggleGroup type="single" defaultValue="daily">
  <ToggleGroupItem value="daily">Diário</ToggleGroupItem>
</ToggleGroup>
```

**Correto (base):**

```tsx
// Single (sem prop extra), defaultValue sempre e array.
<ToggleGroup defaultValue={["daily"]} spacing={2}>
  <ToggleGroupItem value="daily">Diário</ToggleGroupItem>
  <ToggleGroupItem value="weekly">Semanal</ToggleGroupItem>
</ToggleGroup>

// Multi-selection.
<ToggleGroup multiple>
  <ToggleGroupItem value="bold">Bold</ToggleGroupItem>
  <ToggleGroupItem value="italic">Italic</ToggleGroupItem>
</ToggleGroup>
```

**Correto (radix):**

```tsx
// Single, defaultValue is a string.
<ToggleGroup type="single" defaultValue="daily" spacing={2}>
  <ToggleGroupItem value="daily">Diário</ToggleGroupItem>
  <ToggleGroupItem value="weekly">Semanal</ToggleGroupItem>
</ToggleGroup>

// Multi-selection.
<ToggleGroup type="multiple">
  <ToggleGroupItem value="bold">Bold</ToggleGroupItem>
  <ToggleGroupItem value="italic">Italic</ToggleGroupItem>
</ToggleGroup>
```

**Valor unico controlado:**

```tsx
// base — embrulhe/desembrulhe arrays.
const [value, setValue] = React.useState("normal")
<ToggleGroup value={[value]} onValueChange={(v) => setValue(v[0])}>

// radix — string simples.
const [value, setValue] = React.useState("normal")
<ToggleGroup type="single" value={value} onValueChange={setValue}>
```

---

## Slider

Base aceita um numero simples para um unico thumb. Radix sempre exige array.

**Incorreto (base):**

```tsx
<Slider defaultValue={[50]} max={100} step={1} />
```

**Correto (base):**

```tsx
<Slider defaultValue={50} max={100} step={1} />
```

**Correto (radix):**

```tsx
<Slider defaultValue={[50]} max={100} step={1} />
```

Ambos usam arrays para range sliders. `onValueChange` controlado em base pode precisar de cast:

```tsx
// base.
const [value, setValue] = React.useState([0.3, 0.7])
<Slider value={value} onValueChange={(v) => setValue(v as number[])} />

// radix.
const [value, setValue] = React.useState([0.3, 0.7])
<Slider value={value} onValueChange={setValue} />
```

---

## Accordion

Radix exige `type="single"` ou `type="multiple"` e suporta `collapsible`. `defaultValue` e uma string. Base nao usa prop `type`, usa o booleano `multiple` e `defaultValue` sempre e array.

**Incorreto (base):**

```tsx
<Accordion type="single" collapsible defaultValue="item-1">
  <AccordionItem value="item-1">...</AccordionItem>
</Accordion>
```

**Correto (base):**

```tsx
<Accordion defaultValue={["item-1"]}>
  <AccordionItem value="item-1">...</AccordionItem>
</Accordion>

// Multi-select.
<Accordion multiple defaultValue={["item-1", "item-2"]}>
  <AccordionItem value="item-1">...</AccordionItem>
  <AccordionItem value="item-2">...</AccordionItem>
</Accordion>
```

**Correto (radix):**

```tsx
<Accordion type="single" collapsible defaultValue="item-1">
  <AccordionItem value="item-1">...</AccordionItem>
</Accordion>
```
