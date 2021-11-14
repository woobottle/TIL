from collections import deque


def solution(C, B):
  time = 0
  queue = deque()
  queue.append((B, time))
  visited = [{} for _ in range(200001)]

  while C <= 200000:
    C += time
    if time in visited[C]:
      return time

    for _ in range(0, len(queue)):
      current_position, current_time = queue.popleft()
      next_time = current_time + 1

      next_position = current_position + 1
      if 0 <= next_position <= 200000:
        visited[next_position][next_time] = True
        queue.append((next_position, next_time))

      next_position = current_position - 1
      if 0 <= next_position <= 200000:
        visited[next_position][next_time] = True
        queue.append((next_position, next_time))

      next_position = current_position * 2
      if 0 <= next_position <= 200000:
        visited[next_position][next_time] = True
        queue.append((next_position, next_time))

    time += 1

  return -1


print(solution(11, 2))  # 5
