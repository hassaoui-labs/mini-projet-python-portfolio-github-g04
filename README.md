# mini-projet-python-portfolio-github-g04
🎯 Objectifs pédagogiques
- Développer une visibilité professionnelle
- Exploiter l’API GitHub
- Analyser la qualité du code et des contributions

🧩 Description : Créer une application Python capable d’analyser des dépôts GitHub et de générer automatiquement un portfolio professionnel (HTML).

⚙️ Fonctionnalités attendues
- Analyse des repositories GitHub
- Statistiques sur les commits
- Génération de portfolio HTML
- Publication via GitHub Pages

🛠️ Technologies
- Python
- GitHub API
- HTML / CSS
- GitHub Pages

👥 Répartition du travail
- Membre 1 : API GitHub
- Membre 2 : analyse du code
- Membre 3 : génération HTML
- Membre 4 : déploiement

📦 Livrables
       - Dépôt GitHub structuré (Application Python)
       - Wiki Documentation projet 
       - Rapport technique PDF
       - Journal de commits



📋 Description du projet
Le GitHub Portfolio Generator est une application Python qui analyse automatiquement les dépôts GitHub d'un utilisateur et génère un portfolio professionnel au format HTML. L'outil permet aux développeurs de mettre en valeur leurs contributions, langages maîtrisés et projets significatifs.

Fonctionnalités principales
1. Analyse des repositories GitHub
Récupération de tous les dépôts publics

Filtrage des forks

Pagination complète pour récupération exhaustive

Statistiques détaillées par dépôt

2. Calcul de métriques avancées
Nombre de commits par dépôt

Langages de programmation utilisés

Nombre d'étoiles et de forks

Score de qualité calculé selon une formule pondérée

Détection des projets actifs vs. archivés

3. Génération de portfolio HTML
Template responsive avec Jinja2

Interface utilisateur moderne et professionnelle

Classement des projets par score

Visualisation des langages sous forme de badges

Pages web entièrement autonomes

4. Sécurité et robustesse
Auto-échappement HTML pour prévenir XSS

Gestion des erreurs réseau et API

Validation des données d'entrée

Gestion sécurisée des tokens d'API

🏗️ Architecture technique
Structure du projet :
  github-portfolio-generator/
├── main.py              # Point d'entrée principal
├── github_api.py       # Gestion des appels API GitHub
├── analyzer.py         # Analyse des données et calcul des scores
├── html_generator.py   # Génération du template HTML
├── config.py           # Configuration (tokens, URLs)
├── templates/
│   └── portfolio.html  # Template Jinja2
├── output/             # Portfolio généré
└── requirements.txt    # Dépendances Python


Technologies utilisées
Backend (Python 3.8+)
       Requests : Gestion des requêtes HTTP vers l'API GitHub

       Jinja2 : Moteur de templates pour la génération HTML

       Debugpy : Débogage à distance pour le développement

Frontend
       HTML5 : Structure sémantique

       CSS3 : Styles modernes avec flexbox/grid

       JavaScript Vanilla : Interactions simples

Infrastructure
       GitHub API v4 : Récupération des données

       GitHub Pages : Hébergement statique

       Git : Contrôle de version


📊 Algorithme de scoring
Le score de qualité d'un dépôt est calculé selon la formule :

Score = (Commits × 2) + (Étoiles × 5) + (Forks × 3)

Cette pondération favorise :

       Popularité (étoiles et forks) : Indicateur d'utilité communautaire

       Activité (commits) : Indicateur de maintenance et d'évolution

       Originalité (forks exclus de l'analyse) : Focus sur les contributions personnelles


🎨 Interface utilisateur
Le portfolio généré inclut :

Page principale
En-tête : Nom d'utilisateur GitHub et photo de profil

Statistiques globales : Dépôts totaux, étoiles, forks, langages principaux

Classement des projets : Tri par score décroissant

Cartes de projets : Pour chaque dépôt, affiche :

              Nom et description

              Langages utilisés (badges colorés)

              Métriques (commits, étoiles, forks)

              Score de qualité

              Lien direct vers le dépôt

              Design responsive
              Adapté mobile, tablette et desktop

              Palette de couleurs professionnelle

              Typographie lisible

              Animations subtiles

Validation des résultats :
       Comparaison avec les statistiques GitHub natives

       Test avec différents profils utilisateur

       Validation du HTML généré (W3C Validator)

       Tests de responsive design

⚙️ Installation et utilisation
Prérequis :
       Python 3.8 ou supérieur
       Compte GitHub avec des dépôts publics
       Token d'API GitHub avec permissions de lecture
Installation :
       # 1. Cloner le dépôt
       git clone https://github.com/username/mini-projet-python-portfolio-github-g04.git
       cd mini-projet-python-portfolio-github-g04

       # 2. Créer un environnement virtuel
       python -m venv venv
       source venv/bin/activate  # Sur Windows: venv\Scripts\activate

       # 3. Installer les dépendances
       pip install -r requirements.txt

       # 4. Configurer le token GitHub
       # Éditer config.py et remplacer GITHUB_TOKEN par votre token personnel
Utilisation :
       # Exécuter le générateur
       python main.py

       # Entrer le nom d'utilisateur GitHub
       GitHub username: votre-username

       # Le portfolio est généré dans output/portfolio.html


📚 Références techniques
Documentation API GitHub
https://docs.github.com/en/rest

Rate limiting : 5000 requêtes/heure avec token

Pagination : 100 résultats par page maximum

Bibliothèques Python
Requests : https://docs.python-requests.org/

Jinja2 : https://jinja.palletsprojects.com/

Pytest : https://docs.pytest.org/

Standards web
HTML5 : https://developer.mozilla.org/fr/docs/Web/HTML

CSS3 : https://developer.mozilla.org/fr/docs/Web/CSS

Responsive Design : https://developers.google.com/web/fundamentals/design-and-ux/responsive

_______________________________________________________


Dernière mise à jour : Décembre 2024
Version : 1.0.0
Équipe G04 : Ramzi BADACHE 
