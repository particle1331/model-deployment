FROM python:3.9.12-slim

WORKDIR /app

COPY ["*.py", "*.txt", "./"]

COPY ["app", "./app/"]

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]