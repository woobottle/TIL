import sys
input = sys.stdin.readline

def BOJ1065() :
  def is_han_num(num) :
    a, b, c = list(str(num))
    num_a = int(a)
    num_b = int(b)
    num_c = int(c)
    if 2 * abs(num_a-num_b) == abs(num_c-num_a) and abs(num_b - num_a) == abs(num_c - num_b) :
      return True
    return False

  l = [0 for _ in range(1001)]
  for i in range(1, 1000) :
    if i < 100 :
      l[i] = 1
    else :
      if is_han_num(i) :
        l[i] = 1
  
  N = int(input())
  print(sum(l[:N+1]))
  
BOJ1065()
