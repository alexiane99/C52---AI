
# Introduction à Python - Cours 1

## Partie 1 

### Présentation générale de Python

- Bref historique
    - Créé par Guido van Rossum en 1991
    - Nommé d'après la célèbre série télévisée britannique _Monty Python's Flying Circus_
    - Les versions majeures de Python sont :
        - `Python 1.0` (janvier 1994 -> octobre 2000)
        - `Python 2.0` (octobre 2000 -> juillet 2010)
        - `Python 3.0` (décembre 2008 -> présent)
        - `Python 3.13` est la version actuelle et recommandée
        - `Python 3.14` est prévue pour le 7 octobre 2025
    - Aujourd'hui, Python est maintenu par la _Python Software Foundation_ ([PSF](https://www.python.org/psf-landing/)), dispose d'une large communauté de développeurs et de contributeurs et est utilisé dans de nombreux domaines
- Caractéristiques principales :
    - Langage _open source_, avec une large communauté de développeurs et de contributeurs
    - Disponible sur de nombreuses plateformes, y compris Windows, macOS, Linux, iOS, Android, IoT, _embedded_, etc.
    - Langage de programmation polyvalent, utilisé dans divers domaines tels que le développement web, l'analyse de données, l'intelligence artificielle, l'automatisation, etc.
    - Est utilisé par de nombreuses entreprises et organisations, y compris Google, Facebook, NASA, et tellement d'autres
    - Souvent utilisé pour l'enseignement de la programmation en raison de sa syntaxe claire et de sa facilité d'apprentissage
    - Langage de programmation multi-paradigmes. Prend en charge plusieurs styles de programmation : impérative, procédurale, fonctionnelle et orientée objet (tout est `POO`)
    - Langage de programmation de haut niveau offrant plusieurs abstractions facilitant le développement
    - Langage de programmation interprété, permettant d'exécuter du code sans compilation préalable
    - Langage de programmation à typage dynamique (au _run time_), les types de données sont déterminés au moment de l'exécution, plutôt qu'à la compilation (statique, _compile time_)
    - Gestion automatique de la mémoire (_garbage collector_)
    - Support de la programmation asynchrone
    - Langage de programmation extensible, ce qui signifie qu'il peut être étendu avec des modules et des bibliothèques écrits dans d'autres langages, tels que C ou C++ notamment
    - Langage de programmation populaire et très important dans l'industrie, classé parmi les langages les plus utilisés dans le monde :
        - [TIOBE Index](https://www.tiobe.com/tiobe-index/) [`<nom du langage> programming`]
        - [PYPL](https://pypl.github.io/PYPL.html) (_PopularitY of Programming Languages_) [`<nom du langage> tutorial`]
        - [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey) [`<nom du langage> developer`]
        - Les différents index donnent des résultats différents à cause de la méthodologie de calcul et des différents domaines de développement. Simplement dit, dans [`<nom du langage> xyz`], le `xyz` fait référence à l'approche (largement simplifiée).
    - Python est considéré l'un des langages de programmation les plus :
        - faciles à apprendre
        - élégants 
        - pertinents pour les débutants et experts 
    - Les fichiers de code Python sont des fichiers texte avec l'extension `.py` (ex. `mon_script.py`)
    - Lors de sa première exécution, le code source Python `.py` est compilé en `bytecode` et sauvegardé dans un fichier `.pyc`; c'est ce `bytecode`, et non le code source original, qui est ensuite exécuté par la machine virtuelle Python (PVM). Processus similaire à la JMV de Java.
    - Il existe de nombreuses implémentations de Python, la plus courante étant CPython (implémentation de référence), mais il y a aussi Jython (pour Java), IronPython (pour .NET), PyPy (interprétation rapide), MicroPython (pour les microcontrôleurs et systèmes embarqués) et d'autres
    - Il existe plusieurs documents officiels appelés `PEP ###` (_Python Enhancement Proposals_) qui décrivent les améliorations (passées et à venir) ainsi que plusieurs guides adressant divers sujets :
        - [PEP 20](https://peps.python.org/pep-0020/) : Philosophie zen de Python
            - Il devrait y avoir une seule façon évidente de faire les choses - _There should be one -- and preferably only one -- obvious way to do it_
            - La lisibilité compte - _Readability counts_
            - Le simple est meilleur que le complexe - _Simple is better than complex_
            - L'explicite est meilleur que l'implicite - _Explicit is better than implicit_
            - Face à l'ambiguïté, refusez la tentation de deviner - _In the face of ambiguity, refuse the temptation to guess_
            - Maintenant vaut mieux que jamais - _Now is better than never_
            - Si l'implémentation est difficile à expliquer, c'est une mauvaise idée - _If the implementation is hard to explain, it's a bad idea_
            - ...
        - [PEP 8](https://peps.python.org/pep-0008/) : Guide de style pour Python
            - Python est l'un des seuls langages de programmation à avoir un guide de style officiel
            - Une norme de codage est toujours définie pour un projet ou une organisation, Python en propose une qui est largement adoptée mais pas obligatoire
            - Quelques conventions de nommage selon `PEP 8` :
                - les variables et fonctions utilisent le `lower_snake_case` (ex. `ma_variable`, `ma_fonction`, `current_speed`, `accelerate(...)`)
                - les constantes utilisent le `UPPER_SNAKE_CASE` (ex. `PI`, `MAXIMUM_ACCELERATION`)
                - les classes et _types_ utilisent le `PascalCase` (ex. `MaClasse`, `FireTower`)
                - les modules et packages utilisent le `lower_snake_case` (ex. `mon_module`, `mon_package`)
        - ... et plusieurs autres
- Python vs Java et C++
    - Python est à typage dynamique, alors que Java et C++ sont statiquement typés
    - Complexité relative :
        - Python est considéré comme plus simple et plus lisible que Java et C++
        - Java a une syntaxe plus stricte que Python, mais est beaucoup plus facile que C++ (sa syntaxe s'inspire de C++)
        - C++ est considéré comme le langage de programmation le plus complexe de l'industrie, avec une syntaxe nécessitant plusieurs nuances et des concepts très larges ainsi qu'avancés
    - Python est plus flexible que Java et C++, permettant une programmation plus rapide et plus facile
    - Python est souvent utilisé pour l'enseignement de la programmation en raison de sa syntaxe claire et de sa facilité d'apprentissage, tandis que C++ est souvent utilisés dans des contextes plus avancés
    - Python est l'un des langages les plus lents à l'exécution, toutefois il reste très performant pour de nombreux cas d'utilisation, notamment grâce à son écosystème riche en bibliothèques optimisées précompilées

### Éléments de base du langage Python

- Structure syntaxique générale
    - sensible à la casse
    - commentaires :
        - sur une seule ligne débutant par `#`
        - pas de multilignes
    - il n'y a pas de symbole pour terminer une instruction (pas de  point-virgule `;`)
    - les blocs de code sont définis par l'indentation (4 espaces est le standard, les tabulations ne sont pas recommandées)
    - les instructions doivent être sur une seule ligne, à l'exception de :
        - dans certains contextes, si elles sont entre parenthèses `()`, crochets `[]` ou accolades `{}` 
        - avec l'utilisation de la barre oblique inversée `\` à la fin de la ligne
    - il n'y a pas de point d'entrée formel : 
        - pas de `main`
        - chaque fichier Python est appelé un _module_ et peut être exécuté directement
        - les instructions sont exécutées dans l'ordre où elles apparaissent dans le fichier
    - les fichiers texte contenant du code `Python` utilise l'extension `py`
    - langage offrant ne supportant pas tous les concepts de `Java` et `C++` :
        - certains concepts sont similaires mais fondamentalement différents : `struct`, `enum`, `switch`, `static`, `interface`, `override`, `final`,  `union`, `pointer`, `reference`, ...
        - d'autres n'existent pas mais sont compensés par des conventions bien établies : `const`, `private`, `protected`, `package`, `friend`, ...
        - certains concepts n'existent pas du tout : `do-while`, `goto`, ...
    - typage dynamique
    - offre un large éventail de bibliothèque
    - formellement, tout est un objet en `Python` (nous y reviendrons)
- Types fondamentaux
    - `bool`
    - `int`
    - `float` (pas de `double`, en fait le `float` est un `double`)
    - `complex`
    - `str`
    - `bytes` et `bytearray`
    - `None` (équivalent à `null` en `Java` ou conceptuellement similaire `nullptr` en `C++`)
- Les litéraux sont similaires aux autres langages :
    - `int` : `42`, `0x2A`, `0b101010`
    - `float` : `3.14`, `2.71828`, `1.0e-10`
    - `complex` : `1 + 2j`, `3 - 4j`
    - `str` : 
        - avec apostrophes : `'Hello'`, `'''Multiline string'''`
        - avec guillemets : `"World"`, `"""Multiline string"""`
        - pas de préférence, utiliser l'un ou l'autre selon le contexte mais rester cohérent et consistant
    - `bool` : `True`, `False`
    - `None` : `None`
- Deux fonctions utilitaires pour afficher et saisir des données dans la console :
    - `print` pour afficher des données à la console
        - `print(<valeur>, ...)`
        - `print('Hello World!')`
        - `print('Hello', ' ', 'World!')`
    - `input` pour saisir des données depuis la console
        - `result = input(<message>)` pour afficher un message avant la saisie
        - `name = input('Veuillez saisir votre nom : ')`
- Quelques fonctions utilitaires  :
    - Conversion de types :
        - `bool(<valeur>)` pour convertir en booléen
        - `int(<valeur>)` pour convertir en entier
        - `float(<valeur>)` pour convertir en flottant
        - `str(<valeur>)` pour convertir en chaîne de caractères
    - Fonctions de base :
        - `abs(<valeur>)` pour obtenir la valeur absolue
        - `round(<valeur>, <précision>)` pour arrondir un nombre
    - Introspection :
        - `id(<valeur>)` pour obtenir l'identifiant unique d'un objet
        - `type(<valeur>)` pour obtenir le type d'une valeur

```Python
# Exemple de code Python

# Déclaration de variables et utilisation de litéraux
x = 42  # entier
y = 3.14  # flottant
z = 1 + 2j  # complexe
s = 'Hello, World!' # chaîne de caractères

# Affichage des variables
print('Bonjour, Monde!')  # Affiche une chaîne de caractères
print(s)  # Affiche la variable s

# Saisie, concaténation et affichage
response = input("Entrez votre nom : ")  # Saisie utilisateur
print("Bonjour, " + response + "!")  # Affiche un message de bienvenue 
                                     # utilisant l'opérateur de concaténation
```

- Les opérateurs sont très similaires aux autres langages :
    - unaires : `-`, `+`, `not`, `~`
    - binaires : 
        - assignation : `=`
        - arithmétiques : `-`, `+`, `*`, `/`, `%`, `^`
            - différents : `//`, `**`
        - comparaisons : `==`, `!=`, `<`, `<=`, `>`, `>=` 
        - logique : `or`, `and`
        - bit à bit : `&`, `|`, `^`, `~`, `<<`, `>>`
        - opérateurs d'assignation combinée : `+=`, `-=`, `*=`, ...
        - opérateurs d'identité : `is`, `is not`
        - opérateurs d'appartenance : `in`, `not in` (_on y reviens avec les collections_)
        - et plusieurs autres
    - attention, ces opérateurs ne sont pas disponibles :
        - `++`, `--` (incrémentation et décrémentation)
        - `!`, `&&`, `||` (négation logique, et logique, ou logique)
        - `?:` l'opérateur ternaire mais possède l'alternative syntaxique suivante (_beaucoup plus lisible_) :
            - on utilise : `value = x if condition else y`
            - au lieu de : `value = condition ? x : y;`
        - `sizeof`, `&`, `*` et `->` (taille en mémoire, adresse, déréférencement et accès aux membres via un pointeur)
        - et plusieurs autres
    - attention, le `=` n'est pas un opérateur à proprement parlé comme l'opérateur d'assignation existant dans d'autres langages (_nous y reviendrons dans d'autres cours_)
```Python
# Exemple de code Python
# Déclaration de variables
a = 10
b = 5
c = a + b  # Addition
d = a - b  # Soustraction

s = "Hello"
t = "World"
y = s + " " + t  # Concaténation de chaînes
z = '-' * 10 # Répétition de chaînes

test = 'Positif' if a > 0 else 'Négatif'  # Opérateur ternaire
```
- Contrôle de flux
    - `if`, `elif`, `else` (il n'y a pas de `switch-case`)
    - `while` 
    - `for` 
    - `break` 
    - `continue` 
    - `return` 
    - `pass` (instruction vide, _placeholder_, nécessaire pour la syntaxe)
    - `match` (_pattern matching_, à partir de Python 3.10 seulement)
    - `try`, `except`, `finally` et `raise` pour gérer les exceptions
    - la définition d'une section logique utilise une approche par indentation avec l'usage des deux-points `:` plutôt que les accolades `{ }` (4 espaces est le standard)
    - il est possible de créer un bloc logique vide avec `pass` (utile pour les fonctions ou classes non implémentées)
    - attention, il n'y a pas de `do-while` ni de `switch-case` (mais on y revient avec le `match`)

```Python
# Exemple de code Python

test = False
while not test:
    result = input("Entrez un nombre entre 0 et 100 : ") # le résultat est une chaîne de caractères
    if result.isdigit(): # isdigit est une méthode de la classe str
        number = int(result)
        if 0 <= number <= 100:
            test = True
            print("Vous avez entré un nombre valide :", number)
        else:
            print("Le nombre doit être entre 0 et 100.")
    else:
        print("Veuillez entrer un nombre entier valide.")
```


- Particularité de la boucle `for` :
    - itère sur les éléments d'une séquence (comme une liste, un tuple, une chaîne de caractères, etc.)
    - syntaxe : <br>`for <variable> in <séquence> : <faire quelque chose>`
    - par exemple :  <br>`for letter in 'Bonjour' : print(letter)`
    - il existe une fonction utilitaire `range` pour générer une séquence de nombres :
        - `range(<début>, <fin>, <pas>)` génère une séquence linéaire de nombres de `<début>` à `<fin>` (exclusif) avec un pas de `<pas>`
        - si `<début>` est omis, il est considéré comme 0
        - si `<pas>` est omis, il est considéré comme 1
        - par exemple :
            - `range(5)` génère la séquence `[0, 1, 2, 3, 4]`
            - `range(-4, 5)` génère la séquence `[-4, -3, -2, -1, 0, 1, 2, 3, 4]`
            - `range(0, 10, 2)` génère la séquence `[0, 2, 4, 6, 8]`
    - nous reviendrons en détail sur les boucles `for` qui offrent beaucoup plus encore

```Python
# Exemple de code Python

# Boucles for avec range
for i in range(5):  # itère de 0 à 4
    print(i)  # Affiche les nombres de 0 à 4

for i in range(2, 5, 2):  # itère de 2 à 4 avec un pas de 2 => [2, 4]
    for j in range(3, 0, -1):  # itère de 3 à 1 avec un pas de -1 => [3, 2, 1]
        print(i * 100 + j)  # Affiche : 203, 202, 201, 403, 402, 401
```


### Exercices 1

- Utilisez uniquement :
    - les types fondamentaux `int`, `float`, `str`, `bool`
    - les opérateurs arithmétiques, de comparaison et logiques
    - les structures de contrôle de flux `if`, `elif`, `else`, `while`, `for`
    - les fonction `print` et `input` pour interagir avec la console.

- Exercice 1.1 : Devinez un nombre (avec essais limités)
    - Le programme possède un _nombre secret_ défini dans le code par la variable `number` dans l'intervalle [0, 100] (par exemple, 42).
    - L'utilisateur a cinq essais pour le deviner. 

    - Après chaque essai, le programme indique si le nombre à deviner est "Plus haut" ou "Plus bas". 
    - Le jeu se termine si l'utilisateur trouve le nombre ou s'il n'a plus d'essais.

- Exercice 1.2 : Calculatrice simple
    - Créez une calculatrice simple qui peut effectuer les opérations de base : addition, soustraction, multiplication et division.
    - Le programme doit demander à l'utilisateur d'entrer deux nombres et l'opération souhaitée en trois saisies différentes.
    - Affichez le résultat de l'opération.
    - Optionnellement, gérez les erreurs potentielles, comme les erreurs de saisie etla division par zéro.

- Exercice 1.3 : Table de multiplication
    - Demandez à l'utilisateur d'entrer deux nombres entiers entre 2 et 10 (en 2 saisies distinctes).
    - Affichez la table de multiplication de ces nombres.

- Exercice 1.4 : Trier simplement trois nombres (sans fonctions ni collections)
    - Objectif. Afficher trois entiers saisis en ordre croissant sans utiliser de liste ni la fonction `sorted(...)`.
    - Demander à l'usager de saisir trois entiers `a`, `b` et `c` (en 3 saisies distinctes).
    - Réordonner ces trois entiers en ordre croissant.
    - Afficher sur trois lignes :
        - les trois entiers dans l'ordre saisies
        - les trois entiers en ordre croissant sur une seule ligne
        - si les trois variables sont strictement différentes les unes des autres, afficher `Strict` sinon afficher `Non-strict`




# Introduction à Python - Cours 1

## Partie 2b - Structures de données fondamentales

- Présentation
    - Les collections sont des structures de données qui permettent de stocker et de gérer plusieurs éléments sous une seule variable
    - Les tableaux sont un exemple de collection.
    - Cette présentation est sommaire et vise à :
        - présenter les collections fondamentales
        - présenter quelques fonctions et méthodes associées
        - donner un aperçu de leur utilisation
    - Nous reviendrons en détail sur les collections dans ce cours et dans d'autres cours
    - Les collections fondamentales en Python sont :
        - Les chaînes de caractères `str` (oui, c'est une collection de caractères)
        - Les listes `list`
        - Les tuples `tuple`
        - Les dictionnaires `dict`
        - Les ensembles `set`

- Caractéristiques principales des collections :
    - `str` (chaîne de caractères) :
        - Ordonnée par position (comme un tableau)
        - Non modifiable (les caractères ne peuvent pas être ajoutés, supprimés ou modifiés après la création)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation en lecture par position seulement (pas en écriture)
        - Utilise des apostrophes `'...'` ou des guillemets `"..."` pour la création
        - Exemple : 
            - `my_str = str('Hello, World!') # constructeur de chaîne`
            - `my_str = 'Hello, World!' # littéral de chaîne`
            - `print(my_str[0]) # accès en lecture, affiche 'H'`
        - Les méthodes importantes sont :
            - `upper()` pour convertir en majuscules
            - `lower()` pour convertir en minuscules
            - `strip()` pour supprimer les espaces au début et à la fin
            - `replace()` pour remplacer une sous-chaîne par une autre
            - `split()` pour diviser la chaîne en une liste de sous-chaînes
            - `join()` pour joindre une liste de chaînes en une seule chaîne
            - `find()` pour trouver la position d'une sous-chaîne
            - `count()` pour compter les occurrences d'une sous-chaîne    
    - `list` (liste) :
        - Ordonnée par position (comme un tableau)
        - Modifiable (des éléments peuvent être ajoutés, supprimés ou modifiés)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation par position en lecture et en écriture
        - Utilise des crochets `[]` pour la création 
        - Exemple : 
            - `my_list = list(1, 2, 3, 4, 5) # constructeur de liste`
            - `my_list = [1, 2, 3, 4, 5] # littéral de liste`
            - `print(my_list[0]) # accès en lecture`
            - `my_list[0] = 10 # accès en écriture`
        - Les méthodes importantes sont :
            - `append()` pour ajouter un élément à la fin
            - `insert()` pour ajouter un élément à une position donnée
            - `remove()` pour supprimer un élément par valeur
            - `pop()` pour supprimer un élément par position
            - `clear()` pour vider la liste
            - `sort()` pour trier la liste
            - `count()` pour compter les occurrences d'un élément
            - `index()` pour obtenir l'index d'un élément
    - `tuple` (tuple) :
        - Ordonné par position (comme un tableau)
        - Le tuple lui-même n'est pas modifiable (des éléments ne peuvent pas être ajoutés, supprimés ou modifiés après la création)
        - Permet les doublons
        - Utilise des crochets `[]` pour l'indexation par position en lecture seule
        - Utilise des parenthèses `()` pour la création (attention à l'une des rares exceptions syntaxiques du langage Python)
        - Exemple : 
            - `my_tuple = tuple(1, 2, 3, 4, 5) # constructeur de tuple`
            - `my_tuple = (1, 2, 3, 4, 5) # littéral de tuple`
            - `print(my_tuple[0]) # accès en lecture`
        - Les méthodes importantes sont :
            - `count()` pour compter les occurrences d'un élément
            - `index()` pour obtenir l'index d'un élément
    - `set` (ensemble) :
        - Non ordonné (les éléments n'ont pas de position fixe)
        - Modifiable (des éléments peuvent être ajoutés ou supprimés)
        - Interdit les doublons (chaque élément est unique)
        - Utilise des accolades `{}` pour la création
        - Exemple : 
            - `my_set = set([1, 2, 3, 4, 5]) # constructeur de set`
            - `my_set = {1, 2, 3, 4, 5} # littéral de set` (attention à l'une des rares exceptions syntaxiques du langage Python, des accolades vides crées un dictionnaire)
            - `my_set.add(6) # ajouter un élément`
        - Les méthodes importantes sont :
            - `add()` pour ajouter un élément
            - `remove()` pour supprimer un élément (lève une exception si l'élément n'existe pas)
            - `discard()` pour supprimer un élément (ne lève pas d'exception si l'élément n'existe pas)
            - `clear()` pour vider l'ensemble
            - `union()`, `intersection()`, `difference()` pour les opérations ensemblistes
    - `dict` (dictionnaire) :
        - Associatif : les éléments sont stockés sous forme de paires clé-valeur
        - Ordonné seulement pour le parcours (les éléments sont parcourus dans l'ordre d'insertion, à partir de Python 3.7)
        - Non ordonné (les éléments n'ont pas de position fixe)
        - Modifiable (des éléments peuvent être ajoutés, supprimés ou modifiés)
        - Utilise des crochets `[]` pour l'indexation par clé en lecture et écriture
        - Les doublons sont :
            - interdits pour les clés
            - permis pour les valeurs
        - Utilise des accolades `{ clé: valeur, ... }` pour la création
        - Exemple : 
            - `my_dict = dict(a=1, b=2, c=3) # constructeur de dictionnaire`
            - `my_dict = {'a': 1, 'b': 2, 'c': 3} # littéral de dictionnaire`
            - `print(my_dict['a']) # accès en lecture, affiche 1`
            - `my_dict['a'] = 10 # accès en écriture, modifie la valeur associée à la clé 'a' - le 1 devient 10`
- Quelques fonctions et méthodes utiles pour les collections :
    - Outils génériques fonctionnant dans toutes les collections :
        - `if <élément> in <collection>` pour vérifier si un élément est dans une collection
            - ex. : `if 'Bob' in my_dict: print("'Bob' est dans le dictionnaire")`
        - `len(<collection>)` pour obtenir la longueur d'une collection
            - ex. : `print(len(my_list)) # affiche 5`
        - `for <value> in <collection>: <action>` pour itérer sur tous les éléments d'une collection
            - ex. : `for item in my_list: print(item)`
- Vous **devez** lire progressivement la documentation officielle pour développer vos compétences et connaissances ([voir](https://docs.python.org/3/tutorial/datastructures.html)).




### Exercices 2

- Vous devez utiliser exclusivement :
    - les mêmes instructions que les exercices 1
    - les collections fondamentales

- Exercice 2.1 : 
    - Objectif : Déterminer si une phrase est un palindrome.
    - Un palindrome est un mot ou une phrase qui se lit de la même manière dans les deux sens en ignorant les espaces, les accents, les signes de ponctuation et la casse.
    - Par exemple, ces mots : ressasser, kayak, radar, etc. 
    - On désire mettre l'accent sur les étapes suivantes de résolution :
        1. Normaliser la phrase en mettant chaque lettre dans une liste(mettre en minuscules, enlever les espaces, les accents et la ponctuation)
        2. Créer une deuxième liste qui est l'inverse de la première
        3. Comparer les deux listes
    - Vous devez parcourir toutes les phrases suivantes et déterminer si elles sont des palindromes en inscrivant l'une ou l'autre des phrases suivantes selon le résultat :
        - Oui : '< la phrase entre apostrophes >'
        - Non : '< la phrase entre apostrophes >'
    - Phrases à tester (pour simplifier, elles ne possède ni accents ni signes de ponctuation) :
``` Python
# Phrases à tester (les accents ont été retirés)
tests = (
    'Esope reste ici et se repose',
    'Elu par cette crapule',
    'Engage le jeu que je le gagne',
    'La mariee ira mal',
    'Eric notre valet alla te laver ton cire',
    'Il est incroyable',
    'Able was I ere I saw Elba',
    'A man a plan a canal Panama',
    'Was it a car or a cat I saw',
    'Never odd or even',
    'Madam, I m Adam',
    'Hello World',
    'A Toyota’s a Toyota',)
```
Sachez que Python offre des outils puissants permettant la simplification de cet exercice mais ce n'est pas le but ici. Voici une solution toute simple.

``` Python
# Solution ultra simple et compacte ()
text = "Esope reste ici et se repose"
normalized_text = text.lower().replace(" ", "")
reversed_text = str(reversed(normalized_text))
print(f"{'Oui' if normalized_text == reversed_text else 'Non'} :", text)
```


 - Exercice 2.2 : 
    - Objectif : Manipuler une collection pour créer des statistiques.
    - Vous devez créer deux dictionnaire qui compte :
        - le nombre d'individus pour chacun des genres : `gender_count`
        - pour chaque ville, le nombre d'individus et l'âge moyen : `city_stat`
    - Vous devez afficher les résultats sous la forme :
        - Genres :
            - femme : 11
            - homme : 9
            - autre : 4
        - Villes :
            - Montréal : 6 individus avec un âge moyen de 35 ans
            - Québec : 5 individus avec un âge moyen de 40 ans
            - ...
    - Vous devez utiliser la collection `data` suivante :
```python
data = [
    ("Tremblay, Marc", 41, "Montréal", 'h'),
    ("Lévesque, Annie", 30, "Gatineau", 'f'),
    ("Beaulieu, Denis", 58, "Longueuil", 'h'),
    ("Aubin, Christine", 41, "Saguenay", 'f'),
    ("Gauthier, Julie", 33, "Québec", 'f'),
    ("Boucher, Geneviève", 37, "Sherbrooke", 'f'),
    ("Bergeron, Mathieu", 36, "Gatineau", 'h'),
    ("Poirier, Daniel", 63, "Saguenay", 'h'),
    ("Gagnon, Laure", 27, "Montréal", 'f'),
    ("Morin, Philippe", 54, "Québec", 'h'),
    ("Caron, Zoé", 21, "Gatineau", 'x'),
    ("Bélanger, Thomas", 42, "Laval", 'h'),
    ("Pelletier, Maude", 24, "Laval", 'f'),
    ("Langlois, Patrick", 50, "Sherbrooke", 'h'),
    ("Simard, Noé", 34, "Longueuil", 'x'),
    ("Roy, Étienne", 35, "Montréal", 'h'),
    ("Ouellet, Kevin", 38, "Laval", 'h'),
    ("Côté, Myriam", 22, "Montréal", 'f'),
    ("Lavoie, Nadine", 46, "Québec", 'f'),
    ("Bouchard, Alex", 31, "Montréal", 'x'),
    ("Fortin, Samuel", 19, "Québec", 'h'),
    ("Girard, Valérie", 26, "Longueuil", 'f'),
    ("Gagné, Chantal", 29, "Laval", 'f'),
    ("Lefebvre, Simon", 18, "Saguenay", 'h'),
    ("Lapointe, Amélie", 23, "Sherbrooke", 'f'),
    ("Dufour, Olivier", 40, "Montréal", 'h'),
    ("Boucher, Camille", 28, "Gatineau", 'f'),
    ("Lemieux, Alexandre", 39, "Québec", 'h'),
    ("Desjardins, Élise", 32, "Laval", 'f'),
    ("Morissette, Vincent", 45, "Longueuil", 'h'),
    ("Caron, Sarah", 20, "Saguenay", 'f'),
    ("Bélanger, Maxime", 44, "Sherbrooke", 'h')]
```


### Exercice 2.3 : 
- Objectif : Validater les parenthèses, crochets et accolades ()[]{} 
    - Étape 1 : Lire une ligne de texte saisie à la console.
    - Étape 2 : Si la ligne est vide, utiliser cette chaîne de caractères par défaut : <br>
      `phrase = "Au labo (site {Nord [A-12]}) nous notons que g(x) = (x+{2y[3z]})/(4u-{5v[6w]}) reste stable."`
    - Étape 3 : Vérifier si les parenthèses, crochets et accolades sont équilibrés.
        - Les parenthèses/crochets/accolades ouvrantes doivent être fermées par des parenthèses/crochets/accolades fermantes
        - Les parenthèses/crochets/accolades doivent être correctement imbriqués, par exemple (ce n'est pas seulement le nombre qui compte) :
            - `([]){} → OK`
            - `([){]} → ERR`
        - Vous devez utiliser une pile pour vérifier l'équilibre des parenthèses, crochets et accolades. Pour y arriver, utilisez une liste avec les méthodes `append` pour ajouter un élément  et `pop` pour retirer le dernier élément ajouté.
    - Étape 4 : Affichez l'un de ces messages :
        - `OK` si les parenthèses, crochets et accolades sont équilibrés
        - `ERR pos = i` si une erreur est détectée, où `i` est la position de la première erreur (_0 based index_)


### Exercice 2.4 :
- Objectif : Effectuer la somme numérique d'un nombre
    - Étape 1 : Lire une ligne de texte saisie à la console.
    - Étape 2 : Si la ligne est vide, utiliser cette chaîne de caractères par défaut : `value = "1234567890"`
    - Étape 3 : Calculer la somme de tous les chiffres dans la chaîne de caractères. Par exemple, pour la chaîne `value = "12345"`, la somme est `15` (`1 + 2 + 3 + 4 + 5`).
    - Étape 4 : Afficher le résultat de la somme.
    - Étape 5 : Recommencer les étapes 3 et 4 en réutilisant le résultat de la somme jusqu'à ce que ce résultat soit de 1 chiffre. Par exemple :
        - `99999999999992 -> 119`
        - `119 -> 11`
        - `11 -> 2`
    - Étape 6 : Afficher le résultat final.
    - Étape 7 : Recommencer les étapes 1 à 6 jusqu'à ce que l'utilisateur saisisse un point `.`.
    - Il existe plusieurs approches pour résoudre cet exercice. Vous pouvez utiliser celle qui vous convient le mieux. L'utilisation de structures de données est très intuitive mais une approche mathématique reste plus efficace. Produire plusieurs solutions utilisant diverses approches est un excellent exercice.
