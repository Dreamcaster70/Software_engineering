value = 10
while value < 50:
    if value % 2 == 0:
        value +=10
    elif value * value > 50:
        value //2
    else: value +=5
    print(value)
