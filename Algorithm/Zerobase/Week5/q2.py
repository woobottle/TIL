def gcdString(A, B) :
  dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
  
  for i in range(1, len(A) + 1) :
    a = A[i-1]
    for j in range(1, len(B) + 1) :
      b = B[j-1]
      if a == b :
        dp[i][j] = dp[i-1][j-1] + 1
      else :
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  return dp[len(A)][len(B)]


A = 'ababcde'
B = 'ababcde'
print(gcdString(A, B))  # 'ababcde'

A = 'ababababab'
B = 'abab'
print(gcdString(A, B))  # 'ab'


A = 'abababab'
B = 'abab'
print(gcdString(A, B))  # 'abab'

A = 'fast'
B = 'campus'
print(gcdString(A, B)) # ''
