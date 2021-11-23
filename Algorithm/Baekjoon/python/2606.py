n = int(input())
pipe_length = int(input())
answer = 0

array = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(pipe_length) :
  start, end = map(int, input().split())
  array[start][end] = 1
  array[end][start] = 1

queue = [1]
visited[1] = True

while queue :
  start = queue.pop(0)
  for i in range(len(array[start])) :
    if array[start][i] == 1 and visited[i] == False :
      answer += 1
      queue.append(i)
      visited[i] = True

print(answer)