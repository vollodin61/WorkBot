#FROM python:3.14.3-slim
#
#WORKDIR /workbot
#
#COPY requirements.txt .
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#CMD ["python", "main.py"]
#FROM ghcr.io/astral-sh/uv:0.7-python3.14.3
#FROM python:3.14.3-slim-bookworm

FROM python:3.14.3-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workbot

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY . .

RUN uv sync --frozen --no-dev

CMD ["uv", "run", "--no-dev", "main.py"]
#CMD ["python", "main.py"]
