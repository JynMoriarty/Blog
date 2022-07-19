from flask import Flask, render_template, redirect, url_for, request, session
<<<<<<< HEAD
from datetime import datetime
from pymongo import MongoClient
import remplirbdd
client = MongoClient("127.0.0.1:27017")
=======
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("127.0.0.1:27017")

db = client.blog
articles = db.articles
>>>>>>> refs/remotes/origin/main
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
    liste_article=articles.find({})
    return render_template("accueil.html",articles=liste_article)

@app.route('/article/<nom>')
def article(nom):
    mon_article =articles.find({"titre" : nom})
    return render_template("article.html", article=mon_article)

    
