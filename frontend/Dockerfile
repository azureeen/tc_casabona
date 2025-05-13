# Utiliser l'image officielle de Ruby
FROM ruby:3.0

# Installer les dépendances système nécessaires
RUN apt-get update -qq && apt-get install -y nodejs npm

# Définir le répertoire de travail
WORKDIR /app

# Copier le Gemfile et le Gemfile.lock (si présent)
COPY frontend/Gemfile /app/
COPY frontend/Gemfile.lock /app/ 

# Installer les dépendances via Bundler
RUN gem install bundler && bundle install

# ➡️ Ajoute cette ligne pour installer 'ffi' manuellement :
RUN gem install ffi -v 1.17.1

# Copier le reste des fichiers du frontend
COPY frontend/ /app/

# Exposer le port
EXPOSE 4000

# Lancer le serveur Jekyll
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
