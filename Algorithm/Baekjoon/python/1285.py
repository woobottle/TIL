n = int(input())
coin = [list(input()) for _ in range(n)]
ans = n * n + 1

for bit in range(1 << n) :
  # 0000 0000 부터 0000 0100 까지
  tmp = [coin[i][:] for i in range(n)]
  for i in range(n) :
    if bit & (1 << i) :
      for j in range(n) :
        if tmp[i][j] == 'H' :
          tmp[i][j] = 'T'
        else :
          tmp[i][j] = 'H'

  tot = 0
  for i in range(n) :
    cnt = 0
    for j in range(n) :
      if tmp[j][i] == 'T' :
        cnt += 1
    # 뒤집는 경우와 안 뒤집는 경우중 작은거 추가하기
    tot += min(cnt, n - cnt)
  ans = min(ans, tot)

print(ans)
