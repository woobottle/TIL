import sys 
input = sys.stdin.readline
target_num = 1e6

def find_routine() :
  routine = 1
  m1, m2 = 1, 2
  while True :
    if m1 == 1 and m2 == 1 :
      break
    
    m1, m2 = m2, (m1 + m2) % target_num
    routine += 1
  return routine

def BOJ2749():
  routine_length = find_routine()
  n = int(input())
  
  fibonacci = [0, 1, 1] + [0] * int(1e7)
  for i in range(3, routine_length):
    fibonacci[i] = int((fibonacci[i-2] % target_num + fibonacci[i-1] % target_num) % target_num)

  print(fibonacci[n % routine_length])


BOJ2749()
