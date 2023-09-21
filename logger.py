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
    title = data[0].split(';')
    for i in range(1, len(data)):
        tempData = data[i].split(';')
        print(f'{title[0]}: {tempData[0]}\n'
              f'{title[1]}: {tempData[1]}\n'
              f'{title[2]}: {tempData[2]}\n'
              f'{title[3][:-1]}: {tempData[3]}\n')
    
def change_line(dataFile, numberRow):
    countID = dataFile[numberRow].split(';')[0] 
    title = dataFile[numberRow].split(';')[1]
    note = dataFile[numberRow].split(';')[2]
    date = dataFile[numberRow].split(';')[3]
    titleCSV = dataFile[0].split(';')    
    print('Вы изменяете заметку:\n'
          f'{titleCSV[0]}: {countID}\n'
          f'{titleCSV[1]}: {title}\n'
          f'{titleCSV[2]}: {note}\n'
          f'{titleCSV[3][:-1]}: {date}')
    answer = input("Какие данные Вы хотите поменять?\n"
                    "1. Название заметки\n"
                    "2. Содержание заметки\n"
                    "3. Название и содержание заметки.\n"
                    "Введите ответ: ")
    while answer != '1' and answer != '2' and answer != '3':
        print("Вы ошиблись!\nВведите корректный номер (1, 2 или 3)")
        answer = input()
    if answer == '1':
        title = title_data()
    elif answer == '2':
        note = note_data()
    elif answer == '3':
        title = title_data()
        note = note_data()
    data = dataFile[:numberRow] + [f'{countID};{title};{note};{datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\n'] + \
                      dataFile[numberRow + 1:]
    if numberRow + 1 == len(dataFile):
        data = dataFile[:numberRow] + [f'{countID};{title};{note};{datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\n']
    with open('data.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Изменения успешно сохранены!')

def changes_data():
    flag = True
    while flag:
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
        try:
            number_journal = int(input(f'Введите номер записи, которую хотите изменить (число от 1 до {len(data)-1}): '))
        except ValueError as e:
            print('Введены неверные данные')
        else:
            while number_journal >= len(data) or number_journal < 1:
                print(f'Введите число от 1 до {len(data)-1}')
                try:
                    number_journal = int(input("Введите номер записи, которую хотите изменить:"))
                except ValueError as e:
                    print('Введены неверные данные')
                
            change_line(data, number_journal)
            flag = False

def delete_data():
    flag = True
    while flag:
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
        try:
            number_journal = int(input(f'Введите номер записи, которую хотите удалить (число от 1 до {len(data)-1}): '))
        except ValueError as e:
            print('Введены неверные данные')
        else:
            while  len(data) <= number_journal  or number_journal < 1 :
                print(f'Введите число от 1 до {len(data)-1}): ')
                try:
                    number_journal = int(input(f"Введите номер записи, которую хотите удалить (число от 1 до {len(data)-1}):"))
                except ValueError as e:
                    print('Введены неверные данные')
            countID = data[number_journal].split(';')[0] 
            title = data[number_journal].split(';')[1]
            note = data[number_journal].split(';')[2]
            date = data[number_journal].split(';')[3]
            titleCSV = data[0].split(';')   
            answer = input(f'{titleCSV[0]}: {countID}\n'
                        f'{titleCSV[1]}: {title}\n'
                        f'{titleCSV[2]}: {note}\n'
                        f'{titleCSV[3][:-1]}: {date}\n'
                        'Удалить данную запись (да / нет)?:')
            
            while answer != 'да' and answer!='нет':
                answer = input("Введены неверные значения, напишите 'да' или 'нет': ")
            if answer == "да":
                if number_journal == len(data)-1:  
                    data = data[:number_journal+1]
                else:
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
                print('Запись успешно удалена.\n')
                flag = False

def print_ID():
    flag = True
    while flag:    
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
        try:
            number_journal = int(input(f'Введите номер записи, которую вывести (число от 1 до {len(data)-1}): '))
        except ValueError as e:
            print('Введены неверные данные')
        else:
            while number_journal >= len(data) or number_journal < 1:
                print(f'Введите число от 1 до {len(data)-1}')
                try:
                    number_journal = int(input(f"Введите номер записи, которую вывести (число от 1 до {len(data)-1}):"))
                except ValueError as e:
                    print('Введены неверные данные')
            countID = data[number_journal].split(';')[0] 
            title = data[number_journal].split(';')[1]
            note = data[number_journal].split(';')[2]
            date = data[number_journal].split(';')[3]
            titleCSV = data[0].split(';')   
            print(f'{titleCSV[0]}: {countID}\n'
                f'{titleCSV[1]}: {title}\n'
                f'{titleCSV[2]}: {note}\n'
                f'{titleCSV[3][:-1]}: {date}\n')   
            flag = False

def print_filter_date():
    flag = True
    while flag: 
        with open('data.csv', 'r', encoding='utf-8') as file:
            data = list(file.readlines())
        try:
            year = int(input('Выведите год:'))
            month = int(input('Введите месяц:'))
            day = int(input('Введите день:'))
            filter_date = datetime.datetime(year, month, day)
        except ValueError as e:
            print('Введены неверные данные')
        else:
        
            command = input('Какие записи вы хотите увидеть?\n'
                    f'1. Найти записи от {year}-{month}-{day}.\n'
                    f'2. Найти записи сделанные ранее {year}-{month}-{day}.\n'
                    f'3. Найти записи сделанные позже {year}-{month}-{day}.\n'
                    'Введите номер команды: ')
            while command != "1" and command != "2" and command != "3":
                command = input('Введите 1,2 или 3: ')
            countNote = 0
            for i in range(1, len(data)):
                data_time = data[i].split(';')[3]
                data_date = data_time.split(" ")[0]
                data_date_split = data_date.split('-')
                note_date = datetime.datetime(int(data_date_split[0]), int(data_date_split[1]), int(data_date_split[2]))
                countID = data[i].split(';')[0] 
                title = data[i].split(';')[1]
                note = data[i].split(';')[2]
                date = data[i].split(';')[3]
                titleCSV = data[0].split(';')    
                if command == '1':
                    if note_date == filter_date:
                        print(f'{titleCSV[0]}: {countID}\n'
                            f'{titleCSV[1]}: {title}\n'
                            f'{titleCSV[2]}: {note}\n'
                            f'{titleCSV[3][:-1]}: {date}\n')
                        countNote +=1  
                elif command == '2':
                    if note_date < filter_date:
                        print(f'{titleCSV[0]}: {countID}\n'
                            f'{titleCSV[1]}: {title}\n'
                            f'{titleCSV[2]}: {note}\n'
                            f'{titleCSV[3][:-1]}: {date}\n')
                        countNote +=1  
  
                elif command == '3':
                    if note_date > filter_date:
                        print(f'{titleCSV[0]}: {countID}\n'
                            f'{titleCSV[1]}: {title}\n'
                            f'{titleCSV[2]}: {note}\n'
                            f'{titleCSV[3][:-1]}: {date}\n')
                        countNote +=1  
            print(f'Найдено записей: {countNote}  из {len(data)-1}')
            flag = False

                

        

            
