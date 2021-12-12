import sys 

def BOJ12865() :
  n, k = map(int, sys.stdin.readline().split())
  item_list = [[0,0]]
  dp = [[0] * (k+1) for _ in range(n+1)]
  for _ in range(n) :
    w,v = map(int, sys.stdin.readline().split())
    item_list.append([w,v])
  
  for i in range(1, n+1) :
    for j in range(1, k+1) :
      weight, value = item_list[i]
      if item_list[i][0] <= j :
        dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)
      else :
        dp[i][j] = dp[i-1][j]

  print(dp[n][k])
  
BOJ12865()


