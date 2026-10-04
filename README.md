# GoodStride

A runnable prototype for finding fictional major-marathon charity places and pressure-testing the fundraising commitment. Built from the 2026-10-04 Idea of the Day; see [source notes](research/notes.md).

## What works

- Filter demo inventory by race, cause, search, and maximum commitment.
- Save a listing, handle empty/loading/error states, and calculate a weekly fundraising target.
- FastAPI matching and fundraising-plan operations with validation/failure tests.
- Responsive static export for GitHub Pages. All inventory and availability are fictional.

## Run

```bash
npm ci
npm run dev
```

```bash
cd api
uv sync --locked
uv run uvicorn main:app --reload
```

## Verify

```bash
npm run typecheck
npm run test:e2e
npm run build
npm run audit:prod
uv run --directory api pytest
```

The public Pages deployment hosts only the static frontend. FastAPI is tested source and is **not deployed**.
