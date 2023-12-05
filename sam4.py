class Counter: # Класс, который считает кол-во вызовов функции
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1 # Счетчик вызова функций
        print(f'Функция {self.func.__name__} вызвана {self.count} раз')
        return self.func(*args, **kwargs)
@Counter
def square(n): # функция вычисления квадрата числа
    number = n*n
    print(number)
@Counter
def factorial(k): # функция вычисления факториала
    result = 1
    for i in range(1, k + 1):
        result *= i
    print(result)
square(2)
square(4)
square(6)
factorial(3)
factorial(10)