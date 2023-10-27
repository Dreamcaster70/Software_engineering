import random
def main():
    x = random.randint(1,6)
    if x == 1 or x == 2:
        print(f"Выпало {x}, вы проиграли")
    elif x == 3 or x == 4:
        print(f"Выпало {x}, кубик перебрасывается")
        main()
    elif x == 5 or x == 6:
        print(f"Выпало {x}, вы победили")
if __name__ == '__main__':
    main()