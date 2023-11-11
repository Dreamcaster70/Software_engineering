def tpl(tpl, value):
    if value in tpl:
        start_index = tpl.index(value)
        end_index = tpl.index(value, start_index+1)+1 if (start_index != -1) and (value in tpl[start_index+1:]) else len(tpl)
        if start_index == end_index:
            a = tuple(tpl[start_index:])
            return a
        b = tuple(tpl[start_index:end_index])
        return b
    return None

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


result = tpl(lst, int(number))
if result is not None:
    print(result)
else:
    print(tuple())