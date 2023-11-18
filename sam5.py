def search(file):
    with open(file, 'r', encoding='utf-8') as f:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        text = f.read()
        for i in alphabet:
            if i in text:
                print(i)
search('input2.txt')

