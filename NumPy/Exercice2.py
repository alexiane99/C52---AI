import numpy as np

# https://www.geeksforgeeks.org/python/how-to-convert-images-to-numpy-array/

def create_image(size):
    color = (255, 0, 0)
    img = np.array([size[0], size[1], color]) #hauteur x largeur x pixel rgb
    return img


size = [500,600]
create_image(size)