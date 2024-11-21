import functions

DATABASE_TXT = "database/base.txt" #место постоянного хранения данных

if __name__ == "__main__":

    library = []  # Хранилище объектов Book
    print("Добро пожаловать в библиотеку\n")
    library = functions.load_data(DATABASE_TXT)
    while True:
        choice = input("\nВыберите следующее действие (для выбора нажмите соответствующую цифру и Enter):\n"
                       "     1. Добавить книгу \n"
                       "     2. Удалить книгу \n"
                       "     3. Найти книгу\n"
                       "     4. Получить список всех книг\n"
                       "     5. Изменить статус книги (в наличии или выдана)\n"
                       "     6. Закончить работу \n"
                       "     7. Тестирование\n")

        if choice == "1":
            record = functions.input_data()
            library = functions.add_book(record, library)

        elif choice == "2":
            ch = functions.get_id()
            library = functions.del_book(str(ch), library)

        elif choice == "3":
            ch = input("Введите строку поиска: название или фильм или год\n")
            res = functions.find_book(ch, library)
            if len(res) == 0:
                print("Ничего не найдено")
            else:
                for k in res:
                    print(k)

        elif choice == "4":
            # вывод в консоль перечень всех книг
            # for i in range(len(library)):
            #     print(library[i].send_record_book(library[i].instance_count))
            functions.list_all(library)

        elif choice == "5":
            id = functions.get_id()
            ch = input("Изменить статус книги\n 1 - в наличии \n 0 - выдана \n")
            try:
                if ch == "1":
                    status = "в наличии"
                elif ch == "0":
                    status = "выдана"
                elif ch != "1" or ch != "0":
                    raise ValueError("Статус имеет только значение 1 или 0 ")
            except ValueError as err:
                print(err)
            else:
                functions.change_stat(id, library, status)

        elif choice == "6":
            functions.write_data(DATABASE_TXT, library)
            print(f"Результат работы сохранен в {DATABASE_TXT}")
            print(" Спасибо что воспользовались нашим сервисом, до следующих встреч")
            break
        elif choice == "7":
            functions.test_add(library)
