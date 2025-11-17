import math, random, time 

# EXERCICES PARTIE 2

#3.1 

class Nombre_aleatoire: 
    
    def __init__(self):
        self.__n = self.get_n()
        self.__values = self.generate_random_values(self.__n, 3, 10000)
        self.__moyenne = self.mean(self.__values)
        self.__mediane = self.mediane(self.__values)
        
    
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
    
    def mediane(self, values):
        liste_trie = sorted(values)
        n = len(liste_trie)
        #mediane = n // 2 #division entiere 
        
        index_mediane = int((n/2))
        
        nb_median = liste_trie[index_mediane - 1]
        
        return nb_median 
            
    def afficher_resultats(self):
        print(f'nombre choisi:{self.__n}\n')
        print(f'liste nb aléatoires:{self.__values}\n')
        print(f'moyenne de la liste:{self.__moyenne}\n')
        print(f'mediane de la liste:{self.__mediane}\n')
        
#3.2
class Analyzer_String():
    def __init__(self):
        self.__phrase = self.get_sentence()
        self.__stats = self.sentence_stats()
        self.afficher_stats(self.__stats)
        
    
    def get_sentence(self):
        phrase = None 
        
        while phrase is None:
            try:
                phrase = str(input("Inscrivez votre phrase:"))
            except ValueError:
                print("Veuillez entrer des caractères valides")
                
                
        return phrase
    
    def get_size(self, sentence):
        return len(sentence)
    
    def specific_char_count(self, sentence, liste):
        counter = 0
        for letter in sentence:
            if letter in liste:
                counter += 1
        return counter 
    
    def get_nb_mots(self, sentence):
        return len(sentence.split())
            
    def sentence_stats(self):
        vowels = 'aeiouy'
        consonants = 'bcdfghjklmnpqrstvwxz'
        special_characters = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
        
        stats = {
            "phrase": self.__phrase,
            "caracteres": self.get_size(self.__phrase),
            "voyelles": self.specific_char_count(self.__phrase, vowels),
            "consonnes": self.specific_char_count(self.__phrase, consonants),
            "speciaux": self.specific_char_count(self.__phrase, special_characters),
            "mots": self.get_nb_mots(self.__phrase)
        }
       
        return stats 
   
    def afficher_stats(self, stats):
        print(f'Votre phrase: {stats["phrase"]}')
        print(f'Nombre de caractères: {stats["caracteres"]}')
        print(f'Nombre de voyelles: {stats["voyelles"]}')
        print(f'Nombre de consonnes: {stats["consonnes"]}')
        print(f'Nombre de caractères spéciaux: {stats["speciaux"]}')
        print(f'Nombre de mots: {stats["mots"]}')
        
        
        
        
def main():
    # n = Nombre_aleatoire()
    # n.afficher_resultats()
    
    a = Analyzer_String()
   

if __name__ == '__main__':
    main()