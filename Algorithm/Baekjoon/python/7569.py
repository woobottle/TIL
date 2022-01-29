from collections import deque
import sys
input = sys.stdin.readline
RIPE = 1
UN_RIPE = 0

def BOJ7569() :
  global M, N, H
  
  def check_value(box, value) :
    has_value = False
    for i in range(H):
      for j in range(N):
        for k in range(M):
          if box[i][j][k] == value :
            has_value = True
            break
    return has_value

  def has_un_ripe(box):
    return check_value(box, UN_RIPE)

  def is_all_ripe(box) :
    return not check_value(box, UN_RIPE)
  
  def bfs(box, curr_day) :
    directions = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1]]
    queue = deque()
    answer = 0

    for i in range(H):
      for j in range(N):
        for k in range(M):
          if box[i][j][k] == 1 :
            queue.append([i, j, k, curr_day])

    while queue :
      curr_z, curr_y, curr_x, curr_day = queue.popleft()
      next_day = curr_day + 1
      
      for dir_x, dir_y, dir_z in directions :
        next_z = curr_z + dir_z
        next_y = curr_y + dir_y
        next_x = curr_x + dir_x
        if 0 <= next_z < H and 0 <= next_y < N and 0 <= next_x < M :
          if box[next_z][next_y][next_x] == 0 :
            answer = max(answer, next_day)
            queue.append([next_z, next_y, next_x, next_day])
            box[next_z][next_y][next_x] = 1

    return answer

  M, N, H = map(int, input().split())
  box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
  day = 0 
  
  for i in range(H) :
    for j in range(N) :
      temp = list(map(int, input().split()))
      for k in range(len(temp)) :
        box[i][j][k] = temp[k]
  
  if is_all_ripe(box) == True :
    print(0)
    return 
  
  day = bfs(box, day)
  
  if has_un_ripe(box) == True :
    print(-1)
    return
  
  print(day)

BOJ7569()
