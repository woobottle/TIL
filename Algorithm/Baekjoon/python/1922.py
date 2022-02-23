import sys
input = sys.stdin.readline

def BOJ1922() :
  N = int(input())
  M = int(input())
  parent = [i for i in range(N+1)]

  def find_parent(x):
    if (x == parent[x]):
      return x
    else:
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

  l = []
  for _ in range(M) :
    l.append(list(map(int, input().split())))
  l.sort(key = lambda x : x[2])
  
  result = 0
  
  for node in l : 
    a, b, cost = node
    
    if find_parent(a) != find_parent(b) :
      union_parent(a, b)
      result += cost
  
  print(result)

BOJ1922()
