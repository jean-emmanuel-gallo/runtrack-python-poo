class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je me nomme {self.nom}.")

class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def enseigner(self):
        print("Le cours commence.")

# Ici nous créons l'élève
eleve = Eleve("Jérome", 15)
eleve.bonjour()
eleve.allerEnCours() 
eleve.age = 15 

# Ainsi que le professeur
professeur = Professeur("Monsieur Berlusconi", 40)
professeur.bonjour() 
professeur.enseigner() 
