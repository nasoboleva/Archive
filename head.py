//Утилита head

import sys

command = input()
if command.startswith("-n"):
    N = int(command.split()[-1])
else:
    N = 10

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

print("\n".join(lines[:N]))