import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

#Задание №1

def sort_name(contacts_list):
    try:
        for contcats in contacts_list:
            last_first_surname = (" ".join(contcats[0:3])).split()
            if len(last_first_surname) < 3:
                last_first_surname.append(' ')
            del contcats[0:3]
            contcats.insert(0, last_first_surname[0])
            contcats.insert(1, last_first_surname[1])
            contcats.insert(2, last_first_surname[2])
    except:
        print('Ошибка, в строке отсутствуют два или более поля lastname, firstname, surname!')

# #Задание №2

def sort_phone(contacts_list):
    for phone in contacts_list:
        pattern = r"(\+7|8)?\s*\(*(\d{3})\)*\s*-*(\d{3})-*(\d{2})-*(\d{2})(\s*\(?(доб.)\s*\D?(\d{4})\)?)*"
        substitution = r"+7(\2)\3-\4-\5 \7\8"
        resault = re.sub(pattern, substitution, phone[5])
        del phone[5]
        phone.insert(5, resault)

# #Задание №3

def filling_voids(contacts_list):
    for i in range(1, len(contacts_list)):
        for n in range(i+1, len(contacts_list)):
            if contacts_list[i][0:2] == contacts_list[n][0:2]:
                for empty in range(0, len(contacts_list[i])):
                    if contacts_list[i][empty] == '' or contacts_list[i][empty] == ' ':
                        contacts_list[i][empty] = contacts_list[n][empty]

def delete_double(contacts_list):
    for i in range(1, len(contacts_list)):
        for n in range(i+1, len(contacts_list)):
            if contacts_list[i][0:2] == contacts_list[n][0:2]:
                del contacts_list[n][0:len(contacts_list[i])]
    count = 0
    for index_list in range(len(contacts_list)):
        if contacts_list[index_list] == [] or contacts_list[index_list] == ['']:
            count += 1
    for index_list in range(len(contacts_list)-count+1):
        if contacts_list[index_list] == [] or contacts_list[index_list] == ['']:
            del contacts_list[index_list]

def write_phonebook(contacts_list):
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list)



if __name__ == '__main__':
    sort_name(contacts_list)
    sort_phone(contacts_list)
    filling_voids(contacts_list)
    delete_double(contacts_list)
    write_phonebook(contacts_list)
