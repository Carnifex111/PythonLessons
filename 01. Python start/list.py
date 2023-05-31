numbers = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'банан', 'апельсин']
mixed = [10, 'hello', True, 3.14]

first_number = numbers[0]  # 1
second_number = numbers[1]  # 2

fruits = ['яблоко', 'банан', 'апельсин']
fruits[1] = 'груша'

fruits = ['яблоко', 'банан', 'апельсин']
length = len(fruits)  # 3

fruits = ['яблоко', 'банан', 'апельсин']
fruits.append('груша')

numbers = [1, 2, 3, 4, 5]
slice1 = numbers[1:3]  # [2, 3]
slice2 = numbers[:3]  # [1, 2, 3]
slice3 = numbers[2:]  # [3, 4, 5]

fruits = ['яблоко', 'банан', 'апельсин']

# Удаляем элемент по индексу Теперь fruits будет равно['яблоко', 'апельсин']
del fruits[1]

fruits = ['яблоко', 'банан', 'апельсин']

fruits.remove('яблоко')  # Удаляем элемент по значению

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers1.extend(numbers2)


fruits = ['яблоко', 'банан', 'апельсин']
fruits.insert(1, 'груша')

numbers = [5, 2, 8, 1, 9]
numbers.sort()
# Теперь numbers будет содержать [1, 2, 5, 8, 9]
