import sys
input = sys.stdin.readline
INF = 1e8

def BOJ2342() : 
  def get_distance(curr, target) :
    if curr == target :
      return 1
    elif curr == 0 :
      return 2 
    elif abs(curr - target) % 2 == 0 :
      return 4
    else : 
      return 3 

  l = list(map(int, input().split()))
  # dp[n 번째 움직임][왼발위치][오른발위치]
  dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(l)+1)]
  dp[0][0][0] = 0

  for i in range(1, len(l)) :
    move = l[i-1]
    for left in range(5) :
      for right in range(5) :
        dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + get_distance(left, move))
        dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + get_distance(right, move))

  result = INF
  for i in range(5) :
    for j in range(5) :
      result = min(result, dp[len(l)-1][i][j])

  print(result)

BOJ2342()
