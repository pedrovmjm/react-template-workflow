# Browser Storage e Autenticacao

Use esta referencia quando a feature envolver cookies, tokens, localStorage, sessionStorage, IndexedDB, session ID, refresh token ou dados sensiveis no cliente.

## Fontes

- OWASP HTML5 Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html
- OWASP Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP JSON Web Token Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
- MDN `localStorage`: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
- MDN HTTP cookies: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

## Politica padrao

- Nao guardar JWT, refresh token, session ID, segredo, PII ou dado de autorizacao em `localStorage` ou `sessionStorage`.
- Preferir cookie definido pelo backend com `HttpOnly`, `Secure` e `SameSite` quando a arquitetura permitir.
- Se usar cookie para autenticacao, validar risco de CSRF e alinhar `SameSite`, metodo HTTP, CSRF token ou BFF conforme arquitetura.
- `localStorage` e `sessionStorage` sao acessiveis por JavaScript da origem; uma falha de XSS pode ler ou alterar os dados.
- Dados vindos de storage client-side nunca sao confiaveis: validar, normalizar e tratar como preferencia, nao como permissao.
- Nao colocar tokens, session IDs, PII ou segredos em URL, query string, fragment, logs, analytics ou mensagem de erro.

## O que pode ir para localStorage/sessionStorage

- Tema visual.
- Idioma.
- Densidade de tabela.
- Preferencia de layout.
- Ultima aba aberta.
- Filtros nao sensiveis de conveniencia, quando a URL nao for a melhor fonte da verdade.

## O que nao pode ir para localStorage/sessionStorage

- Access token.
- Refresh token.
- Session ID.
- API key.
- Segredo.
- Dados pessoais sensiveis.
- Permissoes como fonte de verdade.
- Dados que permitam escalar privilegio ou assumir identidade.

## Decisao recomendada

```md
## Storage/Auth

- Dado:
- Sensibilidade:
- Persistencia necessaria:
- Local recomendado:
- Por que nao URL:
- Por que nao localStorage/sessionStorage:
- Mitigacoes:
- Dono backend/frontend:
```

## Checklist

- [ ] O dado e credencial, token, segredo, PII ou autorizacao?
- [ ] A persistencia e realmente necessaria?
- [ ] Cookie sensivel e definido pelo backend, nao por `document.cookie`?
- [ ] Cookie sensivel usa `HttpOnly`, `Secure` e `SameSite` adequado?
- [ ] CSRF foi considerado quando cookie autentica requests?
- [ ] `localStorage`/`sessionStorage` contem apenas preferencia nao sensivel?
- [ ] URL nao contem token, segredo ou PII?
- [ ] Logout limpa estado client-side nao sensivel e invalida sessao no backend quando aplicavel?
