from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime
from pymongo import MongoClient
import remplirbdd
client = MongoClient("127.0.0.1:27017")
app = Flask(__name__)

@app.route("/")
def accueil():
    liste_article = [

        {
            "titre": "Titre1",
            "text": "Lorem ",
            "date": str(datetime.now())
        }, {
            "titre": "Titre2",
            "text": "Lorem2",
            "date": str(datetime.now())
        },{
            "titre": "Titre3",
            "text": "Lorem3",
            "date": str(datetime.now())
        }
    ]
    return render_template("accueil.html", articles = liste_article)

#@app.route()
#def article():
    #return render_template("article.html")
#@app route("/")
#def bdd():