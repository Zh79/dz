# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


code_number = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'F')

x = int(input("Введите число: "))
print(hex(x))

znak = ''
if x < 0:
    x = x * -1
    znak = '-'

code = []

while x > 0:
    if x < 16:
        code.append(x)
        break
    code.append(x // 16)
    x = x - (x // 16) * 16

print(znak + '0x', end='')
for i in range(len(code)):
    print(code_number[code[i]], end='')
