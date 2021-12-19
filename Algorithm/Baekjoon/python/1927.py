import heapq, sys

def BOJ1927() :
  n = int(sys.stdin.readline())
  list = []
  for _ in range(n) :
    command = int(sys.stdin.readline())
    if command == 0 :
      if len(list) == 0 :
        print(0)
      else :
        print(heapq.heappop(list))
    else :
      heapq.heappush(list, command)

BOJ1927()
