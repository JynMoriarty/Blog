from numpy import number
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
from templates.formulaire import Connexion,Gestion_commentaire, Inscription, Commentaire, Gestion_article, Suppression_article ,Gestion_modification_commentaire ,Gestion_supprestion_commentaire
import hashlib
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
    liste_article = articles.find({}).sort('date',-1)
    try:
        login = session["login"]
    except:
        login = None
    print(login)
    
    return render_template("accueil.html", articles=liste_article, login=login)


@app.route('/article/<nom>', methods=['GET', 'POST'])

def voir_article(nom):
    mon_article = articles.find_one({"titre": nom})
    print({"titre": mon_article["titre"]})
    form = Commentaire()
    if session["login"] is not None:
        id_utilisateur = utilisateurs.find(
            {"login": session["login"][0]}, {'_id'})[0]["_id"]

        # for elmt in curseur:
        new = articles.find({"titre": mon_article["titre"]})[0]["commentaire"]

        if form.validate_on_submit():
            new.append({"date": str(datetime.now()),
                        "Username": session["login"][0],
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
        mot_de_passe_chiffre=form.data["password_inscription"]
        h = hashlib.new('sha256')
        h.update(mot_de_passe_chiffre.encode())
        utilisateurs.insert_one(
            {"login": form.data["login_inscription"], "password":h.hexdigest(), "droit_admin" :False })

        return redirect(url_for("accueil"))
    return render_template("creation_compte.html", form=form)


@app.route('/connexion', methods=['GET', 'POST'])
def connexion():

    form = Connexion()
    if form.validate_on_submit():
        print("c'est bon")
        h = hashlib.new('sha256')

        h.update(form.data["password"].encode())
        mot_de_passe_a_retrouve = h.hexdigest()
        utilisateur = utilisateurs.find_one(
            {"login": form.data["login"], "password": mot_de_passe_a_retrouve })
        print(utilisateur)
        if form.data["login"] == utilisateur["login"] and mot_de_passe_a_retrouve == utilisateur["password"]:
            session["login"] = [utilisateur["login"],utilisateur["droit_admin"]]
            return redirect(url_for("accueil"))
    return render_template("connexion.html", form=form)



@app.route("/logout")
def logout():
    session["login"] = None
    return redirect("/")


    

@app.route('/administration_creation', methods=['GET', 'POST'])
def administration_creation():
    liste_article = articles.find({}).sort('date',-1)
    form = Gestion_article()
    id_utilisateur = utilisateurs.find(
        {"login": session["login"][0]}, {'_id'})[0]["_id"]
    titre_article = form.data["article_ajout_titre"]
    texte_article = form.data["article_ajout_texte"]

    if form.validate_on_submit():

        new = articles.find_one({"titre": titre_article})

        if new != None:
            print("ce nom d'article existe déja , veuillez entrer un nouveau nom ")
        else:
            article = {"titre": titre_article,
                       "date": str(datetime.now()),
                       "texte": texte_article,
                       "Username": session["login"],
                       "User_ID": id_utilisateur,
                       "commentaire": []}
            articles.insert_one(article)

    return render_template("page_administration_creation.html", form=form, articles=liste_article)


@app.route('/administration_modification', methods=['GET', 'POST'])
def administration_modification():
    liste_article = articles.find({}).sort('date',-1)
    form1 = Gestion_article()
    form2 = Suppression_article()

    if form1.validate_on_submit():
        new1 = articles.find_one({"titre": form1.data["article_ajout_titre"]})
        if new1 is not None:
            titre_article = form1.data["article_ajout_titre"]

            texte_article = form1.data["article_ajout_texte"]
            print(texte_article)
            print("c'est bon")
            articles.update_one({"titre": titre_article},
                                {"$set": {
                                    "texte": texte_article
                                }
            })
    if form2.validate_on_submit():
        new2 = articles.find_one(
            {"titre": form2.data["article_suppression_titre"]})
        if new2 is not None:
            titre_article_a_supprimer = form2.data["article_suppression_titre"]
            articles.delete_one({"titre": titre_article_a_supprimer})

    return render_template("page_administration_modification.html", form1=form1, articles=liste_article, form2=form2)


@app.route("/moderation_commentaire")
def moderation_commentaire():
    liste_article = articles.find({}).sort('date',-1)
    try:
        login = session["login"]
    except:
        login = None
    return render_template("affichage_article_pour_commentaire.html", articles=liste_article, login=login)


@app.route('/voir_commentaire_article/<nom>', methods=['GET', 'POST'])
def voir_commentaire_article(nom):
    form1=Gestion_modification_commentaire()
    form2=Gestion_supprestion_commentaire()
    mon_article = articles.find_one({"titre": nom}).sort('date',-1)
    print("c'est bon")
    print(mon_article)
    commentaire_a_changer = mon_article["commentaire"]
    # print(commentaire_a_changer[0])
    longueur_commentaire = articles.find({"titre": nom}, {"commentaire"})[0]
    # print(len(longueur_commentaire))

    liste_des_commentaires = []
    i = 0
    for elmt in commentaire_a_changer:
        liste_des_commentaires.append(
            (elmt["Username"], elmt["User_ID"], elmt["text"], i))
        
        i += 1
    if form1.validate_on_submit():
        redirect(url_for("/voir_commentaire_article/<nom>/<i>/<texte>"))
    return render_template("moderation_commentaire.html", article=mon_article, liste_commentaire=liste_des_commentaires, form1=form1,form2=form2)


@app.route('/voir_commentaire_article/<nom>/<i>/<texte>', methods=['GET', 'POST'])
def modifier_commentaire_article(nom, recuperer_position_commentaire, texte):

    article = articles.find_one({"titre": nom})
    liste_com = article["commentaire"]
    print(liste_com)
    print(recuperer_position_commentaire)
    liste_com[recuperer_position_commentaire].update({"text":texte})
    article.update(
         {"$set": {"commentaire":liste_com}})
                        

    return redirect(url_for('moderation_commentaire'))
    #return render_template("moderation_commentaire.html",article=article)

@app.route('/supprimer_commentaire/<nom>/<numero>',methods=['GET','POST'])
def supprimer_commentaire(nom,numero):
    article = articles.find_one({"titre": nom})
    liste_comm = article["commentaire"]
    liste_comm.pop(int(numero))
    articles.update_one({"titre":nom},
    {"$set" :{
        "commentaire": liste_comm
    }
    })
    return redirect(url_for("moderation_commentaire"))