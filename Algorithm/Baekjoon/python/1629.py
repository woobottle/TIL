import sys 
input = sys.stdin.readline 

def BOJ1629() :
  def pow(a, b, c) :
    if b == 1 :
      return a % c
    elif b % 2 == 0 :
      return (pow(a, b // 2, c) ** 2) % c
    else :
      return (pow(a, b // 2, c) ** 2) * a % c
  
  A, B, C = map(int, input().split())
  print(pow(A, B, C))
  
BOJ1629()

# a^4 = a^2 * a^2
# a^3 = a^2 * a

# pow(10, 11, 12) => (pow(10, 5, 12) ** 2) * 10 % 12
# pow(10, 5, 12) => (pow(10, 2, 12) ** 2) * 10 % 12
# pow(10, 2, 12) => (pow(10, 1, 12) ** 2) 

# pow(10, 1, 12) => 2
# pow(10, 2, 12) => 4
# pow(10, 5, 12) => 4
# pow(10, 11, 12) => 4
