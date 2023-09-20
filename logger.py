from data_create import title_data, note_data
import datetime


def input_data():
    title = title_data()
    note = note_data()
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
    count = len(data)
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write(f'{count};{title};{note};{datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\n')


def print_data():
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(*data)
    return  data


def change_line(dataFile, numberRow):
    print(f"Меняем данную запись\n{dataFile[numberRow]}\n")
    countID = dataFile[numberRow].split(';')[0] 
    title = dataFile[numberRow].split(';')[1]
    note = dataFile[numberRow].split(';')[2]
    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Название заметки\n"
                       f"2. Содержание заметки\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 2:
        print("Вы ошиблись!\nВведите корректный номер (1 или 2)")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Название заметки\n"
                           f"2. Содержание заметки\n"
                           f"Введите ответ: "))
    if answer == 1:
        title = title_data()
    elif answer == 2:
        note = note_data()
    data = dataFile[:numberRow] + [f'{countID};{title};{note};{datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\n'] + \
                      dataFile[numberRow + 1:]
    if numberRow + 1 == len(dataFile):
        data = dataFile[:numberRow] + [f'{countID};{title};{note};{datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\n']
    with open('data.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Изменения успешно сохранены!')


def changes_data():
    
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
    # print("Какую именно запись по счету Вы хотите изменить?")
    # data = print_data()
    number_journal = int(input('Введите номер записи, которую хотите изменить: '))
    change_line(data, number_journal)


def delete_data():
    # print("Какую именно запись по счету Вы хотите удалить?")
    # data = print_data()
    number_journal = int(input('Введите номер записи, которую хотите удалить: '))
    while  0 < number_journal > len(data):
        print('Ты дурак?! Даю тебе последний шанс')
        number_journal = int(input('Введите номер записи: '))
    if number_journal == len(data):
        print(f'Удалить данную запись\n{data[number_journal]}')    
        data = data[:number_journal+1]
    else:
        print(f'Удалить данную запись\n{data[number_journal]}')
        data = data[:number_journal] + data[number_journal + 1:]
    while number_journal<len(data):
        title = data[number_journal].split(';')[1]
        note = data[number_journal].split(';')[2]
        time = data[number_journal].split(';')[3]
        if number_journal == len(data)-1:
            data = data[:number_journal] + [f'{number_journal};{title};{note};{time}']
        else:
            data = data[:number_journal] + [f'{number_journal};{title};{note};{time}'] + \
                data[number_journal + 1:]
        number_journal+=1
    with open('data.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Изменения успешно сохранены!')

def print_ID():
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
    number_journal = int(input('Введите номер записи, которую вывести: '))
    print(data[number_journal])
    
        
def print_filter_date():
    with open('data.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
    year = int(input('Выведите год:'))
    month = int(input('Введите месяц:'))
    day = int(input('Введите день:'))
    command = int(input('Какие записи вы хотите увидеть?\n'
            f'1. Найти записи этого от {year}-{month}-{day}.\n'
            f'2. Найти записи сделанные ранее {year}-{month}-{day}.\n'
            f'3. Найти записи сделанные позже {year}-{month}-{day}.\n'
            'Введите номер команды: '))
    filter_date = datetime.datetime(year, month, day)
    for i in range(1, len(data)):
        data_time = data[i].split(';')[3]
        data_date = data_time.split(" ")[0]
        data_date_split = data_date.split('-')
        note_date = datetime.datetime(int(data_date_split[0]), int(data_date_split[1]), int(data_date_split[2]))
        if command == 1:
            if note_date == filter_date:
                print(data[i])
        elif command == 2:
            if note_date < filter_date:
                print(data[i])
        elif command == 3:
            if note_date > filter_date:
                print(data[i])

        

            
