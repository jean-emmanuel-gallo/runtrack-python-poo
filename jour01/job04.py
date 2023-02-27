class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prénom = prenom

    def SePrésenter(self):
          print("Bonjour, je me nomme", self.nom, self.prénom)

personne1 = Personne("Doe", "John")
personne1.SePrésenter()

personne2 = Personne("Dupont", "Jean")
personne2.SePrésenter()
    