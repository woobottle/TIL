n = int(input())
l = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
max_value = dp[0]
for i in range(1, n) :
  if (max_value <= l[i]) :
    dp[i] = max(dp) + 1
    max_value = l[i]
  else : 
    dp[i] = max(dp)

print(dp)
print(dp[n-1])

# 6
# 10 20 10 30 20 50
# 6
# 10 20 10 20 30 40
