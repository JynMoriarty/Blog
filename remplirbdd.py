from pymongo import MongoClient
from datetime import datetime
client = MongoClient("127.0.0.1:27017")
db = client.blog
article = db.articles


article.test.insert_one(

    {   
        "titre" : "Chapitre 1 : Le commencement",
        "date":str(datetime.now()),
        "pseudo" : "Michel",
        "texte":"Il était une fois , une guerre sanglante qui opposa les chevaliers du continent d'Enkidiev et les insectes du seigneur Amecareth",
        "commentaire": "."
    }   

)

