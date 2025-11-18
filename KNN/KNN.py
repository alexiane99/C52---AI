import numpy as np

import numpy as np
#import matplotlib.pyplot as plt
from math import *
from typing import Tuple, Optional


# L'algorithme KNN (k-Nearest-Neighbours) consiste à classifier un objet en utilisant d'autres objets comparables 
# dont la classe a été préalablement établie (étiquetage)
# 5 Étapes 
# 1-Disposer dans un espace à n dimensions les données d'apprentissage
# 2-Disposer dans cet espace l'objet à classifier
# 3-Calculer la distance entre l'objet à classifier et chacune des données d'apprentissage
# 4-On retient les K voisins les plus proches 
# 5-On retient la classe la plus fréquente parmi les K voisins 
#
# Problèmes possibles:
# -> si la distance la plus proche est trop grande
# Solution : ajouter un critère de distance maximum pour accepter la classification
# -> si plusieurs classes partagent la même fréquence 
# Solution : déterminer la classe qui présente la plus petite distance ou la distance moyenne la plus petite
#
# 2 phases du KNN
# A-Préparation des données d'apprentissage (Lecture/Traitement/Insertion des données d'apprentissage)
# B-Classification (Lecture/ Traitement/ Classification)

class KNNNumpy():
    def __init__(self, k , dist, all_images, image_actuel):
        
        self.__k = k #nb de voisins à considérer
        self.__dist_max = dist #distance maximale au-delà duquel une image 
        # est jugée trop éloignée pour être classée 
        
        #all_images (vecteur_image, label)
        #all_images = [([150, 0.3, 72], "pomme"), ([200, 1.0, 50], "banane")]
        #(list, zip(*)) sépare la liste de tuples en 2 listes : données // labels
        #map convertit en liste classique 
        #np.array 
        self.__all_data, self.__all_label = map(list, zip(*all_images)) 

        self.__all_data = np.array(self.__all_data)
        self.__all_label = np.array(self.__all_label)



    def predict_image_actuelle(self, image_vector):
        #Prédit la classe de l'image actuelle en utilisant les 3 axes calculés
        return self.predict(image_vector)

    
    def add_point(self, data, label):
        """
        ========= exemple d'utilisation =========
        knn_n.add_point([150, 0.3, 72], "pomme")
        """
        if len(self.__all_data) == 0:
            self.__all_data = np.array([data])
            self.__all_label = np.array([label])
        else:
            self.__all_data = np.append(self.__all_data, [data], axis=0)
            self.__all_label = np.append(self.__all_label, label)
        
    def add_points(self, all_data, all_label): 
            """
            ========= exemple d'utilisation =========
            knn_n.add_points(np.array([[150, 0.3, 72], [200, 0.8, 50]]), np.array(["pomme", "banane"]))
            """
            self.__all_data = np.array(all_data)
            self.__all_label = np.array(all_label)

    @property
    def all_data(self):
        return self.__all_data
    @property
    def dist_max(self):
        return self.__dist_max
    @property
    def all_label(self):
        return self.__all_label
            
    def predict(self, image):
        
        image = np.array(image)

        # calculer la distance euclidienne entre l'image et tous les pts connus ( retourne la norme d'une matrice ou d'un vecteur)
        distances_array = np.linalg.norm(self.__all_data - image, axis=1)
        
        # np.argsort -> ensuite il faut les trier du plus proche au plus éloigné
        # [:self._k] -> garde les indices des k voisins plus proches 
        k_indices = np.argsort(distances_array)[:self.__k] #argsort retourne les indices correspondant au tri des éléments
        k_distances = distances_array[k_indices] #distances 
        k_labels = self.all_label[k_indices] #labels /étiquettes


        # Si le plus proche voisin est trop éloigné, on considère que
        # l'image n'appartient à aucune classe connue 
        distance_min = k_distances[0]
        if distance_min > self.__dist_max:
            return None, distance_min, 0 #confiance = nulle 
        

        # On compte combien de fois chaque label apparaît dans les k voisins plus proches 
        # compter celui qui a le plus de fois le meme type
        # Si égalité, on doit départager 
        unique, compte = np.unique(k_labels, return_counts=True)

        max_count = np.max(compte)
        tied_labels = unique[compte == max_count]

        # calculer la distance moyenne des voisins
        # la classe la plus proche en moyenne l'emporte 
        
        if len(tied_labels) > 1:
            # égalité, sur le même rang
            # Cas d'ex-aequo : calculer la distance moyenne pour chaque classe ex-aequo
            best_label = None
            best_avg_distance = float('inf')
            
            for label in tied_labels:
                label_distances = k_distances[k_labels == label]
                avg_distance = np.mean(label_distances)
                
                if avg_distance < best_avg_distance:
                    best_avg_distance = avg_distance
                    best_label = label
            
            predicted_label = best_label
            avg_distance = best_avg_distance
        else:
            # Cas normal : une seule classe majoritaire
            predicted_label = unique[np.argmax(compte)]
            avg_distance = np.mean(k_distances[k_labels == predicted_label])
        
        # Calculer un indice de confiance (0 à 1)
        # Plus la distance est petite par rapport à dist_max, plus la confiance est élevée
        confiance = max(0, 1 - (avg_distance / self.__dist_max))

        return predicted_label, avg_distance, confiance

    @property
    def k(self):
        return self.__k
    
    @k.setter
    def k(self, k):
        if not(1 <= k <= len(self.__all_label)):
            raise ValueError("k doit être entre 1 et " + str(len(self.__all_label)))
        self.__k = k

    @property
    def ndim(self):
        if len(self.__all_data) == 0:
            return 0
        return len(self.__all_data[0])

    

