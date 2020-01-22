import datetime

class Period:
    def __init__(self):
        pass

    def __enter__(self):
        self.date_start = datetime.datetime.now()
        print(f"время начала работы кода: {self.date_start}")
        return self.date_start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.date_finish = datetime.datetime.now()
        self.period = self.date_finish - self.date_start
        print(f"время окончания работы кода: {self.date_finish}")
        print(f"продолжительность работы кода: {self.period}")

if __name__ == '__main__':

    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

    #добавление нового документа (a)
    def add_document(doc_list,document_reference):
        document = 0
        for key in document_reference:
            if doc in directories[key]:
                document = 1

        if document == 0:
            type_doc=str(input("Введите тип документа: "))
            name=str(input("Введите имя владельца документа: "))
            num_shelf=str(input("Введите номер полки в справочнике документов: "))

            if num_shelf not in document_reference.keys():
                document_reference[num_shelf] = []

            document_reference[num_shelf].append(doc)

            doc_list.append({"type": type_doc, "number": doc, "name": name})
        else:
            print("Документ уже добавлен в справочник")

    print("a – команда, которая добавит новый документ в каталог и в перечень полок" "\nq - выход")

    with Period() as x:

        while True:
            print()
            user_input=str(input("Введите команду:"))
            if user_input == "a":
                doc=str(input("Введите номер документа: ")) 
                add_document(documents,directories)

                print("Справочник документов")
                for document in documents:
                    print(document)

                print()
                print("Справочник месторасположения документов")
                for shelves in directories:
                    print (shelves, directories[shelves])

            elif user_input == "q":
                break