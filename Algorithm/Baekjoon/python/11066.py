import sys
input = sys.stdin.readline
INF = 1e9

def BOJ11066() :
  global files
  global presum
  global cache
  
  def dp(start, end) :
    if start == end :
      return files[start]
    
    if cache[start][end] != 0 :
      return cache[start][end]

    result = INF
    sum = presum[end+1] - presum[start]
    for i in range(start, end) :
      result = min(result, dp(start, i) + dp(i+1, end) + sum)
      cache[start][end] = result
    return result


  T = int(input())
  for _ in range(T) :
    K = int(input())
    files = list(map(int, input().split()))
    presum = [0 for _ in range(K+1)]
    cache = [[0 for _ in range(K+1)] for _ in range(K+1)]

    for i in range(1, K+1) :
      presum[i] = presum[i-1] + files[i-1]
    
    result = INF
    for i in range(K-1) :
      result = min(result, dp(0, i) + dp(i+1, K-1))
    print(result)
  

BOJ11066()

# dp를 i부터 j까지 더했을때의 최솟값
# https://www.acmicpc.net/board/view/53172
