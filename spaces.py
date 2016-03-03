s = input()
s1 = " "
sign = ['?', '!', ',', '.', '-']

for i in range(len(s)):
    if (s1[-1] in sign) and (i > 0) and (s[i] != ' '):
        s1 = s1 + ' '
    elif s[i] == '-':
        s1 = s1 + ' '
    s1 = s1 + s[i] 
    
print(s1[1:])       
       