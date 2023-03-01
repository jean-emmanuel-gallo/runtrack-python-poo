class Ville:
    def __init__(self, nom, nombrehab):
        self.__nom = nom
        self.__nombrehab = nombrehab

    def get_nom(self):
        return self.__nom

    def get_nombrehab(self):
        return self.__nombrehab

    def ajouter_population(self):
        self.__nombrehab += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        self.__ville.ajouter_population()


# Nous allons créer un objet Ville ayant pour arguments Paris et 100000 :
paris = Ville("Paris", 1000000)

# Ici nous affichons le nombre d'habitants de la ville de Paris sur la console :
print(f"Il y a {paris.get_nombrehab()} habitants à {paris.get_nom()}.")

# Nous allons créer un SECOND objet Ville ayant cette fois-ci pour arguments Marseille et 861635 : 
marseille = Ville("Marseille", 861635)

# Comme pour Paris, nous affichons le nombre d'habitants de la ville de Marseille sur la console : 
print(f"Il y a {marseille.get_nombrehab()} habitants à {marseille.get_nom()}.")

# Ensuite, nous créons les objets suivants :  
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Maintenant que nous avons crée les objets Paris et Marseille, nous allons y ajouter les nouvelles personnes : 
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Pour finir, nous allons print les nombres d'habitants de Paris et Marseille après l'arriver des nouvelles personnes créees plus haut : 
print(f"Il y a maintenant {paris.get_nombrehab()} habitants à {paris.get_nom()}.")
print(f"Il y a maintenant {marseille.get_nombrehab()} habitants à {marseille.get_nom()}.")