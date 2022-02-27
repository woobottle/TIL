import sys
input = sys.stdin.readline

def BOJ10423() :
  N, M, K = map(int, input().split())
  plants = list(map(int, input().split()))

  graph = []
  parent = [i for i in range(N+1)]

  for _ in range(M) : 
    graph.append(list(map(int, input().split())))
  
  graph.sort(key = lambda x : x[2])
  
  def find_parent(x) :
    if parent[x] == x :
      return x 
    
    y = find_parent(parent[x])
    parent[x] = y
    return y

  def union_parent(parent_a, parent_b) :
    if parent_a not in plants and parent_b in plants :
      parent[parent_a] = parent_b
    elif parent_a in plants and parent_b not in plants :
      parent[parent_b] = parent_a
    elif parent_a not in plants and parent_b not in plants :
      if parent_a > parent_b :
        parent[parent_b] = parent_a
      else :
        parent[parent_a] = parent_b

  result = 0 
  for a, b, cost in graph :
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a != parent_b and (parent_a not in plants or parent_b not in plants) :
      union_parent(parent_a, parent_b)
      result += cost

  print(result)
  
BOJ10423()
