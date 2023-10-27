from sam5 import triangle
if __name__ == '__main__':
    a = int(input('Введите сторону a: '))
    b = int(input('Введите сторону b: '))
    c = int(input('Введите сторону c: '))
    if a+b>c and a+c>b and b+c>a:
        triangle(a, b, c)
    else:
        print('Треугольника с такими сторонами не существует')

