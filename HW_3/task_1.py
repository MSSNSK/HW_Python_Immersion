# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


lst_items = [11, 'два', 55, 'один', 11, 'три', 33, 'два', 55, 'один', 77, 77, 77, 'ТРИ']
lst_duplicate = []
VALUE_DUPLICATE = 2

for i in lst_items:
    if lst_items.count(i) == VALUE_DUPLICATE:
        lst_duplicate.append(i)
print(list(set(lst_duplicate)))
