import sys
input = sys.stdin.readline

def BOJ3460() :
  T = int(input())
  for _ in range(T) :
    n = int(input())
    l = ""
    while n != 0 :
      if n % 2 == 0 :
        l += '0'
      else :
        l += '1'
      n //= 2
    
    for index, val in enumerate(l) :
      if val == '1' :
        print(index, end = ' ')

BOJ3460()
