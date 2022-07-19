from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient
from datetime import datetime
client = MongoClient("127.0.0.1:27017")
db = client.blog
articles = db.articles
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/article")
def article():
    return render_template("article.html",all_articles = articles.find_one())

