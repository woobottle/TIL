def BOJ1679():
  n, k = map(int, input().split())
  graph = [1e9] * 100001
  queue = []
  graph[n] = 0
  queue.append([n, 0])
  while queue:
    current_node, current_time = queue.pop(0)

    next_node = current_node - 1
    if 0 <= next_node <= 100000 and graph[next_node] > current_time + 1:
      graph[next_node] = current_time + 1
      queue.append([next_node, current_time + 1])

    next_node = current_node + 1
    if 0 <= next_node <= 100000 and graph[next_node] > current_time + 1:
      graph[next_node] = current_time + 1
      queue.append([next_node, current_time + 1])

    next_node = current_node * 2
    if 0 <= next_node <= 100000 and graph[next_node] > current_time + 1:
      graph[next_node] = current_time + 1
      queue.append([next_node, current_time + 1])

  print(graph[k])


BOJ1679()
