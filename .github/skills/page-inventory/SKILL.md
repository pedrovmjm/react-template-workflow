---
name: page-inventory
description: Cria, revisa e atualiza inventarios funcionais de paginas, registrando motivo de existencia, responsabilidade, rota, arquivos, estados esperados, dados, dependencias, criterios de aceite, riscos e oportunidades futuras. Use quando uma pagina nova for planejada/criada, quando uma pagina existente for alterada ou quando o workflow precisar consultar a memoria de produto da tela.
---

## Proposito

Manter uma memoria curta, verificavel e util de cada pagina do produto, para que planejamento, implementacao, testes e revisoes partam do motivo real da tela existir.

O inventario nao substitui brief, arquitetura, layout ou testes. Ele conecta essas decisoes em um registro de pagina: por que a pagina existe, qual responsabilidade ela tem, o que se espera dela hoje e que oportunidades podem ficar para depois.

## Quando usar

- Ao criar ou planejar uma pagina nova.
- Ao revisar uma pagina existente e precisar entender responsabilidade, rota, estados, dados ou pendencias.
- Ao alterar comportamento principal, fluxo, permissoes, dados, estados de UI ou arquivos relevantes de uma pagina.
- Ao fechar uma implementacao de pagina e registrar o que foi realmente entregue.
- Ao preparar handoff para produto, design, backend, QA ou outro agente.

## Entradas

- Pedido do usuario.
- Brief da feature.
- Mapa de fluxo, quando existir.
- Plano de arquitetura, rota e ownership de arquivos.
- Plano de layout e componentes.
- Codigo ou arquivos reais da pagina, quando ja existir implementacao.
- Gates executados, riscos aceitos e pendencias.

## Saidas

- Inventario planejado, quando a pagina ainda nao existe.
- Inventario implementado, quando a pagina ja existe no codigo.
- Revisao de divergencias entre inventario e codigo.
- Lista curta de atualizacoes necessarias quando uma mudanca altera a responsabilidade da pagina.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/page-inventory.template.md` | Use para criar ou atualizar inventario de pagina de forma consistente. | Modelo com motivo de existencia, responsabilidade, experiencia esperada, dados, UI, qualidade e futuro. |

## Procedimento

1. Identifique a pagina, rota, status e arquivos principais.
2. Declare por que a pagina existe, separando problema, objetivo do usuario e objetivo de negocio.
3. Defina responsabilidade positiva e nao responsabilidade da pagina.
4. Registre experiencia esperada: entrada, jornada principal, saidas e estados obrigatorios.
5. Liste dados, dependencias, permissoes, origem das informacoes e riscos de dados sensiveis.
6. Conecte a UI ao design system, componentes shadcn/ui e decisoes visuais relevantes.
7. Relacione criterios de aceite, gates, testes recomendados e riscos conhecidos.
8. Separe ideias futuras do escopo atual, sem transformar oportunidade em requisito implicito.
9. Quando houver codigo existente, compare inventario e implementacao real e marque divergencias.

## Regras

- Inventario deve ser curto o bastante para ser lido antes de planejar ou codar.
- Nao inventar rota, arquivo, API ou permissao sem fonte real; marcar como decisao aberta.
- Diferenciar claramente planejado, implementado e pendente.
- Nao duplicar detalhes extensos de arquitetura, design system ou testes; referenciar a decisao essencial.
- Registrar mudancas de responsabilidade como decisao relevante.
- Ideias futuras devem ficar fora dos criterios de aceite atuais.
- Se nao houver artefato persistente solicitado, entregar o inventario na resposta do agente.
- Se houver artefato persistente solicitado, manter o formato estavel e evitar documentos vazios ou checklists soltos.

## Checklist

- [ ] A pagina tem nome, rota e status.
- [ ] Arquivos principais foram listados quando existem.
- [ ] O motivo de existencia esta claro.
- [ ] Responsabilidades e nao responsabilidades foram separadas.
- [ ] Jornada principal e estados obrigatorios foram registrados.
- [ ] Dados, permissoes e dependencias foram mapeados.
- [ ] UI referencia design system, componentes ou baseline aprovado.
- [ ] Criterios de aceite e gates esperados estao visiveis.
- [ ] Futuro esta separado do escopo atual.
- [ ] Divergencias entre codigo e inventario foram apontadas quando aplicavel.

## Anti-patterns

- Criar inventario como burocracia sem impacto no planejamento.
- Repetir o brief inteiro em vez de registrar memoria da pagina.
- Misturar ideias futuras com aceite da entrega atual.
- Documentar responsabilidade vaga como "mostrar informacoes".
- Omitir estados vazios, erro, loading ou permissao.
- Tratar documentacao desatualizada como fonte confiavel sem comparar com o codigo.

## Criterios de conclusao

- Outro agente consegue entender a pagina antes de planejar ou editar.
- Produto, design, backend e QA conseguem ver o que a pagina promete entregar.
- Mudancas relevantes de comportamento tem uma atualizacao documental clara ou uma pendencia registrada.
