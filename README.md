# GrandPy_Bot
Ce projet est le septième réalisé dans le cadre du parcours **OpenClassrooms** ***[Développeur Python](https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python)***.  
Le site est accessible à l'adresse suivante : **[Mon appli](http://grandpy-bot-nz.herokuapp.com/)**  
Il a été réalisé de manière responsive, pour pouvoir s'adapter à des supports plus petits, tels mobiles ou tablettes.

GrandPy-Bot est une application réalisée en langage Python (3.6.8), avec le framework Flask. Après avoir posé une question concernant un lieu, GrandPy répondra en indiquant :
- l'adresse du lieu
- quelques mots à propos du lieu
- une carte GoogleMap pointant sur le lieu

## Instalation en local
- Forker ce projet GitHub
- Créer un environnement virtuel à la racine du projet
- Installer les dépendances : *pip install -r requirements.txt*

## Lancement en local
- Il est nécessaire d'enregistrer dans vos variables local, la variable *GM_KEY = "votreCléAPIGoogleMaps"*
- Dans la racine du projet, lancer la commande : *python3 run.py*
- Se rendre, avec votre navigateur web, à l'adresse suivante : *http://127.0.0.1:5000/*

## APIs utilisés
- ***[MediaWiki](https://www.mediawiki.org/wiki/API:Main_page)***
- ***[GoogleMaps](https://cloud.google.com/maps-platform/?hl=fr)***

## Packages utilisés
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** : le micro-framework de Python
- **[Requests](https://requests-fr.readthedocs.io/en/latest/)** : librairie HTTP
- **[Pytest](https://docs.pytest.org/en/latest/)** : pour la réalisation des tests unitaires

## Lancement des test
A la racine du projet, lancer la commande : *pytest*

## Langages web utilisés
- HTML5
- CSS3
- Javascript, avec le framework Jquery

## Utilisation de l'application
- Ecrire sa question dans le champs de recherche
- Cliquer sur *Demander* ou appuyer sur *Entrée*
- Le bot a plusieurs réponses possibles :
  - S'il trouve une réponse il affiche l'adresse, raconte une histoire à propos du lieu et affiche une carte
  - S'il ne trouve pas de réponse il demande à avoir une question plus concise
  - Si la question est trop courte et que GrandPy ne possède pas assez d'éléments il dmeande à avoir une question plus précise

