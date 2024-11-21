import functions

DATABASE_TXT = "database/base_test.txt"


def check_del(library: list):
    before_del = len(library)
    assert len(functions.del_book(1, library)) == before_del - 1 , "запись не удалена: тест не пройден"
    print ("удаление -  успешно")

def check_change_status(library: list):
    before = library[0].get_status()
    functions.change_stat(1, library, "выдана")
    after = library[0].get_status()
    assert before != after, "статус не изменился: тест не пройден"
    print ("смена статуса -  успешно")

def check_find(library: list):
    spisok = functions.find_book("Буратино", library)
    assert len(spisok) == 1, 'тест не пройден, запись не найдена'
    spisok = functions.find_book("Милосердие", library)
    assert len(spisok) == 0, 'тест не пройден, список не пустой'
    print("поиск -  успешно")

def check_add(library: list):
    record = ["Название","Автор","2000"]
    before = len(library)
    after = len(functions.add_book(record, library))
    assert after == before + 1, "Запись не добавлена, тест не пройден"
    print ("добавление записи -  успешно")

if __name__ == "__main__":
    library = functions.load_data(DATABASE_TXT)


    check_change_status(library)
    check_find(library)
    check_add(library)
    check_del(library)
    print("тесты закончены")
