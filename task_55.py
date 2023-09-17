'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телоефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (например, имя или фамилию человека)
4. Используйте функции. Ваша программа не должна быть линейной.'''

print('Программа - телефонный справочник с записью в файл')

command = ['+', '-', '1', '9', '0']

def input_record():
    family = input('Введите фамилию абонента: ').strip().title()
    name = input('Введите имя абонента: ').strip().title()
    patronymic = input('Введите отчество абонента: ').strip().title()
    phone_number = input('Введите номер телефона в формате "ххх-ххх-хххх": ').strip()
    return f'{family} {name} {patronymic} - {phone_number}\n'

def write_file():
    with open('phone_number.txt', 'r', encoding='UTF-8') as file:
        return file.readlines()

def add_record():
    with open('phone_number.txt', 'a', encoding='UTF-8') as file:
        file.write(input_record())
    return print('Запись добавлена!')

def remove_record():
    lines = write_file()
    print('Введите данные для удаления записи:')
    data = input_record()
    if data in lines:
        with open('phone_number.txt', 'w', encoding='UTF-8') as file:
            for line in lines:
                if line != data: file.write(line)
            return print('Запись удалена!')
    else: print('Введенных Вами данных не существует.')

def update_record():
    lines, lines_new = write_file(), []
    print('Введите данные записи, которую хотите отредактировать:'); data = input_record()
    print('Введите новые данные записи:'); replace_data = input_record()
    if data in lines:
        for line in lines:
            if line != data: lines_new.append(line)
            else: lines_new.append(line.replace(data, replace_data))
        with open('phone_number.txt', 'w', encoding='UTF-8') as file:
            for line_new in lines_new:
                file.write(line_new)
        return print('Запись изменена!')
    else: print('Введенных Вами данных не существует.')

def print_all_record():
    pass

def print_if_record():
    pass

def continuation():
    print('Желаете завершить работу с программой?')
    symbol = input('Нажмите знак "+", если желаете продолжить и любой другой, если хотите завершить: ')
    if symbol == '+': return True
    else: return False

flag = True
print('Желаете ли Вы ознакомиться со списком команд перед использованием программы?')
answer = input('Нажмите знак "+" и Enter, если да и любой другой знак в противносм случае: ')

command_references = f'''
{command[0]} - добавление записи в файл
{command[1]} - удаление записи с файла
{command[2]} - редактирование записи в файле
{command[3]} - печать всех записей на экране монитора
{command[4]} - печать записей с использованием фильтра
'''

if answer == '+':
    print(command_references)

while flag:
    symbol = input('Введите команду для работы с файлом: ')
    if symbol == command[0]: add_record(); flag = continuation()
    elif symbol == command[1]: remove_record(); flag = continuation()
    elif symbol == command[2]: update_record(); flag = continuation()
    elif symbol == command[3]: print_all_record(); flag = continuation()
    elif symbol == command[4]: print_if_record(); flag = continuation()
    else: print('Введена неверная команда. Пожалуйста, перевведите!'); continue