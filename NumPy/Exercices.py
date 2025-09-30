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
#a = np.multiply(salaire_horaire, heures_par_semaine)
# print(a)
# print(np.sum(a))

a = np.sum(np.multiply(salaire_employes, heures_par_semaine))
print(a)

#QUESTION 2
b = np.sum(np.multiply(a, semaine_par_annee)) #multiplier la masse salariale hebdomadaire par nb semaine --> masse salariale annuelle 
d = np.divide(b, salaire_employes.size) #pour trouver la moyenne, on divise par le nb d'employés, soit la taille du tableau car représente chaque employé
print(d)

#b = np.divide((np.sum(np.multiply(a, semaine_par_annee))), a.size)
#print(b)

#QUESTION 3
c = np.divide((np.sum(salaire_employes)), salaire_employes.size) #moyenne, mais médian --> 25.12$ ?? 
c = np.median(salaire_employes) #existe une fonction median dans numpy
print(c)

#fonction join


#QUESTION 4
e = np.array(salaire_employes < 15.5) #crée un tableau qui contiendra uniquement les valeurs en deça de 15.5 
print(e)



#QUESTION 5



#QUESTION 6