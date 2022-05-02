nom = "inconnu"

def demanderNom():
    global nom
    nom = prompt("Quel est votre nom?")

def direBonjour():
    alert("Bonjour " + nom + "!")
