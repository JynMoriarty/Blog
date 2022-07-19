from multiprocessing import connection
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,Length

class Connexion(FlaskForm):
    email = StringField("Email : ")
    
    
    #password = PasswordField("password : ",validators=[DataRequired(),Length(min=4,max=50)])
    #remember =BooleanField("Sauvegarder les identifiants",default=False)
    #submit = SubmitField("Entrer") 

    #pour le html

#{{form.hidden_tag()}}
#<p>{{form.email.label()}}{{form.email()}}</p>
#<p>{{form.password.labe()}}{{form.password()}}</p>
#<p>{{form.remember.label()}}{{form.remember()}}</p>
#<p>{{form.submit()}}</p>