n = int(input('Введите количество кустов, растущих на грядке: '))
dict_bed, flag = dict(), True
for i in range(1, n+1):
    count = int(input(f'Введите количество ягод, содержащихся на {i} кусте: '))
    dict_bed[i] = count
while flag:
    number = int(input('Введите номер куста, с которой необходимо собрать урожай: '))
    if number > n or number <= 0:
        print('Номер куста находится вне диапазона количества кустов. Перевведите!')
        continue
    elif 1 < number < n:
        count_berry = dict_bed[number] + dict_bed[number+1] + dict_bed[number-1]; flag = False
    elif number == 1:
        count_berry = dict_bed[number] + dict_bed[number+1] + dict_bed[n]; flag = False
    elif number == n:
        count_berry = dict_bed[number] + dict_bed[1] + dict_bed[number-1]; flag = False
print(f'Максимальное число ягод, который может собрать модуль, находясь над {number} кустом равно {count_berry}')
