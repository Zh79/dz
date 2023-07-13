# Создайте функцию генератор чисел Фибоначчи (см. Википедию)
from functools import reduce

# fib1 = fib2 = 1
# fib = [fib1, fib2 = fib2, fib1 + fib2 for i in range(2, n)] так не сработало

fib = lambda n: reduce(lambda x, y: (x[0] + x[1], x[0]), [(1, 1)] * (n - 2))[0] #только для положительных
print(fib(int(input("Введите число: "))+1))


