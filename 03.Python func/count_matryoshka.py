def count_matryoshka(matryoshka):
    if matryoshka == 1:
        return 1
    else:
        return matryoshka + count_matryoshka(matryoshka - 1)


# Проверка функции
print(count_matryoshka(5))  # 15
print(count_matryoshka(3))  # 6
print(count_matryoshka(1))  # 1
