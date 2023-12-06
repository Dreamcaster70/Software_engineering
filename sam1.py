def fib(n):
    a, b = 1, 1
    for i in range (n):
        yield a
        a, b = b, a+b
for num in fib(200):
    print(num)