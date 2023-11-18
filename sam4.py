text = input('Введите текст: ')
with open('input1.txt', 'r') as f:
    words = f.read().split()
for i in words:
    while i in text.lower():
        a = len(i)*'*'
        b = text.lower().index(i)
        text = text.replace(text[b:b+len(i)], a)
print(text)