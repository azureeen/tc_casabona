# Utilisation de Python 3.13 pour le container
FROM python:3.13-slim

# Installer les outils nécessaires pour PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le container
COPY . /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port du serveur Django
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
