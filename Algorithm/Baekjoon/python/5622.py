import sys
input = sys.stdin.readline

def BOJ5622() :
  l = list(input().rstrip())
  answer = 0

  for s in l :
    i = ord(s)
    if i <= 67 : # ABC
      answer += 3
    elif i <= 70 : # DEF
      answer += 4
    elif i <= 73 : # GHI
      answer += 5
    elif i <= 76 : # JKL
      answer += 6
    elif i <= 79 : # MNO
      answer += 7
    elif i <= 83 : # PQRS
      answer += 8
    elif i <= 86 : # TUV
      answer += 9
    elif i <= 90 : # WXYZ
      answer += 10
  
  print(answer)

BOJ5622()
