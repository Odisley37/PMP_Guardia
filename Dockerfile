# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev netcat gcc \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório da aplicação
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar todo o código para dentro do container
COPY . .

# Comando default (sobrescrito no docker-compose)
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
