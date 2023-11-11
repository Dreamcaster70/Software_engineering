request = int(input('Введите номер кабинета: '))
dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 4321, 'access': True},
    103: {'key': 1111, 'access': True},
    104: {'key': 0000, 'access': True},
    105: {'key': 9999, 'access': True},
}
responce = dictionary.get(request)
if not responce:
    responce=dictionary[None]
key = responce.get('key')
access = responce.get('access')
print(key,access)