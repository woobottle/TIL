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
    for j in range(total + 1) :
      if j < cost :
        dp[i][j] = dp[i-1][j] # 코스트가 현재 앱의 끄는 비용보다 작으면 앱을 끄지 못한다
      else :
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte) 
        # 끄지않고 그대로 두어서 확보할 수 있는 메모리가 더 큰경우와 꺼서 메모리를 확보하는 경우의 비교

      if dp[i][j] >= M :
        result = min(result, j)
  
  print(dp)
  if M == 0 :
    print(0)
  else :
    print(result)
BOJ7579()
