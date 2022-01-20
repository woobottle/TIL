import sys 
input = sys.stdin.readline

def BOJ1789() :
  S = int(input())
  
  result = 0
  num = 0
  while True :
    if result + num > S :
      break
    result += num
    num += 1
  print(num-1)

BOJ1789()
