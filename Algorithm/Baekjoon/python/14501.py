import sys
input = sys.stdin.readline

def BOJ14501() :
  n = int(input())
  work = []
  for _ in range(n) :
    work.append(list(map(int, input().split())))

  dp = [0 for _ in range(n+1)]
  day, cost = work[0]

  for i in range(n-1, -1, -1) :
    day, cost = work[i]
    
    complete_day = i + day
    if complete_day <= n :
      dp[i] = max(dp[i+1], dp[complete_day] + cost)
    else :
      dp[i] = dp[i+1]
    
  print(dp[0])
BOJ14501()


