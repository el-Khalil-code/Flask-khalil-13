from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import re
from datetime import datetime

app = Flask(__name__)

# Configuration
app.secret_key = 'votre_clé_secrète'

# Configuration MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'formulaire_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialisation de MySQL
mysql = MySQL(app)

# Expression régulière pour valider l'email
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom_complet = request.form['nom_complet'].strip()
        ville = request.form['ville'].strip()
        email = request.form['email'].strip()

        # Validation côté serveur
        form_valid = True

        # Réinitialisation des données de session
        session['nom_complet'] = nom_complet
        session['ville'] = ville
        session['email'] = email

        # Validation nom_complet
        if not nom_complet:
            flash('Le nom complet est obligatoire', 'error')
            form_valid = False

        # Validation ville
        if not ville:
            flash('La ville est obligatoire', 'error')
            form_valid = False

        # Validation email
        if not email:
            flash('L\'email est obligatoire', 'error')
            form_valid = False
        elif not re.match(email_regex, email):
            flash('Veuillez fournir une adresse email valide', 'error')
            form_valid = False

        if form_valid:
            # Connexion à la base de données et insertion
            cur = mysql.connection.cursor()

            # Date d'inscription actuelle
            date_inscription = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insertion dans la base de données
            cur.execute("INSERT INTO inscriptions(nom_complet, ville, email, date_inscription) VALUES(%s, %s, %s, %s)",
                        (nom_complet, ville, email, date_inscription))

            # Validation de la transaction
            mysql.connection.commit()

            # Fermeture du curseur
            cur.close()

            # Redirection vers la page de confirmation
            return redirect(url_for('confirmation'))

    return render_template('formulaire.html')


@app.route('/confirmation')
def confirmation():
    # Vérification que les données sont dans la session
    if 'nom_complet' not in session or 'ville' not in session or 'email' not in session:
        return redirect(url_for('formulaire'))

    # Récupération des données de session pour l'affichage
    nom_complet = session.get('nom_complet')
    ville = session.get('ville')
    email = session.get('email')

    # Nettoyage des données de session après utilisation
    session.pop('nom_complet', None)
    session.pop('ville', None)
    session.pop('email', None)

    return render_template('confirmation.html', nom_complet=nom_complet, ville=ville, email=email)


@app.route('/inscrits')
def inscrits():
    # Connexion à la base de données
    cur = mysql.connection.cursor()

    # Récupération de tous les inscrits
    cur.execute("SELECT * FROM inscriptions ORDER BY date_inscription DESC")

    # Récupération des résultats
    inscrits = cur.fetchall()

    # Fermeture du curseur
    cur.close()

    return render_template('inscrits.html', inscrits=inscrits)


if __name__ == '__main__':
    app.run(debug=True)