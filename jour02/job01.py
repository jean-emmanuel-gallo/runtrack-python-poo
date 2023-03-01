class Rectangle: 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur 

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


#Création d'un rectangle avec une longueur de 30 et une largeur de 20
rectangle = Rectangle(30, 20)

#Afficher les attributs initiaux 
print("La longueur est de :", rectangle.get_longueur())
print("La largeur est de :", rectangle.get_largeur())


#Modification de la longueur ainsi que de la largeur 
rectangle.set_longueur(20)
rectangle.set_largeur(10)

#Afficher les attributs modifiés 
print("La longueur est désormais de :", rectangle.get_longueur())
print("La largeur est désormais de :", rectangle.get_largeur())