class Dima:
    __slots__ = ['name']
    def __init__(self, name):
        if name == 'Дима':
            self.name = f'Да, я {name}'
        else:
            self.name = f'Я не {name}, а Дима'
person1= Dima('Иван')
person2 = Dima('Дима')
print(person1.name)
print(person2.name)