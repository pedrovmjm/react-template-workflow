---
name: security-review
description: Revisa riscos de seguranca frontend, incluindo XSS, HTML/Markdown, Mermaid, PlantUML, uploads, cookies, tokens, localStorage/sessionStorage, links externos, validacao de input e dependencias. Use antes da revisao final ou sempre que houver entrada de usuario ou storage client-side.
---

# Skill: security-review

## Nome

security-review

## Proposito

Revisar riscos de seguranca frontend e definir mitigacoes proporcionais.

## Quando usar

- Apos implementacao.
- Antes da revisao final.
- Sempre que houver HTML, Markdown, Mermaid, PlantUML, upload, cookies, tokens, localStorage/sessionStorage, links externos ou entrada de usuario.

## Entradas

- Brief.
- Plano de componentes.
- Plano do content renderer, quando aplicavel.
- Codigo implementado.
- Dependencias adicionadas.

## Saidas

- Revisao de seguranca.
- Achados por severidade.
- Mitigacoes obrigatorias e opcionais.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/security-review.template.md` | Use em revisoes de seguranca antes do fechamento ou quando houver entrada de usuario, conteudo rico, storage, upload, tokens ou dependencia nova. | Modelo de saida para superficies avaliadas, achados por severidade, mitigacoes, riscos aceitos e bloqueios. |
| `references/browser-storage-auth.md` | Use quando houver cookies, JWT, session ID, refresh token, localStorage, sessionStorage, IndexedDB ou persistencia client-side. | Politica e referencias OWASP/MDN para decidir onde guardar credenciais, preferencias e dados sensiveis. |

## Procedimento

1. Liste superficies de entrada do usuario.
2. Revise XSS e HTML injection.
3. Revise Markdown, Mermaid e PlantUML.
4. Revise cookies, tokens, storage e URLs.
5. Revise upload e validacao.
6. Revise links externos.
7. Revise dependencias.
8. Classifique riscos e recomende mitigacao.

## Checklist

- [ ] Conteudo do usuario e tratado como nao confiavel.
- [ ] Nao ha HTML bruto sem sanitizacao.
- [ ] Tokens nao aparecem em storage inadequado ou logs.
- [ ] Credenciais nao sao persistidas em `localStorage`/`sessionStorage`.
- [ ] Cookies sensiveis usam atributos seguros e nao dependem de `document.cookie`.
- [ ] Uploads validam tipo, tamanho e conteudo quando possivel.
- [ ] Links externos em nova aba usam `rel`.
- [ ] Dependencias novas tem justificativa.

## Exemplos

- Links externos: `target="_blank"` exige `rel="noopener noreferrer"`.
- Markdown: sanitizar antes de renderizar HTML.
- PlantUML: usar service boundary para controlar endpoint e limites.
- Storage permitido: tema, densidade, idioma, preferencia de layout e filtros nao sensiveis.
- Storage bloqueado: JWT, refresh token, session ID, segredo, PII e qualquer dado usado como prova de autenticacao/autorizacao.

## Anti-patterns

- Confiar em extensao de arquivo.
- Guardar token sensivel em `localStorage` sem necessidade.
- Guardar JWT, refresh token ou session ID em `localStorage`/`sessionStorage`.
- Expor token em URL, log, query string ou erro de API.
- Usar `dangerouslySetInnerHTML` como atalho.
- Expor stack trace ou resposta bruta de API ao usuario.
