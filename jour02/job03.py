class Livre: 
    def __init__(self,titre, auteur, pages):
        self.__titre = titre 
        self.__auteur = auteur
        self.__pages = pages 
        self.__disponible = True

    def get_titre(self):
        return self__titre

    def set_titre(self, titre):
        return self.__titre

    def get_auteur(self):
        return self__auteur 

    def set_auteur(self, auteur):
        return self.__auteur

    def get_pages(self):
        return self_pages


    def vérification(self):
        if self.__disponible == True:
            return ("Livre disponible")
        else : 
            return ("Le livre est indisponible")


        def emprunter(self):
            if self.__disponible == True:
                self.__disponible = False
                return ("Vous avez pris le livre")
            else : 
                return ("Le livre est indisponible")

            
        def rendre(self):
            if self.__disponible == False:
                self.__disponible = True
                return ("Vous avez rendu le livre")
            else : 
                return ("Le livre n'est pas en votre possession")

#Création d'un livre avec un titre, un auteur, et un nombre de pages 
livre = Livre("Naruto", "Masashi Kishimoto", 50)
print(livre.emprunter())
