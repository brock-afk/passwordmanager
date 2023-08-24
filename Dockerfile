FROM python:3.11.4-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.5.1

COPY . /app/

RUN poetry install --sync

ENTRYPOINT [ "poetry", "run" ]

CMD [ "python", "-m", "passwordmanager" ]