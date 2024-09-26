from Pokemon import Pokemon
import random

class Hierba(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, 'Hierba', 'Fuego')

    def defensa(self, danio):
        if danio > self._defensa:
            if self._velocidad > 50:
                if random.randrange(0,2) == 0:
                    danio -= self._defensa
                    if danio < 0:
                        danio = danio*-1
                    self._vida -= danio
            else:
                self._vida -= danio