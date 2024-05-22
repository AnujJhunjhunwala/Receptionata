FROM python:3.12-slim-bookworm

RUN apt update && apt -y upgrade \
    && apt install -y build-essential \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

WORKDIR /receptionata/api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src

EXPOSE 8000

CMD ["python", "src/main.py"]
