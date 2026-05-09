# Composição de Componentes

## Conteúdo

- Itens sempre dentro de seu componente de grupo
- Callouts usam Alert
- Estados vazios usam o componente Empty
- Notificacoes toast usam sonner
- Escolhendo entre componentes de overlay
- Dialog, Sheet e Drawer sempre precisam de Title
- Card structure
- Button não tem prop isPending nem isLoading
- TabsTrigger deve ficar dentro de TabsList
- Avatar sempre precisa de AvatarFallback
- Use Separator em vez de hr bruto ou divs com borda
- Use Skeleton para placeholders de carregamento
- Use Badge em vez de spans customizados

---

## Itens sempre dentro de seu componente de grupo

Nunca renderize itens diretamente dentro do container de conteudo.

**Incorreto:**

```tsx
<SelectContent>
  <SelectItem value="apple">Apple</SelectItem>
  <SelectItem value="banana">Banana</SelectItem>
</SelectContent>
```

**Correto:**

```tsx
<SelectContent>
  <SelectGroup>
    <SelectItem value="apple">Apple</SelectItem>
    <SelectItem value="banana">Banana</SelectItem>
  </SelectGroup>
</SelectContent>
```

Isso se aplica a todos os componentes baseados em grupos:

| Item | Grupo |
|------|-------|
| `SelectItem`, `SelectLabel` | `SelectGroup` |
| `DropdownMenuItem`, `DropdownMenuLabel`, `DropdownMenuSub` | `DropdownMenuGroup` |
| `MenubarItem` | `MenubarGroup` |
| `ContextMenuItem` | `ContextMenuGroup` |
| `CommandItem` | `CommandGroup` |

---

## Callouts usam Alert

```tsx
<Alert>
  <AlertTitle>Aviso</AlertTitle>
  <AlertDescription>Algo precisa de atencao.</AlertDescription>
</Alert>
```

---

## Estados vazios usam o componente Empty

```tsx
<Empty>
  <EmptyHeader>
    <EmptyMedia variant="icon"><FolderIcon /></EmptyMedia>
    <EmptyTitle>Ainda não há projetos</EmptyTitle>
    <EmptyDescription>Comece criando um novo projeto.</EmptyDescription>
  </EmptyHeader>
  <EmptyContent>
    <Button>Criar Projeto</Button>
  </EmptyContent>
</Empty>
```

---

## Notificacoes toast usam sonner

```tsx
import { toast } from "sonner"

toast.success("Alterações salvas.")
toast.error("Algo deu errado.")
toast("Arquivo excluído.", {
  action: { label: "Desfazer", onClick: () => undoDelete() },
})
```

---

## Escolhendo entre componentes de overlay

| Caso de uso | Componente |
|----------|-----------|
| Tarefa focada que exige entrada | `Dialog` |
| Confirmacao de acao destrutiva | `AlertDialog` |
| Painel lateral com detalhes ou filtros | `Sheet` |
| Painel inferior mobile-first | `Drawer` |
| Informacao rapida no hover | `HoverCard` |
| Conteudo contextual pequeno no clique | `Popover` |

---

## Dialog, Sheet e Drawer sempre precisam de Title

`DialogTitle`, `SheetTitle`, `DrawerTitle` são obrigatórios para acessibilidade. Use `className="sr-only"` se estiver visualmente oculto.

```tsx
<DialogContent>
  <DialogHeader>
    <DialogTitle>Editar Perfil</DialogTitle>
    <DialogDescription>Atualize seu perfil.</DialogDescription>
  </DialogHeader>
  ...
</DialogContent>
```

---

## Card structure

Use a composição completa; não despeje tudo em `CardContent`:

```tsx
<Card>
  <CardHeader>
    <CardTitle>Membros da Equipe</CardTitle>
    <CardDescription>Gerencie sua equipe.</CardDescription>
  </CardHeader>
  <CardContent>...</CardContent>
  <CardFooter>
    <Button>Convidar</Button>
  </CardFooter>
</Card>
```

---

## Button não tem prop isPending nem isLoading

Componha com `Spinner` + `data-icon` + `disabled`:

```tsx
<Button disabled>
  <Spinner data-icon="inline-start" />
  Salvando...
</Button>
```

---

## TabsTrigger deve ficar dentro de TabsList

Nunca renderize `TabsTrigger` diretamente dentro de `Tabs`; sempre envolva em `TabsList`:

```tsx
<Tabs defaultValue="account">
  <TabsList>
    <TabsTrigger value="account">Conta</TabsTrigger>
    <TabsTrigger value="password">Senha</TabsTrigger>
  </TabsList>
  <TabsContent value="account">...</TabsContent>
</Tabs>
```

---

## Avatar sempre precisa de AvatarFallback

Sempre inclua `AvatarFallback` para quando a imagem falhar ao carregar:

```tsx
<Avatar>
  <AvatarImage src="/avatar.png" alt="Usuário" />
  <AvatarFallback>JD</AvatarFallback>
</Avatar>
```

---

## Use componentes existentes em vez de markup customizado

| Em vez de | Use |
|---|---|
| `<hr>` ou `<div className="border-t">` | `<Separator />` |
| `<div className="animate-pulse">` com divs estilizadas | `<Skeleton className="h-4 w-3/4" />` |
| `<span className="rounded-full bg-green-100 ...">` | `<Badge variant="secondary">` |
