from datetime import datetime #импорт функции datetime из модуля datetime для даты и времени
from math import sqrt #импорт функции sqrt из модуля math для вычисления квадратного корня
def main(**kwargs): # функция main с использованием параметров **kwargs
    for key in kwargs.items(): # итерирование по элементам словаря
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # вычисление евклидова расстояния до значения key[1]
        print(result) # выводит результат
"""
result - евклидово расстояние до key[1]
"""
if __name__ == '__main__': #точка входа
    start_time = datetime.now() # запоминание текущего времени
    main( # вызов функции main с заданными аргументами
        one=[10,3],
        two=[5,4],
        three=[15,13],
        four=[93,53],
        five=[133,15]
    )
    time_costs = datetime.now() - start_time # время потраченное на выполнение
    print(f"Время выполнения программы - {time_costs}") # выводит время выполнения