FROM python:3.12-slim

RUN apt-get update && apt-get install -python
    postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/

COPY /req.txt ../req.txt

RUN pip3 install --upgrade pip3
RUN pip3 install --no-cache-dir -r ../req.txt

COPY . ../

ENV PYTHONPATH= /usr/srs
ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1



