class Tomato:
    states = {1: 'отсутствует', 2: 'цветение', 3: 'зеленый', 4: 'красный'}
    def __init__(self, _index):
        self._index = _index
        self._state = self.states[1] #принимает первое значение из словаря
        """
        данные атрибуты являются защищенными
        """
    def grow(self):
        if self._state != Tomato.states[4]: #проверка выхода за границы
            current_index = list(self.states.keys())[list(self.states.values()).index(self._state)]
            self._state = self.states[current_index + 1] #переход на следующее состояние
        print(self._state)
    def is_ripe(self):
        if self._state == [4]: #проверка зрелости
            print('Помидор созрел')
        else:
            print('Помидор еще не созрел')
class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(i) for i in range(1,amount+1)] #создание списка
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow() #пробегаемся по каждому томату и меняем зрелость
    def all_are_ripe(self):
        count = 0
        for tomato in self.tomatoes:
            if tomato._state == Tomato.states[4]:
                count +=1
            else:
                break
        return count == self.amount
    """
    если счетчик совпадает с кол-вом томатов возвращается True
    """
    def give_away_all(self):
        self.tomatoes = [] #чистится список томатов
class Gardener:
    def __init__(self, name, _plant):
        self.name = name #публичный
        self._plant = _plant #защищенный
    def work(self):
        print('Работник работает')
        self._plant.grow_all() #метод класса TomatoBush
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Садовник собирает урожай')
        else:
            print('Не все помидоры еще созрели, нужно еще поработать')
    @staticmethod
    def knowledge_base():
        print('Поддерживайте оптимальную температуру,\n'
              'Вовремя поливайте кусты,\n'
              'Следите за освещенностью,\n'
              'Удобряте почву')
Gardener.knowledge_base()
tomato_bush = TomatoBush(3)
gardener = Gardener('Steve', tomato_bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()


