date = input('Введите дату: ')
transfer = int(input('Введите количество переводов: '))
car = int(input('Введите траты на авто: '))
shop = int(input('Введите траты в супермаркетах: '))
food = int(input('Введите траты на еду: '))
other = int(input('Введите остальные расходы: '))
all = car+shop+food+other
with open('sam31.txt', 'a+') as f:
    f.write(f'\nВаши расходы на {date}:\n'
            f'Переводы: {transfer}руб.\n'
            f'Авто: {car}руб.\n'
            f'Супермаркеты: {shop}руб.\n'
            f'Еда: {food}руб\n'
            f'Остальное: {other}руб\n'
            f'Итог: {all}руб')
print(f'Ваши расходы на {date}:\n'
            f'Переводы: {transfer}руб.\n'
            f'Авто: {car}руб.\n'
            f'Супермаркеты: {shop}руб.\n'
            f'Еда: {food}руб\n'
            f'Остальное: {other}руб\n'
            f'Итог: {all}руб\n')