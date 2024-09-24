from pokemon import *
class Hierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Hierba", "Fuego") 
        
    def defender(self, oponente):
        if self._defensa < oponente.get_ataque:
            if self._velocidad > 50:
                if random.randint(1,100) >= 50:
                    self.vida_restante(oponente.get_ataque)
            else:
                self.vida_restante(oponente.get_ataque)




