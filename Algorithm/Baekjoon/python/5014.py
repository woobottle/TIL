from collections import deque
import sys
input = sys.stdin.readline
MAX_VALUE = 1000001

def BOJ5014() :
  F, S, G, U, D = map(int, input().split())
  visited = [False for _ in range(F+1)] 
  dict = {}
  
  for i in range(1, F + 1) :
    dict[i] = MAX_VALUE

  queue = deque()
  queue.append([S, 0])
  dict[S] = 0
  while queue :
    curr_stair, count = queue.popleft()
    next_count = count + 1
    
    next_stair = curr_stair + U
    if next_stair <= F and dict[next_stair] > next_count :
      dict[next_stair] = next_count
      queue.append([next_stair, next_count])

    next_stair = curr_stair - D
    if next_stair >= 1 and dict[next_stair] > next_count :
      dict[next_stair] = next_count
      queue.append([next_stair, next_count])

  if dict[G] == MAX_VALUE :
    print("use the stairs")
  else :
    print(dict[G])


BOJ5014()
