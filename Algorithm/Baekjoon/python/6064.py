import sys
input = sys.stdin.readline

def BOJ6064() :
  def getYear(M, N, x, y) :
    MAX_NUM = M * N
    
    while x <= MAX_NUM :
      if x % N == y % N:
        return x
      x += M
    return -1

  T = int(input())
  for _ in range(T) :
    M, N, x, y = map(int, input().split())
    print(getYear(M, N, x, y))

BOJ6064()

# k - x 에 m을 나누면 나머지가 0이다.
# k - y 에 n을 나누면 나머지가 0이다.

# EX) M=10, N=12, x=3, y=9
#     1) 3 % 12 != 9 % 12
#     2) 13 % 12 != 9 % 12
#     3) 23 % 12 != 9 % 12
#     4) 33 % 12=9 % 12=9
