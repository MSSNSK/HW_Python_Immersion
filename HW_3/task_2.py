# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


import string


txt = '''
Россия - священная наша держава,
Россия - любимая наша страна.
Могучая воля, великая слава -
Твоё достоянье на все времена!

Славься, Отечество наше свободное,
Братских народов союз вековой,
Предками данная мудрость народная!
Славься, страна! Мы гордимся тобой!

От южных морей до полярного края
Раскинулись наши леса и поля.
Одна ты на свете! Одна ты такая -
Хранимая Богом родная земля!

Славься, Отечество наше свободное,
Братских народов союз вековой,
Предками данная мудрость народная!
Славься, страна! Мы гордимся тобой!

Широкий простор для мечты и для жизни
Грядущие нам открывают года.
Нам силу даёт наша верность Отчизне.
Так было, так есть и так будет всегда!

Славься, Отечество наше свободное,
Братских народов союз вековой,
Предками данная мудрость народная!
Славься, страна! Мы гордимся тобой!
'''

text = txt.translate(str.maketrans('', '', string.punctuation)).lower().split()
res = {}
SHOW_LIMIT = 10

for word in text:
    res[word] = res.get(word, 0) + 1

most_frequent_words = [i for i, j in sorted(res.items(), key=lambda item: item[1], reverse=True)[:SHOW_LIMIT]]
print(*most_frequent_words, sep='\n')
