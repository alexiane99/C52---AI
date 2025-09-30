import numpy as np

salaire_horaire = [ 9.50, 33.50, 30.25, 10.75, 41.50, 16.75, 18.00, 15.50, 21.00,
                   15.25, 21.50, 38.00, 25.25, 42.00, 25.00, 18.75, 37.25, 38.50,
                   40.00, 41.00]
heures_par_semaine = 37.5           # nombre d'heures travaillées par semaine
semaine_par_annee = 52              # nombre de semaines payées par année

salaire_employes = np.array(salaire_horaire)
print(salaire_employes)

## 1) On vous demande de : 
#  1. calculer la masse salariale hebdomaraire
#  2. calculer la moyenne salariale annuelle
#  3. calculer le salaire horaire médian
#  4. produire la liste de tous les salaires inférieurs à 15.50 \$/heure
#  6. calculer combien d'employé font au moins 30.00 \$/heure
#  7. calculer le coût annuel d'une augmentation de la masse salariale de 2.5% uniquement pour les employés faisant moins de 25.00 \$/heure

#QUESTION 1
masse_salariale_hebdo = np.sum(np.multiply(salaire_employes, heures_par_semaine))
print(f'masse salariale hebdo: {masse_salariale_hebdo}')

#QUESTION 2
masse_salariale_annuelle = np.sum(np.multiply(masse_salariale_hebdo, semaine_par_annee)) #multiplier la masse salariale hebdomadaire par nb semaine --> masse salariale annuelle 
moyenne_salariale = np.divide(masse_salariale_annuelle, salaire_employes.size) #pour trouver la moyenne, on divise par le nb d'employés, soit la taille du tableau car représente chaque employé
print(f'moyenne salariale: {moyenne_salariale}')

#QUESTION 3
salaire_moyen = np.divide((np.sum(salaire_employes)), salaire_employes.size) #moyenne --> 25.12$ mais médian ?? 
print(f'salaire moyen: {salaire_moyen}')

salaire_median = np.median(salaire_employes) #existe une fonction median dans numpy
print(f'salaire median: {salaire_median}')

#QUESTION 4
small_salary = np.array(salaire_employes[salaire_employes < 15.5]) #crée un tableau qui contiendra uniquement les valeurs en deça de 15.5 
print(f'salaires sous 15.5$/h: {small_salary}')

#QUESTION 5
rich_employee = np.array(salaire_employes[salaire_employes >= 30.00])
print(f'salaires en haut de 30.00$/h: {rich_employee}')
nb_rich = rich_employee.size
print(f'nb salariés: {nb_rich}')

#QUESTION 6
salaire_moins25 = np.array(salaire_employes[salaire_employes < 25.00])
print(f'salaires sous 25.00$/h: {salaire_moins25}')
nb_moins25 = salaire_moins25.size
print(f'nb employes: {nb_moins25}')
masse_salariale_moins25 = np.multiply((np.multiply(salaire_moins25, heures_par_semaine)), semaine_par_annee)
augm = np.multiply(masse_salariale_annuelle, 2.5)
print(f'augmentation 2.5%: {augm}')