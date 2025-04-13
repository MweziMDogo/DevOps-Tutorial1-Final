FROM python:3.9-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY server.py .
COPY index.html .
COPY styles.css .

EXPOSE 8080

HEALTHCHECK CMD curl -f http://localhost:8080/ || exit 1

CMD ["python", "server.py"]
