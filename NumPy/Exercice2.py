import numpy as np

# https://www.geeksforgeeks.org/python/how-to-convert-images-to-numpy-array/

#data[x,y] // data[row, column]  

#QUESTION 1 : Créer l'image (array de 0)
def create_image(size): #size étant un tuple 
    img = np.full((size[0], size[1]),0) 
    return img
    return np.zeros((size[1][0]), dtype = np.uint8)

#QUESTION 2 : Fill with selected color
def fill(img, color): #color = 1 ? 0
    # !! image = np.ones(image.size), dtype = np.uint8 !! pas bon 
    #image[0:, 0:] = color // ne pas mettre le dernier car exclut
    # ou [:,:]
    # ou [:]
    #img[:] = color #va chercher toutes les valeurs et les attribues à la couleur sélectionnée
    img[img != color] = color #va chercher toutes les couleurs qui ne sont pas de la couleur sélectionnée et y attribue la valeur

#QUESTION 3 : Reset à zéro
def clear(img):
    img[img != 0] = 0

#QUESTION 4
def randomize(img, percent):
    rng = np.random.default_rng()
    n = rng.random(image.shape) #crée un nb aléatoire pour toutes les images de la matrice iamge
    t = n <= percent
    c = t.astype(img.dtype)
    img[:] = c
    #img[:] = (rng.random(img.shape) <= percent).astype(img.dtype)
    #img[:] = np.random.choice([0,1], p=[percent, percent]) #avec probabilités -> https://www.geeksforgeeks.org/python/numpy-random-choice-in-python/
    # ne fonctionne pas car ne respecte pas le percent
#QUESTION 5
def draw_point(img, pt, color):
    img[pt[0],pt[1]] = color

#QUESTION 6
def draw_rectangle(img, top_left, bottom_right): #top_left = x0, y0 // bottom_right = x1, y1
    img[top_left[0]:bottom_right[0], top_left[1]] = 2 #rangée 1 (x0 à x1; y0 )
    img[top_left[0], top_left[1] : bottom_right[1]] = 2 #colonne 1 (x0; y0 à y1)
    img[top_left[0]:bottom_right[0], bottom_right[1]] = 2 #dernière rangée (x0 à x1; y1)
    img[bottom_right[0], top_left[1]:bottom_right[1]] = 2 #dernière colonne (x1; y0 à y1)
    img[bottom_right[0], bottom_right[1]] = 2

    #le coin en bas à gauche (bottom_right = ?) # car le dernier élément est exclut!!

#     x0, y0               x1,y0
#     XXXXXXXXXXXXXXXXXXXXXXXXXX
#     XXXXXXXXXXXXXXXXXXXXXXXXXX
#     XXXXXXXXXXXXXXXXXXXXXXXXXX
#     x0, y1               x1, y1 

#QUESTION 7
def reset_border(img):
    # -1 étant la dernière colonne/rangée
    # img[0,:] = 3 #x0
    # img[:, 0] = 3 #y0
    # img[-1, :] = 3 #x1
    # img[:, -1] = 3 #y1

    img[:, [0,-1]] = 3 #sélection indices
    img[[0,-1], :] = 3 
    
#QUESTION 8
def draw_random_point(img, color):
    liste = np.array(img)
    # print(liste.shape) => (10,10)
    # print(liste.shape[0]) 10

    dimx = liste.shape[0]
    dimy = liste.shape[1]
    ptx = np.random.choice(dimx, 1)
    pty = np.random.choice(dimy, 1)
    img[ptx,pty] = color

#QUESTION 9
def inverse_random_point(img, color):
    liste = np.array(img)
    dimx = liste.shape[0]
    dimy = liste.shape[1]
    ptx = np.random.choice(dimx, 1)
    pty = np.random.choice(dimy, 1)
    img[ptx,pty] = color

#QUESTION 10
def distance_between_two_points(img):
    
    pt1,pt2 = np.where(img == 1)

    d = (((pt2[1] - pt1[1])**2) + ((pt2[0] - pt1[0])**2))**0.5
    
    return round(d,4)

#QUESTION 11
def draw_circle(img, center, radius):
    
    cx = center[0]
    cy = center[1]
    
    liste_pts = np.array([(cx - radius, cy - radius),(cx, cy - radius),(cx + radius, cy - radius), 
                          (cx - radius, cy),           (cx, cy),           (cx + radius, cy), 
                          (cx - radius, cy + radius), (cx, cy + radius), (cx + radius, cy + radius)
                        ]
                        )
    #rayon : longueur
    
    print(liste_pts)
    listex = liste_pts[:,0] #prend toutes les valeurs de x (indice 0)
    listey = liste_pts[:,1] #prend toutes les valeurs de y (indice 1)
    
    img[listex, listey] = 1




def draw_circle_prof(image, center, radius):
    # xr = np.arange(image.shape[1])
    # yr = np.arange(image.shape[0])
    # xi, yi = np.meshgrid(xr, yr)
    # cx, cy = center
    # dx = xi - cx
    # dy = yi - cy 
    # dist = np.sqrt(dx ** 2 + dy **2) #ou **0.5
    # d = np.round(dist,1).astype(np.int32) 
    # trace = (dist <= radius).astype(np.int32)
    # new_im = np.logical_or(image or trace)
    # iamge = new_im

    cx, cy = center
    r2 = radius *2
    c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    image[(c - cx)**2 + (r - cy )**2 <= r2**2] = 1 

    return image

# def draw_circle(img, center, radius, value=1):
#     # """
#     # Dessine un cercle dans un tableau 2D NumPy.

