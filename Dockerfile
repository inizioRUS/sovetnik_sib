FROM python:3.11.10-bullseye

RUN apt-get update

USER bot

WORKDIR /app

COPY  . .

RUN pip install -r requirements.txt

CMD ["fastapi", "dev", "main.py"]
