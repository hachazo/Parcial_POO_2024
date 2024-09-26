from Pokemon import Pokemon

class Fuego(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, 'Fuego', 'Agua')

    def defensa(self, danio):
        if danio > self._ataque:
            danio -= self._defensa
            if danio < 0:
                danio = danio*-1
            self._vida -= danio