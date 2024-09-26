import random

class Entrenador:
    def __init__(self, nombre,nivel, pokemon):
        self._nombre = nombre
        self._nivel = nivel
        self._pokemon = pokemon
        self._pokedex = []
        
    # def atrapar_pokemon(self, pokemon):
    #     for i in range(3):
    #         pokemon.set_salvajismo(pokemon.get_alvajismo() - pokemon.get_salvajismo() * 0.10)
    #         if self._nivel >= pokemon.get_salvajismo():
                
    #             self._pokemon.atacaque(pokemon)
    #             if pokemon._vida <= 0:
    #                 print("El pokemon no pudo ser atrapado")
    #                 return False
    #             else:
    #                 self._pokedex.append(pokemon)
    #                 print("El pokemon fue atrapado")
    #                 return True
    #         else:
    #                 self._pokedex.append(pokemon)
    #                 print("El pokemon fue atrapado")
    #                 return True
    def atrapar_pokemon(self, pokemon):
        for intento in range(3):
            # Reducir el salvajismo del Pokémon salvaje
            pokemon.set_salvajismo(pokemon.get_salvajismo() * 0.90)
            
            # Verificar si el nivel del entrenador es mayor o igual al salvajismo del Pokémon
            if self._nivel >= pokemon.get_salvajismo():
                # El entrenador ataca al Pokémon salvaje
                self._pokemon.ataque(pokemon)
                
                if pokemon.get_vida() <= 0:
                    print(f"Intento {intento + 1}: El Pokémon no pudo ser atrapado, ha sido debilitado.")
                    return False
                else:
                    self._pokedex.append(pokemon)
                    print(f"Intento {intento + 1}: ¡El Pokémon fue atrapado exitosamente!")
                    return True
            else:
                print(f"Intento {intento + 1}: El Pokémon no fue atrapado, nivel insuficiente.")

        print("El Pokémon escapó después de 3 intentos.")
        return False
    
    def imprimir(self):
        print("")
        print("====================================")
        print("Entrenador: ", self._nombre)
        print("Nivel: ", self._nivel)
        print("")
        self._pokemon.imprimir()
        for pokemon in self._pokedex:
            pokemon.imprimir()
            