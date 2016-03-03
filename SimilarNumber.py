//Последовательности, максимально согласующиеся с исходными

N = int(input())
svid = [0] * N
for i in range(N):
    svid[i] = input();
M = int(input())
podoz = [0] * M
for i in range(M):
    podoz[i] = [input(), 0]
    for j in range(N):
        for elem in svid[j]:
            if elem not in podoz[i][0]:
                break
        else:
            podoz[i][1] += 1

maximum = max(podoz, key = lambda pair: (pair[1]))
maximum = maximum[1]
for i in range(M):
    if podoz[i][1] == maximum:
        print(podoz[i][0])

