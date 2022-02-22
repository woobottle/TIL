import sys
input = sys.stdin.readline

def BOJ10809() :
  s = list(input().rstrip())
  l = [-1 for _ in range(26)]

  for i in range(len(s)) :
    if l[ord(s[i]) - 97] == -1 :
      l[ord(s[i]) - 97] = i

  print(*l)

BOJ10809()
