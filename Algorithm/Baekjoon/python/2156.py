import sys
input = sys.stdin.readline

def BOJ2156() :
  n = int(input())
  dp = [[0 for _ in range(3)] for _ in range(n)]
  l = []
  for _ in range(n) :
    l.append(int(input()))
  
  # dp[i][0] = 해당 잔을 마시지 않은 경우
  # dp[i][1] = 앞의 잔을 마시지 않고 해당 잔을 마신 경우
  # dp[i][2] = 앞의 잔을 마시고 해당 잔을 마신 경우

  dp[0] = [0, l[0], l[0]]
  
  for i in range(1, n) :
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + l[i]
    dp[i][2] = dp[i-1][1] + l[i]

  print(max(dp[n-1]))

BOJ2156()
