class CarOil:
    def __init__(self, brand, viscosity, type, volume):
        self.brand = brand
        self.viscosity = viscosity
        self.type = type
        self.volume = volume
    def Info(self):
        print(f'Бренд {self.brand}, вязкость {self.viscosity}, тип {self.type}, объем {self.volume} л.')
my_carOil = CarOil('Ravenol', '5w40', 'Synthetic', '4')
my_carOil.Info()