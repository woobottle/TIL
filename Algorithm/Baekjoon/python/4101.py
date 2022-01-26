import sys 
input = sys.stdin.readline

def BOJ4101() :
  while True :
    a, b = map(int, input().split())
    
    if a == b == 0 :
      break

    if a > b : 
      print("Yes")
    else :
      print("No")

BOJ4101()