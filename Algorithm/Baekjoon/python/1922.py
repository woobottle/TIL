# import sys
# input = sys.stdin.readline

# def BOJ1922() :
#   N = int(input())
#   M = int(input())
#   parent = [i for i in range(N+1)]

#   def find_parent(x):
#     if (x == parent[x]):
#       return x
#     else:
#       y = find_parent(parent[x])
#       parent[x] = y
#       return y

#   def union_parent(a, b) :
#     parent_a = find_parent(a)
#     parent_b = find_parent(b)
#     if parent_a > parent_b :
#       parent[parent_b] = parent_a
#     else :
#       parent[parent_a] = parent_b

#   l = []
#   for _ in range(M) :
#     l.append(list(map(int, input().split())))
#   l.sort(key = lambda x : x[2])
  
#   result = 0

#   for node in l : 
#     a, b, cost = node
    
#     if find_parent(a) != find_parent(b) :
#       union_parent(a, b)
#       result += cost
  
#   print(result)

# BOJ1922()

import sys
import heapq
input = sys.stdin.readline


def BOJ1922():
  N = int(input())
  M = int(input())
  visited = [False for _ in range(N+1)]
  graph = [[] for _ in range(N+1)]
  
  for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

  queue = []

  def prim() :
    answer = 0 
    heapq.heappush(queue, (0, 1))
    
    while queue :
      curr_cost, curr_node = heapq.heappop(queue)
      if visited[curr_node] == False :
        visited[curr_node] = True
        answer += curr_cost
        for next_node, next_cost in graph[curr_node] :
          heapq.heappush(queue, (next_cost, next_node))
    return answer
  
  print(prim())
  
BOJ1922()
