def delete(tpl, value):
    while value in tpl:
        tpl.remove(value)
    result = tuple(tpl)
    return result
user_input = input('Введите входные данные: ')
lst = []

for i in user_input:
    if i.isdigit():
        lst.append(int(i))

number = int(input('Введите число которое нужно удалить: '))
print(delete(lst, number))