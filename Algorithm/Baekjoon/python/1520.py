import sys
input = sys.stdin.readline

def BOJ1520() :
  global M, N
  global l
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  
  def get_load(dp, curr_x, curr_y):
    
    if curr_x == M - 1 and curr_y == N - 1 :
      return 1
    if dp[curr_x][curr_y] != -1 :
      return dp[curr_x][curr_y]
    
    dp[curr_x][curr_y] = 0
    for dir_x, dir_y in directions :
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y
      if 0 <= next_x < M and 0 <= next_y < N and l[next_x][next_y] < l[curr_x][curr_y] :
        dp[curr_x][curr_y] += get_load(dp, next_x, next_y)
    return dp[curr_x][curr_y]

  M, N = map(int, input().split())
  l = []
  for _ in range(M) :
    l.append(list(map(int, input().split())))
  
  dp = [[-1 for _ in range(N)] for _ in range(M)]
  print(get_load(dp, 0, 0))
  

BOJ1520()
