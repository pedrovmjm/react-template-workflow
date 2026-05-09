---
name: content-renderer
description: Planeja renderizacao segura e reutilizavel de Markdown, Mermaid e PlantUML no frontend, com sanitizacao, fallback, service boundary, estados de loading/erro e testes. Use quando a feature exibir conteudo rico ou HTML controlado.
---

# Skill: content-renderer

## Nome

content-renderer

## Proposito

Planejar renderizacao segura e reutilizavel de Markdown, Mermaid e PlantUML no frontend.

## Quando usar

- Quando a feature precisa exibir conteudo rico.
- Quando houver blocos de codigo fenced Markdown.
- Quando Mermaid ou PlantUML forem aceitos como entrada.

## Entradas

- Brief da feature.
- Plano de componentes.
- Requisitos de seguranca.

## Saidas

- Plano de content renderer.
- Estrategia de renderizacao, seguranca e testes.

## Artefatos auxiliares

| Artefato | Quando usar | Para que serve |
| --- | --- | --- |
| `templates/content-renderer-plan.template.md` | Use ao planejar renderer de Markdown, fenced code, Mermaid, PlantUML ou HTML controlado. | Modelo de saida para tipos de conteudo, arquitetura, sanitizacao, fallback, loading/error, service boundary, testes e riscos. |

## Procedimento

1. Identifique tipos de conteudo aceitos.
2. Defina API publica do `RichContentRenderer`.
3. Defina estrategia Markdown com sanitizacao.
4. Defina Mermaid com fallback de erro.
5. Defina PlantUML por service seguro.
6. Defina loading, empty e error states.
7. Defina testes de renderizacao e seguranca.
8. Registre riscos de dependencias.

## Checklist

- [ ] Markdown suporta fenced code blocks.
- [ ] Markdown nao confiavel e sanitizado.
- [ ] Mermaid renderiza diagrama com fallback.
- [ ] PlantUML usa service boundary.
- [ ] Nao ha `dangerouslySetInnerHTML` inseguro.
- [ ] Renderers sao reutilizaveis.
- [ ] Estados de erro e loading existem.

## Exemplos

```txt
src/features/content-renderer/
├── components/
├── hooks/
├── services/
├── types/
└── index.ts
```

## Anti-patterns

- Renderizar HTML bruto do usuario.
- Misturar parsing, chamada remota e layout em um unico componente.
- Acoplar Mermaid ou PlantUML a uma pagina especifica.
- Ignorar erro de diagrama invalido.
