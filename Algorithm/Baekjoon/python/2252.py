import sys
input = sys.stdin.readline

def BOJ2252() :
  N, M = map(int, input().split())
  count_of_line = [0] * (N+1)
  graph = [[] for _ in range(N+1)]
  queue = []
  
  for _ in range(M) :
    A, B = map(int, input().split())
    count_of_line[B] += 1
    graph[A].append(B)

  for i in range(1, N+1) :
    if count_of_line[i] == 0 :
      queue.append(i)
  
  while queue :
    student = queue.pop(0)
    for i in graph[student] :
      count_of_line[i] -= 1
      if count_of_line[i] == 0 :
        queue.append(i) 
    print(student, end = ' ')

BOJ2252()