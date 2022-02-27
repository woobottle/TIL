import math
import heapq
import sys
input = sys.stdin.readline

def BOJ4386() :
  
  def get_dist(x1, y1, x2, y2) :
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)) 

  n = int(input())
  stars = []
  for _ in range(n) :
    stars.append(list(map(float, input().split())))

  graph = [[] for _ in range(n+1)]
  visited = [False for _ in range(n+1)]

  for i in range(len(stars)) :
    for j in range(i+1, len(stars)) :
      x1, y1 = stars[i]
      x2, y2 = stars[j]
      cost = get_dist(x1, y1, x2, y2)
      graph[i].append([cost, j])
      graph[j].append([cost, i])

  def prim() :
    result = 0
    queue = []
    queue.append([0, 1])

    while queue :
      curr_cost, curr_node = heapq.heappop(queue)

      if visited[curr_node] == False :
        visited[curr_node] = True
        result += curr_cost
        for next_cost, next_node in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))

    return result

  print(prim())
BOJ4386()
