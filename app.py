from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime
from pymongo import MongoClient
import remplirbdd
from templates.formulaire import Connexion,Inscription,Commentaire
client = MongoClient("127.0.0.1:27017")
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
from multiprocessing import connection
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,Length




client = MongoClient("127.0.0.1:27017")

db = client.blog
articles = db.articles
utilisateurs =db.utilisateurs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'

@app.route("/",methods = ["GET","POST"])
def accueil():
    liste_article=articles.find({})
    try : 
        login = session["login"]
    except:
        login =None
    return render_template("accueil.html", articles = liste_article,login=login)


@app.route('/article/<nom>',methods=['GET','POST'])
def voir_article(nom):
    mon_article =articles.find_one({"titre" : nom})
    print({"titre":mon_article["titre"]})
    form = Commentaire()
    id_utilisateur = utilisateurs.find({"login": session["login"]},{'_id'})[0]["_id"]
    #for elmt in curseur:
    new = articles.find({"titre":mon_article["titre"]})[0]["commentaire"]
 
    if form.validate_on_submit():
        new.append({"date" :str(datetime.now()),
                        "Username" :session["login"],
                        "User_ID" : id_utilisateur,
                        "text" : form.data["commentaire_utilisateur"],
                        "validé" : False

                        })
        print(new)         
        articles.update_one({"titre":mon_article["titre"]},
            {"$set" : {
                "commentaire" : new
                }
            }
        )    


    return render_template("article.html", article=mon_article,form=form)




@app.route('/inscription/',methods=['GET','POST'])
def inscription():
    form = Inscription()
    if form.validate_on_submit():
        creation_utilisateur = utilisateurs.insert_one({"login" :form.data["login_inscription"],"password":form.data["password_inscription"]})
        print(creation_utilisateur)
        return redirect(url_for("accueil"))
    return render_template("creation_compte.html",form=form)



@app.route('/connexion',methods=['GET','POST'])
def connexion():
    
    form=Connexion()
    if form.validate_on_submit(): 
        utilisateur = utilisateurs.find_one({"login" :form.data["login"],"password":form.data["password"]})
        if form.data["login"] == utilisateur["login"] and form.data["password"] == utilisateur["password"]:
            session["login"] = utilisateur["login"]
            return redirect(url_for("accueil"))
    return render_template("connexion.html", form=form)
