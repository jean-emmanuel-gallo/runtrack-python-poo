class Forme:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.radius ** 2
rectangle = Forme(10, 5)
aire_rectangle = rectangle.aire()
print("Aire du rectangle : ", aire_rectangle)

cercle = Cercle(5)
aire_cercle = cercle.aire()
print("Aire du cercle : ", aire_cercle)