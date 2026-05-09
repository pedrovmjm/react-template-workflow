# Performance Basica no React

Use esta referencia dentro de `react-best-practices`. Nao crie um agente separado so para performance comum de React.

## Checklist

- Estado derivado simples nao usa `useEffect`.
- `memo`, `useMemo` e `useCallback` aparecem somente quando reduzem custo real ou estabilizam contrato necessario.
- Rotas, editores, graficos e paineis pesados podem usar import dinamico.
- Listas grandes tem paginacao, virtualizacao ou limite explicito.
- Imagens fora do primeiro viewport usam `loading="lazy"` e dimensoes definidas.
- Bibliotecas grandes sao justificadas pelo valor que entregam.
- Build continua passando apos mudanca de imports ou lazy loading.

## Exemplo: lazy loading de painel pesado

```tsx
import { lazy, Suspense } from "react";

const ReportsPanel = lazy(() => import("./reports-panel"));

export function ReportsRoute() {
  return (
    <Suspense fallback={<p>Carregando relatorios...</p>}>
      <ReportsPanel />
    </Suspense>
  );
}
```

## Exemplo: evitar estado derivado

```tsx
const visibleItems = items.filter((item) => {
  return item.name.toLowerCase().includes(query.toLowerCase());
});
```
