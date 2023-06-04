def name_funс(param):
    # Тело функции
    result = 1 + param
    return result


def say_hello(name):
    print("Привет, " + name + "!")


# Вызов функции
# say_hello('Виктор')


def x_plus_y(x, y):
    return x + y


a = x_plus_y(1, 2)


def print_age(name):
    if name == 'Леша':
        return 'Леша'
    elif name == 'Аня':
        return 'Аня'
    else:
        return 'Имя не было введено'


name = print_age()

print(name)
