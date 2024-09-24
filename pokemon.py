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
    
    def set_vida(self,vida):
        self._vida = self._vida - vida
        
    def get_tipo(self):
        return self._tipo
    
    def get_ataque(self):
        return self._ataque

    def get_salvajismo(self):
        return self._salvajismo
    
    def set_salvajsmo(self,salvajismo):
        self._salvajismo = self._salvajismo - salvajismo
    
    def recibir_danio(self, danio, oponente):
        oponente.set_vida = oponente.get_vida() - danio
    
    def ataque(self, oponente):
        
        if oponente.get_tipo == self._debilidad:
            probabilidad = random.randint(1,100)
            
            if probabilidad <= 70:
                self.recibir_danio(self._ataque + self._ataque * 0.5, oponente)
        else:
            self.recibir_danio(self._ataque, oponente)

    def mostar_pokemon(self):
        print(f"Nombre: {self._nombre} Tipo: {self._tipo} Ataque: {self._ataque} Defensa: {self._defensa} Velocidad: {self._velocidad} Salvajismo: {self._salvajismo}")