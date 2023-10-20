x=[1,4,6,8,9,15,15,62,79]
y=int(input('Переменная: '))
if y in x:
    if y % 2 == 0:
        print('Четная')
    else:print('Нечетная')
else:
    print(f"Переменной {y} нет в массиве")
