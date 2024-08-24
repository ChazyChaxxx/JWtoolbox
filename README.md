# Juridic Ways toolbox

## Description
Ce site internet permet de tester des fonctionalités avant le développement à grande échelle.

## Fonctionnalités
- **calculateur de profit subsistant** : Calculer la nouvelle valeur d'un investissement après ré-évaluation d'un bien.
- **Calendrier interactif** : Coloriez les jours selon le parent responsable.
- **Formulaire de contact** : Envoyez des questions ou des suggestions via un formulaire simple.

## Installation

### Prérequis
- **Python 3.x**
- **Flask**
- **Node.js et npm** (pour compiler les fichiers SCSS)
- **Sass** (pour convertir les fichiers SCSS en CSS)

### Étapes
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/ChazyChaxxx/JWtoolbox.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd votre-repo
    ```
3. Installez les dépendances Python :
    ```bash
    pip install -r requirements.txt
    ```
4. Installez les dépendances Node.js :
    ```bash
    npm install
    ```
5. Compilez les fichiers SCSS en CSS :
    ```bash
    sass --watch static/sass:static/css
    ```
6. Lancez l'application :
    ```bash
    flask run
    ```

## Utilisation
1. Ouvrez votre navigateur et accédez à `http://localhost:5000`.

## Structure du Projet
- `static/`: Contient les fichiers CSS, JS et les images.
- `templates/`: Contient les fichiers HTML pour les pages du site.
- `app.py`: Le script principal pour exécuter l'application Flask.
- `requirements.txt`: Liste des dépendances Python.
- `static/sass/`: Contient les fichiers SCSS pour le style du projet.

## Problèmes connus
- Soucis d'interactivité avec les SCSS. (pas de bouton menu, pas de sous-menus dépliables)
- Formulaire de contact non fonctionnel à l'heure actuelle
- Calendrier interactif ne contient pas encore l'algorythme de calcul

## Contribuer


## Licence


## Contact
