

from model import change_line, create, delete_line, read
from view import print_db, record_id

phonebook = {}
phonebook_last_id = 0


def get_user_data() -> dict:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    discrip = input('Введите должность: ')
    return surname, name, phone, discrip

def export_db(db: dict, filepath, delimeter: str = "#" ) -> None:
    with open(filepath, mode= 'w', encoding= 'utf-8' ) as file:
        for idx, data in db.items():
            file.write(f"{data['surname']}{delimeter}{data['name']}{delimeter}{data['phone']}{delimeter}{data['discrip']}\n")

def get_file_name() -> str:
    return input('Введите имя файла: ')

def get_fillter_name() -> str:
    return input('Введите фильтр: ') 

def import_db(db: dict, filepath: str, last_id: int, delimeter: str = "#" ) -> tuple:
    with open(filepath, mode= 'r', encoding= 'utf-8' ) as file:
        for line in file:
            _data = line.strip().split(delimeter)
            db[last_id] = {'surname': _data[0], 'name': _data[1], 'phone': _data[2], 'discrip':_data[3]}
            last_id +=1
               
    return db, last_id

def menu(db: dict, last_id: str) -> None:
    while True:
        print('Возможные действие:')
        print('1 - Создать запись;')
        print('2 - Вывести данные;')
        print('3 - Экспортировать данные в файл;')
        print('4 - Импортировать данные из файла;')
        print('5 - Найти запись по фильтру;')
        print('6 - Удалить запись;')
        print('7 - Заменить значение в записи;')
        print('8 - Выход.')
        user_input = input('Введите действие: ')
        if user_input == '1':
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        if user_input == '2':
            print_db(db)        
        if user_input == '3':
            export_db(db, get_file_name())
        if user_input == '4':
            db, last_id = import_db(db, get_file_name(), last_id)
        if user_input == '5':
            find_id = read(db, get_fillter_name())
            record_id(db, find_id)
        if user_input == '6':
            find_id = read(db, get_fillter_name())
            delete_line(db, find_id)
        if user_input == '7':
            find_id = read(db, get_fillter_name())
            change_line(db, find_id)

        elif user_input == '8':
            break


menu(phonebook, phonebook_last_id)