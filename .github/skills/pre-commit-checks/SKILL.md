---
name: pre-commit-checks
description: "Run all project validation checks before committing. Use when: before commit, validate changes, run checks, verify everything works, pre-commit, run all tests, check my work, ready to commit."
---

# Pre-Commit Checks

Runs all required validation checks before committing changes, as specified in the project's contribution guidelines.

## When to Use

- Before committing any changes
- After finishing a feature to verify nothing is broken
- When asked to validate or check work

## Procedure

### 1. Run Backend Tests

```bash
bash scripts/run-server-tests.sh
```

All Python unit tests must pass. If tests fail, fix the issues before continuing.

### 2. Build the Frontend (if client/ files changed)

```bash
cd client && npm run build
```

The build must succeed with no errors.

### 3. Run E2E Tests (if client/ files changed)

Start the application first, then run Playwright tests:

```bash
cd client && npx playwright test
```

### 4. Verify Documentation is Updated

Check whether these files need updates based on the changes made:

- **[README.md](../../README.md)** — Update if new functionality was added
- **[copilot-instructions.md](../../.github/copilot-instructions.md)** — Update if project structure, scripts, or programming guidance changed
- **Instruction files in `.github/instructions/`** — Update if patterns or conventions changed

### 5. Verify Code Standards

- All Python functions have type hints for parameters and return values
- SQLAlchemy models are used for database interactions
- Flask blueprints are used for route organization
- Svelte components use `<script lang="ts">`
- Tailwind CSS is used for styling (no raw CSS unless global)
- Dark mode theme is maintained

## Decision Tree

```
Changes include server/ files?
├── Yes → Run backend tests (step 1)
└── No  → Skip

Changes include client/ files?
├── Yes → Run build (step 2) AND e2e tests (step 3)
└── No  → Skip

New functionality added?
├── Yes → Update README and copilot-instructions (step 4)
└── No  → Skip
```

## Checklist

- [ ] Backend tests pass (`scripts/run-server-tests.sh`)
- [ ] Frontend builds successfully (`cd client && npm run build`)
- [ ] E2E tests pass (`cd client && npx playwright test`)
- [ ] README updated (if new features)
- [ ] Copilot instructions updated (if structure/patterns changed)
- [ ] Type hints present on all Python functions
- [ ] Dark mode theme maintained in UI changes
