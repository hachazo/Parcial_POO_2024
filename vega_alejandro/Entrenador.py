

class Entrenador:
    
    def __init__(self, nombre, nivel, pokemon):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__pokemon = pokemon
        self.__pokedex = []

    def atrapar(self, pokemon_salvaje):
        valor = int(pokemon_salvaje.get_salvajismo()-pokemon_salvaje.get_salvajismo()*0.10)
        pokemon_salvaje.set_salvajismo(valor)
        self.__pokemon.ataque(pokemon_salvaje)
        if self.__nivel > pokemon_salvaje.get_salvajismo() and pokemon_salvaje.get_vida() > 0:
            self.__pokedex.append(pokemon_salvaje)
            print('Se atrapo al pokemon')
            return True
        if(pokemon_salvaje.get_vida() < 0):
            print('El pokemon no pudo ser atrapado porque su vida bajo a 0')
            return False
    
    def imprimir(self):
        print('Pokedex')
        for i in self.__pokedex:
            i.imprimir()
