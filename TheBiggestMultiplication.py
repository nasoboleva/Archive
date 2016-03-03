//Наибольшее произведение

N = int(input())
mas = input().split()
minimum = [10**9] * 2
minimum[0] = int(mas[0])
maximum = [-10**9] * 3
maximum[0] = int(mas[0])
for i in range(1, N):
    if int(mas[i]) < minimum[1]:
        if int(mas[i]) < minimum[0]:
                minimum[1] = minimum[0]
                minimum[0] = int(mas[i])
        else:
            minimum[1] = int(mas[i])
    if int(mas[i]) > maximum[2]:
        if int(mas[i]) > maximum[1]:
            if int(mas[i]) > maximum[0]:
                    maximum[2] = maximum[1]
                    maximum[1] = maximum[0]
                    maximum[0] = int(mas[i])
            else:
                maximum[2] = maximum[1]
                maximum[1] = int(mas[i])        
        else:
            maximum[2] = int(mas[i])
if minimum[0] * minimum[1] * maximum[0] > maximum[0] * maximum[1] * maximum[2]:
    minimum.append(maximum[0])
    print(*minimum)
else:
    print(*maximum)
