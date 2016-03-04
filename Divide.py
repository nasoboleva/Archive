//Преобразовать дробь в десятичную, с учетом периода:

num = int(input())
den = int(input())

int_part = num // den
rem = num % den
num = rem * 10

quotients = []
remainders = [rem]

while num != 0:
   quo = num // den
   rem = num % den
   quotients.append(quo)
   if rem in remainders:
       i = remainders.index(rem)
       quotients = quotients[:i] + ["("] + quotients[i:] + [")"]
       break

   remainders.append(rem)
   num = rem * 10

print(int_part, end=".")
print("".join(map(str, quotients)))

