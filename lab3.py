def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i]*15)//10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')
if __name__ == '__main__':
    data([1, 11, 'gadfwa', 'i', 'python', 231, 35])