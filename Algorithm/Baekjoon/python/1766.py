import heapq
import sys
input = sys.stdin.readline

# 번호가 작은 문제를 먼저 풀어야 하므로 heapq를 사용하자

def BOJ1766() :
  N, M = map(int, input().split())
  count_of_line = [0] * (N+1)
  graph = [[] for _ in range(N+1)]
  heap = []
  result = []
  
  for _ in range(M) :
    a, b = map(int, input().split())
    count_of_line[b] += 1
    graph[a].append(b)
    
  for i in range(1, N+1) :
    if count_of_line[i] == 0 :
      heapq.heappush(heap, i)

  while heap :
    curr = heapq.heappop(heap)
    result.append(curr)
    for i in graph[curr] :
      count_of_line[i] -= 1
      if count_of_line[i] == 0 :
        heapq.heappush(heap, i)

  print(*result)
BOJ1766()
