# Moteur de jeu de la vie (Game Of Life).
#
# Version préliminaire simple et fonctionnelle.
#
# Cette implémentation respecte l'encapsulation et l'utilisaiton des propriétés.
#
# Toutefois, elle est sans :  
#  - documentation
#  - tests
#  - optimisation
#  - interface graphique (c'est désirée puisque c'est un moteur)


import random
import copy


class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None #permet de sauvegarder une copie temporaire pour la prochaine génération sans écraser l'ancienne

        #self.survie_rule = tuple(2,3)

        #Approche avec une table de recherche : LUT (Look-up Table)
        #                    0, 1, 2, 3, 4, 5, 6, 7 , 8 --> nb de voisins vivants 
        # permet d'éviter l'utilisation de if, ce qui ralentit le processus
        self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        self.__dead_rule = (0, 0, 0, 1, 0, 0, 0, 0, 0)

        #                0,                       1
        self.__rules = (self.__dead_rule, self.__alive_rule)
        
        self.resize(width, height) #permet de créer la grille vide 
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.resize(value, self.__height) #attribue directement le resize pour ne pas avoir à le mentionner chaque fois
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.resize(self.__width, value)
        
    def cell_value(self, x, y): #lecture de la case
        # no input validation for performance consideration
        return self.__grid[x][y]
        
    def set_cell_value(self, x, y, value): #changer la valeur de la case 
        # no input validation for performance consideration
        self.__grid[x][y] = value
    
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        self.__grid = []
        self.__temp = []
        
        self.__grid = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        self.__grid = [[0] * self.__height for _ in range(self.__width)]
        self.__temp = copy.deepcopy(self.__grid) 

        for x in range(width):
            self.__grid.append([])
            self.__temp.append([])
            for _ in range(height):
                self.__grid[x].append(0)
                self.__temp[x].append(0)
    
    #permet de créer 2 grilles vides remplies de 0 

    def randomize(self, percent=0.5):
        # petit correctif ici, on ne touche pas aux bords
        for y in range(1, self.__height - 1): 
            for x in range(1, self.__width - 1):
                self.__grid[x][y] = int(random.random() > percent)
        
    def process(self): #c'est ici qu'on calcule la nouvelle génération, la logique du jeu
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                neighbours = 0 #permet de compter tous les voisins autour de x, y et le retire (0,0)
                neighbours = sum(self.__grid[x-1][y-1:y+2]) \
                           + sum(self.__grid[x][y-1:y+2:2]) \
                           + sum(self.__grid[x+1][y-1:y+2]) 
                #slicing : saute de 2, passe le centre
                # bon code et claire aussi même si long à écrire
                # neighbours = self.__grid[x-1][y-1] \
                #             + self.__grid[x-1][y] \
                #             + self.__grid[x-1][y+1] \
                #             + self.__grid[x][y-1] \
                #             + self.__grid[x][y+1] \
                #             + self.__grid[x+1][y-1] \
                #             + self.__grid[x+1][y] \
                #             + self.__grid[x+1][y+1] \
                            
                for i in range(-1,2):
                    for j in range(-1,2):
                        # if i != 0 or j != 0:
                        #     # neighbours += 1 if world[x+i][y+j] == 1 else 0
                        #     neighbours += self.__grid[x+i][y+j]
                        neighbours += self.__grid[x+i][y+j]
                neighbours -= self.__grid[x][y]

                if self.__grid[x][y] == 0: # mort
                    # self.__temp[x][y] = 1 if neighbours == 3 else 0
                    #self.__temp[x][y] = int(neighbours == 3) #naît s'il y a 3 voisins

                    self.__temp[x][y] = self.__dead_rule[neighbours]
                else: # vivant
                    # temp[x][y] = 1 if neighbours == 2 or neighbours == 3 else 0
                    # self.__temp[x][y] = 1 if neighbours in (2, 3) else 0
                   
                    self.__temp[x][y] = int(neighbours in (2,3)) #demeure vivant si 2 ou 3 voisins

                    #self.__temp[x][y] = self.__alive_rule[neighbours]
                    # in --> lent :(
                    
                #self.__temp[x][y] = self.__rules[self.__grid[x][y][neighbours]]

        # for y in range(self.__height):
        #     for x in range(self.__width):
        #         self.__world[x][y] = self.__temp[x][y]

        # from copy import deepcopy
        # self.__world = deepcopy(self.__temp)
        self.__grid, self.__temp = self.__temp, self.__grid # à la fin, on interchange les grilles
    
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__grid[x][y], end='')
            print()
        print()
    
    
    
    
    
# quelques tests simples    
def main():
    gol = GOLEngine(12, 10)
    
    gol.resize(12, 9)
    print(f'taille : {gol.width} x {gol.height}')

    gol.width = 13
    gol.height = 8
    print(f'taille : {gol.width} x {gol.height}')

    gol.set_cell_value(4, 3, 0)
    gol.set_cell_value(5, 3, 1)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')

    gol.randomize(0.95)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')

    gol.randomize(0.05)
    print(f'(4, 3) = {gol.cell_value(4, 3)}')
    print(f'(5, 3) = {gol.cell_value(5, 3)}')
    
    gol.randomize(0.5)
    gol.print()
    gol.process()
    gol.print()

    pass


if __name__ == '__main__':
    main()
    


# ---------------------------------------------------------
### Proposition d'exercices
# ---------------------------------------------------------
# 1. Tentez d'améliorer le moteur afin de le rendre plus performant.
#    Par exemple, on peut éviter des allocations mémoire inutiles, des conditions inutiles et des boucles explicites en Python.
# 2. Ajouter une méthode 'fill(cell_value)' qui remplit toute la grille avec la valeur donnée (0 ou 1).
# 2. Changer le code pour qu'on puisse changer la règle du jeu (naissance et survie).
#    Par exemple, la règle actuelle est : naissance = 3, survie = 2 ou 3.
#    On pourrait imaginer une règle comme : naissance = 3 ou 6, survie = 2, 3 ou 4.
#    Faites en sorte qu'on puisse définir ces deux groupes de conditions, que vous donnez accès à des propriétés et que la fonction process les utilise.
# 3. Ajouter dans le moteurs des propriétés en lecture seule pour donner accès à ces statistiques :
#    - nombre de cellules totales
#    - nombre de cellules vivantes (en absolu et en relatif)
#    - nombre de cellules mortes (en absolu et en relatif)
#    - nombre de générations (nombre d'appels à process) 
#      Attention, dès que la grille change (resize, randomize ou fill), le compteur doit être remis à zéro.
#



