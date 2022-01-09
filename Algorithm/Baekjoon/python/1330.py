import sys 
input = sys.stdin.readline

def BOJ1330():
  A,B = map(int, input().split())
  if A > B :
    print('>')
  elif A < B :
    print('<')
  else :
    print('==')

BOJ1330()