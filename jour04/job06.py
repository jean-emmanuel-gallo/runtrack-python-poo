class Véhicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVéhicule(self):
        print(f"Marque: {self.marque}, Modèle :, Année: {self.année}, Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Véhicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.portes = 4

    def informationsVéhicule(self):
        super().informationsVéhicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre.")


class Moto(Véhicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.roue = 2

    def informationsVéhicule(self):
        super().informationsVéhicule()
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("La moto démarre.")


voiture = Voiture("Mercedes", "Class A", 2022, 18500)
voiture.informationsVéhicule()
voiture.demarrer()

moto = Moto("Yamaha","1200 VMAX", 1987, 4500)
moto.informationsVéhicule()
moto.demarrer()