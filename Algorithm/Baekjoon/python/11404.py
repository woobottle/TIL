import sys
input = sys.stdin.readline

def BOJ11404() :
  n = int(input())
  m = int(input())
  dist = [[1e9 for _ in range(n)] for _ in range(n)]
  for _ in range(m) :
    a, b, c = list(map(int, input().split()))
    dist[a - 1][b - 1] = min(dist[a-1][b-1], c)
  
  
  for k in range(n) :
    for i in range(n) :
      for j in range(n) :
        if dist[i][k] != 0 and dist[k][j] != 0 :
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  
  for i in range(n) :
    for j in range(n) :
      if i != j :
        if dist[i][j] == 1e9 :
          print(0, end=' ')
        else :
          print(dist[i][j], end=' ')
      else :
        print(0, end=' ')
    print()

BOJ11404()
