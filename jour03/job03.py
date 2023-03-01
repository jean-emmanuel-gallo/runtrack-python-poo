class tâche:
    def __init__(self, titre, description, statut='A faire'):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = 'Terminée'


class ListeDetâches:
    def __init__(self):
        self.tâches = []

    def ajouter_tâche(self, tâche):
        self.tâches.append(tâche)

    def supprimer_tâche(self, tâche):
        self.tâches.remove(tâche)

    def afficher_liste(self):
        for tâche in self.tâches:
            print(f"{tâche.titre} - {tâche.description} - {tâche.statut}")

    def filter_liste(self, statut):
        filtered_tâches = []
        for tâche in self.tâches:
            if tâche.statut == statut:
                filtered_tâches.append(tâche)
        return filtered_tâches
# Création des tâches
tâche1 = tâche("Aller à la salle", "Faire du développé couché")
tâche2 = tâche("Apprendre Python", "Parce que je galère comme un fou")
tâche3 = tâche("Bosser encore sur Python", "Parce que je galère toujours comme un fou")

# Création de la liste de tâches
liste_tâches = ListeDetâches()

# Ajout des tâches à la liste
liste_tâches.ajouter_tâche(tâche1)
liste_tâches.ajouter_tâche(tâche2)
liste_tâches.ajouter_tâche(tâche3)

# Afficher la liste des tâches
print("Liste des tâches :")
liste_tâches.afficher_liste()

# Supprimer une tâche
liste_tâches.supprimer_tâche(tâche2)

# Afficher  la liste des tâches mise à jour
print("Liste des tâches après suppression :")
liste_tâches.afficher_liste()

# Marquage d'une tâche comme terminée
tâche1.marquer_comme_finie()

# Affichage de la liste des tâches à faire
print("Liste des tâches à faire :")
tâches_a_faire = liste_tâches.filter_liste('A faire')
for tâche in tâches_a_faire:
    print(f"{tâche.titre} - {tâche.description}")