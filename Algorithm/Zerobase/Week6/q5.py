def solution(N, M, V, edges):
  visited = [0 for _ in range(N + 1)]
  array = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

  for start, end in edges :
    array[start][end] = 1
    array[end][start] = 1
  

  def dfs(start):
    queue = [start]
    visited[start] = 1
    print(start, end = ' ')

    while queue :
      start = queue.pop()
      
      for i in range(1, N + 1) :
        if array[start][i] and not visited[i] :
          visited[i] = 1
          print(i, end = ' ')
          queue.append(i)
    
  dfs(V)


N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

solution(N, M, V, edges) # 1 2 3 4
