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
def draw_rectangle(img, top_left, bottom_right):
    pass
    img[top_left[0], ] #ça doit prendre meshgrid https://python.19633.com/fr/python-tag-1/NumPy-1/1001020347.html

#QUESTION 7

#QUESTION 8

#QUESTION 9

#QUESTION 10

#QUESTION 11

#QUESTION 12

#QUESTION 13

#QUESTION 14




# TESTS 
size = (10, 10)
image = create_image(size)
print(image)

fill(image, 1)
print(image)

clear(image)
print(image)

randomize(image, 0.5)
print(image)

draw_point(image, (4,4), 1)
print(image)

draw_rectangle(image, (1,1), (4,4))
print(image)

print(np.meshgrid(np.array([0, 1, 2, 3]), np.array([10, 11]), np.array([100, 101])))