import mistery as mist


if __name__ == '__main__':
    num = mist.mistery("Сто одежек и все без застежек.", ["капуста", "капустка", "капустище"], 5)
    if num >= 0:
        print(f"Вы угадали с {num} попытки.")
    else:
        print("Вы не угадали... ")