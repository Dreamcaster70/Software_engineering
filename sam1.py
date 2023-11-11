user_input = input('Введите числа разделенные пробелом: ').split()
user_list = list(user_input)
user_tupl = tuple(user_input)
print(f'Список: {user_list}, \nКортеж: {user_tupl}')