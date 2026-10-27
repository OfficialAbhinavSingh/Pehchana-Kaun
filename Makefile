.PHONY: setup dev-api dev-web check check-api check-web fmt db-up db-down migrate simulate

setup:
	cd backend && uv sync
	cd web && pnpm install

dev-api:
	cd backend && uv run uvicorn pehchana.main:app --reload --port 8000

dev-web:
	cd web && pnpm dev

check: check-api check-web

check-api:
	cd backend && uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest

check-web:
	cd web && pnpm lint && pnpm typecheck && pnpm build

fmt:
	cd backend && uv run ruff check --fix . && uv run ruff format .

migrate:
	cd backend && uv run pk migrate

# Rehearse the phone flow against a running backend: make simulate TARGET=https://...
simulate:
	cd backend && uv run pk simulate-call --target $(or $(TARGET),http://localhost:8000)

db-up:
	docker compose up -d db

db-down:
	docker compose down
