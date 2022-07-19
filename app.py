from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("127.0.0.1:27017")

db = client.blog
articles = db.articles
app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def accueil():
    liste_article=articles.find({})
    return render_template("accueil.html",articles=liste_article)

@app.route('/article/<nom>')
def article(nom):
    mon_article =articles.find({"titre" : nom})
    return render_template("article.html", article=mon_article)

    
