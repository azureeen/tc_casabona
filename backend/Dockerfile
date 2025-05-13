# Utilisation de l'image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements pour installer les dépendances
COPY backend/requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du backend dans le conteneur
COPY backend/ /app/

# Exposer le port 8000 pour l'application Django
EXPOSE 8000

# Commande pour démarrer Django
CMD ["python", "tc_casabona_admin/manage.py", "runserver", "0.0.0.0:8000"]
