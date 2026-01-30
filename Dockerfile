FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    JUPYTER_TOKEN=workshop \
    PYTHONPATH=/workspace/ti/src \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH=/opt/venv/bin:$PATH

WORKDIR /workspace

COPY pyproject.toml uv.lock /workspace/

RUN uv venv /opt/venv \
    && uv sync --frozen --no-dev

COPY docker/start-jupyter.sh /usr/local/bin/start-jupyter
RUN chmod +x /usr/local/bin/start-jupyter

COPY . /workspace

EXPOSE 8888

CMD ["/usr/local/bin/start-jupyter"]
