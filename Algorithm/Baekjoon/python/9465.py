import sys
input = sys.stdin.readline

def BOJ9465() :
  T = int(input())
  for _ in range(T) :
    n = int(input())
    sticker = []
    for _ in range(2) :
      sticker.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    for i in range(1, n) :
      dp[0][i] = max(dp[1][i-1] + sticker[0][i], dp[0][i-1])
      dp[1][i] = max(dp[0][i-1] + sticker[1][i], dp[1][i-1])
    
    print(max(dp[0][n-1], dp[1][n-1]))

BOJ9465()

# dp는 이전의 결과값을 이용하는 것이다.
# 선택하는 경우, 선택하지 않는경우?
# 두개 라인으로 생성하고 두개씩 비교?
