//"Черепашка" умеет ходить по клетчатому полю и закрашивать клетки. Поле бесконечно во все стороны, а клетки поля имеют целочисленные //координаты (оси направлены стандартным образом: абсцисса вправо, ордината вверх). В начале черепашка находится в клетке (0, 0).

//Черепашка понимает следующие команды:

//    left — шагни влево;
//    right — шагни вправо;
//    up — шагни вверх;
//    down — шагни вниз;
//    paint — закрась текущую клетку;
//    loop N — повтори вложенный блок команд N раз. Здесь N — явно заданное натуральное число, а все вложенные команды блока отделяются //отступом в 4 пробела. Циклы могут быть вложены друг в друга.


import sys

i = 0
x = 0
y = 0
painted = []
text = []

for line in sys.stdin:
    text.append(line.rstrip())


def commands(line, x, y):
    if line == "up":
        return x, y + 1
    if line == "down":
        return x, y - 1
    if line == "right":
        return x + 1, y
    if line == "left":
        return x - 1, y
    if line == "paint":
        painted.append((x, y))
        return x, y


def loop(text, N, i, nest, x, y):
    cycle = []
    for l in range(N):
        j = i
        while j < len(text) and text[j][:4 * nest] == " " * 4 * nest:
            if text[j].startswith("lo", 4 * nest):
                j, x, y = loop(text, int(text[j][-1]), j + 1, nest + 1, x, y)
            else:
                x, y = commands(text[j][4 * nest:], x, y)
                j += 1

    return j, x, y

while i < len(text):
    if text[i].startswith("lo"):
        i, x, y = loop(text, int(text[i][-1]), i + 1, 1, x, y)
    else:
        x, y = commands(text[i], x, y)
        i += 1

painted = list(set(painted))
for x, y in sorted(painted):
    print(x, y)
