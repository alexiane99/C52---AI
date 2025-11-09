
# Introduction à Python - Cours 1

## Partie 1c

### Devoir 

L'objectif est de produire un petit programme permettant à un joueur de résoudre un labyrinthe.

Vous avez à votre disposition le labyrinthe suivant disponible dans un tuple de chaîne de caractères. Les chemins sont représentés par des espaces vides, les murs par des caractères spéciaux, l'entrée du labyrinthe par `S` (_Start_) et la sortie par `G` (_Goal_).

``` Python
maze = (
    '┌S┬────────────────┬───────────┐',
    '│ │                │           G',
    '│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤',
    '│ └─┘     │ │   │    │   │   │ │',
    '│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │',
    '│ ┌── │ │ │ │ │ │ │    │   │   │',
    '│ │   │   │ │ │ │ │ ┌──┴─┬─┴─┐ │',
    '│ │ ──┴───┘ │ │ │ │ │    │   │ │',
    '│ │         │ │   │ │  │ │ │ │ │',
    '│ └─────────┘ └───┴─┘  │ │ │ │ │',
    '│                      │   │   │',
    '└──────────────────────┴───┴───┘',
)
```

Le joueur, représenté par un astérisque `*`, doit se déplacer dans le labyrinthe en suivant les chemins représentés par des espaces vides. Le but est d'atteindre la sortie `G` en partant de l'entrée `S`.

Le joueur peut se déplacer dans les quatre directions cardinales (haut, bas, gauche, droite) en utilisant les touches `w`, `a`, `s`, `d` respectivement (minuscule ou majuscule).

