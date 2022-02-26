dos_list = {}  # досье
fio_list = []  # ФИО
pos_list = []  # должность
n = 0
i = 0  # индекс в fio_list
j = 0  # индекс в pos_list


def AddDossier(index, fio_value, dol_value):
    dos_list[index] = (fio_value + ' ' + '-' + ' ' + dol_value)


def AppendFio(surname_value, name_value, patronymic_value):
    fio_list.append(surname_value + ' ' + name_value + ' ' + patronymic_value)


def AppendPos(work_value):
    pos_list.append(work_value)


def OutputDossier(list_value):
    for key, value in list_value.items():
        print('{0}: {1}'.format(key, value))


def DeleteEmployee(list_view):
    print('Выберите порядковый номер сотрудника:')
    OutputDossier(dos_list)
    delete_number = input('Введите номер сотрудника, которого хотите удалить: ')
    del list_view[delete_number]
    print('Сотрудник успешно удалён:')
    if len(list_view) > 0:
        OutputDossier(list_view)
    else:
        print('Вы удалили последнего сотрудника, список пуст')


def SearchEmployee(search_list):
    if len(search_list) > 0:
        print('Для начала поиска по фамилии, выберите нужную фамилию из списка:')
        OutputDossier(search_list)
        search_number = input('Введите выбранную фамилию из списка: ')
        for key, value in search_list.items():
            if search_number not in value:
                print('Такой фамилии нет')
            else:
                print('{0}: {1}'.format(key, value))
                continue
    else:
        print('Сейчас список сотрудников пуст, поиск не возможен')


while True:
    print('Меню программы:')
    print('1 - Добавить досье')
    print('2 - Вывести досье')
    print('3 - Удалить досье')
    print('4 - Поиск по фамилии')
    print('5 - Выход из программы')
    print('Выберите пункт меню:')
    num_item = int(input())
    if num_item == 1:
        n += 1
        num_index = str(n)
        while True:
            surname_s = str(input('Фамилия сотрудника: '))
            first_let = surname_s[0]
            if surname_s.isalpha() and 7 <= len(surname_s) <= 14 and first_let.isupper():
                while True:
                    name_s = str(input('Имя сотрудника: '))
                    first_let_name = name_s[0]
                    if name_s.isalpha() and 2 <= len(name_s) <= 10 and first_let_name.isupper():
                        while True:
                            patronymic_s = str(input('Отчество сотрудника: '))
                            first_let_patr = patronymic_s[0]
                            if patronymic_s.isalpha() and 9 <= len(patronymic_s) <= 16 and first_let_patr.isupper():
                                while True:
                                    work_s = str(input('Должность сотрудника: '))
                                    first_let_w = work_s[0]
                                    if work_s.isalpha() and 6 <= len(work_s) <= 30 and first_let_w.isupper():
                                        AppendFio(surname_s, name_s, patronymic_s)
                                        AppendPos(work_s)
                                        AddDossier(num_index, fio_list[i], pos_list[j])
                                        print('Сотрудник успешно добавлен в базу данных')
                                        i += 1
                                        j += 1
                                        break
                                    else:
                                        print('Не верный формат записи, пример: -> "Главный менеджер"')
                                break
                            else:
                                print('Не верный формат записи, пример: -> "Александрович"')
                        break
                    else:
                        print('Не верный формат записи, пример: -> "Александр"')
                break
            else:
                print('Не верный формат записи, пример: -> "Александров"')
        continue
    elif num_item == 2:
        if len(dos_list) == 0:
            print('Список сотрудников сейчас пуст, пожалуйста, добавьте нового сотрудника через меню "1"')
        else:
            print('Список сотрудников в базе данных:')
            OutputDossier(dos_list)
        continue
    elif num_item == 3:
        if len(dos_list) == 0:
            print('Список сотрудников сейчас пуст, невозможно удалить кого-либо')
        else:
            DeleteEmployee(dos_list)
        continue
    elif num_item == 4:
        SearchEmployee(dos_list)
    elif num_item == 5:
        print('Всего хорошего')
        break



