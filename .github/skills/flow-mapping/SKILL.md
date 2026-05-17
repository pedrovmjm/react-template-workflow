---
name: flow-mapping
description: Mapeia fluxo do usuario, fluxo de dados, estados do painel e dependencias de backend antes da arquitetura e implementacao frontend. Use depois do brief e antes do planejamento tecnico de telas profissionais.
---

# Skill: flow-mapping

## Nome

flow-mapping

## Proposito

Criar um mapa pre-implementacao que conecte objetivo do usuario, jornada, dados necessarios, estados da interface e contratos esperados do backend.

Use esta skill para evitar que a implementacao comece apenas por componentes ou layout, sem uma compreensao clara do que a tela precisa mostrar, permitir e comunicar.

## Quando usar

- Depois do brief da feature.
- Antes da arquitetura, layout, planejamento de componentes ou implementacao.
- Em paineis, dashboards, formularios, tabelas, telas de detalhe, CRUDs, funis e fluxos multi-etapa.
- Quando backend e frontend precisam alinhar payload, filtros, status, permissoes e acoes.
- Quando houver incerteza sobre jornada do usuario, estados da tela ou origem dos dados.

## Entradas

- Pedido do usuario e brief.
- Rotas e telas existentes.
- Entidades de dominio conhecidas.
- Contratos de API, mocks, exemplos de payload ou modelos existentes.
- Regras de permissao, status, papeis e transicoes.
- Design system e telas similares como contexto, sem decidir layout final.

## Saidas

- Fluxo do usuario.
- Mapa do painel por secao.
- Fluxo de dados e origem de cada informacao.
- Lista de acoes, eventos e efeitos esperados.
- Requisitos de backend.
- Estados de UI por area critica.
- Perguntas abertas e bloqueios.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/flow-mapping.template.md` | Use quando precisar entregar um mapa completo e repetivel antes da implementacao. | Modelo de saida para jornada, painel, dados, backend, estados, riscos e gates. |
| `references/ux-experience-cases.md` | Use quando precisar embasar decisoes de jornada, estados de tela, mensagens, empty/error states ou alinhamento frontend-backend com exemplos reais. | Referencias curtas de GOV.UK, GOV.UK One Login, Atlassian, Stripe e NN/g, com aplicacao pratica no workflow. |

## Procedimento

1. Reescreva o objetivo principal do usuario em uma frase.
2. Liste o caminho feliz da jornada, da entrada ate o feedback final.
3. Mapeie fluxos alternativos, bloqueios, permissoes e erros relevantes.
4. Divida o painel em secoes operacionais, sem decidir visual final.
5. Para cada secao, liste dados exibidos, dados editaveis, dados derivados e acoes.
6. Identifique origem de cada dado: API, rota, query string, cache, estado local, permissao ou constante.
7. Liste filtros, ordenacao, paginacao, busca, agregacoes e includes necessarios.
8. Descreva mutations e eventos com efeito esperado, feedback e invalidacao provavel.
9. Registre requisitos de backend e perguntas abertas.
10. Entregue gates que precisam estar claros antes da implementacao.

## Uso das referencias

- Leia `references/ux-experience-cases.md` quando a feature envolver uma tela profissional nova, painel operacional, dashboard, fluxo multi-etapa, empty/error state ou alinhamento com backend.
- Use as referencias para justificar decisoes de fluxo e estados, nao para copiar UI externa.
- Ao citar um caso real na saida, conecte o exemplo ao risco da feature: jornada quebrada, dado ausente, mensagem fraca, permissao nao mapeada ou contrato de backend incompleto.

## Checklist

- [ ] Jornada principal tem entrada, passos, decisao e feedback.
- [ ] Fluxos alternativos e erros foram considerados.
- [ ] Cada secao do painel tem dados e acoes claros.
- [ ] Dados exibidos, editaveis e derivados estao separados.
- [ ] Origem dos dados foi identificada.
- [ ] Filtros, paginacao, ordenacao e agregacoes foram mapeados.
- [ ] Estados loading, empty, error, success e permission denied foram previstos.
- [ ] Requisitos de backend foram descritos em termos verificaveis.
- [ ] Perguntas abertas nao foram transformadas em suposicoes silenciosas.

## Exemplos

### Requisito de backend bom

- `GET /orders?status=&q=&page=` retorna itens paginados, totais por status e permissao `canCancel` por item.

### Requisito de backend fraco

- Backend precisa mandar os pedidos da tela.

### Estado de painel bom

- Lista vazia com filtro ativo mostra empty state contextual e acao para limpar filtros.

### Estado de painel fraco

- Se nao tiver dado, mostrar alguma mensagem.

## Anti-patterns

- Comecar por grid, cards ou shadcn/ui antes da jornada.
- Descrever payload como "dados necessarios" sem campos.
- Omitir permissoes e status bloqueantes.
- Tratar erro e empty state como detalhe de implementacao.
- Criar cache, store ou mutation sem mapear o efeito no usuario.
