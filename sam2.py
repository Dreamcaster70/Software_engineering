def read(file):
    try:
        with open(file, 'r') as f:
            text = f.read()
            if not text:
                raise Exception('Пустой файл')
            else:
                print(text)
    except Exception as ex:
        print(f"Ошибка {ex}")
print('Пустой файл:')
read('empty.txt')
print('Непустой файл:')
read('file.txt')