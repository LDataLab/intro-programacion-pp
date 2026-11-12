# Imagen del pipeline de EcoBici (m12).
# Construir:  docker compose build
# Ejecutar:   docker compose run --rm etl

FROM python:3.12-slim

# curl descarga los CSV y el CLI de DuckDB.
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# CLI de DuckDB (el pipeline lo llama como: duckdb data/db/ecobici.duckdb -f ...)
# TARGETARCH lo asigna Docker: amd64 (Ubuntu, WSL2) o arm64 (Mac con Apple Silicon)
ARG TARGETARCH
RUN curl -fsSL "https://github.com/duckdb/duckdb/releases/latest/download/duckdb-cli-linux-${TARGETARCH}.tar.gz" \
        | tar -xz -C /usr/local/bin duckdb \
    && chmod +x /usr/local/bin/duckdb

# uv: el mismo gestor de paquetes que usamos en la clase
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# 1) Dependencias primero: esta capa se reutiliza mientras no cambie uv.lock
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# 2) Código del proyecto
COPY . .
RUN uv sync --frozen \
    && mkdir -p data/raw data/db

ENV PATH="/app/.venv/bin:$PATH"

CMD ["bash", "pipelines/etl-ecobici.sh"]
