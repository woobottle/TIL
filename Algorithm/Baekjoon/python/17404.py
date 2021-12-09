n = int(input())
cost = []
for _ in range(n):
  cost.append(list(map(int, input().split())))

for i in range(1, len(cost) - 1):
  cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
  cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
  cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

cost[n-1][0] = min(cost[n-2][1], cost[n-2][2]) + cost[n-1][0]
cost[n-1][1] = min(cost[n-2][0], cost[n-2][2]) + cost[n-1][1]
cost[n-1][2] = min(cost[n-2][0], cost[n-2][1]) + cost[n-1][2]

print(cost)
print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))
