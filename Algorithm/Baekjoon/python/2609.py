import sys
input = sys.stdin.readline

def BOJ2609() :
  def get_first(a, b) :
    if b == 0 :
      return a
    return get_first(b, a % b)

  A, B = map(int, input().split())
  first = get_first(A, B)
  
  print(first)
  print((A * B) // first)

BOJ2609()
