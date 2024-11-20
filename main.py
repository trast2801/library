class Book:
    _counter = 0  # формирует уникальный номер книги

    def __init__(self, title: str, author: str,
                 year:str, status: str):
        Book._counter += 1
        self.id = Book._counter
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @property
    def instance_count(self):
        ''' статический метод счетчик коли-ва созданный объектов'''
        return (Book._counter)

    def change_status(self, id, new_status):
        self.status = new_status

    def send_id(self):
        return self.id

    def send_record_book(self, id):
        '''
         выводит атрибуты  книг с их id, title, author, year и status
        '''
        return (f"id = {self.id}! автор {self.author}! название: {self.title}! год выпуска {self.year}!"
                f" статус: {self.status} ")

    def send_record_book_wihtout_id(self, id):
        '''
         выводит атрибуты  книг с их id, title, author, year и status
        '''
        return (f"!автор {self.author}! название: {self.title}! год выпуска {self.year}!"
                f" статус: {self.status} ")

    def ret_name(self):
        return self.title


def add_book(library):
    ''' Добавляет записи в хранилище'''
    name = 0
    record = input("Введите через запятую следущую информацию:\n"
                   "название книги, автор, год издания: \n")
    record = record.split(",")
    # if len(record) < 3:
    #     print("\nОшибка - должно быть так: название книги, автор, год издания\n")
    #     return library
    # title = record[0]
    # author = record[1]
    # god = record[2]
    status = "в наличии"
    # ниже строки отладки - удалить
    name += 1
    title = "название" + str(name)
    author = "автор" + str(name)
    god = name
    #
    library.append(Book(title, author, god, status))

    return library


def del_book(id: int, library):
    ''' удаляет запись о книге по ID, если id не существует генерит исключение'''
    result_search = None
    try:
        for i in range(len(library)):
            if int(id) == library[i].send_id():
                library.pop(i)
                return library
        if result_search == None:
            raise ValueError ("Книги с таким ID - нет")
    except ValueError as err:
        print (err)
    return library

def change_stat(id: int, library, status: str):
    ''' меняет статус в записи о книге по ID, если id не существует генерит исключение'''
    result_search = None
    try:
        for i in range(len(library)):
            if int(id) == library[i].send_id():
                library[i].change_status(id, status)
                return library
        if result_search == None:
            raise ValueError ("Книги с таким ID - нет")
    except ValueError as err:
        print (err)
    return library

def find_book(str_for_search: str, library):
    spisok = [] #результат поиска
    for i in range(len(library)):
        if str_for_search in library[i].send_record_book_wihtout_id(library[i].instance_count):
            spisok.append(library[i].send_record_book(library[i].instance_count))
    return spisok
def get_id():
    '''функция проверяет id на соответстиве числу'''
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

if __name__ == "__main__":

    library = [] # Хранилище объектов Book
    print("Добро пожаловать в библиотеку")

    while True:
        choice = input("\nВыберите следующее действие (для выбора нажмите соответствующую цифру и Enter):\n"
                       "     1. Добавить книгу \n"
                       "     2. Удалить книгу \n"
                       "     3. Найти книгу\n"
                       "     4. получить список всех книг\n"
                       "     5. Изменить статус книги (в наличии или выдана)\n"
                       "     6. Закончить работу \n")

        if choice == "6":
            print(" Спасибо что воспользовались нашим сервисом, до следующих встреч")
            break
        elif choice == "1":
            library = add_book(library)
        elif choice == "2":
            ch = get_id()
            library = del_book(str(ch), library)
        elif choice == "3":
            ch = input("Введите строку поиска: название или фильм или год\n")
            res = find_book(ch,library)
            if len(res) == 0:
                print ("Ничего не найдено")
            else:
                for k in res:
                    print (k)

        elif choice == "4":
            # вывод в консоль перечень всех книг
            for i in range(len(library)):
                print(library[i].send_record_book(library[i].instance_count))
        elif choice == "5":
            id = get_id()
            ch = input("Изменить статус книги\n 1 - в наличии \n 0 - выдана \n")
            try:
                if ch == "1":
                    status = "в наличии"
                elif ch == "0":
                    status = "выдана"
                elif ch != "1" or ch != "0":
                    raise ValueError ("Статус имеет только значение 1 или 0 ")
            except ValueError as err:
                print(err)
            else:
                change_stat(id, library, status)



