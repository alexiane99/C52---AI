import numpy as np

# https://www.geeksforgeeks.org/python/how-to-convert-images-to-numpy-array/

#QUESTION 1 : Créer l'image (array de 0)
def create_image(size): #size étant un tuple 
    img = np.full((size[0], size[1]),0) 
    return img

#QUESTION 2 : Fill with selected color
def fill(img, color): #color = 1 ? 0
    
    #img[:] = color #va chercher toutes les valeurs et les attribues à la couleur sélectionnée
    img[img != color] = color #va chercher toutes les couleurs qui ne sont pas de la couleur sélectionnée et y attribue la valeur

#QUESTION 3 : Reset à zéro
def clear(img):
    img[img != 0] = 0

#QUESTION 4
def randomize(img, percent):
    img[:] = np.random.choice([0,1], p=[percent, percent]) #avec probabilités -> https://www.geeksforgeeks.org/python/numpy-random-choice-in-python/

#QUESTION 5
def draw_point(img, pt, color):
    img[pt[0]][pt[1]] = color

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
    img[0,:] = 3
    img[:, 0] = 3
    img[-1, :] = 3
    img[:, -1] = 3
    
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
    #rayon : longueur
    rx = img[center[0] + radius][center[1]]
    ry = img[center[0]][center[1]] + radius
    pass

#QUESTION 12
def area(image):
    pass

#QUESTION 13
def centroid(image):
    pass

#QUESTION 14
def perimeter(image):
    pass




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
draw_point(image, (4,4), 1)
print(image)

print("\n#Q6\n") 
draw_rectangle(image, (1,1), (4,4))
print(image)

print("\n#Q7\n")
reset_border(image)
print(image)

# liste = np.array(image)
# print(liste.shape)
# print(liste.shape[0])

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