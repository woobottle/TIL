import sys 
input = sys.stdin.readline

def BOJ2753() :
  year = int(input())
  is_special = False

  if year % 4 == 0 :
    if year % 100 != 0 :
      is_special = True
    if year % 400 == 0 :
      is_special = True 

  if is_special :
    print(1)
  else :
    print(0)

BOJ2753()