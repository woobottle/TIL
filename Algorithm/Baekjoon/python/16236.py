import heapq

def BOJ16236() :
  n = int(input())
  graph = []
  q = []

  for i in range(n) :
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(len(line)) :
      if line[j] == 9 :
        heapq.heappush(q, (0, i, j))
        graph[i][j] = 0

  direction = [[0,1], [0,-1], [1,0], [-1,0]]
  result = 0
  body, eat = 2, 0
  visited =[[0] * n for _ in range(n)]

  while q :
    dist, curr_x, curr_y = heapq.heappop(q)

    if 0 < graph[curr_x][curr_y] < body :
      eat += 1
      graph[curr_x][curr_y] = 0
      if body == eat :
        eat = 0
        body += 1
      result += dist
      dist = 0
      q = []
      visited =[[0] * n for _ in range(n)]

    for dir in direction :
      dir_x, dir_y = dir
      next_x = dir_x + curr_x
      next_y = dir_y + curr_y
      if 0 <= next_x < n and 0 <= next_y < n and 0 <= graph[next_x][next_y] <= body and visited[next_x][next_y] == 0:
        visited[next_x][next_y] = True
        heapq.heappush(q, (dist+1, next_x, next_y))

  print(result)

BOJ16236()

# https://rebas.kr/714
