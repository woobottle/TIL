import sys
input = sys.stdin.readline

def BOJ1152() :
  sentence = list(filter(lambda x: x != '' , list(input().strip().split(" "))))
  print(len(sentence))


BOJ1152()
