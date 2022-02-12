import math
import sys
input = sys.stdin.readline
max_num = 1e8

def BOJ438() :
  def get_dist(one, two) :
    x, y = one
    x1, y1 = two
    return math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2))
  
  n = int(input())
  graph = []
  for _ in range(n) :
    graph.append(list(map(float, input().split())))
  
  graph.sort()
  cost = []
  
  for i in range(n) :
    temp_cost = max_num
    for j in range(n) :
      if i != j :
        temp_cost = min(temp_cost, get_dist(graph[i], graph[j]))
    cost.append(temp_cost)

  print("{0:.2f}".format(sum(cost)))

BOJ438()
