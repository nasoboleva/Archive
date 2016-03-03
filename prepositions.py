//на каких позициях в запросах могут встречаться предлоги в строке

import sys

places = set()
prepositions = input().split()

for line in sys.stdin:
    string = line.split()
    for i in range(len(string)):
        if string[i] in prepositions:
            places.add(i + 1)

print(" ".join(map(str, sorted(places))))