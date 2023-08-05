'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

N = int(input('Введите целое число: '))
numbers = []
index = 0
flag = True

while flag:
    prod_numbers = 2 ** index
    if prod_numbers <= N:
        numbers.append(prod_numbers)
        index += 1
    else:
        flag = False

print(*numbers)