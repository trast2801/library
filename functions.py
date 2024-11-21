import classes


def input_data() -> str:
    record = input("Введите через запятую следущую информацию:\n"
                   "название книги, автор, год издания: \n")
    record = record.split(",")
    return record

def add_book(record, library: list) -> list:
    ''' Добавляет записи в хранилище'''


    if len(record) < 3:
        print("\nОшибка - должно быть так: название книги, автор, год издания\n")
        return library
    title = record[0]
    author = record[1]
    god = record[2]
    status = "в наличии"
    # ниже строки отладки - удалить
    # name += 1
    # title = "название" + str(name)
    # author = "автор" + str(name)
    # god = name
    #
    library.append(classes.Book(title, author, god, status))

    return library


def del_book(id: int, library: list) -> list:
    ''' удаляет запись о книге по ID, если id не существует генерит исключение'''
    result_search = None
    try:
        for i in range(len(library)):
            if int(id) == library[i].send_id():
                library.pop(i)
                return library
        if result_search == None:
            raise ValueError("Книги с таким ID - нет")
    except ValueError as err:
        print(err)
    return library


def change_stat(id: int, library: list, status: str) -> list:
    ''' меняет статус в записи о книге по ID, если id не существует генерит исключение'''
    result_search = None
    try:
        for i in range(len(library)):
            if int(id) == library[i].send_id():
                library[i].change_status(id, status)
                return library
        if result_search == None:
            raise ValueError("Книги с таким ID - нет")
    except ValueError as err:
        print(err)
    return library


def find_book(str_for_search: str, library: list) -> list:
    spisok = []  # результат поиска
    for i in range(len(library)):
        if str_for_search in library[i].send_record_book_wihtout_id(library[i].instance_count):
            spisok.append(library[i].send_record_book(library[i].instance_count))
    return spisok


def get_id() -> int:
    '''функция проверяет id на соответствие числу'''
    ch = input("Введите номер ID:")
    if ch == None:
        print("Вы не ввели ID номер книги \n")
    else:
        try:
            ch = int(ch)
        except ValueError:
            print("Номер должен быть числом \n")
        else:
            return ch


def write_data(filename: str, library: list) -> None:
    '''функция сохраняет рузельтат работы в файле'''
    spisok = []
    for i in range(len(library)):
        spisok.append(library[i].send_record_book_wihtout_id(library[i].instance_count))
    with open(filename, encoding="UTF-8", mode="w") as file:
        file.writelines(spisok)
    file.close()


def load_data(filename: str) -> list:
    '''загружает данные из внешнего хранилища. Если файла не существует то его создает'''

    with open(filename, encoding="UTF-8") as f:
        library = []
        file = f.readlines()
        if len(file) == 0:
            return library
        else:
            for i in file:
                result = i.split("~")
                library.append(classes.Book(result[0], result[1], result[2], result[3].strip()))

    f.close()
    print("данные загружены успешно")
    return library

def list_all(library: list):
    for i in range(len(library)):
        print(library[i].send_record_book(library[i].instance_count))
