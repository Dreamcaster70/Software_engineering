def info(name, age, workplace):
    print(f'Имя: {name}, возраст: {age}, место работы: {workplace}')
Petya = ('Петр', 40, 'УРГЭУ')
Vova = ('Владимир', 30, 'УРФУ')
info(*Petya)
info(*Vova)