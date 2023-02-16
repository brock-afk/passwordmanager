FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . /app/

RUN pip install -e .

ENTRYPOINT [ "python", "-m", "passwordmanager" ]