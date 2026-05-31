FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install uvicorn

COPY . .

ENTRYPOINT []

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
