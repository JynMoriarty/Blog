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