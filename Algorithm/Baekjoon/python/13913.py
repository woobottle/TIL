def BOJ13913():
  n, k = map(int, input().split())
  graph = [1e9] * 100001
  queue = []
  graph[n] = 0
  queue.append([n, 0])
  dict = {n: n}
  while queue:
    current_node, current_time = queue.pop(0)
    next_time = current_time + 1

    next_node = current_node - 1
    if 0 <= next_node <= 100000 and graph[next_node] > next_time:
      graph[next_node] = next_time
      dict[next_node] = current_node
      queue.append([next_node, next_time])

    next_node = current_node + 1
    if 0 <= next_node <= 100000 and graph[next_node] > next_time:
      graph[next_node] = next_time
      dict[next_node] = current_node
      queue.append([next_node, next_time])

    next_node = current_node * 2
    if 0 <= next_node <= 100000 and graph[next_node] > next_time:
      graph[next_node] = next_time
      dict[next_node] = current_node
      queue.append([next_node, next_time])

  print(graph[k])
  result = str(k)
  temp = k
  for _ in range(graph[k]):
    result = result + ' ' + str(dict[temp])
    temp = dict[temp]
  print(' '.join(result.split()[::-1]))


BOJ13913()
