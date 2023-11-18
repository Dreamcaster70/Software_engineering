def counter(file):
    with open(file, 'r', encoding='utf-8') as f:
        count = len(" ".join(f.readlines()).split())
        print(f'Количество слов в тексте: {count}')

def word(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', ' ').lower().split()
        print(f'Самое часто встречающееся слово: {max(set(text), key=text.count)}')

counter('article.txt')
word('article.txt')
