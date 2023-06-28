# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые
# переменные без s на конце.


def sort_names_variables(var_dict: dict):
    MIN_LEN_VAR = 1
    SEARCH_EL_OBJ = -1
    var_nms_srt = [i for i in var_dict if len(i) > MIN_LEN_VAR and i[SEARCH_EL_OBJ] == 's']
    for j in var_nms_srt:
        var_dict[j[:SEARCH_EL_OBJ]] = var_dict[j]
        var_dict[j] = None


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = 'NoName', 'OtherName', 'NewName'
sx = 42

print(f'Исходные переменные:\n'
      f'{datas = },\n{s = },\n{names = },\n{sx = };\n')
sort_names_variables(globals())
print(f'Итоговые переменные:\n'
      f'{datas = },\n{s = },\n{names = },\n{sx = };\n\n'
      f'{data = },\n{s = },\n{name =},\n{sx = }.')
