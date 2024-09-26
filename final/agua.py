from pokemon import *

class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre, "Agua", "Hierba")

    def ataque(self, oponente):
        if self._tipo == oponente.get_debiliad():
            oponente.defender(self._ataque + self._ataque * 0.7)
        oponente.defender(self._ataque)
    
    def defender(self, danio):
        if self._defensa < danio:
            probabilidad = random.randint(1,100)
            if probabilidad <= 30:
                self._vida = self._vida - danio * 0.5
            else:
                self._vida = self._vida - danio