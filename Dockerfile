FROM python:3.14-slim

# copia o binário do uv da imagem oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1º só as dependências (aproveita o cache do Docker)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# 2º o código
COPY apps ./apps

# coloca o .venv no PATH para chamar o uvicorn direto
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8000"]
