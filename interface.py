from file_handling import create_file, write_file, read_file, remove_row, copy_data
from os.path import exists


def interface():
    print("Добрый день!\nЭто программа для работы с телефонными справочниками.\n"
          "В ней есть следующие команды:\n1. Записать в файл: w\n2. Прочитать файл: r\n"
          "3. Удалить строку из справочника: d\n4. Копировать данные в новый файл: c\n"
          "5. Выйти: q")
    file_name = input('Введите имя файла, с которым хотите работать: ')
    file_name += '.csv'
    while not exists(file_name):
        variable = input('Такого файла нет. Создать новый (y/n), выход (q): ')
        while variable not in 'ynq':
            variable = input('Выберите "y", "n" или "q"!!! ')
            continue
        if variable == 'y':
            create_file(file_name)
        elif variable == 'n':
            file_name = input('Введите имя файла: ')
            file_name += '.csv'
            continue
        elif variable == 'q':
            break
    else:
        while True:
            command = input('Введите команду: ')
            while command not in 'qwrdc':
                command = input('Такой команды нет, введите верную команду: ')
                continue
            if command == 'q':
                break
            elif command == 'w':
                write_file(file_name)
            elif command == 'r':
                print(*read_file(file_name))
            elif command == 'd':
                remove_row(file_name)
            elif command == 'c':
                copy_data(file_name)
