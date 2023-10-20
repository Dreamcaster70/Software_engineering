x=[1,2,3,8,10,11,15,16,17]
flag=False
for value in x:
    if value % 2 == 1:
        flag=True
if flag is True:
        print('Нечетное число есть')
else:
        print('Нечетного числа нет')