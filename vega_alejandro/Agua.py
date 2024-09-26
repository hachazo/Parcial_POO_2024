from Pokemon import Pokemon
import random

class Agua(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, 'Agua', 'Hierba')

    def ataque(self, atacado):
        if self._tipo == atacado.get_debilidad():
            atacado.defensa(int(self._ataque * 1.70))
            pass
        atacado.defensa(self._ataque)

    def defensa(self, danio):
        if danio > self._ataque:
            danio -= self._defensa
            if danio < 0:
                danio = danio*-1
            if random.randrange(0,100) < 30:
                danio -= danio*0.50
                self._vida -= danio
            else:
                self._vida -= danio