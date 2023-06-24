# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
#
friend = {
    '1': ('palatka', 'spalnik', 'fonar', 'gas gorelka'),
    '2': ('palatka', 'spalnik', 'tent', 'perchatki'),
    '3': ('palatka', 'film', 'tent', 'fonar'),
}

l = list()
for k, v in friend.items():
    l.append(friend[k])

vse = []
for i in range(len(l)):
    for j in range(len(l[i])):
        vse.append(l[i][j])
vse = set(vse)
print(f"Друзья взяли {vse}")

for k in friend:
    s1 = set(friend[k])
    for i in friend:
        if i == k:
            None
        else:
            s2 = set(friend[i])
            s1 = s1 - s2

    print(f"Уникальные вещи друга {k} {s1}")

for k in friend:
    s1 = set(friend[k])
    s3 = vse
    for i in friend:
        if i != k:
            s2 = set(friend[i])
            s3 = s3 & s2


    print(f"Вещи которые есть у всех кроме {k} друга {s3 - s1}")

# print(f"Вещи которые есть у всех кроме первого друга {v2 & v3 - v1}")
# print(f"Вещи которые есть у всех кроме второго друга {v1 & v3 - v2}")
# print(f"Вещи которые есть у всех кроме третьего друга {v1 & v2 - v3}")
