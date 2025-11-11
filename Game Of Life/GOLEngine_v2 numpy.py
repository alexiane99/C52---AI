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
import numpy as np 
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
        self.__alive_rule = None
        self.__dead_rule = None
        self.__rules = None
        # self.__born_rule = (3, )
        # self.__survive_rule = (2, 3)
        # Approche avec une table de recherche : LUT (Look-Up Table)
        #                    0, 1, 2, 3, 4, 5, 6, 7, 8 <--- Nbr de voisins vivants
        # self.__alive_rule = (0, 0, 1, 1, 0, 0, 0, 0, 0)
        # self.__dead_rule  = (0, 0, 0, 1, 0, 0, 0, 0, 0)
        #               0                 1
        # self.__rules = (self.__dead_rule, self.__alive_rule)
        
        self.resize(width, height)
        # self.set_rules(alive_rule, dead_rule)
    
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

    @property
    def alive_rule(self):
        return self.__alive_rule

    @alive_rule.setter
    def alive_rule(self, value):
        self.__alive_rule[value - 1] = 1 
        

    @property
    def dead_rule(self):
        return self.dead_rule

    @dead_rule.setter
    def dead_rule(self, value):
        self.__dead_rule[value - 1] = 1

    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, alive_rule, dead_rule):
       self.__rules = (alive_rule, dead_rule)
    
    @property
    def all_cells(self):
        dimy, dimx = self.__grid.shape
        return dimy * dimx 
    
    @property 
    def cells_alive(self):
        counter = 0 

        for dimy, dimx in np.ndindex(self.__grid.shape):
            if self.__grid[dimy, dimx] == 1:
                counter += 1
        
        return counter
    
    @property 
    def cells_dead(self):
        counter = 0 

        for dimy, dimx in np.ndindex(self.__grid.shape):
            if self.__grid[dimy, dimx] == 0:
                counter += 1
        
        return counter

    # À VÉRIFIER 
    def cell_value(self, x, y):
        # no input validation for performance consideration
        return self.__grid[x][y]
    
    # À VÉRIFIER 
    def set_cell_value(self, x, y, value):
        # no input validation for performance consideration
        self.__grid[x][y] = value
    
    # AJOUT 
    def fill(self, cell_value):
        self.__grid[:] = cell_value 
    
    def set_rules(self, alive_rule, dead_rule):
        self.__alive_rule = np.zeros(8)
        self.__alive_rule[alive_rule - 1] = 1

        self.__dead_rule = np.zeros(8)
        self.__dead_rule[dead_rule - 1] = 1
    
    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('width and height must be greater or equal to 3.')

        self.__width = width
        self.__height = height
        self.__grid = np.zeros((width, height))
        self.__temp = deepcopy(self.__grid)


    def randomize(self, percent=0.5):
        rng = np.random.default_rng()
        self.__grid[:] = (rng.random((self.__grid.shape)) <= percent) #astype(self.__grid.dtype)
        
    def processing(self): #tutorial : https://www.youtube.com/watch?v=cRWg2SWuXtM 

        for dimy, dimx in np.ndindex(self.__grid.shape):
            voisins_vivants = int(np.sum(self.__grid[dimy-1:dimy+2, dimx-1:dimy+2]) - (self.__grid[dimy, dimx]))

        if self.__grid[dimy, dimx] == 1:

            # à revérifier avec les alive & dead rules 
            if self.__alive_rule[voisins_vivants - 1] == 1: #si le chiffre correspond, les cells sont vivantes
                self.__grid[dimy, dimx] = 1
            else:
                self.__grid[dimy, dimx] = 0
  
         
    
    def print(self):

        for dimy, dimx in np.ndindex(self.__grid.shape):
            print("█" if self.__grid[dimy, dimx] == 1 else " ", end='')

        print()
    
class GameView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.__game_view = QHBoxLayout()

    
# quelques tests simples    
def main():
    gol = GOLEngine(12, 10)
   
    gol.resize(12, 9)
    gol.set_rules(3,4)

    print(f'taille : {gol.width} x {gol.height}')
    print(f'total cells :{gol.all_cells}')

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
    gol.processing()
    gol.print()

    pass

    valide = True

    
    while (valide):
        os.system("cls") #clear la console 
        gol.randomize(0.5)
        gol.print()
        gol.processing()
        gol.print()
        print(f'cells vivantes :{gol.cells_alive}')
        print(f'cells mortes :{gol.cells_dead}')

        time.sleep(0.1)

        if(keyboard.is_pressed("q")):
            valide = False
            break


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


