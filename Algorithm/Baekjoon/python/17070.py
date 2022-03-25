# import sys
# input = sys.stdin.readline

# def BOJ17070() :
#   N = int(input())
#   graph = []
#   for _ in range(N) :
#     graph.append(list(map(int, input().split())))

#   answer = [[[0] * N for _ in range(N)] for _ in range(N)]
#   answer[0][0][1] = 1

#   for x in range(0, N) :
#     for y in range(2, N) :
#       # 가로, 세로
#       if graph[x][y] == 0 :
#         answer[0][x][y] = answer[0][x][y-1] + answer[2][x][y-1]
#         answer[1][x][y] = answer[1][x-1][y] + answer[2][x-1][y]
#       # 대각선
#       if graph[x][y] == 0 and graph[x-1][y] == 0 and graph[x][y-1] == 0 :
#         answer[2][x][y] = answer[0][x-1][y-1] + answer[1][x-1][y-1] + answer[2][x-1][y-1]

#   print(answer[0][N-1][N-1] + answer[1][N-1][N-1] + answer[2][N-1][N-1])

# BOJ17070()

# # https://pacific-ocean.tistory.com/458



import sys 
input = sys.stdin.readline

def BOJ17070() :
  N = int(input())
  dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
  graph = []
  
  for _ in range(N) :
    graph.append(list(map(int, input().split())))
  
  dp[0][1][0] = 1
  
  for i in range(N) :
    for j in range(2, N) :
      if graph[i][j] == 0 :
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
      
      if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0 :
        dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

  print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])

BOJ17070()
