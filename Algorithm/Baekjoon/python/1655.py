import heapq
import sys

def BOJ1655():
  n = int(sys.stdin.readline())
  leftheap = []
  rightheap = []
  
  for _ in range(n) :
    input_num = int(sys.stdin.readline())

    if len(leftheap) == len(rightheap) :
      heapq.heappush(leftheap, (-input_num, input_num))
    else :
      heapq.heappush(rightheap, (input_num, input_num))
    
    if rightheap and leftheap[0][1] > rightheap[0][1] :
      leftmin = heapq.heappop(leftheap)[1]
      rightmin = heapq.heappop(rightheap)[0]
      heapq.heappush(leftheap, (-rightmin, rightmin))
      heapq.heappush(rightheap, (leftmin, leftmin))

    print(leftheap[0][1])

BOJ1655()

# https: // art-coding3.tistory.com/44
