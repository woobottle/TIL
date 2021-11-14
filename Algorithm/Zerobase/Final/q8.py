def solution(N, K, L, apples, moves):
  time = 0
  APPLE = 1
  BODY = 2
  head_x, head_y = 0, 0
  body = [[0,0]]
  DIRECTION = [[1,0], [0, 1], [-1, 0], [0, -1]]
  current_dir = 0

  map = [[0] * (N) for _ in range(N)]
  for apple in apples :
    x, y = apple
    map[x-1][y-1] = APPLE    

  set_moves = {}
  for move in moves :
    temp_time, direction = move
    set_moves[temp_time] = direction

  next_x = 0
  next_y = 0
  map[0][0] = BODY

  while 0 <= next_x < N and 0 <= next_y < N : 
    time += 1
    move_x, move_y = DIRECTION[current_dir]
    next_x = head_x + move_x
    next_y = head_y + move_y
    
    if next_x >= N or next_y >= N  :
      break
    
    if map[next_y][next_x] == 0 :
      map[next_y][next_x] = BODY
      body.append([next_x, next_y])
      tail_x, tail_y = body[0]
      map[tail_y][tail_x] = 0
      body.pop(0)
    elif map[next_y][next_x] == APPLE:
      map[next_y][next_x] = BODY
      body.append([next_x, next_y])
    elif map[next_y][next_x] == BODY:
      break
    
    head_x = next_x
    head_y = next_y
    
    if set_moves.get(time):
      if set_moves.get(time) == 'D':
        current_dir = (current_dir + 1) % 4
      elif set_moves.get(time) == 'L':
        current_dir = (current_dir + 3) % 4

  return time


N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves)) # 9

N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves)) # 21

N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves)) # 13
