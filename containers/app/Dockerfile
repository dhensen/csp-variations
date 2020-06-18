FROM python:3.7.7-buster
RUN pip install pipenv

RUN mkdir -p /app
WORKDIR /app

ENV PIPENV_VENV_IN_PROJECT=1

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv install

COPY config /app/config
COPY csp_variations /app/csp_variations

EXPOSE 8000

CMD . /app/.venv/bin/activate && exec daphne -b 0.0.0.0 -p 8000 config.asgi:application
