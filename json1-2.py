from zipfile import ZipFile
import os


def human_read_format(n):
    list_1 = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПТ"]
    for i in range(7):
        if n / 1024 < 1:
            return str(n) + list_1[i]
        else:
            n = round(n / 1024)


name = "input.zip"

with ZipFile(name) as zipi:
    zip_files = zipi.namelist()
    for i in zip_files:
        flag = 1
        if i[-1] == "/":
            flag = 0
        list_of_path = i.rstrip('/').split("/")
        if flag:
            print("  " * (len(list_of_path) - 1) + list_of_path[-1] +
                  " " + os.path.getsize(name + "/" + i))
        else:
            print("  " * (len(list_of_path) - 1) + list_of_path[-1])