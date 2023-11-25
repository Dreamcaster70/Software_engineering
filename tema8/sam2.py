class CarOil:
    def __init__(self, brand, viscosity, type, volume, price, country):
        self.brand = brand
        self.viscosity = viscosity
        self.type = type
        self.volume = volume
        self._price = price
        self.__country = country

    def Info(self):
        print(f'Бренд {self.brand}, вязкость {self.viscosity}, тип {self.type}, объем {self.volume} л.')

    def MoreInfo(self):
        print(f'Цена {self._price}, Страна производства {self.__country} ')

class GearboxOil(CarOil):
    def __init__(self, brand, viscosity, type, volume, price, country, gearboxtype):
        super().__init__(brand, viscosity, type, volume, price, country)
        self.gearboxtype = gearboxtype

    def GearboxOilInfo(self):
        print(f'Тип кпп {self.gearboxtype}')
def print_oil_info(oil):
    oil.Info()
    oil.MoreInfo()

my_carOil = CarOil('Ravenol', '5w40', 'Synthetic', '4', '6000', 'Германия' )
my_gearboxOil = GearboxOil('FUCHS Titan', '75w90', 'Synthetic', '5', '5800', 'Германия', 'ATF')

print_oil_info(my_carOil)
print_oil_info(my_gearboxOil)
my_gearboxOil.GearboxOilInfo()
