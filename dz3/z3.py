# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import string

s = 'Public module variables: whitespace -- a string containing all ASCII whitespace ascii_lowercase -- a string containing all ASCII lowercase letters ' \
    'ascii_uppercase -- a string containing all ASCII uppercase letters' \
    'ascii_letters -- a string containing all ASCII letters' \
    'digits -- a string containing all ASCII decimal digits' \
    'hexdigits -- a string containing all ASCII hexadecimal digits' \
    'octdigits -- a string containing all ASCII octal digits' \
    'punctuation -- a string containing all ASCII punctuation characters' \
    'printable -- a string containing all ASCII characters considered printable'
s = s.translate \
    (str.maketrans('', '', string.punctuation))
s = s.lower().split()

dikt = {}
for i in s:
    dikt[i] = dikt.get(i, 0) + 1

res = []

for k in dikt:
    res.append((k, dikt[k]))

res.sort(key=lambda v: (v[1]), reverse=True)
for i in range(10):
    print(res[i][0])
