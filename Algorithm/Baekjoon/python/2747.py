import sys 
input = sys.stdin.readline

def BOJ2747() :
  fibonacci = [0, 1, 1] + [0] * 46
  for i in range(3, 46) :
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

  n = int(input())
  print(fibonacci[n])

BOJ2747()