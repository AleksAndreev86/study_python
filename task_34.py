# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

string_list = input('Введите стих Винни-Пуха: ').lower().split()
counter = 1

def count_letter(phrase):
    count = 0
    for i in phrase:
        if any([i == 'а', i == 'е', i == 'и', i == 'о', i == 'у']):
            count += 1
    return count

for string in range(len(string_list)):
    if string == 0: keeping = count_letter(string_list[string])
    else:
        storage = count_letter(string_list[string])
        if keeping != storage: print('Пам Парам')
        else:
            counter += 1
            if counter == len(string_list): print('Парам пам-пам')