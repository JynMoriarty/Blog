import hashlib

utilisateur = {"username" : "Antoine", "password" : None}

input_mot_de_passe = input("Entrez un mot de passe")
print(input_mot_de_passe)

h = hashlib.new('sha256')
h.update(input_mot_de_passe.encode())

utilisateur["password"] = h.hexdigest()

print(utilisateur["password"])