from agua import *
from fuego import * 
from hierba import * 
from entrenador import *

pokemon1 = Agua("Squirtle")
pokemon1.mostar_pokemon()
entrenador1 = Entrenador("daira",random.randint(0,100), Agua("Squirtle"))

lista_pokemon = []

for i in range(10):
    tipo = random.randint(1,3)
    if tipo == 1:
        pokemon_agua = Agua("Pokemon {}".format(i))
        lista_pokemon.append(pokemon_agua)
    elif tipo == 2:
        pokemon_fuego = Fuego("Pokemon {}".format(i))
        lista_pokemon.append(pokemon_fuego)
    else:
        pokemon_hierba = Hierba("Pokemon {}".format(i))
        lista_pokemon.append(pokemon_hierba)

for pokemon in lista_pokemon:
    entrenador1.atrapar_pokemon(pokemon)
entrenador1.mostrar_pokedex()