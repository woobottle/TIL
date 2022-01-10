def BOJ1389() :
  n, m = map(int, input().split())
  temp = [[1e9] * n for _ in range(n)]
  for _ in range(m) :
    start, end = map(int, input().split())
    temp[start-1][end-1] = 1
    temp[end-1][start-1] = 1
  
  for mid in range(n) :
    for start in range(n) :
      for end in range(n) :
        if mid != end and temp[start][mid] and temp[mid][end]:
          temp[start][end] = min(temp[start][end], temp[start][mid] + temp[mid][end])
  
  result = 1e9
  p = 0
  for i in range(n) :
    total = sum(temp[i])
    if result > total :
      result = total
      p = i
  
  print(p+1)

BOJ1389()

