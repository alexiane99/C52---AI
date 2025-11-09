# import copy
from copy import deepcopy


a = 1
b = 3.14
c = 1 + 2j
d = 'str' # "str"
e = True
f = None
g = b'allo' # byte
h = bytearray(b'allo')

def print_info(value):
    print(f'{str(type(value)) + ' ':.<25} at {str(hex(id(value))):<15} : {value = }') # type(a).__name__

def print_all_info():
    separator = '-' * 80
    print(separator)
    print_info(a)
    print_info(b)
    print_info(c)
    print_info(d)
    print_info(e)
    print_info(f)
    print_info(g)
    print_info(h)
    print(separator)

print_all_info()

a += 1
b += 3.141592654
c += 1+2j
d += ' cool!'
e = not e
f = None
g += b' maman'
h += bytearray(b' maman')

print_all_info()


# Structures de données fondamentales

# Name                      | type  | Mutable   | Subscriptable[read/write] | Iterable  | Duplicate
# Nom                       | type  | Modifiable| Indexable[lect./écrit.]   | Itérable  | Doublon
my_str = 'Hello world' #    | str   | 0         | [1/0] par position        | 1         | 1
my_list = [0, -1, 20, 7,46]#| list  | 1         | [1/1] par position        | 1         | 1
my_tuple = (0, 1, 2, 3, 4) #| tuple | 0         | [1/0] par position        | 1         | 1
my_set = {0, 1, 2, 3, 4} #  | set   | 1         | [0/0]                     | 1         | 0
my_dicti = {0:'zero', #     | dict  | 1         | [1/1] par la clé          | 1         | [0:1] 
            1:'one',
            'two':2,
            3:'...'} 

# indexation
my_list[0] = 10
print(my_list[3])
# my_list[13] = 10
print(my_list[-1])
print(my_list[-3])
# print(my_list[-33])

# indexation++ => slicing
# [from : to] # to est exclu
print(my_list[1:3])
print(my_list[0:1])
print(my_list[3:10])
print(my_list[ :4]) # rien dans le from => 0
print(my_list[2: ]) # rien dans le to => le dernier INCLUSIVEMENT
print(my_list[2:-1])
print(my_list[:])
# [from : to : step] # to est exclu
print(my_list[0:4:2])
print(my_list[4:1:-1])
print(my_list[4::-2])
print(my_list[-1:-3:-1])
pass



# Itérateur
# i = my_list.get_iterator()
# while i != my_list.get_last_iterator():
#     print(value_of_i)
#     i += 1

for value in my_list:
    print(value)

# n = input('Veuillez saisir un entier')
n = 2
for _ in range(n):
    print('allo')

my_list = [1, 2, 3]
my_str = 'ZUT'
for info in zip(my_list, my_str):
    print(info[1] * info[0])
for n, char in zip(my_list, my_str):
    print(char * n)

colors = ('Red', 'Blue', 'Yellow')
for i, color in enumerate(colors):
    print(i + 1, ' ', color)

data = { 123:'Marcel'
        ,456:'Éric'
        ,789:'Jean-Marc'
        ,666:'Jean-Christophe'}
for k in data: # ne parcour que les clés
    print(k)
for k in data.keys(): 
    print(k)
for v in data.values(): 
    print(v)
for k, v in data.items(): 
    print(k, ' ~ ', v)
 


nom, prenom = 'Labonté', 'Éric'



# Création de liste
# 1 liste vide
a = []
a = list()

# Construction avec valeurs
# 2a construction manuelle
a = []
for value in range(10, 22, 3):
    if value % 2 == 0:
        a.append(value)
# 2b construction avec itérateur
a = list(range(10))
a = list(data)
a = list(data.values())
a = list(data.items())
# 2c litéral
a = [0, 10, 20]
# 2d
a = [None] * 20
# 2e - 'comprehension list'
# a = []
# for value in range(10):
#     if value % 2 == 0:
#         a.append(value)
a = [value for value in range(10) if value % 2 == 0]
#          ^________for_________^     
#    ^___^ append
#                    conditionnel ^_______________^
a = [value ** 2 for value in range(10)]
a = [char for char in 'Python']
a = [-1 for _ in range(10)]
a = [[0, 'allo', 3.14] for _ in range(10)]
pass






# Référence, garbage collector et concepts reliés

