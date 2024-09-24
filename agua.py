from pokemon import *

class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Agua", "Hierba")
        
    def ataque(self, oponente):
        if oponente.get_tipo == self._debilidad:
                self.recibir_danio(self._ataque * 0.7,oponente)
        else:
            self.recibir_danio(self._ataque,oponente)

    def defender(self,oponente):
        if self._defensa < oponente.get_ataque:
            if random.randint(1,100) <= 30:
                self.vida_restante(oponente.get_ataque * 0.5)
            else:
                self.vida_restante(oponente.get_ataque)