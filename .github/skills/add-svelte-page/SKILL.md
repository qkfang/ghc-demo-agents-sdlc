---
name: add-svelte-page
description: "Scaffold a new frontend page with Astro routing and Svelte component. Use when: add page, new page, create frontend view, add UI page, new Svelte component with page, add route to frontend, new client page."
---

# Add Svelte Page

Creates a new frontend page using Astro for routing and a Svelte component for interactive content, following project conventions.

## When to Use

- Adding a new page to the frontend (e.g., publishers list, about page variant)
- Creating a detail view for a new resource
- Adding a new interactive section to the site

## Procedure

### 1. Create the Svelte Component

Create `client/src/components/<Name>.svelte` following the pattern in [GameList.svelte](../../client/src/components/GameList.svelte) or [GameDetails.svelte](../../client/src/components/GameDetails.svelte):

- Use `<script lang="ts">` with typed interfaces for API data
- Fetch data from the backend API using `onMount` with `async/await`
- Track `loading`, `error`, and data state
- Handle all states in the template: loading skeleton, error message, empty state, and data display
- Use Tailwind CSS classes exclusively for styling (no `<style>` blocks unless scoped/global is needed)
- Follow dark mode theme: `bg-slate-800/60`, `text-slate-100`, `border-slate-700/50`
- Use rounded corners: `rounded-xl`, `rounded-lg`
- Add `data-testid` attributes to key elements for e2e testing

### 2. Create the Astro Page

Create the page file in `client/src/pages/`:

- For list pages: `client/src/pages/<resource>.astro`
- For detail pages: `client/src/pages/<resource>/[id].astro`

Follow the pattern in [index.astro](../../client/src/pages/index.astro) or [[id].astro](../../client/src/pages/game/[id].astro):

- Import `Layout` from `../../layouts/Layout.astro` (adjust relative path)
- Import the Svelte component
- For list components: use `client:only="svelte"` directive
- For detail components that need SSR params: use `client:load` and pass the ID from `Astro.params`
- For dynamic routes: add `export const prerender = false;` in frontmatter
- Set a descriptive `<Layout title="...">`

### 3. Wire Up Navigation (if needed)

Update [Header.astro](../../client/src/components/Header.astro) to add a nav link to the new page.

### 4. Verify the Build

```bash
cd client && npm run build
```

### 5. Add E2E Tests (if applicable)

Create `client/e2e-tests/<resource>.spec.ts` following existing patterns in:
- [home.spec.ts](../../client/e2e-tests/home.spec.ts)
- [games.spec.ts](../../client/e2e-tests/games.spec.ts)

Run e2e tests:
```bash
cd client && npx playwright test
```

## Styling Reference

- Background: `bg-slate-800/60 backdrop-blur-sm`
- Borders: `border border-slate-700/50`
- Hover effects: `hover:border-blue-500/50 hover:shadow-blue-500/10`
- Text: headings `text-slate-100`, body `text-slate-300`, muted `text-slate-400`
- Transitions: `transition-all duration-300`
- Cards: `rounded-xl overflow-hidden shadow-lg`
- Buttons: `px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg`

## Checklist

- [ ] Svelte component uses TypeScript with typed interfaces
- [ ] Component handles loading, error, and empty states
- [ ] Dark mode theme with Tailwind classes
- [ ] Rounded corners on all boxes/cards
- [ ] Astro page uses Layout wrapper
- [ ] Correct client directive (`client:only="svelte"` or `client:load`)
- [ ] Dynamic routes have `prerender = false`
- [ ] Build succeeds (`npm run build` in client/)
- [ ] Navigation updated if page is user-facing
