n = int(input())
l = []

for i in range(n) :
  l.append(list(map(int, input().split())))

dp = l.copy()
for i in range(1, len(l)) :
  for j in range(len(l[i])) :
    if j == 0 :
      dp[i][j] = dp[i-1][j] + l[i][j]
    elif j == len(l[i]) - 1 :
      dp[i][j] = dp[i-1][j-1] + l[i][j]
    else :
      dp[i][j] = max(dp[i-1][j-1] + l[i][j], dp[i-1][j] + l[i][j])

print(max(dp[n-1]))
