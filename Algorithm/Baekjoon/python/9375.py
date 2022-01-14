import sys 
input = sys.stdin.readline

def BOJ9375() :
  T = int(input())
  for _ in range(T) :
    n = int(input())
    dict = {}
    for _ in range(n) :
      _, type = input().split()
      if type in dict :
        dict[type] += 1
      else :
        dict[type] = 1
    
    answer = 1
    
    for i in dict.values() :
      answer *= (i+1)
    print(answer - 1)

BOJ9375()