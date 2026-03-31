# Project Guidelines

## Overview

Tailspin Toys crowdfunding platform for games with a developer theme. Flask backend API with SQLAlchemy ORM, Astro/Svelte frontend with Tailwind CSS.

## Architecture

- `server/` — Flask backend (blueprints, SQLAlchemy models, RESTful API)
- `client/` — Astro/Svelte frontend (Tailwind CSS, dark mode theme)
- `scripts/` — Development and deployment scripts
- `data/` — SQLite database files
- `docs/` — Project documentation (deployed to GitHub Pages)

## Code Style

### Python / Flask

- Use type hints for all function parameters and return values
- Use SQLAlchemy models for database interactions
- Use Flask blueprints for organizing routes (register in `server/app.py`)
- Follow RESTful API design principles
- See `server/routes/games.py` as the endpoint prototype

### Svelte / Astro

- Use Svelte for interactive components; Astro for page routing and static content
- Follow Svelte's reactive programming model
- Create reusable components when functionality is used in multiple places

### Styling

- Use Tailwind CSS classes for styling
- Maintain dark mode theme throughout the application
- Use rounded corners for UI elements
- Follow modern UI/UX principles with clean, accessible interfaces

### GitHub Actions Workflows

- Explicitly set workflow permissions
- Add comments to document what tasks are being performed

## Build and Test

Use the existing scripts rather than running commands manually:

- `scripts/setup-env.sh` — Install all Python and Node dependencies
- `scripts/run-server-tests.sh` — Set up env then run all Python tests
- `scripts/start-app.sh` — Set up env then start both backend and frontend servers

### Pre-commit Checklist

- Run Python tests (`scripts/run-server-tests.sh`) to verify backend
- For frontend changes, run builds in `client/` and the end-to-end tests
- When making API changes, update and run corresponding tests
- When updating models, include database migrations if needed

## Conventions

- New endpoints require tests — use `unittest` with in-memory SQLite (see `.github/instructions/python-tests.instructions.md`)
- New functionality must include README updates
- Keep this file and `.github/copilot-instructions.md` updated with any structural or guidance changes
- The Python virtual environment lives in `venv/` at the project root
