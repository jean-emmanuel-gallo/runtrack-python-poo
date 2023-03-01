class Livre: 
    def __init__(self,titre, auteur, pages):
        self.__titre = titre 
        self.__auteur = auteur
        self.__pages = pages 

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        return self.__titre

    def get_auteur(self):
        return self.__auteur 

    def set_auteur(self, auteur):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    

#Création d'un livre avec un titre, un auteur, et un nombre de pages 
livre = Livre("Naruto", "Masashi Kishimoto", 50)

#Afficher attributs initiaux 
print("Le titre du livre est", livre.get_titre())
print("L'auteur du livre se nomme", livre.get_auteur())
print("Le nombre de pages est de", livre.get_pages())
