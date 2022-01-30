import sys
input = sys.stdin.readline

def BOJ1427() :
  l = int(input())
  s = list(str(l))
  s.sort(reverse=True)
  
  for i in s :
    print(i, end="")

BOJ1427()
