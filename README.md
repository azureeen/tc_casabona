# 🎾 Tennis Club Casabona - Site Vitrine 🚀

Le site vitrine officiel du **Tennis Club Casabona**, développé avec un frontend **Jekyll**, un backend **Django**, et une base de données PostgreSQL. L'application est conteneurisée avec **Docker** et orchestrée via docker-compose pour un déploiement facile sur un VPS KV2 chez Hostinger.

---


## 🔥 Fonctionnalités
- ✅ Site vitrine avec gestion de contenu depuis l'admin Django  
- ⚡ Frontend Jekyll pour un rendu rapide et optimisé  
- 🔄 Backend Django pour la gestion dynamique des données  
- 🗄️ Base de données PostgreSQL pour le stockage structuré  
- 🐳 Docker Compose pour le déploiement unifié (frontend + backend + DB)  
- 🤖 Intégration future d'un chatbot interactif basé sur l'IA  

---

## 📂 Arborescence du projet
```plaintext
.
├── backend
│   ├── Dockerfile
│   ├── manage.py
│   ├── tc_casabona_admin
│   └── ...
│
├── frontend
│   ├── Dockerfile
│   ├── _config.yml
│   ├── index.html
│   └── ...
│
├── docker-compose.yml
├── README.md
└── ...
```

##  ⚙️ Installation locale

### Prérequis :
- Docker
- Docker Compose

### Étapes :

1️⃣ Cloner le dépôt :
```bash
git clone https://github.com/tonrepo/tc_casabona.git
cd tc_casabona
```
2️⃣ Lancer l'application :
```bash
sudo docker-compose up --build
```
3️⃣ Accéder aux services :
- Frontend (Jekyll) : http://localhost:4000
- Backend (Django Admin) : http://localhost:8000/admin

## 🗄️ Gestion du contenu

Le contenu du site vitrine peut être modifié directement depuis l'interface **Django Admin**, permettant une gestion simple et rapide.
L'objectif est de centraliser le contenu statique dans des fichiers YAML ou dans le modèle Django, afin de permettre une mise à jour en temps réel.


## 🚀 Déploiement

Le site est prévu pour être déployé sur un **VPS KV2 à Hostinger**.
Les commandes nécessaires pour le déploiement en production seront ajoutées prochainement.


## 🔄 Améliorations futures
- 🔍 **Chatbot interactif IA** pour guider les utilisateurs
- 📈 **Statistiques en temps réel** sur les matchs et les événements
- 🔐 **Sécurisation avancée** avec Nginx en reverse proxy

## 👥 Contributeurs
- Arthur Trochon — Développeur principal

## 📜 Licence

Projet sous licence MIT.