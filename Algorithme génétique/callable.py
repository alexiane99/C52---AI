from random import random


def browse(data, task, final_task = None):
    for i, _ in enumerate(data):
        data[i] = task(data[i])

    if final_task is not None:
        final_task()


# Fonction (1)
def print_value(value):
    print(f'{value} ', end = '')
    return value

def print_end_of_line():
    print()


class Exposant:

    def __init__(self, exp = 2):
        self.exp = exp

    def __call__(self, _): # functor (5)
        return int(random() * 100)

    def square(self, value): # Méthode (2)
        return value ** self.exp


def main():

    data = list(range(7))
    browse(data, print_value, print_end_of_line)

    test = Exposant() # <<< Classe dans le sens d'instanciation (3)
    finalize = lambda : browse(data, print_value, print_end_of_line)
    browse(data, test.square, finalize)


    browse(data, lambda v: v * (1 if v % 2 else -1), finalize) # lambda (4)
    

    browse(data, test, finalize)



if __name__ == '__main__':
    main()


# for v in data:
#     print(f'{v} ', end='')
# print()

# for i, v in enumerate(data):
#     data[i] = v ** 2

# for i in range(len(data)):
#     print(f'{data[i]} ', end='')
# print()

# for i, v in enumerate(data):
#     data[i] = v * (1 if v % 2 else -1)

# for i, v in enumerate(data):
#     print(f'{data[i]} ', end='')
# print()