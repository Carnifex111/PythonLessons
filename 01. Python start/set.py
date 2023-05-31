fruits = {'яблоко', 'банан', 'апельсин'}
numbers = set([1, 2, 3, 4, 5])
mixed = {1, 'hello', True}

numbers = {1, 2, 3, 4, 5, 1, 2}
# Результат: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)

fruits = {'яблоко', 'банан', 'апельсин'}
is_apple_in_fruits = 'яблоко' in fruits
# Результат: True

fruits = {'яблоко', 'банан', 'апельсин'}
fruits.add('груша')  # Добавляет элемент в множество
fruits.remove('яблоко')  # Удаляет элемент из множества
# Удаляет элемент, если он присутствует, иначе ничего не делает
fruits.discard('ананас')
fruits.clear()  # Удаляет все элементы из множества
