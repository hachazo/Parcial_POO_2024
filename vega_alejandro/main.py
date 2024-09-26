import random
from Agua import Agua
from Hierba import Hierba
from Fuego import Fuego
from Entrenador import Entrenador

pokemons_salvajes = []

opciones = ['Agua','Hierba','Fuego']

for i in range(0,11):
    opcion = random.choice(opciones)
    if opcion == 'Agua':
        pokemons_salvajes.append(Agua('pokemon {}'.format(i)))
    if opcion == 'Hierba':
        pokemons_salvajes.append(Hierba('pokemon {}'.format(i)))
    if opcion == 'Fuego':
        pokemons_salvajes.append(Fuego('pokemon {}'.format(i)))

random.shuffle(opciones)

entrenador = Entrenador("Ale", random.randrange(0,100), pokemons_salvajes[0])

for pokemon in pokemons_salvajes:
    posibilidades = 0
    while(posibilidades<3):
        posibilidades = posibilidades+1
        print('El entrenador realizo un ataque al pokemon {}'.format(pokemon.get_nombre()))
        res = entrenador.atrapar(pokemon)
        if(res == True):
            print('El pokemon {} ha sido atrapado'.format(pokemon.get_nombre()))
            pass
        if(res == False):
            print("El pokemon {} no ha podido ser atrapado".format(pokemon.get_nombre()))
            pass

entrenador.imprimir()