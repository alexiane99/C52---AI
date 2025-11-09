
# Introduction à Python - Cours 2

## Partie 2a

### Fonctions

- Le paradigme de programmation fonctionnelle est très important en Python
- Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique
- Une fonction est définie à l'aide du mot-clé `def` suivi du nom de la fonction, des parenthèses et d'un deux-points `:`
- Une fonction peut prendre des paramètres en argument (déclarée entre parenthèses et considérée comme des variables locales)
- Les fonctions retournent toujours une valeur (à quelques exceptions près)
    - explicitement avec le mot-clé `return`
    - implicitement, si aucune valeur n'est retournée, ainsi la fonction retourne toujours `None`
- La syntaxe générale est la suivante :
```Python
# Exemple de définition de fonction

def nom_de_la_fonction_1():
    # bloc de code
    pass
    # retourne implicitement None

def nom_de_la_fonction_2(param1, param2):
    # bloc de code
    return valeur_de_retour

def print_hello():
    print("Hello, World!")

def add(a, b):
    resuilt = a + b
    return result
```
- Comme pour tous les autres langages, les fonctions peuvent être appelées en utilisant leur nom suivi de parenthèses et en passant les arguments requis
```Python
# Exemple d'appel de fonction

print_hello()
add(5, 10)
```

- Les fonctions peuvent également être définies avec des paramètres par défaut, ce qui permet de les appeler sans fournir tous les arguments

```Python
# Exemple de fonctions avec un paramètre par défaut

def add(a, b=0):
    return a + b

def print_message(message = "Hello, World!", count = 1):
    for _ in range(count):
        print(message)

# Exemple d'appel de fonction avec un paramètre par défaut
result = add(5, 10)  # b prend la valeur donnée de 10
result = add(5)  # b prend la valeur par défaut de 0

print_message()  # affiche "Hello, World!" une fois
print_message("Bonjour maman!")  # affiche "Bonjour maman!" une fois
print_message("Bonjour, le monde!", 3)  # affiche "Bonjour, le monde!" trois fois

```

