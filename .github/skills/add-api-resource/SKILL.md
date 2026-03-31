---
name: add-api-resource
description: "Scaffold a complete Flask API resource: SQLAlchemy model, blueprint route, and unit tests. Use when: add endpoint, create API resource, new model, new route, add entity, CRUD endpoint, new REST resource, scaffold backend."
---

# Add API Resource

Creates a complete Flask API resource with model, route, and tests following project conventions.

## When to Use

- Adding a new entity/resource to the backend API
- Scaffolding CRUD endpoints for a new database table
- Creating a new model with associated routes and tests

## Procedure

### 1. Create the SQLAlchemy Model

Create `server/models/<resource>.py` following the pattern in [game.py](../../server/models/game.py):

- Inherit from `BaseModel` (defined in [base.py](../../server/models/base.py))
- Define columns with appropriate types and constraints
- Add `@validates` decorators using `self.validate_string_length()` from BaseModel
- Implement `__repr__` and `to_dict()` methods
- Use `camelCase` for JSON keys in `to_dict()` (e.g., `starRating` not `star_rating`)
- Define relationships with `relationship()` and `back_populates`

### 2. Register the Model

Update [server/models/__init__.py](../../server/models/__init__.py):

- Import the new model class after `db` is defined
- Export it so routes and tests can use `from models import <Model>`

### 3. Create the Blueprint Route

Create `server/routes/<resource>.py` following the pattern in [games.py](../../server/routes/games.py):

- Create a `Blueprint` named after the resource
- Define a base query function with necessary joins (use `isouter=True` for optional relationships)
- Implement `GET /api/<resources>` (list all) returning `jsonify(list)`
- Implement `GET /api/<resources>/<int:id>` (get one) returning 404 if not found
- Use type hints: `-> Response` and `-> tuple[Response, int] | Response`
- Use the model's `to_dict()` for serialization

### 4. Register the Blueprint

Update [server/app.py](../../server/app.py):

- Import the new blueprint
- Call `app.register_blueprint(<resource>_bp)`

### 5. Create Unit Tests

Create `server/tests/test_<resource>.py` following the pattern in [test_games.py](../../server/tests/test_games.py):

- Use `unittest.TestCase` with type hints throughout
- Define `TEST_DATA` dict with all seed data at the class level
- Define `<RESOURCE>_API_PATH` as a class constant
- In `setUp`: create Flask app with `sqlite:///:memory:`, register blueprint, call `init_db(self.app, testing=True)`, create tables, seed data
- In `tearDown`: call `db.session.remove()`, `db.drop_all()`, `db.engine.dispose()`
- Create `_seed_test_data()` helper to populate related entities
- Create `_get_response_data()` helper to parse JSON responses
- Write tests for: successful list, successful get-by-id, 404 for missing id
- Test both response status codes and response body content

### 6. Run Tests

Run tests using the project script:

```bash
bash scripts/run-server-tests.sh
```

### 7. Update Documentation

- Add the new resource to the Repository Structure section in [copilot-instructions.md](../../.github/copilot-instructions.md) if it introduces a new directory
- Update [README.md](../../README.md) with the new API endpoint

## Checklist

- [ ] Model inherits from `BaseModel` with validators
- [ ] Model registered in `models/__init__.py`
- [ ] Route uses Blueprint pattern with base query function
- [ ] Route returns proper HTTP status codes (200, 404)
- [ ] Blueprint registered in `app.py`
- [ ] Tests use in-memory SQLite with proper setup/teardown
- [ ] Tests cover success and not-found cases
- [ ] All tests pass via `scripts/run-server-tests.sh`
- [ ] Type hints on all function signatures
