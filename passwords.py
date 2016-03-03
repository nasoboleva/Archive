
//Программа, которая по заданной строке с паролем кроме самой этой строки сгенерирует и все возможные варианты, получаемые заменой одной или нескольких букв I на l и наоборот. Вывести их нужно в алфавитном порядке. 

import itertools
words = input().split()
ind = [i for i in range(len(words))]
combination = []
for i in range(1, len(words) + 1):
    for comb in itertools.permutations(words, i):
        combination.append(comb)

for elem in sorted(combination):
    print("".join(elem))
