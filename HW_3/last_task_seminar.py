# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
#
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
#
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
#
# Код должен расширяться на любое большее количество друзей.


friends_objects = {
    'Юрий': ('Палатка', 'Термос', 'Спички', 'Консервы', 'Уголь'),
    'Георгий': ('Палатка', 'Котелок', 'Соль', 'Крупа', 'Мангал'),
    'Евгений': ('Спальный мешок', 'Котелок', 'Спички', 'Картофель', 'Баран')
}

all_frnds_obj = set()
uniq_frnds_obj = {}
except_one_obj = {}

for friend in friends_objects:
    uniq_obj = set(friends_objects[friend])
    except_obj = set()
    for next_friend in friends_objects:
        if next_friend != friend:
            uniq_obj -= set(friends_objects[next_friend])
            if not except_obj:
                except_obj |= (set(friends_objects[next_friend]))
            else:
                except_obj.intersection_update(set(friends_objects[next_friend]))
    all_frnds_obj |= set(friends_objects[friend])
    uniq_frnds_obj[friend] = uniq_obj
    except_one_obj[friend] = except_obj - set(friends_objects[friend])

print(f'''Все вещи: {all_frnds_obj};
Уникальные вещи: {uniq_frnds_obj};
Вещи, которые есть у всех друзей, кроме одного: {except_one_obj}.''')
