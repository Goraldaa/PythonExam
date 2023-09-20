def title_data():
    flag = True
    while flag:
        title = input('Введите заголовок заметки. Не используйте символ ";": ')
        flag = False
        if ';' in title:
            print("Не используйте в названии символ ';'")
            flag = True
    print("Данные успешно сохранены")
    return title


def note_data():
    flag = True
    while flag:
        note = input('Введите тело заметки. Не используйте символ ";": ')
        flag = False
        if ';' in note:
            print("Не используйте в тексте символ ';'")
            flag = True
    print("Данные успешно сохранены")
    return note

