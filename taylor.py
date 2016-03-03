//Ряды Тейлора

def Taylor(x):
   s = 0.0
   summand = x
   N = 100000
   for i in range(2, N + 1):
       s += summand
       summand *= -1 * x * (i - 1) / i
   return s

x = float(input())
print(Taylor(x))

