def sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))
if __name__ == '__main__':
    print(sort((1, 10, 8, 5, 6, 7)))
    print(sort((3, 'x', 4,7,8,1)))