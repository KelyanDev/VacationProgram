# ================================================================================================================================================================= #
# 4. Projet n°4
# Aider un enseignant à planifier ses vacances
# Avant de partir en vacances, chaque enseignant doit s'assurer qu'il n'a pas de cours planifiés avant son retour.

# Objectif
# Afficher, pour un enseignant permanent du département donné, et pour chaque période de vacances scolaires (Toussaint, Décembre, Hiver, Printemps et Ete), l’intitulé et la date de leur dernière intervention avant les vacances, l’intitulé et la date de leur première intervention après les vacances (date de reprise) et le nombre de jours de vacances complets dont il bénéficie. Pour les vacances d’été, on considère la date de reprise fixée au 01-09-2024.

# Cahier des charges fonctionnel
# Les données seront extraites d’ADE.
# Le choix de l’enseignant sera paramétrable.
# Le script prend en compte toute l’année universitaire, c’est à dire du 1 septembre au 31 août.
# Le nombre de jours de vacances ne comptera que des jours complets non travaillés. Par exemple, si un enseignant finit ses cours le 26-10-2011 à 10h, cette journée ne sera pas comptée dans les jours de vacances.
# Fonctions spécifiques au projet
# Le script doit être découpé en différentes fonctions, pour suivre les principes de structuration du code.
# ================================================================================================================================================================= #

import pandas as pd
from datetime import datetime

ADECalendar = pd.read_csv("D:\VSCode\SAE15\ADECal.csv")

## Classe "Vacances", qui s'occupera de réaliser l'intégralité du code. Elle peut prendre en compte
class Vacances():
    ## Initialisation des attributs
    def __init__(self, prof=None):
        self.edt = ADECalendar.copy()
        self.liste = self.liste_enseignants()
        if prof == None:
            self.enseignant = self.def_enseignant()
        else:
            self.enseignant = prof
        self.cours = self.periode_cours()
        self.toussaint = self.det_vac(['2023-10-28:','2023-11-06:'])
        self.decembre = self.det_vac(['2023-12-23:','2024-01-08:'])
        self.hiver = self.det_vac(['2024-02-24:','2024-03-04:'])
        self.printemps = self.det_vac(['2024-04-13:','2024-04-29:'])
        self.ete = self.det_vac(['2024-06-20:','2024-09-01:'])

    ## Definition de la liste de l'intégralité des enseignants, triée par ordre alphabétique
    def liste_enseignants(self):
        temp_liste = set(self.edt['Enseignant'])
        liste = list(temp_liste)
        liste = [element for element in liste if not isinstance(element, float)]
        liste = sorted(liste)
        liste.remove('2A')
        liste.remove('1ATP2') 
        liste.remove('Intervenant à préciser')
        return liste
    
    ## Choix de l'enseignant, afin de choisir quel sera l'emploi du temps à analyser
    def def_enseignant(self):
        enseignant = input(f'\n Choix enseignant parmis proposition suivantes (merci de respecter la syntaxe): \n\n {self.liste} \n')
        return enseignant
    
    ## Définition de l'emploi du temps de l'enseignant préalablement choisi. Ainsi, seul son emploi du temps personnel est analysé
    def periode_cours(self):
        return self.edt[self.edt["Enseignant"] == self.enseignant].sort_values(by='Date')
    
    ## Determine la date ainsi que les horaires de début et fin de vacances pour l'enseignant préalablement choisi, en fonction de la période de vacance entrée en paramètres
    def det_vac(self,periode):
        try:
            debut = datetime.strptime (periode[0], "%Y-%m-%d:")
            fin = datetime.strptime (periode[1], "%Y-%m-%d:")

            dernier_cours = None
            premier_cours = None

            #Définition de la date du dernier cours avant les vacances
            for last in self.cours['Date']:
                last_dt = datetime.strptime(last, "%Y-%m-%d:")
                if last_dt > debut:
                    break
                dernier_cours = last

            #Définition de la date du premier cours après les vacances
            for first in self.cours['Date']:
                first_dt = datetime.strptime(first, "%Y-%m-%d:")
                if first_dt > fin:
                    premier_cours = first
                    break
        
            #Définition du nombre de jours de vacances
            nb_jours = (datetime.strptime(premier_cours, "%Y-%m-%d:") - datetime.strptime(dernier_cours, "%Y-%m-%d:")).days -1
        
            #Définition des heures de cours de l'emploi du temps de l'Enseignant
            horaires_debut = self.cours.loc[self.cours['Date'] == dernier_cours, 'HEnd']
            horaires_fin = self.cours.loc[self.cours['Date'] == premier_cours, 'HStart']
            h1 = datetime.strptime("00:00:00", "%H:%M:%S")

            #Définition de l'heure de début de svacances
            for i in horaires_debut:
                if h1 < datetime.strptime(i, "%H:%M:%S"):
                    h1 = datetime.strptime(i, "%H:%M:%S")
            h1 = h1.strftime("%H:%M:%S")

            #Définition de l'heure de fin des vacances
            for y in horaires_fin:
                h2 = datetime.strptime(y, "%H:%M:%S")
                if h2 < datetime.strptime(y, "%H:%M:%S"):
                    break
            h2 = h2.strftime("%H:%M:%S")

            #Définition des cours correspondant, en fonction de la date et de l'heure (.values[0] permet d'obtenir une chaîne de caractère)
            nom_dernier_cours = self.cours.loc[(self.cours['Date'] == dernier_cours) & (self.cours['HEnd'] == h1), 'Matière'].values[0]
            nom_premier_cours = self.cours.loc[(self.cours['Date'] == premier_cours) & (self.cours['HStart'] == h2), 'Matière'].values[0]
        
            #Renvoi des données de la période de vacances: Le dernier cours et son heure de fin, le premier cours et son heure de début          
            return f"Du {dernier_cours} {h1}, cours de {nom_dernier_cours}, jusqu'au {premier_cours} {h2}, cours de {nom_premier_cours}; vous avez {nb_jours} jours de vacances;"
        except:
            return ("Vos vacances n'ont pas pu être calculé correctement")
    
    #Renvoi l'intégralité des périodes de vacances de l'enseignant défini
    def __str__(self):
        return(f"""Bonjour Mr/Mme {self.enseignant}, voici l'ensemble de vos vacances cette année: 
               -Vacances de toussaint: {self.toussaint}
               -Vacances de décembre: {self.decembre}
               -Vacances d'hiver : {self.hiver}
               -Vacances de printemps : {self.printemps}
               """)