- La surchage de fonction n'est pas supportée en Python. À la place, Python offre un modèle de passage d'arguments différents des autres langages, permettant différents types de passage d'argument. Nous y reviendrons dans d'autres cours.
- En informatique, les fonctions sont un sujet plus large qu'il n'y paraît. Python offre des fonctionnalités avancées que nous couvrirons plus en détail dans ce cours mais davantage à la prochaine session.
- Finalement, rappelez-vous toujours cet axiome `DRY` (_Don't Repeat Yourself_) : évitez de répéter le même code plusieurs fois, utilisez des fonctions pour encapsuler la logique réutilisable. Sauf dans quelques cas particuliers, il est largement préférable de ne pas répéter le même code plusieurs fois dans un programme. C'est la raison même des paradigmes de programmation procédurale, fonctionnelle et orientée objet (en partie)! 
    - Préférez-vous `DRY` ou `WET` (_Write Everything Twice_ ou _We Enjoy Typing_) ?
    - Évidemment, il y a quelques exceptions et nuances, mais en général, c'est une excellente règle! Surtout pour de jeunes programmeurs en situation d'apprentissage. 
    - Cette pratique demande un effort supplémentaire qui se développe au fil des années et qui est recherchée dans l'industrie (fonctions, structures, classes, ...).



### Modules

- Un module est un fichier Python contenant du code réutilisable, tel que des fonctions, des classes ou des variables.
- Les modules permettent de structurer le code en séparant les fonctionnalités en fichiers distincts, facilitant ainsi la réutilisation et la maintenance du code.
- Pour utiliser un module, il faut l'importer dans le script Python en utilisant le mot-clé `import` suivi du nom du module.
- Pour utiliser un élément spécifique du module dans le code, il faut préfixer le nom de l'élément par le nom du module suivi d'un point `.`. Par exemple, si le module s'appelle `math` et que l'on souhaite utiliser la fonction `sqrt`, on écrira `math.sqrt(9)`.
- Il est possible d'importer un module entier ou des éléments spécifiques d'un module en utilisant la syntaxe `from <module> import <element>`. Avec cette syntaxe, on peut utiliser directement l'élément sans préfixer par le nom du module. De plus, les autres éléments du module ne sont pas importés, ce qui peut être utile pour éviter les conflits de noms.
- Il est aussi possible d'utiliser un alias créé par le mot réservé `as` renommant le module ou l'élément importé, ce qui peut être utile pour éviter les conflits de noms ou pour simplifier le code. Par exemple, on peut écrire `import tkinter as tk` pour renommer le module `tkinter` en `tk`, et ensuite utiliser `tk` pour accéder aux éléments de ce module. Par exemple, `tk.Button()` au lieu de `tkinter.Button()`.

```Python
# Importation du module math

import math
result = math.sqrt(16)  # result vaut 4.0
```

```Python
# Importation spécifique de la fonction sqrt du module math

from math import sqrt
result = sqrt(25)  # result vaut 5.0
```

```Python
# Importation du module math avec un alias
import math as m
result = m.sqrt(36)  # result vaut 6.0
```

- Python dispose d'une vaste bibliothèque standard de modules intégrés, tels que `math`, `os`, `sys`, `random`, `datetime`, etc. Ces modules offrent des fonctionnalités variées pour effectuer des opérations mathématiques, manipuler des fichiers et des répertoires, générer des nombres aléatoires, travailler avec des dates et des heures, etc.
- Il est également possible d'installer des modules tiers à l'aide de gestionnaires de paquets tels que `pip`. Ces modules peuvent être trouvés sur le [Python Package Index (PyPI)](https://pypi.org/), qui est la principale source de bibliothèques Python.
- Il est également possible de créer ses propres modules en écrivant du code dans un fichier Python et en l'importer dans d'autres scripts. Pour cela, il suffit de créer un fichier avec l'extension `.py` contenant le code souhaité, puis de l'importer dans un autre script en utilisant le mot-clé `import` suivi du nom du fichier sans l'extension `.py`. Nous couvrirons ce sujet dans la prochaine partie.

- Quelques modules standards importants :
    - `math` : fournit des fonctions mathématiques de base comme `pi`, `sin`, `cos`, `tan`, `sqrt`, `pow`, `log`, `exp`, etc
    - `random` : permet de générer des nombres aléatoires
        - `random.random()` : génère un nombre à virgule flottante aléatoire entre 0 et 1 (la borne supérieure est excluse)
        - `random.randint(a, b)` : génère un entier aléatoire entre `a` et `b` (la borne supérieure est incluse)
        - `random.uniform(a, b)` : génère un nombre à virgule flottante aléatoire entre `a` et `b` (la borne supérieure est incluse)
        - `random.choice(sequence)` : choisit un élément aléatoire dans une séquence
    - `datetime` : permet de travailler avec les dates et les heures
        - `datetime.datetime.now()` : obtient la date et l'heure actuelles
        - `datetime.timedelta(days=1)` : représente une durée de temps
        - `datetime.date.today()` : obtient la date actuelle
    - `time` : permet de travailler avec le temps
        - `time.sleep(seconds)` : suspend l'exécution du programme pendant un certain nombre de secondes
        - `time.time()` : obtient le temps écoulé depuis le 1er janvier 1970 (timestamp)
        - `time.perf_counter()` : obtient un compteur pour mesurer le temps d'exécution
    - `re` : permet de travailler avec les expressions régulières
        - `re.match(pattern, string)` : tente de faire correspondre un motif au début d'une chaîne
        - `re.findall(pattern, string)` : trouve toutes les occurrences d'un motif dans une chaîne
    - `os` : permet d'interagir avec le système d'exploitation
        - `os.path` : fournit des fonctions pour manipuler les chemins de fichiers
        - `os.environ` : permet d'accéder aux variables d'environnement
    - `sys` : fournit des fonctions et des variables pour interagir avec l'interpréteur Python
        - `sys.argv` : liste des arguments de la ligne de commande
        - `sys.exit()` : permet de quitter le programme
    - ... et bien d'autres encore !

```Python
# Exemple d'utilisation de quelques modules standards

# Importation des modules
import math
import random
import time

# Définition des constantes et variables
COUNT = 10000
RANGE = 10000
ref_time = time.perf_counter()  # prend un compteur de référence

# Fait un calcul relativement lourd
for _ in range(COUNT):
    # Génère un entier aléatoire dans l'intervalle [-RANGE, RANGE]
    value = random.randint(-RANGE, RANGE)
    # Calcule la racine carrée de la valeur aléatoire
    value = math.sqrt(value)  

# Calcule le temps écoulé et l'affiche
elapsed_time = time.perf_counter() - ref_time  
print("Temps écoulé pour ", COUNT, " itérations : ", elapsed_time, " secondes")
```

### Exercices 3

- Exercice 3.1 : 
    - Générerez _n_ nombres aléatoires dans l'intervalle [0, 100] et affichez à l'écran ces statistiques :
        - le nombre de valeurs générées
        - valeur la plus petite
        - valeur la plus grande
        - moyenne
        - le temps d'exécution de l'algorithme
        - optionnellement :
            - la variance (la variance est la moyenne des carrés des écarts à la moyenne)
            - l'écart-type (l'écart-type est la racine carrée de la variance)
            - la médiane
    - _n_ est un nombre saisie par l'utilisateur au début du programme. Il doit être borné entre 3 et 10000. Si l'utilisateur saisit une valeur invalide, le programme remplace automatiquement par 100.
    - voici quelques considérations pour cet exercice :
        - vous pouvez utiliser les modules `random`, `math` et `time`
        - vous pouvez utiliser une liste pour stocker les valeurs aléatoires
        - les fonctions suivantes existent directement dans le _core_ Python :
            - `len(...)`
            - `min(...)`
            - `max(...)`
            - `sum(...)`
            - `sorted(...)`
        - pratiquez-vous en créant ces fonctions utilitaires :
            - `get_n()` : retourne la valeur _n_ saisie par l'utilisateur (la valeur est adaptée)
            - `generate_random_values(n, min_value, max_value)` : génère et retourne une liste de _n_ valeurs aléatoires dans l'intervalle [min_value, max_value]
            - `mean(values)` : calcule et retourne la moyenne d'une liste de valeurs
            - `variance(<à votre choix>)` : calcule et retourne la variance d'une liste de valeurs
            - `stddev(<à votre choix>)` : calcule et retourne l'écart-type d'une liste de valeurs
            - `median(<à votre choix>)` : calcule et retourne la médiane d'une liste de valeurs

- Exercice 3.2 :
    - Écrivez un programme qui demande à l'utilisateur de saisir une phrase et qui affiche :
        - le nombre de caractères
        - le nombre de voyelles : <br> `vowels = 'aeiouy'`
        - le nombre de consonnes : <br> `consonants = 'bcdfghjklmnpqrstvwxz'`
        - le nombre de caractères spéciaux (ponctuation, espaces, etc.) :  <br> `special_characters = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`
        - le nombre de mots
    - Vous devez créer au moins ces fonctions utilitaires :
        - `get_sentence()` : retourne la phrase saisie par l'utilisateur
        - `sentence_stats(sentence)` : une seule fonction qui retourne un tuple avec les statistiques suivantes :
            - le nombre de caractères
            - le nombre de voyelles
            - le nombre de consonnes
            - le nombre de caractères spéciaux
            - le nombre de mots
    - Autres astuces :
        - consulter la méthode `str.split()` 

- Exercice 3.3 :
    - Faites un jeu de dés pour un utilisateur. 
    - Au démarrage d'une partie, le programme demande à l'utilisateur les 3 informations suivantes :`
        - combien de dés, entre 1 et 4, par défaut 2
        - combien le nombre de faces de chaque dé (entre 4 et 16, par défaut 6)
        - combien de tours, entre 1 et 10, par défaut 2
    - Ensuite, le programme passe les _t_ tours et joue pour les deux joueurs (l'utilisateur et lui-même). À chaque tour :
        - il lance tous les dés pour les joueurs
        - il affiche les résultats de tous les dés
        - il affiche la somme cumulée de chaque joueur pour le tour
        - il affiche la somme cumulée de chaque joueur pour la partie
        - il invite l'utilisateur à appuyer sur une touche pour passer au tour suivant
    - À la fin de la partie, le programme affiche le gagnant (le joueur avec la somme la plus élevée) et les scores finaux.
    - Faites un effort pour créer des fonctions pertinentes.


# Introduction à Python - Cours 2

## Partie 2b

### Programmation orientée objet

- Généralités et rappels :
    - La POO est un paradigme de programmation qui permet de modéliser des objets du monde réel (abstraits ou concrets) en utilisant des classes et des objets.
    - La POO permet de structurer le code en regroupant les données et les comportements associés dans des entités appelées classes. 
    - Une classe est une définition d'un type d'objet, tandis qu'un objet est une instance de cette classe.
    - La POO permet de créer des objets qui encapsulent des données et des comportements, facilitant ainsi la réutilisation du code et la modularité. `DRY`
    - Rappelez-vous les grands principes de la POO :
        - **Abstraction** : représenter des concepts abstraits et concrets par des classes et des objets simples.
        - **Encapsulation** : regrouper les données et les comportements associés dans une classe.
        - **Héritage** : permettre à une classe de hériter des propriétés et des méthodes d'une autre classe.
        - **Polymorphisme** : permettre à des objets de différentes classes d'être traités de manière uniforme.
    - La POO n'est pas sans faille et ne prétend pas être la solution à tous les problèmes de programmation. Comme tous les paradigmes de programmation, elle offre des avantages et des inconvénients. Comme tout, son usage est une question de compromis. Néanmoins, son importance dans l'industrie et le développement logiciel fait d'elle le paradigme le plus important dans l'apprentissage du métier. Elle permet un excellent formalisme, une abstraction des concepts en jeu et une excellente organisation du code.

- En Python :
    - En Python, la programmation orientée objet (POO) est fondamentale. En fait, Python est un langage orienté objet par défaut. Plus précisément, **tout** est un objet en Python, y compris les fonctions et les types de données primitifs.
    - Déclaration d'une classe :
        - En Python, les classes sont définies à l'aide du mot-clé `class` suivi du nom de la classe et d'un deux-points `:`.
        - Les attributs (variables) et les opérations (méthodes ou fonctions) de la classe sont définis à l'intérieur de la classe.
        - Contrairement aux langages statiques C++ et Java, la déclaration des attributs n'est pas limitée à la définition statique de la classe, ils peuvent être ajouté dynamiquement à n'importe quel moment.
        - Les attributs sont généralement définis dans la méthode spéciale `__init__`, qui est appelée lors de la création d'une instance de la classe. Cette méthode permet d'initialiser les attributs de l'objet. Nous reviendrons en détail sur cette méthode dans d'autres cours.
        - Les opérations sont généralement définies comme des méthodes de la classe, en utilisant le mot-clé `def` suivi du nom de la méthode et d'un deux-points `:`. La première variable d'une méthode **est toujours** `self`, qui fait référence à l'instance de la classe (exactement comme `this` de C++ et Java). La différence est que `self` doit être explicitement déclaré dans la définition de la méthode en Python alors qu'il est implicite en C++ et Java.
        - Python ne supporte pas les modificateurs d'accès (le masquage : `package`,`public`, `protected` et `private`) comme en C++ et Java. Nous reviendrons sur ce sujet plus tard cette session. 
    - Héritage :
        - L'héritage est également pris en charge en Python, permettant à une classe de hériter des propriétés et des méthodes d'une autre classe. La syntaxe pour l'héritage est `class NomDeLaClasse(NomDeLaClasseParent):`.
        - Contrairement à Java mais comme C++, Python supporte l'héritage multiple, ce qui signifie qu'une classe peut hériter de plusieurs classes parentes.
    - Polymorphisme :
        - Le polymorphisme est également pris en charge, permettant à des objets de différentes classes d'être traités de manière uniforme. 
        - Contrairement à C++ et Java, il n'y a pas de mots réservés comme `virtual`, `override` et `final` spécifiques pour déclarer le polymorphisme.
        - En fait, il suffit de définir des méthodes avec le même nom dans différentes classes pour que le polymorphisme fonctionne (_override_ implicite).
    - Instanciation d'une classe, création d'un objet :
        - Pour créer une instance (un objet) d'une classe, il suffit d'appeler le nom de la classe comme une fonction, en passant les arguments requis par la méthode `__init__` si nécessaire.
        - Contrairement à d'autres langages, il n'existe pas d'opérateur `new` en Python. De plus, comme en Java et contrairement à C++, Python utilise un _garbage collector_ pour gérer automatiquement la mémoire. Donc, pas besoin d'utiliser manuellement la fonction `free` ou l'opérateur `delete`.
        - Par exemple, si la classe s'appelle `MaClasse`, on peut créer une instance en écrivant `mon_objet = MaClasse()`.
    - Le sujet du _POO- est vaste et complexe. Il reste plusieurs autres concepts importants à aborder, tels que les classes abstraites, les interfaces, les propriétés, les décorateurs, etc. 

```Python
# Exemple de définition de classe

# Déclaration de la classe
class UneClasse:

    # Méthode spéciale d'initialisation
    def __init__(self, valeur = 0):
        # On crée un attribut 'valeur' pour l'objet
        self.valeur = valeur

    # Définition d'une méthode
    def afficher(self):
        print("Valeur :", self.valeur)

# Exemple d'instanciation de la classe et d'utilisation de l'objet
obj_1 = UneClasse() # <<< Création d'une instance de la classe
obj_2 = UneClasse(42) # <<< Création d'une instance de la classe

# Accès direct à un attribut de l'objet
print(obj_1.valeur)  # <<< en lecture
obj_1.valeur = 100 # <<< en écriture

# Appel d'une méthode de l'objet
obj_1.afficher()
```




## Gestion d'exceptions

- En Python, la gestion des exceptions est effectuée à l'aide des mots-clés `try`, `except`, `finally` et `raise`.
- Le bloc `try` contient le code qui peut potentiellement générer une exception. Si une exception se produit, le flux d'exécution est transféré au bloc `except`.
- Le bloc `except` contient le code qui gère l'exception. Il est possible 
    - de capturer des exceptions spécifiques en spécifiant le type d'exception après le mot-clé `except`
    - d'avoir plusieurs blocs `except` pour gérer différents types d'exceptions
    - d'utiliser un bloc `except` sans spécifier de type d'exception pour capturer toutes les exceptions 
- Le bloc `finally` est optionnel et contient le code qui sera exécuté à la fin, qu'une exception se soit produite ou non. Il est souvent utilisé pour libérer des ressources ou effectuer des opérations de nettoyage.
- Le mot-clé `raise` est utilisé pour déclencher une exception manuellement. Il peut être utilisé pour signaler des erreurs spécifiques ou pour relancer une exception capturée.
- Il existe des exceptions intégrées en Python, telles que `ValueError`, `TypeError`, `IndexError`, `KeyError`, etc. Il est également possible de créer des exceptions personnalisées en définissant une nouvelle classe qui hérite de la classe `Exception`.

```Python
# Exemple complet de gestion d'exceptions

def process(data, index):
    if not isinstance(data, list):
        raise TypeError("data doit être une liste")
    if len(data) == 0:
        raise ValueError("data ne peut pas être vide")
    if index < 0 or index >= len(data):
        raise IndexError("index hors limites")
    
    return data[index]

value = [0, 1, 2, 3, 4]

try:
    result = process(value, 10)
    print("Résultat :", result)
except TypeError as e:
    print("TypeError :", e)
except ValueError as e:
    print("ValueError :", e)
except IndexError as e:
    print("IndexError :", e)
except Exception as e:  # capture toutes les autres exceptions
    print("Exception inattendue :", e)
finally:
    print("Fin du traitement")

``` 






## main

- Fonction `main`
    - En Python, il n'y a pas de fonction `main` par défaut comme dans d'autres langages (C, C++, Java, ...). Cependant, il est courant de définir une fonction `main` pour organiser le code principal du programme.
    - La convention est de définir une fonction `main()` et de l'appeler à la fin du script, en utilisant la condition `if __name__ == "__main__":` pour s'assurer que le code ne s'exécute que si le script est exécuté directement, et non importé en tant que module.
    - Cette convention permet de structurer le code et de le rendre plus lisible, en séparant la logique principale du reste du code. De plus, cela permet de ne pas polluer l'espace de noms global avec des variables et des fonctions définies dans le script.
    - Exemple :
```Python
# Exemple de fonction main

def utility_function():
    print("Ceci est une fonction utilitaire.")

def main():
    # Code principal du programme
    var = 0
    utility_function()
    

if __name__ == "__main__": # <<< Nous reviendrons sur cette syntaxe plus tard
    main()
```


## Modules personnalisés

Pour créer un module personnalisé en Python, il suffit de créer un fichier texte avec l'extension `.py` contenant le code souhaité. Le nom du fichier sera le nom du module.

Ce fichier peut être le point d'entrée principal du programme (le script principal) ou un fichier séparé contenant des fonctions, des classes ou des variables réutilisables.

Pour l'instant, on simplifiera l'importation de fichier en plaçant tous les fichiers dans le même répertoire. Dans d'autres cours, nous verrons comment organiser les modules dans des répertoires et des packages.

```Python
# Fichier my_module.py

une_variable_globale = 42 # HAAAA! Pas de variables globales! (sauf pour quelques exceptions)
UNE_CONSTANTE_GLOBALE = 24 # Ok pour les constantes globales.

def une_fonction(param):
    return param * 2

class UneClasse:
    def __init__(self, value):
        self.value = value

    def afficher(self):
        print("Valeur :", self.value)
```

```Python
# Fichier main.py
# Fichier principal correspondant au point d'entrée souhaité du programme

import my_module as mymo

def main():
    # Code principal du programme
    variable_locale = mymo.UneClasse()
    variable_locale.afficher()
    # ...

if __name__ == "__main__": # Le point d'entrée officiel du programme
    main()
```

### Exercices 4

- Exercice 4.1 : 
    - Créer une classe qui représente un dé nommée `Dice`.
    - La fonction d'initialisation `__init__` doit permettre de définir le nombre de faces du dé (entre 4 et 20, par défaut 6).
    - La classe doit avoir une méthode `roll()` qui simule un lancer de dé et retourne un entier aléatoire entre 1 et le nombre de faces du dé.
    - Créer un module `dice.py` qui contient la définition de la classe `Dice`.
    - Créer un fichier `main.py` qui importe le module `dice` et utilise la classe `Die` pour créer 4 dés de 4, 6, 8 et 12 faces respectivement.
    - Le programme fait 10 lancers de chaque dé et, pour chaque tour, affiche les résultats de chaque dé ainsi que la somme des résultats.
- Exercice 4.2 :
    - Créer un module `math_utils.py` qui contient les fonctions suivantes :
        - `factorial(n)` : calcule et retourne la factorielle de _n_ (n!)
            - si _n_ est négatif, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
            - si _n_ = 0, retourne 1
            - si _n_ > 0, retourne 1 * 2 * 3 * ... * n
        - `triangular(n)` : calcule et retourne le nombre triangulaire de _n_
            - si _n_ est négatif, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
            - si _n_ >= 0, retourne 0 + 1 + 2 + 3 + ... + n
        - `is_prime(n)` : vérifie si _n_ est un nombre premier et retourne `True` ou `False` 
            - un nombre premier est un entier naturel **supérieur à 1** qui n'a que deux diviseurs distincts : 1 et lui-même
            - voici l'approche à utiliser :
                - si _n_ est inférieur ou égal à 1, lever une exception `ValueError` ou afficher un message d'erreur et retourner -1
                - si _n_ est 2, retourne `True`
                - si _n_ est pair, retourne `False`
                - parcourir tous les nombre impairs à partir de 3 jusqu'à _m_ (où  `m = floor(sqrt(n))`) et analyser si le _i_ nombre divise _n_ sans reste
                    - retourner `False` si un diviseur est trouvé
                    - retourner `True` si aucun diviseur n'est trouvé
    - Créer un fichier `main.py` qui importe le module `math_utils` et utilise les fonctions `factorial` et `is_prime` pour afficher la factorielle de 5 et vérifier si 7 est un nombre premier.

- Exercice 4.3 :
    - Créer un module contenant une classe `BankAccount` qui représente un compte bancaire.
        - La fonction d'initialisation doit permettre de définir le nom du titulaire du compte et le solde initial (par défaut 0).
        - La classe doit avoir les méthodes suivantes :     
            - `deposit(amount)` : permet de déposer une somme d'argent sur le compte. Si le montant est négatif ou nul, lever une exception `ValueError`.
            - `withdraw(amount)` : permet de retirer une somme d'argent du compte. Si le montant est négatif ou nul, lever une exception `ValueError`. Si le montant est supérieur au solde, lever une exception `ValueError`.
            - `get_balance()` : retourne le solde actuel du compte.
            - `get_account_holder()` : retourne le nom du titulaire du compte.
    - Créer un module contenant une classe `Bank` qui représente une banque.
        - La fonction d'initialisation doit permettre de définir le nom de la banque.
        - La classe doit avoir les méthodes suivantes :
            - `add_account(account)` : permet d'ajouter un compte bancaire à la banque.
            - `remove_account(account)` : permet de retirer un compte bancaire de la banque.
            - `get_total_balance()` : retourne le solde total de tous les comptes de la banque.
    - Créer un fichier `main.py` qui crée une instance de la classe `Bank`, ajouter plusieurs comptes bancaires à la banque, effectue des dépôts et des retraits sur les comptes, et affiche le solde total de la banque.


# Introduction à Python - Cours 2

## Partie 2c

# Devoir

- Devoir 2 :
    - Créer un module `shapes.py` qui contient les classes suivantes :
        - `Shape` : classe de base _abstraite_ pour toutes les formes géométriques. Elle doit avoir les méthodes suivantes :
            - `bounding_box_width()` qui retourne la largeur de la forme
            - `bounding_box_height()` qui retourne la hauteur de la forme
            - `area()` qui calcule et retourne l'aire de la forme
            - `perimeter()` qui calcule et retourne le périmètre de la forme (optionnel)
            - `to_string(shape_char = '*', background_char = ' ')` qui retourne la forme sous forme de caractères. Par exemple :
                - pour un rectangle de 30 x 3 :
                ```
                ******************************
                ******************************
                ******************************
                ```
                - pour un triangle rectangle de base 15 et de hauteur 7 :
                ```
                **
                ****
                ******
                *********
                ***********
                *************
                ***************
                ```
            - toutes les classes héritant de `Shape` doivent implémenter les 5 méthodes mentionnées ci-dessus.
        - `Square` représente un carré (hérite de `Shape`) :
            - la classe possède un attribut `side` pour la longueur du côté du carré
        - `Rectangle` représente un rectangle (hérite de `Shape`) :
            - la classe possède des attributs `width` et `height` pour la largeur et la hauteur du rectangle
        - `RectTriangle` représente un triangle rectangle (hérite de `Shape`) :
            - la classe possède des attributs `width` et `height` pour la largeur et la hauteur du triangle rectangle
        - `Circle` représente un cercle (hérite de `Shape`) :
            - la classe possède un attribut `radius` pour le rayon du cercle
        - Créer une fonction utilitaire nommée qui crée aléatoirement des forme nommée `create_random_shape(size = 0)`.
            - La fonction détermine aléatoirement laquelle des 4 formes elle créera.
            - le paramètre `size` détermine la taille de la forme. Pour les formes non symétriques, l'autre dimention doit être de `1/2 size`. Si `size <= 0`, `size` est déterminée aléatoirement dans l'intervalle [5, 15].
            - Retourne l'objet de la forme créée.
    - Créer un fichier `main.py` qui :
        - crée 10 instances aléatoires de formes et les insère dans une liste
        - pour chacune des formes, on affiche :
            - la forme en chaîne de caractèrs (bonus, ajouter un encadré)
            - les informations de chaque forme (aire, périmètre, dimensions, etc.)
        - affiche les informations globales suivantes :
            - le nombre de formes
            - la somme des aires
            - la somme des périmètres
        - En bonus, créer une image de 80 x 30 caractères et superposer toutes les formes en leur donnant des position aléatoires et afficher l'image dans la console. Utiliser le caractère espace `' '` pour le fond. Si une forme dépasse les limites de l'image, elle est tronquée.

    
