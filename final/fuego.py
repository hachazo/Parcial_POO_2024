from pokemon import *

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Fuego", "Agua")
        
    def defender(self, danio):
        if self._defensa < danio:
            self._vida = self._vida - danio
            