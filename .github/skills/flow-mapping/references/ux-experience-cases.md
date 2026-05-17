# Referencias de UX e Casos Reais

Use este arquivo como apoio quando o mapa de fluxo precisar de exemplos reais e criterios de boa experiencia antes do desenvolvimento frontend.

## Principios praticos

### Comecar por necessidades reais do usuario

Fonte: GOV.UK Service Manual, "Learning about users and their needs"
https://www.gov.uk/service-manual/user-centred-design/user-needs

Aplicacao no workflow:

- Escreva a necessidade do usuario antes da solucao de tela.
- Trate opinioes internas como suposicoes ate haver evidencia.
- Registre quem usa, o que quer concluir, quando a necessidade aparece e qual resultado espera.
- Para backend, converta a necessidade em dados verificaveis: campos, status, permissoes, historico, anexos, filtros ou acoes.

Exemplo de saida esperada:

- "Como analista financeiro, preciso identificar pagamentos com risco hoje para priorizar cobranca antes do fechamento."
- Dados minimos: `paymentId`, cliente, valor, vencimento, status, risco, responsavel, proxima acao permitida.

### Mapear a jornada inteira, nao so a tela

Fonte: GOV.UK Service Manual, "Map and understand a user's whole problem"
https://www.gov.uk/service-manual/design/map-a-users-whole-problem

Aplicacao no workflow:

- Inclua o que acontece antes e depois da tela.
- Identifique touchpoints externos: email, suporte, planilha, sistema legado, aprovacao manual, notificacao ou exportacao.
- Procure dead ends: usuario nao sabe qual acao tomar, nao entende status, perde contexto ao voltar, nao consegue corrigir erro.
- A tela profissional deve reduzir ambiguidade operacional, nao apenas exibir dados.

### Criar experience maps quando ha varias etapas

Fonte: GOV.UK Service Manual, "Creating an experience map"
https://www.gov.uk/service-manual/user-research/creating-an-experience-map

Aplicacao no workflow:

- Para fluxos longos, mapeie fases, acoes, pensamentos, sentimentos, dependencias e pontos de dor.
- Use o mapa para descobrir interdependencias entre frontend, backend, atendimento, operacao e regras de negocio.
- Converta pontos de dor em requisitos: visibilidade de status, reentrada segura, validacao antecipada, mensagens acionaveis e historico.

## Casos reais

### GOV.UK One Login: jornada antes da implementacao

Fonte: GOV.UK One Login, "Sign in user journey maps"
https://www.sign-in.service.gov.uk/documentation/user-journeys

O caso mostra mapas de jornada para opcoes diferentes de autenticacao. A decisao nao e apenas "criar tela de login": a experiencia muda conforme o usuario cria conta antes ou durante o servico.

Como aplicar:

- Liste entradas possiveis do usuario.
- Compare fluxos alternativos antes de escolher arquitetura.
- Identifique quando o usuario volta para o servico original.
- Para backend, explicite sessoes, redirecionamentos, estados de autenticacao, erros, expiracao e recuperacao.

Checklist derivado:

- [ ] O usuario sabe por que precisa autenticar agora?
- [ ] Ha retorno claro para a tarefa original?
- [ ] Erros de credencial, sessao expirada e 2FA tem recuperacao?
- [ ] O backend entrega estado suficiente para o frontend mostrar progresso e proximo passo?

### Stripe Apps: empty state como parte do fluxo

Fonte: Stripe Docs, "Empty state for Stripe Apps"
https://docs.stripe.com/stripe-apps/patterns/empty-state

O caso reforca que uma tela sem dados nao deve parecer quebrada. Quando nao ha dados disponiveis, o usuario precisa entender o motivo e, quando util, ir direto para o lugar certo no Dashboard.

Como aplicar:

- Diferencie primeiro uso, filtro sem resultado, permissao sem acesso e dados ainda carregando.
- Empty state precisa dizer por que nao ha dados e qual proxima acao faz sentido.
- Para backend, diferencie lista vazia real de erro, permissao e filtro sem resultado.

Checklist derivado:

- [ ] Empty state muda quando ha filtro ativo?
- [ ] Primeiro uso tem acao de onboarding ou criacao?
- [ ] Falta de permissao nao aparece como lista vazia?
- [ ] Backend retorna metadados suficientes para diferenciar os casos?

### Atlassian: mensagens acionaveis em erro, vazio e informacao

Fontes:

- Error messages: https://atlassian.design/foundations/content/designing-messages/error-messages
- Empty state: https://atlassian.design/foundations/content/designing-messages/empty-state
- Designing messages overview: https://design-system-docs-proxy.services.atlassian.com/foundations/content/designing-messages/

O caso mostra que estados de sistema sao parte da experiencia. Uma mensagem profissional informa o que aconteceu, por que importa e o que a pessoa pode fazer agora.

Como aplicar:

- Mensagem de erro deve ser curta, segura e orientada a proximo passo.
- Empty state deve ser contextual: tarefa concluida, primeiro uso, busca sem resultado ou dados indisponiveis.
- Info/warning/success devem usar componente certo e nao interromper o fluxo sem necessidade.
- Para backend, defina codigos/erros que permitam mensagens especificas sem vazar detalhe tecnico.

Checklist derivado:

- [ ] Cada erro esperado tem recuperacao ou proximo passo?
- [ ] Erro tecnico bruto nunca aparece para o usuario?
- [ ] Success confirma o resultado real da acao?
- [ ] Warning aparece antes de perda de dados ou acao irreversivel?

### NN/g: estrutura minima de journey map

Fontes:

- Customer Journey Map Template: https://media.nngroup.com/media/articles/attachments/JMTemplate.pdf
- Empathy Mapping: https://www.nngroup.com/articles/empathy-mapping/

Aplicacao no workflow:

- Use actor/persona, cenario, expectativas, fases, acoes, pensamentos, falas/duvidas, insights e ownership interno.
- Em paineis internos, o "ownership interno" ajuda a descobrir quem fornece cada dado, quem corrige erro e quem responde pela acao.
- O mapa deve gerar decisao: prioridade, contrato de backend, ponto de instrumentacao, componente, estado de UI ou pergunta aberta.

Checklist derivado:

- [ ] Existe ator principal e cenario claro?
- [ ] Fases da jornada foram nomeadas?
- [ ] Acoes e duvidas do usuario foram mapeadas?
- [ ] Insights viraram requisitos ou decisoes abertas?
- [ ] Existe ownership para dados, acoes e excecoes?

## Como transformar referencia em decisao de frontend

Use este formato curto:

```md
## Decisao UX

- Contexto:
- Referencia usada:
- Risco evitado:
- Decisao:
- Impacto em backend:
- Impacto em UI:
- Pergunta aberta:
```

Exemplo:

```md
## Decisao UX

- Contexto: lista de cobranças pode voltar vazia.
- Referencia usada: Stripe empty state + Atlassian empty state.
- Risco evitado: usuario interpretar ausencia de dados como erro.
- Decisao: separar primeiro uso, filtro sem resultado e sem permissao.
- Impacto em backend: resposta precisa diferenciar `total=0`, `filteredTotal=0` e `forbidden`.
- Impacto em UI: tres mensagens e CTAs distintos.
- Pergunta aberta: quem pode liberar permissao para o usuario?
```
