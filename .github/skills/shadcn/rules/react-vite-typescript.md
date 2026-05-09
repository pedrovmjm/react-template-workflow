# React, Vite, TypeScript e Lucide

Estas regras complementam shadcn/ui quando o projeto usa React + Vite + TypeScript + lucide.

## React

- Componentes devem ser pequenos, previsiveis e orientados a composicao.
- Nao use `useEffect` para derivar estado simples; derive durante render quando possivel.
- Use `useEffect` para sincronizacao com sistemas externos: API do browser, subscriptions, timers, eventos globais e bibliotecas imperativas.
- Extraia hooks quando uma regra de comportamento ficar grande, reutilizavel ou dificil de testar dentro do componente.
- Dados remotos devem passar por service/query hook, nao por chamada direta em JSX.
- Estado local fica local; contexto ou store global so entram quando varios pontos da arvore precisam coordenar o mesmo estado.

## Vite

- Variaveis expostas ao cliente precisam de prefixo `VITE_`.
- Segredos nunca devem estar no bundle client-side.
- Respeite aliases definidos em `vite.config.*` e `tsconfig*.json`.
- Nao use APIs Node em codigo que roda no navegador.
- Imports dinamicos devem ter fallback de loading e erro quando impactarem a experiencia.
- Evite side effects globais em modulos importados por componentes.

## TypeScript

- Evite `any`; prefira tipos de dominio, `unknown` validado, generics restritos ou tipos inferidos de schemas.
- Use Zod ou parser equivalente para dados externos, payloads de formulario e respostas de API nao confiaveis.
- Prefira discriminated unions para estados mutuamente exclusivos, como loading/success/error.
- Evite casts (`as`) para esconder erro de modelagem.
- Props exportadas devem descrever o contrato real do componente.
- `index.ts` deve melhorar ergonomia sem criar dependencia circular ou esconder acoplamento ruim.

## Estado e Dados

- TanStack Query deve ser o padrao para server state quando houver cache, retry, invalidacao ou multiplos consumidores.
- Zustand deve ser usado apenas para estado de cliente compartilhado.
- Nao duplique server state em store global.
- Mutations precisam tratar pending, sucesso, erro e invalidacao ou atualizacao de cache.

## Lucide

- Quando `iconLibrary` for `lucide`, importe icones de `lucide-react`.
- Em `Button`, use `data-icon="inline-start"` ou `data-icon="inline-end"`.
- Nao aplique `size-*`, `w-*`, `h-*` ou margem manual em icones dentro de componentes shadcn que ja controlam tamanho.
- Passe icones como componentes (`icon={CheckIcon}`), nao como strings para lookup.
- Botoes apenas com icone precisam de nome acessivel, como `aria-label`.

## Checklist

- [ ] Nenhum segredo foi exposto via `VITE_`.
- [ ] Aliases reais do projeto foram usados.
- [ ] Componentes nao chamam API direto no JSX.
- [ ] Efeitos tem motivo claro.
- [ ] Tipos evitam `any` e casts desnecessarios.
- [ ] Server state nao foi duplicado em Zustand.
- [ ] Icones lucide seguem `iconLibrary`, `data-icon` e acessibilidade.
