def qsort(lst):
    if lst:
        head, *tail = lst
        return qsort([x for x in tail if x <= head]) + \
               [head] + \
               qsort([x for x in tail if x > head])
    return []

N = int(input())
cards = qsort(list(map(int, input().split())))
cards.append("")
n = 0
new = []
for j in range(N):
    if cards[j] != cards[j + 1]:
	    new.append(cards[j])
	    n += 1
K = int(input())
guests = list(map(int, input().split()))
for i in range(K):
    count = 0
    for j in range(n):
	    if (guests[i] < new[j]) :
		    count = j
		    break
    if count == 0 and j == n - 1 and n > 1:
	    count = n
    print(count, j)
	