#Задача 1
'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''
#Решение задачи 1
'''
n = abs(float(input("Введите вещественное число в формате ±xx.xx ")))
n1, n2 = map(int, str(n).split('.'))
sum = 0
while n1 > 0:
    sum += n1 % 10
    n1 //= 10
while n2 > 0:
    sum += n2 % 10
    n2 //= 10
print(sum)
'''


#Задача 2
'''
Напишите программу, которая принимает на вход число N и выдает набор произведений
чисел от 1 до N. Факториал
5! = 120
'''
#Решение задачи 2 (факториал, а не набор факториалов, как было изначально)
'''
n = int(input('Введите неотрицательное число '))
if n < 0: print('Это отрицательное число')
elif n == 0: print(1)
else:
    fact = 1
    for i in range(1, n + 1): fact *= i
    print(fact)
'''


#Задача 3
'''
Задана последовательность натуральных чисел, завершающаяся числом 0.
Требуется определить значение второго по величине элемента в этой последовательности,
то есть элемента, который будет наибольшим, если из последовательности удалить
наибольший элемент.
Пример:
1 7 9 0
Вывод:
7
'''
#Решение задачи 3
'''
arr = [3, 9, 7, 0]
max = arr[0]
for i in arr:
    if i > max: max = i
second_max = arr[0]
for i in arr:
    if i > second_max and i < max: second_max = i
print(second_max)
'''

#Дополнительная задача
'''
Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
после чего дробная часть копеек отбрасывается.Требуется определить:
через сколько лет вклад составит не менее Y рублей.
Пример:
100
10
200
Вывод:
8
'''
#Решение дополнительной задачи
'''
x, p, y = map(int, input("Введите сумму вклада, ежегодный процент и ожидаемую итоговую сумму ").split())
count = 0
while x < y:
    x += x / 100 * p // 1
    count += 1
print(count)
'''