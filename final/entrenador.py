# Se deberá crear un entrenador al que, al momento de crearse, se le asignará un nombre, un nivel de
# entrenador (valor aleatorio de entre 1 y 100) y un pokemon principal.
# Cada entrenador tiene una colección de Pokémon que se registran en su Pokédex.
# El entrenador debe ser capaz de atrapar Pokémon. Para ello, su nivel de entrenador debe ser mayor al
# nivel de salvajismo del Pokémon que quiere atrapar. Podrá realizar hasta 3 ataques para disminuir su
# nivel de salvajismo, por cada ataque se disminuirá un 10%. Sin embargo, si el Pokémon pierde toda su
# vida durante estos ataques, no podrá ser atrapado. Después de cada ataque, se deberá comprobar si es
# posible capturarlo.
# Si logra capturar al Pokémon, este se agrega automáticamente a su Pokédex.
import random

class Entrenador:
    def __init__(self, nombre, pokemon):
        self._nombre = nombre
        self._nivel = random.randint(1,100)
        self._pokemon = pokemon
        self._pokedex = []
        
    def atrapar_pokemon(self, pokemon):
        for i in range(3):
            pokemon.set_salvajismo(pokemon.get_alvajismo() - pokemon.get_salvajismo() * 0.10)
            if self._nivel >= pokemon.get_salvajismo():
                
                self._pokemon.atacaque(pokemon)
                if pokemon._vida <= 0:
                    print("El pokemon no pudo ser atrapado")
                    return False
                else:
                    self._pokedex.append(pokemon)
                    print("El pokemon fue atrapado")
                    return True
            else:
                    self._pokedex.append(pokemon)
                    print("El pokemon fue atrapado")
                    return True
                
    def imprimir(self):
        print("Nombre: ", self._nombre)
        print("Nivel: ", self._nivel)
        self._pokemon.imprimir()
        for pokemon in self._pokedex:
            pokemon.imprimir()