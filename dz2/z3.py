# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

x = input("Введите дробь вида a/b: ")
y = input("Введите дробь вида c/d: ")

x = x.split("/")
y = y.split("/")

s = ['', '']
m = ['', '']

s[0] = int(x[0]) * int(y[1]) + int(x[1]) * int(y[0])
s[1] = int(x[1]) * int(y[1])

m[0] = int(x[0]) * int(y[0])
m[1] = int(x[1]) * int(y[1])


def decrease(a, b):
    if b < a:
        a, b = b, a
    elif b == a:
        return 1

    b1 = b
    a1 = a
    ost = b1 % a1

    while True:
        if ost == 0:
            return a1
        a1 = a1 % ost
        if a1 == 0:
            return ost
        ost = b1 % a1

decr_summ = decrease(s[0], s[1])
decr_mult = decrease(m[0], m[1])

print(f'{int(s[0] / decr_summ)}/{int(s[1] / decr_summ)}')
(print(f'{m[0] / decr_mult}/{m[1] / decr_mult}')) if decr_mult != 1 else print(1)
