class Book:
    _counter = 0  # формирует уникальный номер книги

    def __init__(self, title: str, author: str,
                 year: int, status: bool):
        Book._counter += 1
        self.id = Book._counter
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @property
    def instance_count(self):
        return (Book._counter)

    def find_book(self, id: int, author: str, year: int):
        '''Пользователь может искать книги по title, author или year'''
        pass

    def change_status(self, id, new_status):
        '''
        Пользователь вводит id книги и новый статус (“в наличии”
        или “выдана”).
        '''
        self.status = new_status
        pass

    def send_id(self):
        return self.id

    def send_record_book(self, id):
        '''
         выводит атрибуты  книг с их id, title, author, year и status
        '''
        return (f"id = {self.id}! автор {self.author}! название: {self.title}! год выпуска {self.year}!"
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
    status = True
    # ниже строки отладки - удалить
    name += 1
    title = "название" + str(name)
    author = "автор" + str(name)
    god = name
    #
    library.append(Book(title, author, god, status))

    return library


def del_book(id: int, library):

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

if __name__ == "__main__":

    library = []
    print("Добро пожаловать в библиотеку")
    name = 0
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
            ch=input("Введите номер ID:")
            if ch == None:
                print ("Вы не ввели ID номер книги \n")
            else:
                try:
                    ch = int(ch)
                except ValueError as err:
                    print ("Номер должен быть числом")
                else:
                    library = del_book(ch, library)
        elif choice == "4":
            # вывод в консоль перечень всех книг
            for i in range(len(library)):
                print(library[i].send_record_book(library[i].instance_count))
