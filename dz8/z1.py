# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря
# для заголовков столбца из переданного файла.

import pickle
import csv

d = {"Chisla": [12, 123, 45],
     "Bukvi": ["a", "b", "w"],
     "Imena": ["Ivan", "Petr", "Vasya"]
     }

with open('d.pickle', 'wb') as f:
    pickle.dump(d, f)

with open('d.pickle', 'rb') as f:
    new_d = pickle.load(f)

print(new_d)

with open("csv.csv", mode="w", encoding='utf-8') as w_file:
    k = new_d.keys()
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(k)

    m = []
    for i in new_d:
        m.append(new_d[i])

    zip_rows = zip(*m)
    new_new_d = [list(row) for row in zip_rows]

    for i in range(len(new_new_d)):
        file_writer.writerow(new_new_d[i])
