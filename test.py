def solution(n, clockwise):
  answer = [[0 for _ in range(n)] for _ in range(n)]
  directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
  start = [[0, 0, 0], [n-1, 0, 1], [n-1, n-1, 2],  [0, n-1, 3]]
  index = 1

  def check_graph() :
    for i in range(n) :
      for j in range(n) :
        if answer[i][j] == 0 :
          return True
    
    return False

  while True :
    flag = True
    for i in range(len(start)) :
      x, y, dir_index = start[i]
      answer[x][y] = index
      dir_x, dir_y = directions[dir_index]
      next_x, next_y = x + dir_x, y + dir_y
      
      if answer[next_x][next_y] != 0 :
        dir_index = (dir_index + 1) % 4
        dir_x, dir_y = directions[dir_index]
        next_x, next_y = x + dir_x, y + dir_y

      start[i] = [next_x, next_y, dir_index]

      if check_graph() == False :
        flag = False
        break
    if flag == False :
      break
    index += 1

  if clockwise :
    for i in range(n) :
      answer[i] = answer[i][::-1]
  
  return answer

print(solution(5, True))
print(solution(6, False))
