def main(**kwargs):
    for a,b in kwargs.items():
        print(f"{a}. Mean = {mean(b)}")
def mean(data):
    return sum(data) / float(len(data))
if __name__ == '__main__':
    main(x=[3,3,3], y =[4,4,4])