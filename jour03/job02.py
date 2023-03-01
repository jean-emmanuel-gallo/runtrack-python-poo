class CompteBancaire:
    def __init__(self, numéro, nom, prenom, solde_initial, decouvert=False):
        self.__numéro = numéro
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert = decouvert

    def afficher(self):
        print("Compte n°{} de {} {}: {} €".format(self.__numéro, self.__prenom, self.__nom, self.__solde))

    def afficherSolde(self):
        print("Solde du compte n°{} : {} €".format(self.__numéro, self.__solde))

    def versement(self, montant):
        self.__solde += montant
        print("Versement de {} € effectué sur le compte n°{}. Nouveau solde : {} €".format(montant, self.__numéro, self.__solde))

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible : solde insuffisant")
        else:
            self.__solde -= montant
            print("Retrait de {} € effectué sur le compte n°{}. Nouveau solde : {} €".format(montant, self.__numéro, self.__solde))

    def agios(self, taux):
        if self.__solde < 0:
            self.__solde -= self.__solde * taux
            print("Application des agios ({}%) sur le compte n°{}. Nouveau solde : {} €".format(taux*100, self.__numéro, self.__solde))

    def virement(self, compte_dest, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible : solde insuffisant")
        else:
            self.__solde -= montant
            compte_dest.versement(montant)
            print("Virement de {} € effectué du compte n°{} vers le compte n°{}".format(montant, self.__numéro, compte_dest.getnuméro()))

    def getnuméro(self):
        return self.__numéro
# Ici nous créons le compte
compte1 = CompteBancaire("123456789", "Durand", "Jean", 1000)

# Ici nous y affichons ses informations :
compte1.afficher()
compte1.afficherSolde()

# Voici un exemple de versement et de retrait :
compte1.versement(500)
compte1.retrait(200)

# Ici nous ajoutons l'attribut découvert et nous testons la méthode retrait avec solde négative autorisée : 
compte2 = CompteBancaire("987654321", "Dupont", "Marie", -500, True)
compte2.retrait(1000)

# Application des agios :
compte2.agios(0.05)

# Virement entre deux comptes :
compte1.virement(compte2, 300)