#     # Paramètres :
#     # - img : np.ndarray (2D)
#     #     Tableau représentant l'image.
#     # - center : tuple (cx, cy)
#     #     Coordonnées du centre du cercle (x, y).
#     # - radius : int
#     #     Rayon du cercle.
#     # - value : int ou float
#     #     Valeur à placer dans le cercle (par défaut = 1).
#     # """
#     cx, cy = center
#     rows, cols = img.shape

#     # Crée une grille de coordonnées (X, Y)
#     y, x = np.ogrid[:rows, :cols]

#     # Calcul de la distance de chaque point au centre
#     dist = np.sqrt((x - cx)**2 + (y - cy)**2)

#     # Sélectionne les points proches du rayon (±0.5 pour un contour fin)
#     mask = np.abs(dist - radius) <= 0.5

#     # Applique la valeur sur ces points
#     img[mask] = value
    

#QUESTION 12
def area(img):
    a = np.sum(img[img != 0])
    return a 

#QUESTION 13
def centroid(image,center, radius):
    # dimx = image.shape[1]
    # dimy = image.shape[0]
    
    # tab_x, tab_y = np.meshgrid(np.arange(dimx), np.arange(dimy))
    # return (np.sum(tab_x * image), np.sum(tab_y * image))/np.sum(image)

    x, y = center
    c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    #dist = np.sqrt(np.sqrt((r-y)**2 + (c-x)**2))
    # approche 1 = avec assignation générale
    # circle = (dist <= radius).astype(np.uint8)
    # image[:] = np.logical_or(image[:,:], circle)
    # approche 2 = avec assignation sélective
    # circle = dist <= radius
    # image[circle] = 1
    
    # approche finale
    image[((r-y)**2 + (c-x)**2) <= radius**2] = 1
    #     \________________________________/
    #                      \___ cette série d'opérations 
    #                           retournent une matrice de booléens
    #                           qui sert de masque à l'assignation de 1
    
    print(image)
    # return (np.sum(dimx * image), np.sum(dimy * image))/np.sum(image)

#   c, r = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
#   return (np.sum(r * image), np.sum(c * image)) / area(image)

#QUESTION 14
def perimeter(img):

    shape = np.array(img != 0)
    rangee_x0 = shape[:, 0] 
    colonne_y0 = shape[0, :]
    rangee_x1 = shape[:, -1]
    colonne_y1 = shape[-1, :]

    p = np.sum(rangee_x0 + rangee_x1 + colonne_y0 + colonne_y1)

    return p

def perimeter_test(image):
    y, x = image.shape[:2]
    forme = (image == 1) #création d'un masque (en True or False)

    neighbors = np.zeros((y, x, 8), dtype=bool) #création d'un tableau avec 8 valeurs booléeennes indiquant si les voisins appartiennent aussi à la forme 
    # Haut
    neighbors[1:, :, 0] = image[:-1, :] == 1
    # Bas
    neighbors[:-1, :, 1] = image[1:, :] == 1
    # Gauche
    neighbors[:, 1:, 2] = image[:, :-1] == 1
    # Droite
    neighbors[:, :-1, 3] = image[:, 1:] == 1
    # Haut-gauche
    neighbors[1:, 1:, 4] = image[:-1, :-1] == 1
    # Haut-droite
    neighbors[1:, :-1, 5] = image[:-1, 1:] == 1
    # Bas-gauche
    neighbors[:-1, 1:, 6] = image[1:, :-1] == 1
    # Bas-droite
    neighbors[:-1, :-1, 7] = image[1:, 1:] == 1

    # Contour = pixels de la forme qui ont au moins un voisin à 0
    contour = forme & (~neighbors.all(axis=2)) #le ~ inverse, donc va conserver tous les pixels qui touchent au moins à un 0

    return float(np.sum(contour))




# TESTS 
size = (10, 10)

print("\n#Q1\n")
image = create_image(size)
print(image)

print("\n#Q2\n")
fill(image, 1)
print(image)

print("\n#Q3\n")
clear(image)
print(image)

print("\n#Q4\n")
randomize(image, 0.5)
print(image)

print("\n#Q5\n")
clear(image)
draw_point(image, (4,4), 1)
print(image)

print("\n#Q6\n") 
draw_rectangle(image, (1,1), (4,4))
print(image)

print("\n#Q7\n")
reset_border(image)
print(image)

liste = np.array(image)
print(liste.shape)
print(liste.shape[0])

print("\n#Q8\n")
draw_random_point(image, 5)
print(image)

print("\n#Q9\n")
inverse_random_point(image,4)
print(image)

print("\n#Q10\n")
clear(image)
draw_random_point(image,1)
draw_random_point(image,1)
print(image)
print(distance_between_two_points(image))

print("\n#Q11\n")
clear(image)
print(f'cercle : {draw_circle_prof(image, (5,5), 4)}')
# img = np.zeros((20, 20), dtype=int)
# draw_circle(img, center=(10, 10), radius=6)
# print(img)


print("\n#Q12\n")
clear(image)
draw_rectangle(image, (1,1), (4,4))
print(area(image))
print(image)

print("\n#Q13\n")
print(centroid(image))

# print("\n#Q14\n")
# print(perimeter(image))

# xr = np.arange(image.shape[1])
# print(xr)
# yr = np.arange(image.shape[0])
# print(yr)
# xi, yi = np.meshgrid(xr, yr)
# print(xi, yi)

# print(perimeter_test(image))

