Trouver la meilleure solution

Ex: meilleur équipement à apporter dans son sac considérant le poids total du sac

Genetic Algorithm -> trouver solution qu'on ne peut pas calculer

Algorithme évolutionnaire

Population d'individus

individu = 1 génome avec ses propres caractéristiques (ex: binaire; équipement de randonnée -> item 1 est inclut dans le sac, item 0 ne l'est pas)

On appelle génération l'ensemble des solutions possibles à un moment donné

SELECTION -> fitness function 
détermine ce qui est un bon score, une bonne solution (ex: le poids maximal à ne pas dépasser)

SELECTION DES PARENTS : normalement les meilleurs scores des individus d'une population

MÉTHODES 
-CrossOver function (mutation? à un endroit donné) **RANDOM**!!!
-> on continue le processus de sélection jusqu'à atteindre le nombre d'individus désirés pour la prochaine génération

-Elitisme : garantit la préservation des meilleurs individus pour la prochaine génération

-Mutation : modification aléatoire d'un des bits/gène du chromosome

L'algorithme continue jusqu'à l'atteinte du résultat voulu ou le nombre de générations imposées

ordre des éléments clés:
-représentation génétique de la solution
-fonction qui génère des solutions
-fitness fonction objective
-sélection fonction
-crossover function
-mutation function

Inconvénient de l'algo -> si bcp de résultats, peut être très long à exécuter pour atteindre la solution désirée
