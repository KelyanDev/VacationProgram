# ================================================================================================================================================================= #
# 4. Projet n°4
# Aider un enseignant à planifier ses vacances
# Avant de partir en vacances, chaque enseignant doit s'assurer qu'il n'a pas de cours planifiés avant son retour.

# Objectif
# Afficher, pour un enseignant permanent du département donné, et pour chaque période de vacances scolaires (Toussaint, Décembre, Hiver, Printemps et Ete), l’intitulé et la date de leur dernière intervention avant les vacances, l’intitulé et la date de leur première intervention après les vacances (date de reprise) et le nombre de jours de vacances complets dont il bénéficie. Pour les vacances d’été, on considère la date de reprise fixée au 01-09-2022.

# Cahier des charges fonctionnel
# Les données seront extraites d’ADE.
# Le choix de l’enseignant sera paramétrable.
# Le script prend en compte toute l’année universitaire, c’est à dire du 1 septembre au 31 août.
# Le nombre de jours de vacances ne comptera que des jours complets non travaillés. Par exemple, si un enseignant finit ses cours le 26-10-2011 à 10h, cette journée ne sera pas comptée dans les jours de vacances.
# Fonctions spécifiques au projet
# Le script doit être découpé en différentes fonctions, pour suivre les principes de structuration du code.
# ================================================================================================================================================================= #

import numpy as np
import pandas as pd

ADECalendar = pd.read_csv("D:\VSCode\SAE15\ADECal.csv")

Toussaint = ['28/10/2023','06/11/2023']
Décembre = ['23/12/2023','08/01/2024']
Hiver = ['24/02/2024','04/03/2024']
Printemps = ['13/04/2024','29/04/2024']

class Vacances():
    def __init__(self):
        self.enseignant = self.def_enseignant()
        self.edt = ADECalendar.copy()
        self.cours = self.periode_cours()

    def liste_enseignants(self):
        liste = set(ADECalendar['Enseignant'])
        return liste
    
    def def_enseignant(self):
        liste = self.liste_enseignants()
        enseignant = input(f'Choix enseignant parmis proposition suivantes: \n {liste} \n')
        return enseignant
        
    def periode_cours(self):
        return self.edt[self.edt["Enseignant"] == self.enseignant]
        

Test = Vacances()
print(Test.cours)