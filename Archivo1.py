
import numpy as np
valor = np.sin(np.pi)
print(f"El valor de seno de pi es :{valor}")


class vehiculo:
    def __init__(self,numero_ruedas,numero_puertas):
        self.Numero_ruedas = numero_ruedas
        self.Numero_puertas = numero_puertas
        print("objeto vehiculo creado")

class carro(vehiculo):
    def __init__(self,numero_ruedas,numero_puertas,marca):
        super().__init__(numero_ruedas,numero_puertas)
        self.Marca = marca

Mazda = carro(4,4,"mazda")
BMW =carro(4,2,"bmw")