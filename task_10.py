'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть'''

n = int(input('Введите количество монет: '))
count_heads = 0
count_tails = 0
for i in range(n):
    pos = int(input('Введите позицию монеты: ')) #вводится позиция монеты: 0 - орел,
    if pos == 0:                                 #любое отличное от ноля число - решка555
        count_heads += 1
    else:
        count_tails += 1

print(count_heads if count_heads < count_tails else count_tails)
