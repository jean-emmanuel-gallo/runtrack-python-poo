class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")
personne1 = Personne()

eleve1 = Eleve()

eleve1.affichageAge() 

personne1.modifierAge(25)

personne1.afficherAge() 

personne1.bonjour() 

eleve1.allerEnCours()

professeur1 = Professeur("Mathématiques")
professeur1.enseigner() 