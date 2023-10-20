for i in range(10):
    print(i)
    if i == 0:
        i+=1
    if i == 1:
        continue
    if i == 2:
        i/=2
        print(i)
    if i >=3:
        i*=3
        print(i)
        if i > 6:
            break


