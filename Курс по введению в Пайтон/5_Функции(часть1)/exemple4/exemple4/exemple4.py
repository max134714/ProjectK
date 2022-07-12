def f(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in range(-3, 4):
        y = f(i)
        print('f(', i, ')=', y, sep='')


main()
