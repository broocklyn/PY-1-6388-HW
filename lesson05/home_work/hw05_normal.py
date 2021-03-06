
__author__ = 'Учускин Павел Валерьевич'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import hw05_easy as hw5
import os


def msg():
    print("Вас приветствует программа для работы с папками текущей директории\n"
              "Введите 1, чтобы перейти в папку\n"
              "Введите 2, чтобы просмотреть содержимое текущей папки\n"
              "Введите 3, чтобы удалить папку\n"
              "Введите 4, чтобы создать папку\n")


def content():
    print("В каталоге содержатся следующие папки: \n"  
          f"{hw5.show_f()}")


content()

while True:

    run = input("Начнем? (Y/N): ")

    if run.lower() == "y":
        msg()
        question = input("Введите цифру, соответствующую Вашему выбору ")
        if question == "1":
            name_dir = input("Введите название папки для перехода: ")
            hw5.move(name_dir)
            input(f"Сейчас вы находитесь в {os.getcwd()}")

        elif question == "2":
            print(f"Вы находитесь в папке {name_dir}")
            print(hw5.show_dc())

        elif question == "3":
            a = os.path.dirname(os.path.realpath(__file__))
            os.chdir(a)
            name_del = input("Введите название папки, которую желаете удалить: ")
            hw5.delete(name_del)

        elif question == "4":
            a = os.path.dirname(os.path.realpath(__file__))
            os.chdir(a)
            name_create = input("Введите название папки, которую желаете создать: ")
            hw5.create(name_create)

        else:
            print("Ошибка ввода")
            pass

    elif run.lower() == "n":
        print("Работа программы окончена")
        break

    else:
        print("Ошибка")

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из __easy.py
