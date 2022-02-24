# 크루스칼 알고리즘
import sys
import heapq
input = sys.stdin.readline

def BOJ1197() :
  V, E = map(int, input().split())
  parent = [i for i in range(V+1)]
  l = []

  def find_parent(x) :
    if parent[x] == x :
      return x
    else :
      y = find_parent(parent[x])
      parent[x] = y
      return y

  def union_parent(a, b) :
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    
    if parent_a > parent_b :
      parent[parent_b] = parent_a
    else :
      parent[parent_a] = parent_b

  for _ in range(E) :
    a, b, c = map(int, input().split())
    heapq.heappush(l, (c, a, b))
  
  result = 0
  
  while l :
    cost, a, b = heapq.heappop(l)

    if find_parent(a) != find_parent(b) :
      union_parent(a, b)
      result += cost
  
  print(result)

BOJ1197()

# 프림 알고리즘

import sys
import heapq
input = sys.stdin.readline

def BOJ1197() :
  V, E = map(int, input().split())
  
  graph = [[] for _ in range(V+1)]
  visited = [False for _ in range(V+1)]

  for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

  def prim() :
    result = 0
    queue = []
    queue.append([0, 1])

    while queue :
      curr_cost, curr_node = heapq.heappop(queue)
      if visited[curr_node] == False :
        visited[curr_node] = True
        result += curr_cost
        for next_node, next_cost in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))
          
    return result 

  print(prim())

BOJ1197()
