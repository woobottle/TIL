import sys
input = sys.stdin.readline

def BOJ1699() :
  n = int(input())

  dp = [1e9 for _ in range(100001)]
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3

  for i in range(4, n+1) :
    if (i ** (0.5)) % 1 == 0 :
      dp[i] = 1
    else :
      number = int(i ** (0.5) // 1)
      for j in range(1, number+1) :
        if i % (j ** 2) == 0 :
          dp[i] = min(dp[i], i // (j ** 2))
        else :
          head, _ = divmod(i, j ** 2)
          dp[i] = min(dp[i], head + dp[i - head * j ** 2])
  
  print(dp[n])

BOJ1699()
