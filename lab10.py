global result
def triangle():
    a = float(input('Основание: '))
    h = float(input('Высота: '))
    global result
    result = 0.5*a*h
def rectangle():
    a = float(input('Длина: '))
    b = float(input('Ширина: '))
    global result
    result = a*b
figure = input("1-треугольник, 2-прямоугольник: ")
if figure == '1':
    triangle()
elif figure == '2':
    rectangle()
print(f"S={result}")
