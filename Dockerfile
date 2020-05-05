FROM python:3.7-alpine

LABEL maintainer="Pooria Soltani <pooria.ms@gmail.com>"

ARG INSTALL_PATH
ARG POETRY_VERSION
WORKDIR ${INSTALL_PATH}

RUN adduser -D worker

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev build-base

RUN pip install "poetry==${POETRY_VERSION}"
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker . .
RUN poetry install --no-interaction --no-ansi

USER worker

ARG HOST
ARG PORT
ENV HOST=${HOST}
ENV PORT=${PORT}
CMD uvicorn khayyam_api.main:app --host ${HOST} --port ${PORT}
