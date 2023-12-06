def fib(n):
    with open('fib.txt', 'w') as file:
        a, b = 1, 1
        for i in range (n):
            file.write(f'{a}\n')
            yield a

            a, b = b, a+b
for num in fib(200):
    print(num)