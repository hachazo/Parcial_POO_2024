from pokemon import *
class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Fuego", "Agua")
    
    def defender(self,oponente):
        if self._defensa < oponente.get_ataque:
            self.vida_restante(oponente.get_ataque)