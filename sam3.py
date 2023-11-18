def words(file):
    with open(file, 'r', encoding='utf-8') as f:
        count = len(" ".join(f.readlines()).split())
        print(f'{count} words')
def letters(file):
    with open(file, 'r') as f:
        text = f.read().replace('.', ' ')
        count = len(' '.join(text).split())
        print(f'{count} letters')
def lines(file):
    with open(file, 'r') as f:
        count = len(f.readlines())
        print(f'{count} lines')
print('input file contains: ')
letters('input.txt')
words('input.txt')
lines('input.txt')