Le programme doit gérer la logique associée aux mouvements du joueur, en vérifiant si le mouvement est valide (c'est-à-dire si le joueur ne tente pas de traverser un mur ou de sortir du labyrinthe). Autrement dit, le joueur ne peut pas traverser les murs représentés par les caractères `─`, `│`, `┌`, `┐`, `└`, `┘`, `┬`, `┴`, `├`, `┤`.

À chaque mouvement, le programme doit calculer ces statistiques :
- Le nombre de mouvements effectués.
- Le nombre de mouvements où le joueur a tenté de traverser un mur.
- Le pourcentage de cellules traversées par rapport au nombre total de cellules de type chemin (c'est-à-dire les espaces vides) dans le labyrinthe. Le pourcentage doit être arrondi à une décimale.

Finalement, à chaque mouvement, le programme doit afficher :
    - le labyrinthe original avec la position du joueur représenté par un astérisque `*`
    - les statistiques calculées
    - selon l'état de la partie :
        - si la partie est en cours, un message invitant le joueur à saisir une direction pour continuer à jouer
        - si le joueur a atteint la sortie `G`, un message de victoire et la fin du programme
    - Évidemment, la console _clignotera_ (_flickering_) à chaque mouvement pour afficher le labyrinthe mis à jour. Ce n'est pas important pour ce projet.

Voici deux exemples d'affichage :

- Au démarrage de la partie.

``` 
┌*┬────────────────┬───────────┐
│ │                │           G
│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤
│ └─┘     │ │   │    │   │   │ │
│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │
│ ┌── │ │ │ │ │ │ │    │   │   │
│ │   │   │ │ │ │ │ ┌──┴─┬─┴─┐ │
│ │ ──┴───┘ │ │ │ │ │    │   │ │
│ │         │ │   │ │  │ │ │ │ │
│ └─────────┘ └───┴─┘  │ │ │ │ │
│                      │   │   │
└──────────────────────┴───┴───┘
Number of steps:  0
Number of walls hit:  0
Ratio empty cells visited:  0.0 %

Direction (wasd) :
```

- Pendant la partie.

``` 
┌S┬────────────────┬───────────┐
│ │                │           G
│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤
│ └─┘     │ │   │    │   │   │ │
│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │
│ ┌── │ │ │ │ │ │ │    │   │   │
│ │   │   │ │*│ │ │ ┌──┴─┬─┴─┐ │
│ │ ──┴───┘ │ │ │ │ │    │   │ │
│ │         │ │   │ │  │ │ │ │ │
│ └─────────┘ └───┴─┘  │ │ │ │ │
│                      │   │   │
└──────────────────────┴───┴───┘
Number of steps:  56
Number of walls hit:  6
Ratio empty cells visited:  19.3 %

Direction (wasd) :
```


# Solution simple du projet de labyrinthe

maze_1 = (
    '┌S┬──────────────────┬───────────┐',
    '│ │                  │           │',
    '│ │ ┌───────┐ ┌───┬──┘ ┌───┬───┐ │',
    '│ └─┘       │ │   │    │   │   │ │',
    '│     ┌──── │ │ │ │ ┌──┘ │ │ │ │ │',
    '│ ┌── │     │ │ │ │ │    │   │   │',
    '│ │ ──┴─────┘ │ │ │ │ ┌──┴─┬─┴─┬─┤',
    '│ │           │ │   │ │    │   │ G',
    '│ └───────────┘ └───┤ │  │ │ │ │ │',
    '│                   │    │   │   │',
    '└───────────────────┴────┴───┴───┘',
)

maze_2 = (
    '┌S┬────────────────┬───────────┐',
    '│ │                │           G',
    '│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤',
    '│ └─┘     │ │   │    │   │   │ │',
    '│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │',
    '│ ┌── │ │ │ │ │ │ │    │   │   │',
    '│ │   │   │ │ │ │ │ ┌──┴─┬─┴─┐ │',
    '│ │ ──┴───┘ │ │ │ │ │    │   │ │',
    '│ │         │ │   │ │  │ │ │ │ │',
    '│ └─────────┘ └───┴─┘  │ │ │ │ │',
    '│                      │   │   │',
    '└──────────────────────┴───┴───┘',
)

# maze_n = ...


# -----------------------------------------------------------------------------
# 1. Sélection du maze
maze = maze_2

# Optionnellement
# 1.b Vérification du maze : toutes les lignes doivent avoir la même largeur
# ------------------------
assert all(len(row) == len(maze[0]) for row in maze[1:]), "Lignes de longueurs différentes"
# utilise des notions que nous verrons plus tard
# ------------------------
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# 2. Analyse du labyrinthe
# Caractères attendus du labyrinthe
GOAL_CHAR = 'G'
START_CHAR = 'S'
EMPTY_CHAR = ' '
WALL_CHARS = "┌┐└┘─│├┤┬┴┼"
PLAYER_CHAR = '*'

# Construction des variables d'analyse
line_count = len(maze)
row_count = len(maze[0])
cell_count = line_count * row_count
empty_cells = set()
goal_count = 0
start_count = 0
empty_count = 0
wall_count = 0
invalid_char_count = 0

x, y = 0, 0
start_coord = [0, 0]
goal_coord = [0, 0]
for row in maze:
    for cell in row:
        if cell == START_CHAR:
            start_count += 1
            start_coord = [x, y]
        elif cell == GOAL_CHAR:
            goal_count += 1
            goal_coord = [x, y]
        elif cell == EMPTY_CHAR:
            empty_count += 1
            empty_cells.add((x, y))
        elif cell in WALL_CHARS:
            wall_count += 1
        else: # optionnel
            invalid_char_count += 1 
        
        x += 1
    x = 0
    y += 1

empty_cells_count = len(empty_cells)

# Optionnellement
# Exemple de validation
# ------------------------
assert start_count == 1, "Doit y avoir 1 'S' (start)"
assert goal_count == 1, "Doit y avoir 1 'G' (goal)"
assert invalid_char_count == 0, "Symboles inconnus"
assert goal_count + start_count + empty_count + wall_count == cell_count, "Symboles inconnus"
# ------------------------
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# OK on peut continuer
# 3. Le jeu

# Variables de suivi
win = False
current_coord = [start_coord[0], start_coord[1]]
stat_steps = 0 
stat_wall = 0

# Boucle principale
while not win:
    # Affichage du labyrinthe avec la position actuelle
    print()
    for i in range(len(maze)):
        row = maze[i]
        if i == current_coord[1]:
            position = current_coord[0]
            # sans indexation :
            for j in range(0, position):
                print(row[j], end='')
            print(PLAYER_CHAR, end='')  # Marque la position actuelle
            for j in range(position + 1, len(row)):
                print(row[j], end='')
            print()
            # avec indexation : 
            # print(row[:position] + '*' + row[position+1:])
        else:
            print(row)
    # Affichage des statistiques
    print("Number of steps: ", stat_steps)
    print("Number of walls hit: ", stat_wall)
    print("Ratio empty cells visited: ", round((empty_cells_count - len(empty_cells)) / empty_cells_count * 100, 1), "%")
    print()

    # Demande de direction
    direction = input("Direction (wasd) : ").lower()
    if len(direction) != 1 or direction not in 'wasd':
        print("Direction invalide")
        continue

    # Calcul de la nouvelle position
    if direction == 'w':
        new_coord = [current_coord[0], current_coord[1] - 1]
    elif direction == 's':
        new_coord = [current_coord[0], current_coord[1] + 1]
    elif direction == 'a':
        new_coord = [current_coord[0] - 1, current_coord[1]]
    elif direction == 'd':
        new_coord = [current_coord[0] + 1, current_coord[1]]
    else: # pas nécessaire
        assert False, "Erreur inattendue"

    # Évaluation de la nouvelle position et mise à jour des statistiques
    stat_steps += 1
    value = maze[new_coord[1]][new_coord[0]]
    if value == EMPTY_CHAR:
        current_coord = new_coord
        empty_cells.discard((current_coord[0], current_coord[1]))
    elif value in WALL_CHARS:
        stat_wall += 1
    elif value == GOAL_CHAR:
        current_coord = new_coord
        win = True


# Fin de la partie
# Affichage du labyrinthe avec la position actuelle
# *** on remarque la répétition de code, on devrait faire une fonction
print()
for i in range(len(maze)):
    row = maze[i]
    if i == current_coord[1]:
        position = current_coord[0]
        # avec indexation : 
        print(row[:position] + '*' + row[position+1:])
    else:
        print(row)
# Affichage des statistiques
print("Number of steps: ", stat_steps)
print("Number of walls hit: ", stat_wall)
print("Ratio empty cells visited: ", round((empty_cells_count - len(empty_cells)) / empty_cells_count * 100, 1), "%")
print()
print("Congratulation, you won in", stat_steps, "steps!")

# -----------------------------------------------------------------------------