import random

my_array = []

count_array = int(input('Введите размер массива: '))
for i in range(1, count_array+1):
    my_array.append(random.randint(10, 100))
print('Заполненный массив:', my_array)

random.shuffle(my_array)
print('Перемешанный список:(1 перемешка)', my_array)
random.shuffle(my_array)
print('Перемешанный список:(2 перемешка)', my_array)