from __future__ import annotations
import csv
import datetime
import json
import math
import os.path
from random import randint as rnd
from typing import Callable


def deco_csv(function: Callable):
    create_csvfile()

    def wrapper():
        with open('f.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    function(*coef)

    return wrapper


def json_result(func: Callable):
    result = {}
    if os.path.exists('f1.json'):
        with open('f1.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)
    else:
        with open('f1.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file) \

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        res_key = f'{datetime.datetime.now()}'[:-7]
        result[res_key] = result.get(res_key) + [solve_dict] if result.get(res_key) else [solve_dict]
        with open('f1.json', 'w', encoding='UTF-8', ) as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        return roots

    print("Решения квадратных уравнений в f1.json")
    return wrapper


def create_csvfile():
    with open('f.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(rnd(2, 500)):
            writer.writerow([rnd(-1000, 1000), rnd(-1000, 1000), rnd(-1000, 1000)])


@deco_csv
@json_result
def resh(*args) -> tuple | float | None:
    a, b, c = args
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b / (2 * a)
        return round(x, 2)


resh()
