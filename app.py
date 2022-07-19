from flask import Flask, render_template, redirect, url_for, request, session
import remplirbdd
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route()
def article():
    return render_template("article.html")

@app route("/")
def bdd():