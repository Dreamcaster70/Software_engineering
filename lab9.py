value=10
for i in range(5):
    for k in range(10):
        if i % 2 == 0:
            value +=k
        else:
            i +=1
print(value)
