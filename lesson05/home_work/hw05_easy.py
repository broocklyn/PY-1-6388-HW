
__author__ = 'Учускин Павел Валерьевич'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, re, sys, shutil
# Создание директорий

def mk_dir(dir_num):
    a = 1
    b = dir_num + a
    dir_name =[]
    for i in range(a,b):
        dirs = 'dir_'+str(i)
        os.makedirs(dirs)
        dir_name.append(dirs)
    return print(f'Готово, папки созданы: {dir_name}')

# проверяем:

mk_dir(9)

# Удаление директорий

def rm_dir(dirs):
    dirs = ' '.join(dirs)
    dirs_string = re.findall(r'\w\w\w_\d', dirs)
    for i in dirs_string:
        os.rmdir(i)
		
# проверяем:

dirs = os.listdir()
rm_dir(dirs)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
import shutil
import sys

def lst_dir():
    path = os.getcwd()
    return [d for d in os.listdir(path) if os.path.isdir(d)]

a = lst_dir()

print(a)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
shutil.copy(__file__, __file__ + "_copy.py")



#Функции для задания нормал


def show_dc():  # Содержимое текущей папки
    path = os.getcwd()
    return os.listdir(path)


def move(req_dir):  # Перейти в новую папку
    path = f"{req_dir}"
    try:
        os.chdir(path)
    except NameError:
        print("Переход невозможен")
    else:
        print(f"Папка {req_dir} возможна для перехода")


def delete(req_dir):  # Удалить папку
    path = f"{req_dir}"
    try:
        os.rmdir(path)
    except OSError:
        print(f"Ошибка удаления папки {path} ")
    else:
        print("Удаление прошло успешно")


def create(req_dir):  # Создать папку
    path = f"{req_dir}"
    try:
        os.mkdir(path)
    except OSError:
        print(f"Ошибка создания папки {path} ")
    else:
        print("Папка была успешно создана")