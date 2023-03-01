class Voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self._marque = marque 
        self._modèle = modèle 
        self._année = année 
        self._kilométrage = kilométrage
        self._marche = False
        self._réservoir = 50

    def set_marque(self, marque):
        self._marque = marque

    def set_modèle(self, modèle):
        self._modèle = modèle

    def set_année(self, année):
        self._année = année

    def set_kilométrage(self, kilométrage):
        self._kilométrage = kilométrage

    def set_marche(self, marche):
        self._marche = marche

    def set_réservoir(self, réservoir):
        self._réservoir = réservoir

    
    def get_marque(self):
        return self._marque

    def get_modèle(self):
        return self._modèle

    def get_année(self):
        return self._année

    def get_kilométrage(self):
        return self._kilométrage
    
    def get_marche(self):
        return self._marche

    def get_réservoir(self):
        return self._réservoir

    def démarrer(self):
        if self._vérif_plein() > 10:
            self._marche = True
            print("La voiture démarre.")
        else:
            print("Il n'y a pas assez d'essence dans le réservoir")

    def arrêter(self):
        self._marche = False
        print("La voiture s'arrête.")

    def _vérif_plein(self):
        return self._réservoir

#Instanciation de l'objet voiture 
voiture = Voiture("Volkswagen", "Golf", 2018, 30000)

#Utilisons les mutateurs afin de changer les attributs
voiture.set_marque("BMW")
voiture.set_modèle("X5")
voiture.set_année(2015)
voiture.set_kilométrage(100000)
voiture.set_réservoir(20)

#Maintenant, utilisons les assesseurs afin de récupérer les attributs
print("La marque est :", voiture.get_marque())
print("Le modèle est :", voiture.get_modèle())
print("L'année de la voiture est :", voiture.get_année())
print("Ella un kilométrage de :", voiture.get_kilométrage())
print("Dans le réservoir elle détient :", voiture.get_réservoir(), "L")

#Pour finir, utilisons les méthodes "démarrer" puis "arrêter" 
voiture.démarrer()
voiture.arrêter()