from collections import deque
import sys
input = sys.stdin.readline
LENGTH = 65536
HALF_LENGTH = 32768
INF = 1e6

def BOJ9205() :
  global convenient_and_target
  global pentaport_x, pentaport_y
  
  def bfs(beer, curr_x, curr_y) :
    queue = deque()
    visit = []
    queue.append([curr_x, curr_y, beer])
    visit.append([curr_x, curr_y, beer])
    
    while queue :
      curr_x, curr_y, curr_beer = queue.popleft()

      if curr_x == pentaport_x and curr_y == pentaport_y :
        print("happy")
        return
      for convenient_x, convenient_y in convenient_and_target :
        if [convenient_x, convenient_y, beer] not in visit :
          dist = abs(convenient_x - curr_x) + abs(convenient_y - curr_y)
          if dist <= curr_beer * 50 :
            queue.append([convenient_x, convenient_y, curr_beer])
            visit.append([convenient_x, convenient_y, curr_beer])
    print("sad")
    return

  t = int(input())
  
  for _ in range(t) :
    beer = 20
    n = int(input())
    home_x, home_y = map(int, input().split())
    
    convenient_and_target = []
    for _ in range(n) :
      convenient_and_target.append(list(map(int, input().split())))
    
    pentaport_x, pentaport_y = map(int, input().split())
    convenient_and_target.append([pentaport_x, pentaport_y])

    bfs(beer, home_x, home_y)

BOJ9205()
