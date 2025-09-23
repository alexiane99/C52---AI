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
from copy import deepcopy

import os, keyboard #pip install keyboard
import time
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (QApplication
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                , QTextEdit
                                )

class GOLEngine:
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.__grid = None
        self.__temp = None

        # self.__born_rule = (3, )
        # self.__survive_rule = (2, 3)
        # Approche avec une table de recherche : LUT (Look-Up Table)
        #                    0, 1, 2, 3, 4, 5, 6, 7, 8 <--- Nbr de voisins vivants
        self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        self.__dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)
        #               0                 1
        self.__rules = (self.__dead_rule, self.__alive_rule)
        
        self.resize(width, height)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.resize(value, self.__height)
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.resize(self.__width, value)
        
    def cell_value(self, x, y):
        # no input validation for performance consideration
        return self.__grid[x][y]
        
    def set_cell_value(self, x, y, value):
        # no input validation for performance consideration
        self.__grid[x][y] = value
    
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        self.__grid = []
        self.__temp = []
        
        # self.__grid = [[0 for _ in range(self.__height)] for _ in range(self.__width)]
        self.__grid = [[0] * self.__height for _ in range(self.__width)]
        self.__temp = deepcopy(self.__grid)

    def randomize(self, percent=0.5):
        for y in range(1, self.__height - 1): 
            for x in range(1, self.__width - 1):
                self.__grid[x][y] = int(random.random() > percent)
        
    def process(self):
        for x in range(1, self.__width-1):
            for y in range(1, self.__height-1):
                # neighbours = sum(self.__grid[x-1][y-1:y+2]) \
                #            + sum(self.__grid[x  ][y-1:y+2:2]) \
                #            + sum(self.__grid[x+1][y-1:y+2])
                # neighbours = sum(sum(self.__grid[x-1][y-1:y+2]), 
                #                  sum(self.__grid[x  ][y-1:y+2:2]),
                #                  sum(self.__grid[x+1][y-1:y+2]))
                neighbours = self.__grid[x-1][y-1] \
                           + self.__grid[x-1][y  ] \
                           + self.__grid[x-1][y+1] \
                           + self.__grid[x  ][y-1] \
                           + self.__grid[x  ][y+1] \
                           + self.__grid[x+1][y-1] \
                           + self.__grid[x+1][y  ] \
                           + self.__grid[x+1][y+1]

                # if self.__grid[x][y] == 0: # mort
                #     # self.__temp[x][y] = int(neighbours in self.__born_rule)
                #     self.__temp[x][y] = self.__dead_rule[neighbours]
                # else: # vivant
                #     # self.__temp[x][y] = int(neighbours in self.__survive_rule)
                #     self.__temp[x][y] = self.__alive_rule[neighbours]
                self.__temp[x][y] = self.__rules[self.__grid[x][y]][neighbours]
                    
        self.__grid, self.__temp = self.__temp, self.__grid
    
    def print(self):
        for y in range(self.__height):
            for x in range(self.__width):
                print("█" if self.__grid[x][y] == 1 else " ", end='')
           #print()
        print()
    
    
class GameView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.__game_view = QHBoxLayout()

    
    
    
# quelques tests simples    
def main():
    gol = GOLEngine(12, 10)
   
    gol.resize(12, 9)
    print(f'taille : {gol.width} x {gol.height}')

    gol.width = 100 #13
    gol.height = 75 #8
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

    valide = True

    
    while (valide):
        os.system("cls") #clear la console 
        gol.randomize(0.5)
        gol.print()
        gol.process()
        gol.print()
        time.sleep(0.1)

        if(keyboard.is_pressed("q")):
            valide = False
            break


# if __name__ == '__main__':
#     main()
    


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


