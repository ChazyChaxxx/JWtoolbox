# Importation des modules nécessaires depuis Flask
from flask import Flask, render_template, request, redirect, url_for

# Création de l'application Flask
app = Flask(__name__)

# Définition de la route principale (page d'accueil)
@app.route('/')
def index():
    # Retourne la page index.html et passe une variable 'title' à la page
    return render_template('index.html', title="Calculateur de Profit Subsistant")

# Définition de la route pour la page co-parentalité
@app.route('/co-parentalite')
def co_parentalite():
    # Retourne la page co-parentalite.html
    return render_template('co-parentalite.html')

# Définition de la route pour la page profit subsistant
@app.route('/profitsubsistant')
def profitsubsistant():
    # Retourne la page profitsubsistant.html
    return render_template('profitsubsistant.html')

# Définition de la route pour la page contact
@app.route('/contact')
def contact():
    # Retourne la page contact.html
    return render_template('contact.html')

# Définition de la route pour effectuer le calcul du profit subsistant
@app.route('/calculate', methods=['POST'])
def calculate():
    # Le bloc try-except permet de gérer les erreurs de saisie
    try:
        # Récupération des valeurs envoyées via le formulaire et conversion en flottants
        valeur_initiale = float(request.form['valeur_initiale'])
        investissement = float(request.form['investissement'])
        valeur_actuelle = float(request.form['valeur_actuelle'])

        # Calcul du profit subsistant basé sur le pourcentage de l'investissement par rapport à la valeur initiale
        proportion_investissement = investissement / valeur_initiale
        profit_subsistant = proportion_investissement * valeur_actuelle

        # Créer un récapitulatif des valeurs et de la formule utilisée
        recap = f"Valeur Initiale : {valeur_initiale} €, Investissement : {investissement} €, Valeur Actuelle : {valeur_actuelle} €. "
        formule = "Formule appliquée : (Investissement / Valeur Initiale) * Valeur Actuelle"
        
        # Renvoie la page profitsubsistant.html avec le résultat du calcul et le récapitulatif
        return render_template('profitsubsistant.html', 
                               result=profit_subsistant, 
                               recap=recap, 
                               formule=formule, 
                               title="Résultat du Calcul")
    except ValueError:
        # Gestion des erreurs en cas de mauvaise saisie
        # Si une valeur non numérique est saisie, un message d'erreur est affiché
        error_message = "Veuillez entrer des valeurs numériques valides."
        return render_template('profitsubsistant.html', error=error_message, title="Erreur de Saisie")

# Définition de la route pour réinitialiser le formulaire
@app.route('/reset', methods=['POST'])
def reset():
    # Redirige l'utilisateur vers la page profit subsistant sans effectuer de calcul
    return redirect(url_for('profitsubsistant'))

# Le point d'entrée de l'application
if __name__ == '__main__':
    # Démarre l'application Flask en mode debug, utile pour le développement
    app.run(debug=True)
