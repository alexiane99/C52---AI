
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

