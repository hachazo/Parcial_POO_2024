class Entrenador:
    def __init__(self, nombre, nivel, pokemon):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__pokemon = pokemon
        self.__pokedex = []

    def atrapar_pokemon(self, pokemon):
        if self.__nivel > pokemon.get_salvajismo():
            for i in range(3):
                pokemon.ataque(self.__pokemon)
                if pokemon.get_vida() <= 0:
                    print("No se pudo atrapar el pokemon")
                    break
                if self.__nivel > pokemon.get_salvajismo():
                    print("Pokemon atrapado")
                    self.__pokedex.append(pokemon)
                    break
                pokemon.set_salvajismo(pokemon.get_salvajismo() - pokemon.get_salvajismo() * 0.1)
        else:
            print("No se pudo atrapar el pokemon")
        
    def mostrar_pokedex(self):
        print("")
        print(f"Entrenador: {self.__nombre} Nivel: {self.__nivel}")
        print("Pokedex:")
        for pokemon in self.__pokedex:
            pokemon.mostar_pokemon()