# Ícones

**Sempre use a `iconLibrary` configurada do projeto para imports.** Verifique o campo `iconLibrary` no contexto do projeto: `lucide` → `lucide-react`, `tabler` → `@tabler/icons-react`, etc. Quando o projeto deste template usar lucide, importe de `lucide-react`.

---

## Ícones em Button usam o atributo data-icon

Adicione `data-icon="inline-start"` para prefixo ou `data-icon="inline-end"` para sufixo. Nao adicione classes de tamanho ao icone.

**Incorreto:**

```tsx
<Button>
  <SearchIcon className="mr-2 size-4" />
  Pesquisar
</Button>
```

**Correto:**

```tsx
<Button>
  <SearchIcon data-icon="inline-start" />
  Pesquisar
</Button>

<Button>
  Next
  <ArrowRightIcon data-icon="inline-end"/>
</Button>
```

---

## Sem classes de tamanho em ícones dentro de componentes

Os componentes gerenciam o tamanho dos ícones via CSS. Não adicione `size-4`, `w-4 h-4`, ou outras classes de tamanho a ícones dentro de `Button`, `DropdownMenuItem`, `Alert`, `Sidebar*`, ou outros componentes shadcn, a menos que o usuário peça explicitamente tamanhos customizados de ícone.

**Incorreto:**

```tsx
<Button>
  <SearchIcon className="size-4" data-icon="inline-start" />
  Pesquisar
</Button>

<DropdownMenuItem>
  <SettingsIcon className="mr-2 size-4" />
  Configuracoes
</DropdownMenuItem>
```

**Correto:**

```tsx
<Button>
  <SearchIcon data-icon="inline-start" />
  Pesquisar
</Button>

<DropdownMenuItem>
  <SettingsIcon />
  Configuracoes
</DropdownMenuItem>
```

---

## Passe ícones como objetos de componente, não como chaves string

Use `icon={CheckIcon}`, não uma chave string para um mapa de consulta.

**Incorreto:**

```tsx
const iconMap = {
  check: CheckIcon,
  alert: AlertIcon,
}

function StatusBadge({ icon }: { icon: string }) {
  const Icon = iconMap[icon]
  return <Icon />
}

<StatusBadge icon="check" />
```

**Correto:**

```tsx
// Importe da iconLibrary configurada do projeto (por exemplo, lucide-react ou @tabler/icons-react).
import { CheckIcon } from "lucide-react"

function StatusBadge({ icon: Icon }: { icon: React.ComponentType }) {
  return <Icon />
}

<StatusBadge icon={CheckIcon} />
```
