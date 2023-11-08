# Bot

Un bot Discord écrit en Python, utilisant la bibliothèque discord.py.

## Installation

Pour installer les dépendances nécessaires, exécutez les commandes suivantes :

```bash
pip install python-dotenv
py -3 -m pip install -U discord.py
```

## Commandes disponibles

Ce bot offre plusieurs commandes :

- `ban` : Bannit un utilisateur.
- `unban` : Débannit un utilisateur.
- `banlist` : Affiche la liste des utilisateurs bannis.
- `ping` : Vérifie la latence du bot.
- `message` : Envoie un message.
- `test` : Commande de test.

## Configuration

Pour utiliser ce Bot, dans un fichier `.env` déclarer le token de votre bot comme ceci :

```bash
DISCORD_TOKEN=votre_token
```

Ensuite, remplacez la valeur dans la constante **CHANNEL_LOGS_BAN_UNBAN** par l'ID ou vous voulez que les logs des bans et unbans apparaissent.
