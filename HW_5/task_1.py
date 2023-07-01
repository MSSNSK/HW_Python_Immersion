# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def path_to_file(lnk):
    *parts_path, file_name, file_ext = lnk.replace('.', '\\').split('\\')
    yield 'Путь к файлу => ' + '\\'.join(parts_path) + '\\'
    yield 'Имя файла => ' + file_name
    yield 'Расширение файла => ' + file_ext


link = 'G:\Study\GeekBrains\Python\Iterators and generators.pdf'
print(*path_to_file(link), sep='\n')
