import heapq
import sys
input = sys.stdin.readline
INF = 1e6 + 1

def BOJ2056() :
  N = int(input())
  time = [0]
  graph = [[] for _ in range(N+1)]
  indegree = [0 for _ in range(N+1)]
  queue = []
  
  for i in range(N) :
    temp = list(map(int, input().split()))
    time.append(temp[0])
    
    if len(temp) > 2 :
      indegree[i+1] = len(temp[2:])
      for k in temp[2:] :
        graph[k].append(i+1)

  for i in range(1, N+1) :
    if indegree[i] == 0 :
      heapq.heappush(queue, (time[i], [i, time[i]]))
  
  result = 0
  
  while queue :
    _, [curr, curr_time] = heapq.heappop(queue)
    result = max(result, curr_time)
    for i in graph[curr] :
      indegree[i] -= 1 
      if indegree[i] == 0 :
        next_time = curr_time + time[i]
        heapq.heappush(queue, (next_time, [i, next_time]))
  print(result)

BOJ2056()
