# Тема 9. ООП на Python: концепции, принципы и примеры реализации
Отчет по Теме #9 выполнил:
- Зонов Дмитрий Андреевич
- АИС-21-1

| Задание | Лаб_раб | 
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

| Задание | Сам_раб | 
| ------ | ------ | 
| Тест 1 | + |
| Тест 2 | + |
| Тест 3 | + |
| Тест 4 | + |
| Тест 5 | + |

# Лаб.работа
## Задание №1
### -

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/lab/1%20-%20Uh8pITL.png)

## Задание №2
### -

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/lab/2%20-%20Uv9Nbsf.png)

## Задание №3
### -

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/lab/3%20-%200MnEGqO.png)

## Задание №4
### -

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/lab/4%20-%20NLiNXGH.png)

## Задание №5
### -

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/lab/5%20-%20IjIsoUl.png)


# Самостоятельная работа
## class Tomato
###  

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/sam/2%20-%20de4HCOH.png)


## class TomatoBush
### 

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/sam/3%20-%20PiiuWvS.png)


## Class Gardener 
### 
### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/sam/4%20-%20xSCpSDv.png)

  
## Тесты
### 
1) Вызовите справку по садоводству
2) Создайте объекты классов TomatoBush и Gardener
3) Используя объект класса Gardener, поухаживайте за кустом с
помидорами
4) Попробуйте собрать урожай, когда томаты еще не дозрели.
Продолжайте ухаживать за ними
5) Соберите урожай

### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/sam/5%20-%20G6SQU2s.png)


## Результаты тестов
### Вывод в консоль
### Результат.
![Меню](https://github.com/Dreamcaster70/Software_engineering/blob/Tema_9/pic9/sam/6%20-%20zT7KiwB.png)

## Итоговый код
```python
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
```

## Выводы
В данной самостоятельной работе я на собственном примере понял для чего вообще нужно ООП и как оно работает.
