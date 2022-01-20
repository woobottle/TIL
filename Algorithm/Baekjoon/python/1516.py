# 문제에 뭘 먼저 조져야 한다고 나오면 바로 위상정렬
import heapq
import sys
input = sys.stdin.readline

def BOJ1516() :
  N = int(input())
  time = [0 for _ in range(N+1)]
  graph = [[] for _ in range(N+1)]
  indegree = [0 for _ in range(N+1)]
  queue = []
  result = [0 for _ in range(N+1)]

  for i in range(1, N + 1) :
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    temp_graph = temp[1:-1]
    indegree[i] = len(temp_graph)
    for k in temp_graph :
      graph[k].append(i)
  
  for i in range(1, N+1) :
    if indegree[i] == 0 :
      heapq.heappush(queue, (time[i], [i, time[i]]))

  while queue :
    _, [curr, curr_time] = heapq.heappop(queue)
    result[curr] = curr_time
    for i in graph[curr] :
      indegree[i] -= 1
      if indegree[i] == 0 :
        next_time = curr_time + time[i]
        heapq.heappush(queue, (next_time, [i, next_time]))

  for i in range(1, N+1) :
    print(result[i])

BOJ1516()