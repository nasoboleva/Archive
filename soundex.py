//алгоритм Soundex

s = input()
res = ""
res += s[0]
vowels = {'a', 'e', 'h', 'i', 'o', 'u', 'w', 'y'}
letters = {'b': 1,'f': 1, 'p': 1, 'v': 1,
           'c': 2,'g': 2, 'j': 2, 'k': 2, 'q': 2, 's': 2, 'x': 2, 'z': 2,
           'd': 3, 't': 3,
           'l': 4,
           'm': 5, 'n': 5,
           'r': 6}
for i in range(1, len(s)):
    if s[i] not in vowels:
        if res[-1] != str(letters[s[i]]):
            res += str(letters[s[i]])

if len(res) < 4:
    res += '0000'
print(res[:4])
