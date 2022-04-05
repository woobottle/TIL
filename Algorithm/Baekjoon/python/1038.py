# from itertools import combinations
# import sys
# input = sys.stdin.readline

# def BOJ1038() :
#   N = int(input())
#   answers = []

#   for i in range(1, 11) :
#     for comb in combinations(range(0, 10), i) :
#       comb = list(comb)
#       comb.sort(reverse=True)
#       answers.append(int("".join(map(str, comb))))

#   answers.sort()
  
#   try :
#     print(answers[N])
#   except :
#     print(-1)
  
# BOJ1038()
# # https://ryu-e.tistory.com/59

import sys
input = sys.stdin.readline

def BOJ1038() :
  N = int(input())
  answers = []

  def get_decrease(num) :
    answers.append(num)

    peak = int(str(num)[0])
    for i in range(peak + 1, 10) :
      get_decrease(int(str(i) + str(num)))

  for i in range(10) :
    get_decrease(i)
    
  answers.sort()
  
  try :
    print(answers[N])
  except : 
    print(-1)

BOJ1038()
