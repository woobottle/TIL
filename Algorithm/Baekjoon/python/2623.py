import sys
input = sys.stdin.readline

def BOJ2623() :
  N, M = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  count_of_line = [0] * (N+1)
  queue = []
  answer = []
  
  for _ in range(M) :
    temp = list(map(int, input().split()))
    _, b = temp[:2]
    temp_list = temp[2:]
    for i in temp_list :
      graph[b].append(i)
      count_of_line[i] += 1
      b = i

  for i in range(1, N+1) :
    if count_of_line[i] == 0 :
      queue.append(i)
      answer.append(i)

  while queue :
    temp = queue.pop(0)
    for i in graph[temp] :
      count_of_line[i] -= 1
      if count_of_line[i] == 0 :
        queue.append(i)
        answer.append(i)
  
  if len(answer) != N :
    print(0)
  else :
    for i in answer :
      print(i)

BOJ2623()