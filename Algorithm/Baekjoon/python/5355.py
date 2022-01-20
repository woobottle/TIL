import sys 
input = sys.stdin.readline

def BOJ5355() :
  T = int(input())
  for _ in range(T) :
    temp = list(input().split())
    result = float(temp[0])
    for i in temp[1:] :
      if i == "@" :
        result *= 3
      elif i == "%" :
        result += 5
      elif i == "#" :
        result -= 7

    print("{0:.2f}".format(result))

BOJ5355()