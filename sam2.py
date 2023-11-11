def delete(tpl, value):
    if value in tpl:
        tpl.remove(value)
    result = tuple(tpl)
    return result
user_input = input('Введите входные данные: ')
lst = []
number = None
for i in user_input:
    if i.isdigit():
        lst.append(int(i))
    if user_input[-5] == ')':
        if i == ')':
            number = user_input[-2]
            break
number = int(number) if number is not None else None

print(delete(lst, number))