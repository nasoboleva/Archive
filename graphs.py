N, M = map(int, input().split())
S, F = map(int, input().split())
G = [dict() for i in range(N + 1)]
for i in range(M):
	u, v = map(int, input().split())
	G[u][v] = weight
	G[v][u] = weight
used = [False] * (N + 1)
prev = [0] * (N + 1)
for i in range(N):
	minim = 0
	for v in range(1, N + 1):
		if not used[v]:
			if minim == 0 or distance[v] < distance[minim]:
				minim = v
	used[minim] = True
	#prev[i] = minim
	for v in range(1, N + 1):
		if G[minim].get(v) == None:
			distance[v] = distance[v]
		else:
		        distance[v] = min(distance[v], distance[minim] + 
			                  G[minim].get(v))
		prev[v] = v
		
if distance[F] == float('inf'):
	print(-1, file = fout)
else:
	print(distance[F], file = fout)
	print(" ".join(map( str, prev[S:F + 1])), file = fout)
f.close()
fout.close()