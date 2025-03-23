FROM python:3.9-slim

WORKDIR /app

# Копіюємо файл з залежностями та встановлюємо їх
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо код додатку
COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
