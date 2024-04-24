### TAREA
## 1. Agregar metodos setters y getters

class Automovil():
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self):
        velocidad_automovil = self.velocidad
        velocidad_automovil += 10
        print(f"El automovil va a {velocidad_automovil}")
        self.velocidad = velocidad_automovil

    def frenar(self):
        velocidad_automovil = self.velocidad
        velocidad_automovil -= 10
        print(f"El automovil va a {velocidad_automovil}")
        self.velocidad = velocidad_automovil