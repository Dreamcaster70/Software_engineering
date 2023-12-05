def sum():
    try:
        number = input('Введите число: ')
        number = float(number)
        result = number + 2
        print(result)
    except ValueError:
        print('Неподходящий тип данных, введите число')

if __name__ == '__main__':
    sum()
    sum()
    sum()