class Book:
    _counter = 0  # формирует уникальный номер книги

    def __init__(self, title: str, author: str,
                 year: str, status: str):
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
        return (f"id = {self.id}! название: {self.title}! автор {self.author} ! год выпуска {self.year}!"
                f" статус: {self.status} ")

    def send_record_book_wihtout_id(self, id):
        '''
         выводит атрибуты  книг с их id, title, author, year и status для поиска
        '''
        return (f"{self.title}~{self.author}~{self.year}~{self.status}\n")

