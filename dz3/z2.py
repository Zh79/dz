# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

spisok = ['с', 'п', 'и', 'с', 'о', 'к', 'с', 'о', 'с', 'и', 'с', 'о', 'к', 1, 1, 2]

dikt = {}

for i in spisok:
    dikt[i] = dikt.get(i, 0) + 1

res = []
for k in dikt:
    if dikt[k] == 2: # не понятно дублирующимися это которых только двое или больше 1
        res.append(k)

print(res)