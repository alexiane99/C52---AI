import random 

class Case:
    def __init__(self, x, y, etat):
        self.x = x
        self.y = y
        self.etat = etat
    
    def get_xy(self):
        return self.x, self.y
    

    
    

class Grille:
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.grille = []
        self.dict_voisins = [(-1,-1), (0,-1), (1,-1), 
                    (-1,0),                (1,0),
                    (-1,1), (0,1), (1,1)]
        
        # self.dict_voisins = { 'v1': (-1,-1), 'v2': (0,-1), 'v3': (1,-1), 
        #             'v4': (-1,0),                'v5': (1,0),
        #             'v6': (-1,1), 'v7': (0,1), 'v8': (1,1) }

    # dict voisins (disposition)
    # v1 | v2 | v3
    # v4 |    | v5
    # v6 | v7 | v8

    # dict_voisins = { 'v1': (-1,-1), 'v2': (0,-1), 'v3': (1,-1), 
    #                 'v4': (-1,0),                'v5': (1,0),
    #                 'v6': (-1,1), 'v7': (0,1), 'v8': (1,1) }

    def init_grille(self):
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                self.grille.append(Case(x, y, random.randint(0,1)))

    def retourne_nb_case(self):
        return self.dim_x * self.dim_y
    

    def afficher_grille_debug(self):
        for ele in self.grille:
            print(f"Position X: {ele.x} Position Y: {ele.y} Etat: {ele.etat}")
        
    def afficher_grille(self):
        x = 0 # à améliorer 
        for y in self.grille:
            if (x % self.dim_x) == 0:
                print('\n', end="")
            print(y.etat, end="")
            x+=1

    # def get_case(self, x, y):
    #     return case.x, case.y

    # def get_grille(self):
    #     return self.grille

    def check_etat(self, x, y):
        for ele in self.grille:
            if ele.x == x and ele.y == y:

                print(ele.etat)
                return ele.etat
            
    
    def verif_nb_voisins_vivants(self, case): # paramètre case, verif avec pep8

        nvv = 0

        #for ele in self.grille:
        for v in self.dict_voisins:
            tempx = v[0] + case.x
            tempy = v[1] + case.y

            self.check_etat(tempx,tempy)
               

    class GOLEngine:
        def __init__(self, width, height):
            self.__width = None
            self.__height = None

    def resize(self, width, height):
        if width < 3 or height < 3:
            raise ValueError('...')
        
        self.__width = width
        self.__height = height
        self.__grid = []

        for x in range(self.__width): # _ instead of x 
            self.__grid.append([])
            for _ in range(self.__height):
                self.__grid[x].append(0) #-1 instead of x (ajoute une rangée de 0 après la dernière ligne)

    @width.setter
    def width(self, value):
        self.resize(value, self.__height)              
               
    def set_cell_value(self, x, y, value):
        if value in (0, 1, True, False):
            value = int(bool(value))
            self.__grid[x][y] = value

    def randomize(self, percent=0.5):
        for x in range(self.__width):
            for y in range(self.__height):
                self.__grid[x][y] = int(random() <= percent)
    
    def process(self):
        for x in range(1, self.__width): #pour retirer les extrémités 
            




g = Grille(10, 12)

g.init_grille()
g.afficher_grille_debug()

#g.afficher_grille
# grille = g.get_grille
# print(grille)

# print(g.retourne_nb_case())


# print(g.grille[0])

# g.verif_nb_voisins_vivants(g.grille[50])


print(g.verif_nb_voisins_vivants(g.grille[50]))

    

