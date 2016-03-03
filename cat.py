//Реализация аналога консольной утилиты cat на python.
//Программа принимает ключи

//    -E, отображать символ "доллар" в конце каждой строки;
//    -n, нумеровать все строки вывода;
//    -s, удалять повторяющиеся пустые строки в выводе;
//    -T, отображать символы табуляции, как


import sys

def E(text):
    new_text = []
    for line in text:
        new_text.append(line + "$")
    return new_text


def n(text):
    new_text = []
    i = 1
    for line in text:
        new_text.append(str(i) + " " + line)
        i += 1
    return new_text


def s(text):
    new_text = [text[0]]
    for i in range(1, len(text)):
        if text[i] != text[i - 1] or text[i] != "":
            new_text.append(text[i])
    return new_text


def T(text):
    new_text = []
    for line in text:
        new_text.append(line.replace("\t", "^I"))
    return new_text

text = []

command = sys.stdin.readline().split()
for line in sys.stdin:
    text.append(line.replace("\n", ""))

if len(text) > 0:
    if "-s" in command:
        text = s(text)
    if "-E" in command:
        text = E(text)
    if "-n" in command:
        text = n(text)
    if "-T" in command:
        text = T(text)
    print("\n".join(text))
