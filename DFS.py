filer = open("components1.in", "r")
filew = open("components1.out", "w")
n = int(filer.readline().rstrip())
a = [[] for i in range(n + 1)] 
visit = [False] * (n + 1)
count = 0

def dfs(v):
    visit[v] = True
    for j in a[v]:
        if visit[j] != True:
            dfs(j)
    
for i in range(1, n + 1):
    array = list(map(int, filer.readline().rstrip().split()))
    for t in range(1, n + 1):
        if array[t - 1] == 1:
            a[i].append(t)
            
            
            
for i in range(1, len(visit)):
    if visit[i] != True:
        dfs(i)
        count += 1
        
    
print(count, file = filew) 


filer.close()
filew.close()