with open('laba.txt', 'a+') as file:
    file.write('\nNew line')
with open('laba.txt', 'r') as file:
    for i in file:
        print(i)