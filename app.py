from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Calculateur de Profit Subsistant")

# Route pour la page co-parentalité
@app.route('/co-parentalite')
def co_parentalite():
    return render_template('co-parentalite.html')

# Route pour la page profit subsistant
@app.route('/profitsubsistant')
def profitsubsistant():
    return render_template('profitsubsistant.html')

# Route pour la page contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        valeur_initiale = float(request.form['valeur_initiale'])
        investissement = float(request.form['investissement'])
        valeur_actuelle = float(request.form['valeur_actuelle'])

        # Calcul du profit subsistant (par exemple)
        profit_subsistant = valeur_actuelle - (valeur_initiale + investissement)
        
        return render_template('profitsubsistant.html', result=profit_subsistant, title="Résultat du Calcul")
    except ValueError:
        # Gestion des erreurs en cas de mauvaise saisie
        return redirect(url_for('profitsubsistant'))

@app.route('/reset', methods=['POST'])
def reset():
    return redirect(url_for('profitsubsistant'))

if __name__ == '__main__':
    app.run(debug=True)
