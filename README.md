# TerangaConnect

Application de messagerie instantanée entre étudiants, développée avec Flask et MySQL, déployée via Docker.

---

## Technologies utilisées

- **Python / Flask** — backend et gestion des routes
- **MySQL** — base de données pour les utilisateurs et les messages
- **Docker / Docker Compose** — conteneurisation et déploiement
- **HTML / CSS** — interface utilisateur

---

## Fonctionnalités

- Créer un compte utilisateur
- Se connecter avec un nom d'utilisateur et un mot de passe
- Envoyer des messages entre utilisateurs
- Consulter l'historique des messages
- Page de monitoring (nombre d'utilisateurs et de messages)

---

## Lancer le projet

**Prérequis :** avoir Docker et Docker Compose installés.

```bash
# 1. Cloner ou décompresser le projet
# 2. Se placer dans le dossier
cd examenDEVNET

# 3. Lancer les conteneurs
docker-compose up --build
```

L'application sera accessible sur : **http://localhost:5000**

---

## Structure du projet

```
examenDEVNET/
├── app/
│   ├── templates/      # Pages HTML (chat, login, register, monitor)
│   ├── static/         # Feuille de style CSS
│   ├── models.py       # Modèles de base de données
│   ├── routes.py       # Routes principales
│   └── api_routes.py   # Routes API
├── run.py              # Point d'entrée de l'application
├── docker-compose.yml  # Configuration Docker
└── requirements.txt    # Dépendances Python
```
