def BOJ1389() :
  n, m = map(int, input().split())
  temp = [[0] * n for _ in range(n)]
  for _ in range(m) :
    start, end = map(int, input().split())
    temp[start-1][end-1] = 1
    temp[end-1][start-1] = 1
  
  for mid in range(n) :
    for start in range(n) :
      for end in range(n) :
        if mid == end :
          continue
        elif temp[start][mid] and temp[mid][end] :
          if temp[start][end] == 0 :
            temp[start][end] = temp[start][mid] + temp[mid][end]
          else :  
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

