'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''

count = int(input('Введите количество элементов в списке: '))
array, index_list = list(), list()
index_min = int(input('Введите заданный минимум: '))
index_max = int(input('Введите заданный максимум: '))

def add_numbers(count=count, quantity=1):
    if count + 1 == quantity:
        return array
    else:
        number = int(input(f'Введите {quantity} элемент списка: '))
        array.append(number); quantity += 1
        return add_numbers(count, quantity=quantity)
    
def index_range(count=count, quantity=0):
    if count == quantity:
        return index_list
    else:
        if index_min <= list_numbers[quantity] <= index_max:
            index_list.append(quantity); quantity += 1
            return index_range(count=count, quantity=quantity)
        else:
            quantity += 1; return index_range(count=count, quantity=quantity)
        
list_numbers = add_numbers()
        
print(*index_range())