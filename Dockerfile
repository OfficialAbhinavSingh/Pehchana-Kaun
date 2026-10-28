# Backend image for any host that runs containers (Fly.io, Railway, Render, Cloud Run).
# Build from the repo root, because the backend reads bolna/arms.yaml next to backend/:
#   docker build -t pehchana-api .
# The web site is not in this image: it deploys separately (WS3-06).
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=never

# Same layout as the repo: config.py finds bolna/ two levels above backend/src.
WORKDIR /app/backend

# Dependencies first, so code changes do not reinstall them.
COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY backend/ ./
COPY bolna/ /app/bolna/
RUN uv sync --locked --no-dev && chmod +x start.sh

RUN useradd --system --create-home app && chown -R app /app
USER app

# ENV=prod makes the app refuse to boot on dev secrets (see pehchana.config).
# FORWARDED_ALLOW_IPS=* trusts X-Forwarded-For, which the per-client web-call limit needs
# behind a host's proxy. Never expose this container directly to the internet: anyone
# could then spoof their IP.
ENV PATH="/app/backend/.venv/bin:$PATH" ENV=prod FORWARDED_ALLOW_IPS="*" PORT=8000
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD python -c "import os,urllib.request as u; u.urlopen(f'http://127.0.0.1:{os.environ[\"PORT\"]}/healthz', timeout=4)"

CMD ["./start.sh"]
