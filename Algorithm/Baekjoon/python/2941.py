import sys
input = sys.stdin.readline

def BOJ2941() :
  words = input().rstrip()
  croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

  for i in croatian :
    words = words.replace(i, '*')
  print(len(words))

BOJ2941()
