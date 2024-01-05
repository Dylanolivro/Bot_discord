[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
# Bot

Un bot Discord écrit en Python, utilisant la bibliothèque discord.py.

## Installation

Pour installer les dépendances nécessaires, exécutez les commandes suivantes :

```bash
py -3 -m pip install -U discord.py
pip install python-dotenv
python -m pip install requests
```

## Commandes disponibles

Ce bot offre plusieurs commandes :

- `ban` : Bannit un utilisateur.
- `banlist` : Affiche la liste des utilisateurs bannis.
- `calcul` : Calcul 2 nombres, addition, soustraction, multiplication et division.
- `clear` : Supprime tous les messages d'un canal ou un nombre spécifique de ceux-ci.
- `help` : Affiche la liste des commandes avec leur description.
- `joke` : Affiche une blague aléatoire.
- `message` : Envoie un message.
- `ping` : Vérifie la latence du bot.
- `poll` : Créer un sondage à réponse unique.
- `role` : Création d'un message qui va permettre d'attribuer des rôles en fonctions des réactions.
- `today` : Affiche la date du jour au format : lundi 01 janvier 2000.
- `unban` : Débannit un utilisateur.


## Fonctionnalités supplémentaires

- Il repère les messages qui finissent par “quoi” et “ping”, et y répond par “feur” et “pong”.

- Il ajoute un message dans un canal dédié pour chaque nouvelle ligne ajoutée à la base de données.


## Configuration

Pour utiliser ce Bot, dans un fichier `.env` au même niveau que le fichier `main.py`, déclarer le token de votre bot comme ceci :

```bash
DISCORD_TOKEN=votre_token
```

Ensuite, n’oubliez pas de remplacer les valeurs des constantes dans le fichier `config.py` :

- **CHANNEL_LOGS_BAN_UNBAN**
- **CHANNEL_MESSAGE_AUTO**

 par l’ID des canaux où vous souhaitez que les journaux des bannissements, des débannissements et des messages automatiques apparaissent.

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://dylan-olivro.students-laplateforme.io/)
