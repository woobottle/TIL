import sys
input = sys.stdin.readline

def BOJ14719() :
  H, W = map(int, input().split())
  l = list(map(int, input().split()))

  graph = [[0 for _ in range(W)] for _ in range(H)]
  
  for i in range(H) :
    for j in range(W) :
      if l[j] == H - i :
        graph[i][j] = 1
        l[j] -= 1

  for i in range(H) :
    start = -1
    end = -1

    for j in range(W) :
      if graph[i][j] == 1 :
        if start != -1 :
          end = j
          for k in range(start + 1, end) :
            graph[i][k] = 3
          start = end
          end = 0

        start = j
        

  answer = 0
  for i in range(H) :
    for j in range(W) :
      if graph[i][j] == 3 :
        answer += 1
  print(answer)

BOJ14719()
