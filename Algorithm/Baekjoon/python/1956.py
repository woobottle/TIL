import sys
v, e = map(int, input().split())
INF = 100000000
dist = [[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e) :
  start, end, distance = map(int, sys.stdin.readline().split())
  dist[start][end] = distance

for k in range(1, v + 1) :
  for i in range(1, v + 1) :
    for j in range(1, v + 1) :
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  print(dist)

answer = INF
for i in range(1, v+1) :
  answer = min(answer, dist[i][i])

if answer == INF :
  print(-1)
else :
  print(answer)

