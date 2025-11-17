import keyboard

# EXERCICES PARTIE 1 

def devinez_nb(): #1.1

    #while not keyboard.is_pressed("q"): 
        nb_secret = 42
        nb_essais = 5
        reussi = False 

        while nb_essais > 0:
            reponse = int(input("Devinez le nombre entre 0 à 100 : ")) # à transformer en int car reçoit une chaîne de caractères
            if reponse > nb_secret:
                print("Plus bas")
                nb_essais -= 1
            elif reponse < nb_secret:
                print("Plus haut")
                nb_essais -= 1
            elif reponse == nb_secret:
                print(f'Bravo! Vous avez obtenu la bonne réponse, le nb secret était bien {reponse}')
                reussi = True
                break 

        if not reussi:
            print(f'Vous avez utilisé tous vos essais, la bonne réponse était {nb_secret}')   

        nb_essais = 5 #on reset le nb secret à 5 
    
    #print("finish")


def calculatrice_simple():
    pass


def trier_trio_nombres(): #1.4 

    #while not keyboard.is_pressed("q"): 
        a = None
        b = None
        c = None

        while a == None:

            a = int(input("Choisissez un premier nombre : "))
            print("choix valide")

            while b == None:
                b = int(input("Choisissez un second nombre : "))
                print(" choix valide")
            
                while c == None:
                    c = int(input("Choisissez un troisieme nombre : "))
                    print(" choix valide")

        # ordre a - b - c
        print(f'a: {a}, b: {b}, c:{c}')

        while a > b: 
            #if a > b:
            a, b = b, a 
            print(f'a: {a}, b: {b}, c:{c}')
            if b > c:
                b, c = c, b
                print(f'a: {a}, b: {b}, c:{c}')
    
        print(f'a: {a}, b: {b}, c:{c}')
    
    #print("finish")


def trouver_palindromes():

    list_normalized = []
    inversed_list = []

    tests = (
    'Esope reste ici et se repose',
    'Elu par cette crapule',
    'Engage le jeu que je le gagne',
    'La mariee ira mal',
    'Eric notre valet alla te laver ton cire',
    'Il est incroyable',
    'Able was I ere I saw Elba',
    'A man a plan a canal Panama',
    'Was it a car or a cat I saw',
    'Never odd or even',
    'Madam, I m Adam',
    'Hello World',
    'A Toyota’s a Toyota',)

    for t in tests: # pour chaque élément dans tests
        t.lower().strip().replace(" ", "")
        list_normalized.append(t)
    
    inversed_list = list_normalized[::-1] # https://www.geeksforgeeks.org/python/python-reversing-list/

    size = len(list_normalized)

    for i in range(size):
        if list_normalized[i] == inversed_list[i]:
            print(f'{i}eme phrase est un palindrome')


def stats_city():
    data = [
    ("Tremblay, Marc", 41, "Montréal", 'h'),
    ("Lévesque, Annie", 30, "Gatineau", 'f'),
    ("Beaulieu, Denis", 58, "Longueuil", 'h'),
    ("Aubin, Christine", 41, "Saguenay", 'f'),
    ("Gauthier, Julie", 33, "Québec", 'f'),
    ("Boucher, Geneviève", 37, "Sherbrooke", 'f'),
    ("Bergeron, Mathieu", 36, "Gatineau", 'h'),
    ("Poirier, Daniel", 63, "Saguenay", 'h'),
    ("Gagnon, Laure", 27, "Montréal", 'f'),
    ("Morin, Philippe", 54, "Québec", 'h'),
    ("Caron, Zoé", 21, "Gatineau", 'x'),
    ("Bélanger, Thomas", 42, "Laval", 'h'),
    ("Pelletier, Maude", 24, "Laval", 'f'),
    ("Langlois, Patrick", 50, "Sherbrooke", 'h'),
    ("Simard, Noé", 34, "Longueuil", 'x'),
    ("Roy, Étienne", 35, "Montréal", 'h'),
    ("Ouellet, Kevin", 38, "Laval", 'h'),
    ("Côté, Myriam", 22, "Montréal", 'f'),
    ("Lavoie, Nadine", 46, "Québec", 'f'),
    ("Bouchard, Alex", 31, "Montréal", 'x'),
    ("Fortin, Samuel", 19, "Québec", 'h'),
    ("Girard, Valérie", 26, "Longueuil", 'f'),
    ("Gagné, Chantal", 29, "Laval", 'f'),
    ("Lefebvre, Simon", 18, "Saguenay", 'h'),
    ("Lapointe, Amélie", 23, "Sherbrooke", 'f'),
    ("Dufour, Olivier", 40, "Montréal", 'h'),
    ("Boucher, Camille", 28, "Gatineau", 'f'),
    ("Lemieux, Alexandre", 39, "Québec", 'h'),
    ("Desjardins, Élise", 32, "Laval", 'f'),
    ("Morissette, Vincent", 45, "Longueuil", 'h'),
    ("Caron, Sarah", 20, "Saguenay", 'f'),
    ("Bélanger, Maxime", 44, "Sherbrooke", 'h')]

    gender_count = dict(h=0, f=0, x=0) 
    city_stat = {} #contiendra le nom des villes 
    temp_city = []

    for d in data:
        age = d[1]
        ville = d[2]
        gender = d[3]

        gender_count[gender] += 1 

        if len(temp_city) == 0 or ville not in temp_city:
            temp_city.append(ville)
            city_stat[ville] = dict(nb_hab=0, sum_age=0, age_moyen=0) # chaque ville aura son dico de stats
            city_stat[ville]["sum_age"] += age
        else:
            city_stat[ville]["nb_hab"] += 1
            city_stat[ville]["sum_age"] += age
    
    print(f'Gender count\n H: {gender_count['h']}, F: {gender_count['f']}, X:{gender_count['x']}')

    for city in city_stat:
        
        sum_age = city_stat[city]["sum_age"]
        nb_hab = city_stat[city]["nb_hab"]
        age_moyen = round((sum_age/nb_hab),2)

        city_stat[city]["age_moyen"] = age_moyen

        print(f'{city}, Nb habs: {city_stat[city]["nb_hab"]}, Age moyen : {city_stat[city]["age_moyen"]}')
    

def valider_syntaxe():
    phrase = "Au labo (site {Nord [A-12]})"

    normalized_p = phrase.strip()

    tuple1 = ("{", "}")
    tuple2 = ("(", ")")
    tuple3 = ("[", "]")

    all_tuples = (tuple1, tuple2, tuple3)

    size = len(all_tuples)

    for i in range(size):
        if all_tuples[i][0] in normalized_p:
            if all_tuples[i][1] in normalized_p:
                print(f'syntaxe valide {all_tuples[i]}')
            else:
                print(f'syntaxe invalide {all_tuples[i]}')


def main():

    #devinez_nb()
    #calculatrice_simple()
    #trier_trio_nombres()
    #trouver_palindromes()
    #stats_city()
    valider_syntaxe()



if __name__ == '__main__':
    main()