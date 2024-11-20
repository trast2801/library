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

    def add_book(self):
        '''
        Пользователь вводит title, author и year, после чего книга
        добавляется в библиотеку с уникальным id и статусом “в наличии”
        '''
        pass

    def del_book(self, id):
        ''' Пользователь вводит id книги, которую нужно удалить'''
        pass

    def find_book(self, id: int, author: str, year: int):
        '''Пользователь может искать книги по title, author или year'''
        pass

    def change_status(self, id):
        '''
        Пользователь вводит id книги и новый статус (“в наличии”
        или “выдана”).
        '''
        pass

    def send_record_book(self, id):
        '''
         выводит атрибуты  книг с их id, title, author, year и status
        '''
        return (f"id = {self.id}! автор {self.author}! название: {self.title}! год выпуска {self.year}!"
                f" статус: {self.status} ")

    def ret_name(self):
        return self.title


if __name__ == "__main__":

    library = []
    print("Добро пожаловать в библиотеку")
    name = 0
    while True:
        choice = input("Выберите следующее действие (для выбора нажмите соответствующую цифру и Enter):\n"
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
            record = input("Введите через запятую следущую информацию:\n"
                           "название книги, автор, год издания\n")
            record = record.split(",")
            print(record)
            if len(record) < 3:
                print("Ошибка - должно быть так: название книги, автор, год издания")

            title = record[0]
            author = record[1]
            god = record[2]
            status = True
            # ниже строки отладки - удалить
            name += 1
            title = "название" + str(name)
            author = "автор" + str(name)
            god = name

            #
            library.append(Book(title, author, god, status))

        elif choice == "4":
            for i in range(len(library)):
                print(library[i].send_record_book(library[i].instance_count))
