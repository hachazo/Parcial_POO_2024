import random
from abc import ABC

class Pokemon(ABC):  
    def __init__(self, nombre,tipo,debilidad,vida=100):
            self._nombre = nombre
            self._vida = vida
            self._tipo = tipo
            self._debilidad = debilidad
            self._ataque = random.randint(0,100)
            self._defensa = random.randint(0,100)
            self._velocidad = random.randint(0,100)
            self._salvajismo = random.randint(0,100)

    def get_vida(self):
        return self._vida
    
    def get_debiliad(self):
        return self._debilidad
    
    def get_tipo(self):
        return self._tipo
    
    def get_salvajismo(self):
        return self._salvajismo
    
    def get_ataque(self):
        return self._ataque
    
    def set_salvajismo(self, salvajismo):
        self._salvajismo = salvajismo
    
    def ataque(self, oponente):
        if self._tipo == oponente.get_debiliad():
            probabilidad = random.randint(1,100)
            
            if probabilidad <= 70:
                oponente.defender(self._ataque + self._ataque * 0.5) # oponente.defender(self.ataque* 1.5)    
        else:
            oponente.defender(self._ataque)
            
    # def imprimir(self):
    #     print("Nombre: ", self._nombre)
    #     #print("Tipo: ", self._tipo)
    #     print("Ataque: ", self._ataque)
    #     print("Defensa: ", self._defensa)
    #     print("Velocidad: ", self._velocidad)
    #     print("Salvajismo: ", self._salvajismo)
    def imprimir(self):
        print(f"Nombre: {self._nombre} Tipo: {self._tipo} Ataque: {self._ataque} Defensa: {self._defensa} Velocidad: {self._velocidad} Salvajismo: {self._salvajismo:.2f}")