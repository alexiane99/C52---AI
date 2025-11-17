import math, random, time 

# EXERCICES PARTIE 2

#3.1 

class Nombre_aleatoire: 
    
    def __init__(self):
        self.__n = self.get_n()
        self.__values = self.generate_random_values(self.__n, 3, 10000)
        self.__moyenne = self.mean(self.__values)
        
    
    def get_n(self):
        n = None 
        while n is None:
            try: 
                n = int(input("Choisissez un nombre entre 3 et 10000: "))
                
                if(n < 3 or n > 10000):
                    print("Nombre invalide, le nombre attribué par défaut est 100.")
                    n = 100 
            except ValueError:
                print("Veuillez entrer un nombre valide")
                n = None 
            
        return n 
    
    def generate_random_values(self, n, min_value, max_value):
        
        liste_nombres = []
        
        for _ in range(n):
            value = random.randint(min_value, max_value)
            liste_nombres.append(value)
        
        return liste_nombres
    
        #return [random.randint(min_value, max_value) for _ in range(n)]
    
    def mean(self, values):
        return (sum(values)/len(values))
            
    def afficher_resultats(self):
        print(f'nombre choisi:{self.__n}\n')
        print(f'liste nb aléatoires:{self.__values}\n')
        print(f'moyenne de la liste:{self.__moyenne}\n')
        
        
def main():
    n = Nombre_aleatoire()
    n.afficher_resultats()
    

if __name__ == '__main__':
    main()