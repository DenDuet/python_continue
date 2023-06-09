import rand_number as gen


if __name__ == '__main__':
    res = gen.rand_number(1,12,6)
    if res:
        print("Число угадано.")
    else:
        print("Число не угадано.")