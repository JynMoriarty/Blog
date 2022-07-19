from pymongo import MongoClient
from datetime import datetime
client = MongoClient("127.0.0.1:27017")
db = client.blog
articles = db.articles


article1 =(

    {   
        "titre" : "Chapitre 1 : Le commencement",
        "date":str(datetime.now()),
        "texte":"Il était une fois , une guerre sanglante qui opposa les chevaliers du continent d'Enkidiev et les insectes du seigneur Amecareth",
        "commentaire": [
            {
            "date" :str(datetime.now()),
            "Username": None,
            "User_ID": None,
            "text": "lorem ipsum"
        
            }, {
            "date" :str(datetime.now()),
            "Username": None,
            "User_ID": None,
            "text": "lorem ipsum 2"
        
            }
        ]   
    }        

)
reponse = articles.insert_one(article1)
print(articles.find_one({}))