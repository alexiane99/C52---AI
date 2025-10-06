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
    img[top_left[0]:bottom_right[0], top_left[1]] = 1 #rangée 1 (x0 à x1; y0 )
    img[top_left[0], top_left[1] : bottom_right[1]] = 1 #colonne 1 (x0; y0 à y1)
    img[top_left[0]:bottom_right[0], bottom_right[1]] = 1 #dernière rangée (x0 à x1; y1)
    img[bottom_right[0], top_left[1]:bottom_right[1]] = 1 #dernière colonne (x1; y0 à y1)
    
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
    
    dimx = np.array([0] * 10)
    dimy = np.array([0] * 10)
    ptx = np.random.choice(dimx, 1)
    pty = np.random.choice(dimy, 1)
    img[ptx,pty] = color

#QUESTION 9
def inverse_random_point(img, color):
    pt = np.random.choice(img[img == color], 1)
    img[pt[0], pt[1]] = color

#QUESTION 10
def distance_between_two_points(img):
    # a^2 + b^2 = c^2s
    
    pt1, pt2 = img[img[:] == 1]
    
    d = (((pt2[1] - pt1[1])**2) + ((pt2[0] - pt1[0])**2))**0.5
    
    return d

#QUESTION 11
def draw_circle(image, center, radius):
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

#Q1
image = create_image(size)
print(image)

#Q2
fill(image, 1)
print(image)

#Q3
clear(image)
print(image)

#Q4
randomize(image, 0.5)
print(image)

#Q5
draw_point(image, (4,4), 1)
print(image)

#Q6
draw_rectangle(image, (1,1), (4,4))
print(image)

#Q7
reset_border(image)
print(image)

#print(np.ndarray.shape())

#Q8
# draw_random_point(image, 1)
# print(image)

#Q9
# inverse_random_point(image,0)
# print(image)

#Q10
# print(distance_between_two_points(image))