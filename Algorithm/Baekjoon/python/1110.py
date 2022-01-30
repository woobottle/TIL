import sys
input = sys.stdin.readline

def BOJ1110() :
  count = 0
  N = int(input())
  temp = int(N)
  
  while True :
    count += 1
    head, body = divmod(temp, 10)
    new_num = body * 10 + (head + body) % 10
    if new_num == N :
      break
    temp = int(new_num)

  print(count)
BOJ1110()
