n = int(input('Введите количество чисел, содержащихся в первом наборе: '))
m = int(input('Введите количество чисел, содержащихся во втором наборе: '))

def count_number(count):
    number_list = []
    for i in range(1, count+1):
        number = int(input(f'Введите {i} число для набора из {count} элементов и нажмите Enter: '))
        number_list.append(number)
    return number_list

set_n = set(count_number(n))
set_m = set(count_number(m))
print(*sorted(set_n.union(set_m)))