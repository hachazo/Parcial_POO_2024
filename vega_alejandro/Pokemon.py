from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    
    def __init__ (self,nombre,tipo,debilidad):
        self._nombre = nombre
        self._tipo = tipo
        self._vida = 100
        self._ataque = random.randrange(0,100)
        self._defensa = random.randrange(0,100)
        self._velocidad = random.randrange(0,100)
        self._debilidad = debilidad
        self._salvajismo = random.randrange(0,100)

    @abstractmethod
    def defensa(self, danio):
        pass

    def ataque(self, atacado):
        if self._tipo == atacado.get_debilidad():
            if random.randrange(0,100) < 70:
                atacado.defensa(int(self._ataque * 1.50))
                pass
        atacado.defensa(self._ataque)

    def imprimir(self):
        print("Nombre: {}".format(self._nombre))
        print("Ataque: {}".format(self._ataque))
        print("Defensa: {}".format(self._defensa))
        print("Velocidad: {}".format(self._velocidad))
        print("Salvajismo: {}".format(self._salvajismo))

    def get_debilidad(self):
        return self._debilidad
    
    def get_salvajismo(self):
        return self._salvajismo

    def set_salvajismo(self,valor):
        self._salvajismo = valor
    
    def get_nombre(self):
        return self._nombre

    def get_vida(self):
        return self._vida