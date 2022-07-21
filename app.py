from wtforms import StringField, SubmitField, BooleanField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from multiprocessing import connection
from pprint import pprint
from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import date, datetime
from pymongo import MongoClient
import remplirbdd
from templates.formulaire import Connexion, Inscription, Commentaire, Gestion_article
client = MongoClient("127.0.0.1:27017")
# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string


client = MongoClient("127.0.0.1:27017")

db = client.blog
articles = db.articles
utilisateurs = db.utilisateurs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'


@app.route("/", methods=["GET", "POST"])
def accueil():
    liste_article = articles.find({})
    try:
        login = session["login"]
    except:
        login = None
    return render_template("accueil.html", articles=liste_article, login=login)


@app.route('/article/<nom>', methods=['GET', 'POST'])
def voir_article(nom):
    mon_article = articles.find_one({"titre": nom})
    print({"titre": mon_article["titre"]})
    form = Commentaire()
    id_utilisateur = utilisateurs.find(
        {"login": session["login"]}, {'_id'})[0]["_id"]
    # for elmt in curseur:
    new = articles.find({"titre": mon_article["titre"]})[0]["commentaire"]

    if form.validate_on_submit():
        new.append({"date": str(datetime.now()),
                    "Username": session["login"],
                    "User_ID": id_utilisateur,
                    "text": form.data["commentaire_utilisateur"],
                    "validé": False

                    })
        articles.update_one({"titre": mon_article["titre"]},
                            {"$set": {
                                "commentaire": new
                            }
        }
        )

    return render_template("article.html", article=mon_article, form=form)


@app.route('/inscription/', methods=['GET', 'POST'])
def inscription():
    form = Inscription()
    if form.validate_on_submit():
        creation_utilisateur = utilisateurs.insert_one(
            {"login": form.data["login_inscription"], "password": form.data["password_inscription"]})
        print(creation_utilisateur)
        return redirect(url_for("accueil"))
    return render_template("creation_compte.html", form=form)


@app.route('/connexion', methods=['GET', 'POST'])
def connexion():

    form = Connexion()
    if form.validate_on_submit():
        utilisateur = utilisateurs.find_one(
            {"login": form.data["login"], "password": form.data["password"]})
        if form.data["login"] == utilisateur["login"] and form.data["password"] == utilisateur["password"]:
            session["login"] = utilisateur["login"]
            return redirect(url_for("accueil"))
    return render_template("connexion.html", form=form)


@app.route('/administration_creation', methods=['GET', 'POST'])
def administration_creation():
    liste_article = articles.find({})
    form = Gestion_article()
    id_utilisateur = utilisateurs.find(
        {"login": session["login"]}, {'_id'})[0]["_id"]
    titre_article = form.data["creation_titre_article"]
    texte_article = form.data["creation_texte_article"]

    if form.validate_on_submit():

        new = articles.find_one({"titre": titre_article})

        if new != None:
            print("ce nom d'article existe déja , veuillez entrer un nouveau nom ")
        else:
            article ={"titre": titre_article,
                                "date": str(datetime.now()),
                                "texte": texte_article,
                                "Username": session["login"],
                                "User_ID": id_utilisateur,
                                "commentaire":[]}
            articles.insert_one(article) 
        
    return render_template("page_administration_creation.html", form=form, articles=liste_article)
