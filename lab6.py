string = 'Строка'
value = input('Введите букву: ')
if value in string:
    index = string.find(value)
    print(f"Буква '{value}' есть в строке под {index} индексом ")
else:
    print(f"Буквы {value} нет в строке")
