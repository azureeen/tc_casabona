# 🎾Projet TC Casabona

Ce projet est une plateforme web pour le club de tennis Casabona, comprenant un backend développé avec Django et un frontend statique généré avec Jekyll. Le projet utilise Docker pour faciliter le développement et le déploiement dans un environnement isolé et reproductible.

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Structure du projet](#structure-du-projet)
- [Docker](#docker)
- [Développement](#développement)
- [Démarrer l'application](#démarrer-lapplication)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Prérequis

Avant de démarrer, assurez-vous que vous avez les outils suivants installés :

- [Docker](https://www.docker.com/get-started) (version 20.10 ou plus récente)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.27 ou plus récente)

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/ton-utilisateur/tc_casabona.git
   cd tc_casabona
   ```
2. Construisez les images Docker pour le backend et le frontend :
    ```bash
    docker-compose build
    ```
3. Lancez les services avec Docker Compose :
    ```bash
    docker-compose up
    ```
    Cela va démarrer trois services :

      - Le backend Django (disponible sur http://localhost:8000)
      - Le frontend Jekyll (disponible sur http://localhost:4000)
      - La base de données PostgreSQL (utilisée par Django)

## Structure du projet

Voici un aperçu de la structure du projet :
```bash
tc_casabona/
├── backend/                     # Code backend Django
│   ├── tc_casabona_admin/       # Application Django principale
│   └── Dockerfile               # Dockerfile pour le backend
├── frontend/                    # Code frontend Jekyll
│   ├── _config.yml              # Configuration de Jekyll
│   ├── Gemfile                  # Dépendances Ruby
│   └── Dockerfile               # Dockerfile pour le frontend
├── .gitignore                   # Fichiers à ignorer par git
├── docker-compose.yml           # Configuration des services Docker
└── README.md                    # Ce fichier
```
## Docker

Le projet utilise Docker pour garantir que tous les développeurs et environnements de production utilisent le même environnement.
### Docker Compose

Le fichier docker-compose.yml définit les services suivants :

- web : Le backend Django qui expose l'API et l'administration du site.
- frontend : Le site statique généré avec Jekyll.
- db : La base de données PostgreSQL pour stocker les données de l'application.

### Utilisation de Docker

Pour démarrer tous les services dans un conteneur Docker, il suffit d'exécuter la commande suivante :
    ```bash
    docker-compose up
    ```
Cela va créer et démarrer les services définis dans le fichier docker-compose.yml.
## Développement

Pour un développement local, les changements que vous apportez au frontend (Jekyll) ou au backend (Django) seront automatiquement répercutés dans l'environnement Docker, grâce à l'utilisation des volumes Docker.
### Backend

Le backend est développé avec Django et géré via manage.py. Les migrations de base de données peuvent être appliquées avec :
    ```bash
    docker-compose run web python /app/tc_casabona-admin/manage.py migrate
    ```
### Frontend

Le frontend est généré avec Jekyll. Pour un environnement de développement local, vous pouvez modifier les fichiers dans le répertoire frontend/ et le site sera automatiquement mis à jour.
## Démarrer l'application

1. Si ce n'est pas déjà fait, construisez les images Docker :
    ```bash
    docker-compose build
    ```
2. Lancez les services avec Docker Compose :
    ```bash
    docker-compose up
    ```
    Accédez à l'application backend via http://localhost:8000 et au frontend via http://localhost:4000.

## Contribuer

1. Fork ce dépôt.
2. Créez une branche pour votre fonctionnalité : git checkout -b ma-fonctionnalite
3. Faites vos modifications et commit : git commit -am 'Ajout de ma fonctionnalité'
4. Poussez vos changements : git push origin ma-fonctionnalite
5. Ouvrez une Pull Request pour discussion et révision.

## Licence

Ce projet est sous la licence MIT. Voir le fichier LICENSE pour plus d'informations.


### Explications des sections ajoutées :
- **Construire les images Docker** : J'ai ajouté les étapes pour construire les images avec Docker.
- **Démarrer l'application** : Les étapes pour démarrer l'application en utilisant Docker et Docker Compose.
- **Contribuer** : Comment contribuer au projet.
- **Licence** : Pour informer de la licence utilisée.

Cela permet à un développeur de démarrer facilement avec ton projet, de contribuer et de faire tourner l'application localement en utilisant Docker.

