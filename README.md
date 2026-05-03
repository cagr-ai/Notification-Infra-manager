# Notification infrastructure

Monorepo for the notification stack: **Vite + React** (`apps/web`) and **FastAPI** (`apps/api`), orchestrated with **pnpm** and **Turborepo**.

## Prerequisites

- **Node.js** 20.19+ or 22.12+ (recommended; Vite 6 needs a recent 20.x)
- **pnpm** 9 (`packageManager` is pinned in the root `package.json`)
- **Poetry** 2.x (for the Python API)
- **MongoDB** reachable from your machine if you use routes that talk to the database (the API boots without Mongo for basic HTTP; Motor connects when you use DB-backed code)

## Install dependencies

From the repository root:

```bash
pnpm install
cd apps/api && poetry install && cd ../..
```

## Environment variables

### API (`apps/api`)

1. Copy the example file:

   ```bash
   cp apps/api/.env.example apps/api/.env
   ```

2. Edit `apps/api/.env`:

   | Variable       | Description |
   |----------------|-------------|
   | `MONGODB_URI`  | MongoDB connection string (e.g. local `mongodb://localhost:27017` or Atlas). |
   | `MONGODB_DB`   | Database name to use (default in example: `notification`). |

Settings are loaded with **pydantic-settings**; see [`apps/api/app/config.py`](apps/api/app/config.py).

### Web (`apps/web`)

1. Copy the example file:

   ```bash
   cp apps/web/.env.example apps/web/.env
   ```

2. Edit `apps/web/.env`:

   | Variable         | Description |
   |------------------|-------------|
   | `VITE_API_URL`   | Base URL of the FastAPI server the browser should call. For local API use `http://localhost:8000`. |

Vite only exposes env vars prefixed with `VITE_` to client code. Use `import.meta.env.VITE_API_URL` in the frontend when you wire API calls.

## Run both apps in development

From the **repository root**, start every package that defines a `dev` script (web + api) in parallel:

```bash
pnpm dev
```

- **Web**: [http://localhost:5173](http://localhost:5173) (Vite default)
- **API**: [http://localhost:8000](http://localhost:8000) (Uvicorn; health check at `/health`)

### Run one app only

```bash
# Frontend only
pnpm --filter web dev

# API only
pnpm --filter api dev
```

## Other useful commands

| Command        | Description |
|----------------|-------------|
| `pnpm build`   | Production build for all workspaces (web → `dist/`; api → refreshes `requirements.txt` for Vercel). |
| `pnpm lint`    | ESLint (web) and Ruff (api). |

## Production / Vercel

Deploy **two Vercel projects** from the same repo, each with its **Root Directory** set to `apps/web` or `apps/api`. Configure `MONGODB_URI` (and optionally `MONGODB_DB`) on the API project, and `VITE_API_URL` on the web project to your deployed API origin.
