# Exemplos de Teste

## Componente com Testing Library

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import { SaveButton } from "./save-button";

describe("SaveButton", () => {
  it("chama onSave ao clicar", async () => {
    const user = userEvent.setup();
    const onSave = vi.fn();

    render(<SaveButton isSaving={false} onSave={onSave} />);

    await user.click(screen.getByRole("button", { name: /salvar/i }));

    expect(onSave).toHaveBeenCalledTimes(1);
  });
});
```

## MSW

```ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/projects", () => {
    return HttpResponse.json([{ id: "p1", name: "Dashboard" }]);
  }),
];
```

## Playwright

```ts
import { expect, test } from "@playwright/test";

test("cria projeto", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: /novo projeto/i }).click();
  await page.getByLabel(/nome/i).fill("Dashboard");
  await page.getByRole("button", { name: /^criar$/i }).click();

  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
});
```
