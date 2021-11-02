import math

def solution(s):
  mid = int(len(s) / 2) 

  flag = s[:mid] == s[mid+1:][::-1]

  if flag :
    return ''
  return s[:mid] + s[:mid][::-1]


s = 'abcdcba'
print(solution(s)) # ''

s = 'bannana'
print(solution(s)) # 'bannab'

s = 'wabe'
print(solution(s)) # 'waaw'
