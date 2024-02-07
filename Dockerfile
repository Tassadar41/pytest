FROM python:3.9-alpine

LABEL "creator"="Rolik Denis"

WORKDIR ./urs/pyTest

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV ENV=dev

CMD pytest -s -v tests/users

