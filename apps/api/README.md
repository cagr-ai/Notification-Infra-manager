# API (FastAPI)

```bash
cd apps/api
poetry install
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Requirements export (Vercel)

After changing dependencies in `pyproject.toml`:

```bash
poetry run python -m scripts.export_requirements
```

This writes `requirements.txt` from `poetry run pip freeze` (dev-only packages like `ruff` are filtered out).
