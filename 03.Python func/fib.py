def fib(n):
    if n <= 0:
        return "Ошибка! Введите положительное число."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


# Проверка функции
print(fib(1))  # 0
print(fib(2))  # 1
print(fib(6))  # 5
print(fib(10))  # 34
