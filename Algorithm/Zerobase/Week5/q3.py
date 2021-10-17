def solution(n, vertex) :
  graph = [[0] * (n + 1) for _ in range(n + 1)]
  for a,b in vertex :
    graph[a][b] = 1
    graph[b][a] = 1
  
  visited = [1]
  queue = [1]
  maps = [0] * (n + 1) 

  while len(queue) != 0 :
    start = queue.pop(0)
    for i in range(1, n + 1) :
      if graph[start][i] == 1 and i not in visited:
        queue.append(i)
        visited.append(i)
        maps[i] = maps[start] + 1
  
  max_value = max(maps)
  count = 0 
  for i in maps :
    if max_value == i :
      count += 1
  return count


print(solution(6, [[3,6], [4,3], [3,2], [1,3], [1,2], [2,4], [5,2]])) # 3