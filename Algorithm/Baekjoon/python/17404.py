n = int(input())
cost = []
INF = 1e9

for _ in range(n):
  cost.append(list(map(int, input().split())))

result = INF

for start_number in range(3) :
  dist = [[0] * 3 for _ in range(len(cost))]

  for i in range(3) :
    if i != start_number :
      dist[0][i] = INF
    else :
      dist[0][i] = cost[0][i]

  for i in range(1, len(cost)):
    dist[i][0] = min(dist[i-1][1], dist[i-1][2]) + cost[i][0]
    dist[i][1] = min(dist[i-1][0], dist[i-1][2]) + cost[i][1]
    dist[i][2] = min(dist[i-1][0], dist[i-1][1]) + cost[i][2]

  for i in range(3) :
    if i != start_number :
      result = min(result, dist[n-1][i])

print(result)
