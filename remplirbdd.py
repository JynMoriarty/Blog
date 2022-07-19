
from pymongo import MongoClient
from datetime import datetime
client = MongoClient("127.0.0.1:27017")
db = client.blog
articles = db.articles

db.articles.drop()
article1 =(

    {   
        "titre" : "Mastering the game of Go with deep neural networks and tree search",
        "date":str(datetime.now()),
        "texte":"The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space and the difficulty of evaluating board positions and moves. Here we introduce a new approach to computer Go that uses ‘value networks’ to evaluate board positions and ‘policy networks’ to select moves. These deep neural networks are trained by a novel combination of supervised learning from human expert games, and reinforcement learning from games of self-play. Without any lookahead search, the neural networks play Go at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play. We also introduce a new search algorithm that combines Monte Carlo simulation with value and policy networks. Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the human European Go champion by 5 games to 0. This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.",
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
articles.insert_one(article1)

article2 =(

    {   
        "titre" : "Microscope à effet tunnel",
        "date":str(datetime.now()),
        "texte":"Le microscope à effet tunnel est un microscope à champ proche qui repose sur « l'effet tunnel », un phénomène relevant de la mécanique quantique.  Mis au point par un duo de chercheurs, l'Allemand Gerd Binnig et le Suisse Heinrich Rohrer en 1981, le microscope à effet tunnel repose donc principalement sur le phénomène quantique (donnant le nom à ce microscope) qui décrit la capacité d'un objet quantique à pouvoir franchir une barrière de potentiel, quelle que soit son énergie, même si elle est trop basse.",
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
articles.insert_one(article2)
article3 =(

    {   
        "titre" : "Médaille Fields 2022 : Hugo Duminil-Copin, explorateur des frontières du hasard",
        "date":str(datetime.now()),
        "texte":"Et de treize. L’école de mathématiques française vient à nouveau d’être récompensée, mardi 5 juillet, par une médaille Fields, une distinction attribuée, tous les quatre ans, depuis 1936, lors du Congrès international des mathématiciens, pour des progrès dans la discipline réalisés par des chercheurs de moins de 40 ans.",
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
articles.insert_one(article3)




