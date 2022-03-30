class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color: {self.color}, Ruedas; {self.ruedas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        self.velocidad = velocidad
        super().__init__(color, ruedas)
    
    def __str__(self):
        return super().__str__(), f"Velocidad: {self.velocidad}"
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        self.tipo = tipo
        super().__init__(color, ruedas)
    
    def __str__(self):
        return super().__str__(), f"Tipo: {self.tipo}"
