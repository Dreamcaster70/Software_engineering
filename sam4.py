def main(*args):
    avarage = sum(args) / len(args)
    print(avarage)
if __name__ == '__main__':
    main(1, 4 , 6, 7, 10, 15)