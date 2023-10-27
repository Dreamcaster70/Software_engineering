def main(x, y, *args):
    a = x # 4
    b = sum(args) # 10, 5, 6, 2, 1 sum = 24
    c = y # 3
    return x + sum(args) - y
if __name__ == '__main__':
    d = main(4, 3, 10, 5, 6, 2, 1)
    print(d)