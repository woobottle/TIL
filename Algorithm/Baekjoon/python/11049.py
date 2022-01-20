import sys 
input = sys.stdin.readline
INF = 2**31

def BOJ11049() : 
  N = int(input())
  l = []
  for _ in range(N) :
    l.append(list(map(int, input().split())))

  dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
  # dp[i][j] = 행렬 i 부터 j까지의 곱의 최솟값
  for i in range(1, len(l)+1) : # 0 1 2 3
    for j in range(N-i) :  # 4 (0, 1, 2, 3), 3 (0, 1, 2), 2 (0, 1),  1 (0)
      if i == 1 :
        dp[j][j+1] = l[j][0] * l[j][1] * l[j+1][1]
      else : # (0,2), (1,3)
        dp[j][j+i] = INF
        
        for k in range(j, j+i) :
          dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + l[j][0] * l[k][1] * l[j+i][1]) 
          # min(ABCD) = min(
          # dp[ABCD], 
          # dp[A] + dp[BCD] + A[0] * A[1] * D[1],
          # dp[AB] + dp[CD] + A[0] * B[1] * D[1], 
          # dp[ABC] + dp[D] + A[0] * C[1] * D[1],
          # )
    
  print(dp[0][len(l)-1])

BOJ11049()