n = int(input())
MAX_COST = 10000001
COLORS = ['r', 'g', 'b']
costs = []
results = [MAX_COST for _ in range(3)]
for _ in range(n) :
  costs.append(map(int, input().split()))


for i in range(len(COLORS)) :
  result = 0
  colors = []
  
  for cost_index in range(len(costs)) :
    cost = costs[cost_index]
    if cost_index == 0 :
      colors[cost_index] = cost[cost_index]
    else :
      pass

  results[i] = min(results[i], result)

print(min(results))
