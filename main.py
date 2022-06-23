def main():
    full_dict = {}

    num = int(input(f"'1' - Добавить день рождения, '2' - Отыскать день рождения, '3' - Изменить день рождения, '4' - удалить день рождения, '5' - выйти с программы, '6' - посмотреть список: "))

    while num != 5:
        if num == 1:
            get_birthday(full_dict=full_dict)

        if num == 2:
            check_birthday(full_dict=full_dict)
        if num == 3:
            change_birthday(full_dict=full_dict)
        if num == 4:
            delete_birthday(full_dict=full_dict)
        if num == 6:
            print(full_dict)
        num = int(input(
            f"'1' - Добавить день рождения, '2' - Отыскать день рождения, '3' - Изменить день рождения, '4' - удалить день рождения, '5' - выйти с программы, '6' - посмотреть список: "))


def get_birthday(full_dict):

    name = input("Введите имя: ")

    birthday_day = int(input("Введите день рождения: "))
    while birthday_day < 1 or birthday_day > 31:
        birthday_day = int(input("Введите верный день рождения: "))

    birthday_month = int(input("Введите месяц рождения(в числах): "))
    while birthday_month < 1 or birthday_month > 12:
        birthday_month = int(input("Введите верный месяц рождения(в числах): "))

    birthday_year = int(input("Введите год рождения: "))
    while birthday_year < 1800 or birthday_year > 2022:
        birthday_year = int(input("Введите верный год рождения: "))

    full_birthday = f"{birthday_day}.{birthday_month}.{birthday_year}"

    full_dict[name] = full_birthday

    print(full_dict)




def check_birthday(full_dict):
    key_for_bd = input("Введите имя человека, у которого хотите найти дату рождения: ")
    if key_for_bd in full_dict:
        print(f"{key_for_bd} имеет день рождения в -", full_dict[key_for_bd])
    else:
        print("Не могу найти такого человека")


def change_birthday(full_dict):
    key_for_bd = input("Введите имя человека, у которого хотите изменить дату рождения: ")
    if key_for_bd in full_dict:
        birthday_day = int(input("Введите день рождения: "))
        while birthday_day < 1 or birthday_day > 31:
            birthday_day = int(input("Введите верный день рождения: "))

        birthday_month = int(input("Введите месяц рождения(в числах): "))
        while birthday_month < 1 or birthday_month > 12:
            birthday_month = int(input("Введите верный месяц рождения(в числах): "))

        birthday_year = int(input("Введите год рождения: "))
        while birthday_year < 1800 or birthday_year > 2022:
            birthday_year = int(input("Введите верный год рождения: "))

        full_birthday = f"{birthday_day}.{birthday_month}.{birthday_year}"

        full_dict[key_for_bd] = full_birthday

        print(f"{key_for_bd} теперь имеет день рождения в - {full_dict}")
    else:
        print("Не могу найти такого человека")


def delete_birthday(full_dict):
    key_for_bd = input("Введите имя  человека, которого хотите удалить с списка: ")

    if key_for_bd in full_dict:

        full_dict.pop(key_for_bd)

        print("Дата рождения удалена!")
    else:
        print("Не могу найти такого человека")

main()
