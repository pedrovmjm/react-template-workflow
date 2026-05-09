# Formulários e Inputs

## Conteúdo

- Formulários usam FieldGroup + Field
- InputGroup exige InputGroupInput/InputGroupTextarea
- Botões dentro de inputs usam InputGroup + InputGroupAddon
- Conjuntos de opcoes (2 a 7 opcoes) usam ToggleGroup
- FieldSet + FieldLegend agrupam campos relacionados
- Estados de validacao e desabilitado

---

## Formulários usam FieldGroup + Field

Sempre use `FieldGroup` + `Field` — nunca `div` bruto com `space-y-*`:

```tsx
<FieldGroup>
  <Field>
    <FieldLabel htmlFor="email">Email</FieldLabel>
    <Input id="email" type="email" />
  </Field>
  <Field>
    <FieldLabel htmlFor="password">Senha</FieldLabel>
    <Input id="password" type="password" />
  </Field>
</FieldGroup>
```

Use `Field orientation="horizontal"` para paginas de configuracao. Use `FieldLabel className="sr-only"` para labels visualmente ocultas.

**Escolhendo controles de formulario:**

- Texto simples → `Input`
- Dropdown com opcoes predefinidas → `Select`
- Dropdown pesquisavel → `Combobox`
- Select HTML nativo sem JavaScript → `native-select`
- Booleano → `Switch` para configuracoes ou `Checkbox` para formularios
- Escolha unica entre poucas opcoes → `RadioGroup`
- Alternancia entre 2 a 5 opcoes → `ToggleGroup` + `ToggleGroupItem`
- Codigo OTP/verificacao → `InputOTP`
- Texto multilinha → `Textarea`

---

## InputGroup exige InputGroupInput/InputGroupTextarea

Nunca use `Input` ou `Textarea` bruto dentro de um `InputGroup`.

**Incorreto:**

```tsx
<InputGroup>
  <Input placeholder="Pesquisar..." />
</InputGroup>
```

**Correto:**

```tsx
import { InputGroup, InputGroupInput } from "@/components/ui/input-group"

<InputGroup>
  <InputGroupInput placeholder="Pesquisar..." />
</InputGroup>
```

---

## Botões dentro de inputs usam InputGroup + InputGroupAddon

Nunca coloque um `Button` diretamente dentro ou ao lado de um `Input` com posicionamento customizado.

**Incorreto:**

```tsx
<div className="relative">
  <Input placeholder="Pesquisar..." className="pr-10" />
  <Button className="absolute right-0 top-0" size="icon">
    <SearchIcon />
  </Button>
</div>
```

**Correto:**

```tsx
import { InputGroup, InputGroupInput, InputGroupAddon } from "@/components/ui/input-group"

<InputGroup>
  <InputGroupInput placeholder="Pesquisar..." />
  <InputGroupAddon>
    <Button size="icon">
      <SearchIcon data-icon="inline-start" />
    </Button>
  </InputGroupAddon>
</InputGroup>
```

---

## Conjuntos de opcoes (2 a 7 opcoes) usam ToggleGroup

Não itere manualmente componentes `Button` com estado ativo.

**Incorreto:**

```tsx
const [selected, setSelected] = useState("daily")

<div className="flex gap-2">
  {["daily", "weekly", "monthly"].map((option) => (
    <Button
      key={option}
      variant={selected === option ? "default" : "outline"}
      onClick={() => setSelected(option)}
    >
      {option}
    </Button>
  ))}
</div>
```

**Correto:**

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"

<ToggleGroup spacing={2}>
  <ToggleGroupItem value="daily">Diário</ToggleGroupItem>
  <ToggleGroupItem value="weekly">Semanal</ToggleGroupItem>
  <ToggleGroupItem value="monthly">Mensal</ToggleGroupItem>
</ToggleGroup>
```

Combine com `Field` para grupos de alternância rotulados:

```tsx
<Field orientation="horizontal">
  <FieldTitle id="theme-label">Tema</FieldTitle>
  <ToggleGroup aria-labelledby="theme-label" spacing={2}>
    <ToggleGroupItem value="light">Claro</ToggleGroupItem>
    <ToggleGroupItem value="dark">Escuro</ToggleGroupItem>
    <ToggleGroupItem value="system">Sistema</ToggleGroupItem>
  </ToggleGroup>
</Field>
```

> **Nota:** `defaultValue` e as props `type`/`multiple` diferem entre base e radix. Veja [base-vs-radix.md](./base-vs-radix.md#togglegroup).

---

## FieldSet + FieldLegend para agrupar campos

Use `FieldSet` + `FieldLegend` para checkboxes, radios ou switches relacionados, não `div` com heading:

```tsx
<FieldSet>
  <FieldLegend variant="label">Preferências</FieldLegend>
  <FieldDescription>Selecione todas as opcoes aplicaveis.</FieldDescription>
  <FieldGroup className="gap-3">
    <Field orientation="horizontal">
      <Checkbox id="dark" />
      <FieldLabel htmlFor="dark" className="font-normal">Modo escuro</FieldLabel>
    </Field>
  </FieldGroup>
</FieldSet>
```

---

## Estados de validacao e desabilitado

Os dois atributos sao necessarios: `data-invalid`/`data-disabled` estilizam o `Field` (label e descricao), enquanto `aria-invalid`/`disabled` estilizam o controle.

```tsx
// Invalid.
<Field data-invalid>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input id="email" aria-invalid />
  <FieldDescription>Endereco de email invalido.</FieldDescription>
</Field>

// Disabled.
<Field data-disabled>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input id="email" disabled />
</Field>
```

Funciona para todos os controles: `Input`, `Textarea`, `Select`, `Checkbox`, `RadioGroupItem`, `Switch`, `Slider`, `NativeSelect`, `InputOTP`.
