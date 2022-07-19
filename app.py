from crypt import methods
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime
from pymongo import MongoClient
import remplirbdd
from templates.formulaire import Connexion
client = MongoClient("127.0.0.1:27017")
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
from multiprocessing import connection
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,Length

class Connexion(FlaskForm):
    email = StringField("Email : ")
    submit=SubmitField("Submit : ")


client = MongoClient("127.0.0.1:27017")

db = client.blog
articles = db.articles
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'

@app.route("/",methods = ["GET","POST"])
def accueil():
    liste_article=articles.find({})
    return render_template("accueil.html", articles = liste_article)


@app.route('/article/<nom>')
def article(nom):
    mon_article =articles.find_one({"titre" : nom})
    return render_template("article.html", article=mon_article)

@app.route('/connexion',methods=['GET','POST'])
def connexion():
    email= None
    form=Connexion()
    return render_template("connexion.html",email=email, form=form)