# Notes personnelles pour KNN 
# Est dépendant de ses voisins pour être classifié 
# k réfère au nombre des plus proches voisins à inclure pour la détermination de la classmethod
# Souvent init à k=5 
# Si k est trop petit, vulnérable au bruit autour
# Si k est trop grand, prendra plus de temps à process
# Pour sélectionner k, sqrt(n) où n est le total des pts à évaluer; 
# Est préférablement impair pour éviter la confusion entre les classes 
# Le KNN est utile lorsque :
#     - Les données ont des labels
#     - Présence de bruit (confusion entre des données à départager)
#     - Le dataset est petit (KNN étant un lazy learner, mais bon début pour commencer)
# On utilise la distance euclidienne pour calculer la distance
# Selon le nb de dimensions


# poids - sucre - eau

data = [

    # Pommes
    [
        [180, 10, 84],
        [170, 11, 85],
        [160, 9, 83],
        [175, 10.5, 84],
        [165, 9.5, 85],
    ],
    # Bananes
    [
        [120, 20, 74],
        [130, 21, 73],
        [125, 19.5, 75],
        [135, 22, 72],
        [128, 20.5, 74],
    ],
    # Pommes de terre
    [
        [200, 1, 79],
        [210, 0.8, 78],
        [190, 1.2, 80],
        [205, 1, 79],
        [195, 0.9, 81]
    ]
]

label = [
    
    # Pommes
    ["pomme", "pomme", "pomme", "pomme", "pomme"],

    # Bananes
    ["banane", "banane", "banane", "banane", "banane"],

    # Pommes de terre
    ["patate", "patate", "patate", "patate", "patate"]
]

class KNNNumpy():
    def __init__(self):
        self.__k = 3
        
        self.__all_data = None #np.array([])
        self.__all_label = None #np.array([], dtype=object)
    
    def add_point(self, data, label):
        """
        ========= exemple d'utilisation =========
        knn_n.add_point([150, 0.3, 72], "pomme")
        """
        if len(self.__all_data) == 0:
            self.__all_data = np.array([data])
            self.__all_label = np.array([label])
        else:
            self.__all_data = np.append(self.__all_data, [data], axis=0)
            self.__all_label = np.append(self.__all_label, label)
        
    def add_points(self, all_data, all_label): 
            """
            ========= exemple d'utilisation =========
            knn_n.add_points(np.array([[150, 0.3, 72], [200, 0.8, 50]]), np.array(["pomme", "banane"]))
            """
            self.__all_data = np.array(all_data)
            self.__all_label = np.array(all_label)

    @property
    def all_data(self):
        return self.__all_data
    @property
    def all_label(self):
        return self.__all_label
            
    def predict(self, image):
        
        image = np.array(image)

        # calculer la distance ( la norme ) entre l'image et chaque pt de training
        # np.linalg.norm(..., axis=1) calcule la norme (distance) par ligne
        distances_array = np.linalg.norm(self.__all_data - image, axis=1)
        
        # ensuite il faut les trier du plus proche au plus éloigné 
        # on prend les k premiers indices
        k_indices = np.argsort(distances_array)[:self.__k]

        k_labels = self.all_label[k_indices]

        # compter celui qui a le plus de fois le meme type
        u, indices = np.unique(k_labels, return_counts=True)

        return u[np.argmax(indices)]

    @property
    def k(self):
        return self.__k
    
    @k.setter
    def k(self, k):
        if not(1 <= k <= len(self.__all_label)):
            raise ValueError("k doit être entre 1 et " + str(len(self.__all_label)))
        self.__k = k

    @property
    def ndim(self):
        if len(self.__all_data) == 0:
            return 0
        return len(self.__all_data[0])

if "__main__" == __name__:
    
    knn_n = KNNNumpy()

    image = [150, 0.3, 72]

    knn_n.add_point([1501, 0.3, 72], "pomme")
    knn_n.add_point([1502, 0.3, 72], "patate")
    knn_n.add_point([1503, 0.3, 72], "banane")
    knn_n.add_point([1504, 0.3, 72], "pomme")
    knn_n.add_point([1504, 0.3, 72], "pomme")
    knn_n.add_point([1504, 0.3, 72], "pomme")
    knn_n.add_points(np.array([[150, 0.3, 72], [150, 0.3, 72], [200, 0.8, 50]]), np.array(["pomme", "pomme", "banane"]))

    knn_n.k = 2
    resultat = knn_n.predict(image)

    print(knn_n.all_label)
    print(knn_n.all_data)
    
    print("Résultat :", resultat)
    print("Dimensions :", knn_n.ndim)

