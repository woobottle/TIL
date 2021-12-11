from collections import deque
n, k = map(int, input().split())

location = [-1] * 100001
time = 0
queue = deque()
queue.append([n, time])
location[n] = 0

while queue :
  curr_n, curr_time = queue.popleft()


  next_n = curr_n * 2
  if 0 <= next_n <= 100000 and (location[next_n] == -1 or location[next_n] > curr_time):
    location[next_n] = curr_time
    queue.appendleft([next_n, curr_time])

  next_n = curr_n + 1
  if next_n <= 100000 and location[next_n] == -1 :
    location[next_n] = curr_time + 1
    queue.append([next_n, curr_time + 1])
  
  next_n = curr_n - 1
  if next_n >= 0 and location[next_n] == -1:
    location[next_n] = curr_time + 1
    queue.append([next_n, curr_time + 1])

print(location[k])
