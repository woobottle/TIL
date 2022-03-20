import sys
input = sys.stdin.readline

def BOJ1806() :
  N, S = map(int, input().split())
  l = list(map(int, input().split()))

  f_p = 1
  s_p = 0
  result = 1e10

  s = [0, l[0]]
  for i in range(1, len(l)) :
    s.append(l[i] + s[i])

  if S > s[-1]:
    print(0)
    return

  while f_p <= N and s_p <= N :
    if s[f_p] - s[s_p] >= S :
      result = min(result, f_p - s_p)
      s_p += 1
      if f_p == s_p :
        f_p += 1
    else :
      f_p += 1

  print(result)

BOJ1806()
