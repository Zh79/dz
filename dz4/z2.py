# Напишите функцию для транспонирования матрицы


def trans_matr(matr):
    zip_rows = zip(*matr)
    trans = [list(row) for row in zip_rows]
    return trans


matr = [[1, 2, 3], [4, 5, 6]]
print(trans_matr(matr))
