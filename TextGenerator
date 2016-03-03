//Генерация текстов
# -*- Encoding: utf-8

from collections import *
from urllib.request import *
import random
text = urlopen("http://ruscorpora.ru/1.txt").read().decode("utf-8")

def language_model(text, n=4):
    ln = defaultdict(Counter)
    text = text.replace("\r","\n" + "@" * n)
    for i in range(len(text) - n):
        context = text[i: i + n]
        symbol = text[i + n]
        ln[context][symbol] += 1
    for context in ln:
        s = 0
        for symbol in ln[context]:
            s += ln[context][symbol]
        for symbol in ln[context]:
            ln[context][symbol] /= s
    return ln

def generate_symbol(ln, context):
    x = random.random()
    for symbol in ln[context]:
        x -= ln[context][symbol]
        if x <= 0:
           return symbol
    return ""

def generate_text(ln, n = 4, count=500):
    text = "@" * n
    buf = []
    for i in range(count):
        symbol = generate_symbol(ln, text[-n:])
        text = (text + symbol)[-n:]
        if symbol != '@':
            buf.append(symbol)
    return ''.join(buf)


ln = language_model(text, 14)
print(generate_text(ln, 14, 1000))

