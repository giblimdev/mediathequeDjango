# Projet Médiathèque

## Description
Une application Django pour la gestion d'une médiathèque, permettant la gestion des emprunts, des membres et des médias.

## Fonctionnalités
- Création, mise à jour et suppression des membres
- Création, mise à jour et suppression des médias
- Gestion des emprunts et des retours

## Instructions pour Exécuter le Programme

1. **Cloner le Dépôt :**
   ```bash
   git clone https://github.com/ton-utilisateur/mediatheque.git
   cd mediatheque

2. **Créer et Activer un Environnement Virtuel :**

   ```bash

python -m venv env
source env/bin/activate  # Pour Linux/MacOS
.\env\Scripts\activate   # Pour Windows

3. **Installer les Dépendances :**

   ```bash

pip install -r requirements.txt
Appliquer les Migrations et Charger les Données de Test :


   ```bash
python manage.py migrate
python manage.py loaddata data_test.json
```

4. **Démarrer le Serveur :**

   ```bash
python manage.py runserver