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
- `help` : Affiche la liste des commandes avec leur description.
- `joke` : Affiche une blague aléatoire.
- `message` : Envoie un message.
- `ping` : Vérifie la latence du bot.
- `poll` : Créer un sondage à réponse unique.
- `role` : Création d'un message qui va permettre d'attribuer des rôles en fonctions des réactions.
- `today` : Affiche la date du jour au format : lundi 01 janvier 2000.
- `unban` : Débannit un utilisateur.

## Configuration

Pour utiliser ce Bot, dans un fichier `.env` à la racine du projet, déclarer le token de votre bot comme ceci :

```bash
DISCORD_TOKEN=votre_token
```

Ensuite, remplacez la valeur de la constante **CHANNEL_LOGS_BAN_UNBAN** par l'ID ou vous voulez que les logs des bans et unbans apparaissent.
