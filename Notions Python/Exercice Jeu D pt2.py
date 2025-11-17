import random, math 
import numpy as np

# Exercice 3.3 :

# Faites un jeu de dés pour un utilisateur.
# Au démarrage d'une partie, le programme demande à l'utilisateur les 3 informations suivantes :`
# combien de dés, entre 1 et 4, par défaut 2
# combien le nombre de faces de chaque dé (entre 4 et 16, par défaut 6)
# combien de tours, entre 1 et 10, par défaut 2

# Ensuite, le programme passe les t tours et joue pour les deux joueurs (l'utilisateur et lui-même). À chaque tour :
# il lance tous les dés pour les joueurs
# il affiche les résultats de tous les dés
# il affiche la somme cumulée de chaque joueur pour le tour
# il affiche la somme cumulée de chaque joueur pour la partie
# il invite l'utilisateur à appuyer sur une touche pour passer au tour suivant
# À la fin de la partie, le programme affiche le gagnant (le joueur avec la somme la plus élevée) et les scores finaux.
# Faites un effort pour créer des fonctions pertinentes.

class Jeu_D():
    def __init__(self, nb_joueurs):
        
        self.__interval_d = (2, 4)
        self.__interval_face = (4, 16)
        self.__interval_tours = (1, 10)
        
        self.__nb_joueurs = nb_joueurs
        self.__nb_d = self.valider_input("Entrez le nb de dés (entre 2 et 4): ", self.__interval_d, 2)
        self.__nb_faces = self.valider_input("Entrez le nb de faces (entre 4 et 16): ", self.__interval_face, 6)
        self.__nb_tours = self.valider_input("Entrez le nombre de tours (entre 1 et 10): ", self.__interval_tours, 2)
        self.__results = self.get_results_partie()
        
    def valider_input(self, instruction, interval, default):
        
        n = None 
       
        try : 
            n = int(input(instruction))
            if (interval[0] <= n <= interval[1]):
                return n 
            else:
                n = default
        except ValueError:
            print("Veuillez entrer un nombre valide")
    
    def get_result_d(self):
        
        resultat = random.randint(1, self.__nb_faces) 
        return resultat
    
    def get_results_partie(self):
        
        results = np.zeros((self.__nb_tours, self.__nb_joueurs, self.__nb_d), dtype=int)
        
        score_final = 0
        scores = np.zeros(self.__nb_joueurs, score_final)
        
        for t in range(self.__nb_tours): 
            print(f'Tour {t+1}:')
            
            for j in range(self.__nb_joueurs): 
                for d in range(self.__nb_d):
                    results[t, j, d] = self.get_result_d()
                
                print(f'Joueur {j+1} : {results[t,j].sum()} pts')
        
        # for i in range(results): #pas sûre
            # for score in results:
                
                # print(f'Pointage final pour Joueur {i + 1} : {score}')
                # best_score_index = results.index(max(results))
                # best_score = results[best_score_index]
                
                # print(f'Joueur {best_score+1} gagne la partie avec {best_score} pts!')
            
        print(f'tableau des résultats:\n {results}')
        return results 
    
        
    
def main():
        
    player = Jeu_D(2)
    

if __name__ == '__main__':
    main()
        
        
        
        

        
        