from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime
from pymongo import MongoClient
from multiprocessing import connection
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,Length

class Connexion(FlaskForm):
    login = StringField("login : ")
    password = PasswordField("password : ")
    remember =BooleanField("Sauvegarder les identifiants",default=False)
    submit = SubmitField("Entrer") 

class Inscription(FlaskForm):
    login_inscription = StringField("login d'inscription : ")
    password_inscription = PasswordField("password inscription : ")
    remember_inscription =BooleanField("Sauvegarder les identifiants",default=False)
    submit_inscription = SubmitField("Entrer pour inscription") 

class Commentaire(FlaskForm):
    commentaire_utilisateur =StringField("Veuillez renter votre commentaire")
    submit_commentaire= SubmitField("Afficher votre commentaire.")

class Gestion_article(FlaskForm):
    article_ajout_titre=StringField("Veuillez entrer le titre de votre article : ")
    article_ajout_texte=StringField("Veuillez taper votre texte : ")
    submit_ajout_texte = SubmitField("Envoyer votre texte") 

class Suppression_article(FlaskForm):
    article_suppression_titre=StringField("Veuillez entrer le titre de votre article : ")
    submit_suppression_texte = SubmitField("Envoyer votre texte") 

class Gestion_commentaire(FlaskForm):
    sauvegarde_id=0
    modifier_le_commentaire=StringField("Veuillez modifier le commentaire : ")
    valider_commentaire=BooleanField("Valider le commentaire")
    submit_modération_commentaire= SubmitField("Afficher votre commentaire.")
