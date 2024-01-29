class Pal:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'poder': self.poder
        }