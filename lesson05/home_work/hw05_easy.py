
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

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