def show(v1, v2):
    print(v1, ' - ', v2, ' - ', hex(id(v1)), hex(id(v2)))

a = 5
b = 10
show(a, b)
b = 5
show(a, b)
a = b # ref copy

a = 'Hello'
b = a + ' world'
show(a, b)

a = [i ** 2 for i in range(10) if i % 2]
b = a # ref copy
show(a, b)

b[1] = 100
show(a, b)

b = a.copy() # shallow copy
show(a, b)
b[1] = 200
show(a, b)

a = [[i, i * 10] for i in range(3)]
b = a.copy()
show(a, b)

b[1][0] = 1000
show(a, b)


a = [[i, i * 10] for i in range(3)]
b = deepcopy(a) # deep copy
show(a, b)
b[1][0] = 1000
show(a, b)


# Changement de sujet
a = (1, 2, 3, 4)
# a[0] = 1000
a = ([0, 1], [2, 3])
a[0][1] = 1000
pass



# f-string
a = 11
b = 3.1415926547889552151564575432134535431
print(f'ici du texte')
print(f'a = {a} \npi = {b}')
print(f'pi = {a * b}')
print(f'{a = }')
print(f'{a:10}')
print(f'{a:>10}')
print(f'{a:.>10}')
print(f'{a:.<10}')
print(f'{a:.^10}')
print(f'{b:~>10.4f}')

from random import random
from datetime import datetime

# -----------------------------------------------------------------------------
# f-string
# -----------------------------------------------------------------------------
# Une chaîne de caractères dans laquelle on retrouve des valeurs issues de 
# variables, de calculs, de résultats de fonctions, etc.
#
# Il suffit de préfixer la chaîne de caractères par un "f" ou "F" pour que les 
# expressions entre accolades soient évaluées et transformée en texte. Si on 
# désire afficher des accolades, il suffit de les doubler.
# 	
# Les f-strings sont apparu avec Python 3.6 et sont maintenant considéré comme
# la méthode la plus efficace pour formater des chaînes de caractères et celle 
# à utiliser de facto. Sachez qu'il existe d'autres méthodes pour formater des
# chaînes de caractères, elles peuvent être moins efficace, plus complexe et, 
# selon le contexte, considérées obsolètes.
#
# L'approche utilisée par Python est tellement efficace que d'autres langages
# ont implémenté des fonctionnalités similaires : JavaScript (ES6), C# (6.0),
# Java (12), PHP (7.0), C++ (20), etc.
#
# Pour plus d'information, voir :
# - https://realpython.com/python-f-strings/
# - https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# - ...
#
# -----------------------------------------------------------------------------
a_string = 'Bonjour'
an_int = 666
a_float = 3.141592654
a_list = [1, 2, 3]
a_tuple = (11, 22, 33)
a_dictionary = { 'Name': 'Orange', 'RGB': (255, 128, 0) }
a_set = { 'apple', 'banana', 'cherry' }
a_datetime = datetime.now()

print(f'Une variable directement   : {a_string}') # entre accolade, la valeur est interprétée et transformée en str
print(f'Le nom et la valeur        : {an_int=}') # le = après la variable
print(f'Un calcul                  : {2.0 * a_float}') # les expressions sont possibles
print(f'Le résultat d\'une fonction : {random()}') # le résultat d'une fonction est une expression

print(f'Le formatage général :') # séparé par un : à droite
print(f' - la largeur et l\'alignement :')
print(f'   - : {an_int:<20}')
print(f'   - : {a_float:^20}')
print(f'   - : {a_string:>20}')
print(f' - le remplissage :')
print(f'   - : {an_int:20}')
print(f'   - : {a_float:.<20}')
print(f'   - : {a_string:.>20}')
print(f'Le formattage d\' un entier :')
print(f' - les bases :')
print(f'   - binaire      : {an_int:b}')
print(f'   - octale       : {an_int:o}')
print(f'   - décimale     : {an_int:d}')
print(f'   - hexadécimale : {an_int:x} ou {an_int:X}')
print(f' - les séparateurs de milliers :')
print(f'   - : {1000000:,}')
print(f'   - : {1000000:_}')
print(f'Le formattage d\' un flottant :')
print(f' - la précision :')
print(f'   - : {a_float:.2f}')
print(f'   - : {a_float:.5f}')
print(f'   - : {a_float:.9f}')
print(f' - les exposants :')
print(f'   - : {a_float:e}')
print(f'   - : {a_float:E}')
print(f'   - : {a_float:.2e}')
print(f'   - : {a_float:.2E}')
print(f' - les pourcentages (100 = 10000%, 1 = 100%, 0.01 = 1%) :')
print(f'   - : {a_float:.2%}')
print(f'   - : {1.0:.5%}')
print(f'   - : {0.25:.1%}')

