class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation d'un objet Animal
animal = Animal()

# Nommer l'animal
animal.nommer("Luna")
print("L'animal se nomme : ", animal.prenom)

# Afficher  l'âge  de l'animal
print("L'age de l'animal  : ", animal.age)

# Vieillissement de l'animal
animal.vieillir()

# Afficher  l'âge de l'animal après vieillissement
print("L'age de l'animal  : ", animal.age)
