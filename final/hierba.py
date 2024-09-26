from pokemon import *

class Hierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Hierba", "Fuego")
        

    def defender(self, danio):
        if self._defensa < danio:
            if self._velocidad <= 50:
                self._vida = self._vida - danio
            else:
                self._vida = self._vida - danio * 0.5
        
