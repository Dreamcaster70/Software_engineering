class Error(Exception): # Класс исключения
    def __init__(self, message='Число нечетное'):
        self.message = message
        super().__init__(self.message)

# Функция для проверки четности числа и бросания исключения при нечетном числе
def number(n):
    try:
        if n % 2 != 0:
            raise Error(n)  # Бросаем исключение, если число нечетное
        else:
            print(f'Число {n} четное')
    except Error as ex:
        print(ex)  # Обрабатываем исключение и выводим сообщение

# Функция для деления числа на 2 и бросания исключения при нечетном числе
def delit(num):
    try:
        if num % 2 != 0:
            raise Error  # Бросаем исключение, если число нечетное
        else:
            result = num / 2  # Результат деления на 2 для четного числа
            print(result)  # Вывод результата
    except Error as ex:
        print(ex)  # Обрабатываем исключение и выводим сообщение
if __name__ == '__main__':
    delit(1)
    number(4)
    delit(6)