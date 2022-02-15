# import sys
# input = sys.stdin.readline

# def BOJ24230() :
#   N = int(input())
#   l = list(map(int, input().split()))
#   count = 0
#   if l[0] != 0 :
#     count = 1

#   for _ in range(N-1) :
#     [a, b] = sorted(list(map(int, input().split())))
#     if l[a-1] != l[b-1] :
#       count += 1

#   print(count)
  
# BOJ24230()

import sys
input = sys.stdin.readline
N = int(input())
colors = list(map(int, input().split()))
graph = {i: [] for i in range(0, N+1)}
graph_colors = [0 for _ in range(N+1)]

for i in range(N-1) :
  a, b  = map(int, input().split())
  if a < b :
    graph[a].append(b)
  else :
    graph[b].append(a)

ans = 0

def paint(idx, color) :
  graph_colors[idx] = color
  for i in graph[idx] :
    paint(i, color)

for idx, color in enumerate(colors) :
  if color == 0 :
    continue
  if graph_colors[idx + 1] != color :
    ans += 1 
    paint(idx+1, color)

print(ans)