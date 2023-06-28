# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def shop(**keywords):
    dictt = {}
    for kw in keywords:
        dictt[keywords[kw]] = kw

    return dictt


kw = {"1": "a",
      "2": "b",
      "3": "c"}

print(shop(**kw))