# -----------------------------------------------------------------------------
print(f'La date et l\'heure :')
print(f' - Aujourd\'hui, c\'est le {a_datetime:%d/%m/%Y}')
print(f' - Il est {a_datetime:%H:%M %S sec}')
print(f' - Il est {a_datetime:%I:%M %S %p}')
print(f' - Il est {a_datetime:%d/%m/%Y %H:%M:%S:%f}')

# -----------------------------------------------------------------------------
print('Les collections (structures de données) :')
print(f' - les listes        : {a_list}')
print(f' - les tuples        : {a_tuple}')
print(f' - les dictionnaires : {a_dictionary}')
print(f' - les ensembles     : {a_set}')

# -----------------------------------------------------------------------------
print(f"Plusieurs valeurs dans une f-string avec des accolades '{{' et '}}', un entier {an_int}, une liste {a_list} et un tuple {a_tuple}.")

# -----------------------------------------------------------------------------
print(f'Les imbrications de {f"{'f-string':->10}":.>20} et {f"{'f-string':-<10}":.<20}.')

# -----------------------------------------------------------------------------
value_1 = 'CVM'
value_2 = None
print(f'Stratégie pour une valeur par défaut si une variable est None.')
print(f' - {value_1 or "valeur par défaut, au cas"}')
print(f' - {value_2 or "valeur par défaut, au cas"}')

# -----------------------------------------------------------------------------
# - il y a beaucoup plus à dire...
# - il est important de consulter la documentation officielle
# - nous reviendrons sur certains détails dans d'autres cours
# - ...

from abc import ABC, abstractmethod
from typing import override

class Shape(ABC):

    def __init__(self):
        super().__init__()
        self.color = [0, 0, 0]  # RGB color : black
        self.center = [0.0, 0.0]  # center position

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def move(self, dx, dy):
        self.center[0] += dx
        self.center[1] += dy


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self._width = width # protected
        self.__height = height # private : ATTENTION au NAME MANGLING

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Width must be a number')
        if value <= 0:
            raise ValueError('Width must be positive')
        self._width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Height must be a number')
        if value <= 0:
            raise ValueError('Height must be positive')
        self.__height = value

    @override
    def draw(self):
        # to do
        pass

    @override
    def perimeter(self):
        return 2 * (self.width + self.height)

    @override
    def area(self):
        return self.width * self.height


def main():
    r = Rectangle(10, 5)
    print(f'taille : {r.width} x {r.height}') # on observe l'accès aux accesseurs malgré l'APPARENCE d'un attribut public

    r.width = 20  # \___ on observe l'accès aux mutateurs malgré l'APPARENCE d'un attribut public
    r.height = 10 # /

    print(f'taille    : {r.width} x {r.height}')
    print(f'perimetre : {r.perimeter()} m')
    print(f'aire      : {r.area()} m²')

    price_by_surface = 2.0 # 2$ / m²
    print(f'prix      : {r.area() * price_by_surface}$')


if __name__ == '__main__':
    main()


# ---------------------------------------------------------
### Proposition d'exercices
# ---------------------------------------------------------
# 1. Améliorer la classe Shape :
#    - ajouter des property pour valider la couleur et la position (pour la couleur, les valeurs doivent être entre 0 et 255)
#    - Dans la classe Shape, ajouter la possibilité de définir la position initiale à même le __init__
# 2. Améliorer la classe Rectangle :
#    - Ajouter ces trois arguments dans la fonction __init__ :  width, height et center
#    - Les métodes area et perimeter doivent être des propriétés en lecture seule (pas de mutateur)
#    - Implémenter la méthode draw (un simple print est suffisant)
# 3. Créer une classe Circle qui hérite de Shape
#    - Ajouter un attribut privé radius avec son accesseur et son mutateur
#    - Implémenter les méthodes draw, perimeter et area