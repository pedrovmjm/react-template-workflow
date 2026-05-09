---
name: feature-brief
description: Transforma pedidos de feature em briefs curtos e verificaveis, com problema, objetivos, escopo, criterios de aceite, riscos, dependencias e areas impactadas. Use antes do planejamento tecnico frontend.
---
## Proposito

Transformar um pedido de feature em um documento curto com problema, objetivos, escopo, criterios de aceite, riscos e areas impactadas.

## Quando usar

- Antes de qualquer planejamento tecnico.
- Quando o pedido do usuario ainda mistura objetivo, solucao e detalhes de UI.
- Quando e preciso alinhar o que entra e o que fica fora da entrega.

## Entradas

- Pedido do usuario.
- Contexto do produto.
- Rotas ou features existentes, quando necessario.

## Saidas

- Brief da feature na resposta do agente ou em template temporario.
- Criterios de aceite testaveis.
- Suposicoes, riscos, dependencias e areas impactadas.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/feature-brief.template.md` | Use quando precisar entregar um brief estruturado, repetir o formato entre agentes ou evitar omitir secoes importantes. | Modelo de saida para problema, objetivos, nao objetivos, criterios de aceite, edge cases, areas impactadas, riscos e dependencias. |

## Procedimento

1. Reescreva a feature em uma frase.
2. Separe problema, objetivo do usuario e objetivo de negocio.
3. Liste nao objetivos para reduzir escopo.
4. Registre suposicoes como itens verificaveis.
5. Escreva criterios de aceite em formato checavel.
6. Liste edge cases e areas impactadas.
7. Registre dependencias e riscos.
8. Crie registros de decisao quando houver escolhas relevantes.

## Checklist

- [ ] O problema esta claro.
- [ ] O objetivo do usuario esta separado da solucao tecnica.
- [ ] O objetivo de negocio esta explicito.
- [ ] Nao objetivos foram definidos.
- [ ] Criterios de aceite podem ser testados.
- [ ] Edge cases foram considerados.
- [ ] Areas impactadas foram listadas.
- [ ] Riscos e dependencias foram registrados.

## Exemplos

### Criterio de aceite bom

- [ ] Ao salvar um formulario valido, o usuario ve confirmacao e a lista e atualizada.

### Criterio de aceite fraco

- [ ] A tela deve funcionar bem.

## Anti-patterns

- Escrever solucao tecnica detalhada antes do problema.
- Omitir nao objetivos.
- Aceitar criterios impossiveis de validar.
- Ignorar dependencias de API, permissao ou design.
