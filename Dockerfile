FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/

COPY /req.txt ./req.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ./req.txt

COPY . .

ENV PYTHONPATH=/usr/src/
ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1



