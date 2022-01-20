import sys
input = sys.stdin.readline

def BOJ7579(): 
  N, M = map(int, input().split())
  bytes = list(map(int, input().split()))
  costs = list(map(int, input().split()))
  total = sum(costs)
  result = total
  
  dp = [[0 for _ in range(total+1)] for _ in range(N + 1)]
  for i in range(1, N+1) :
    byte, cost = bytes[i-1], costs[i-1]
    for j in range(total) :
      if j < cost :
        dp[i][j] = dp[i-1][j] # 코스트가 현재 앱의 끄는 비용보다 작으면 앱을 끄지 못한다
      else :
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)

      if dp[i][j] >= M :
        result = min(result, j)
  
  if M == 0 :
    print(0)
  else :
    print(result)
BOJ7579()
