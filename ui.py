from logger import input_data, print_data, changes_data, delete_data, print_ID, print_filter_date

def interface():
    command = -1
    while command != 7:
        print('Доброго времени суток! Вы попали в консольное приложение Заметки! Что Вы хотите сделать?\n'
              '1. Создать новую заметку\n'
              '2. Удалить существующую заметку\n'
              '3. Изменить существующую заметку\n'
              '4. Вывести все заметки\n'
              '5. Найти заметку по номеру\n'
              '6. Фильтр по дате\n'
              '7. Выход')
        try:
            command = int(input("Введите номер операции: "))
        except ValueError as e:
            print('Введены неверные данные')
        else:
            
            while command < 1 or command > 7:
                print('Введите число от 1 до 7')
                try:
                    command = int(input("Введите номер операции: "))
                except ValueError as e:
                    print('Введены неверные данные')
                    

            if command == 1:
                input_data()
            elif command == 2:
                delete_data()
            elif command == 3:
                changes_data()
            elif command == 4:
                print_data()
            elif command == 5:
                print_ID()
            elif command == 6:
                print_filter_date()
            elif command == 7:
                print("Спасибо, что воспользовались нашими услугами. Всего доброго!")
        