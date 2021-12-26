import sys 
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
directions = [[1,0], [-1,0], [0,1], [0,-1]]

def bfsAndCountZero(array, viruses) :
  height = len(array)
  width = len(array[0])
  visited = [[0] * width for _ in range(height)]
  zero_count = 0

  queue = deque()
  for virus in viruses :
    queue.append(virus)

  while queue :
    curr_x, curr_y = queue.pop()
    for dir in directions :
      dir_x, dir_y = dir
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y
      
      if next_x < 0 or height <= next_x or next_y < 0 or width <= next_y :
        continue
      
      if visited[next_x][next_y] :
        continue

      if array[next_x][next_y] == 0 :
        array[next_x][next_y] = 2
        visited[next_x][next_y] = 1
        queue.append([next_x, next_y])

  for x in range(height) :
    for y in range(width) :
      if array[x][y] == 0 :
        zero_count += 1
  
  return zero_count


def BOJ14502() :
  N, M = map(int, input().split())
  graph = []
  for _ in range(N) :
    graph.append(list(map(int, input().split())))
  
  virus_list = []
  empty_list = []
  answer = 0
  
  for x in range(N) :
    for y in range(M) :
      if graph[x][y] == 2 :
        virus_list.append([x,y])
      elif graph[x][y] == 0 :
        empty_list.append([x,y])
  
  empty_combinations = list(combinations(empty_list, 3))
  
  for empties in empty_combinations :
    for empty in empties :
      x, y = empty
      graph[x][y] = 1

    temp_graph = copy.deepcopy(graph)
    answer = max(answer, bfsAndCountZero(temp_graph, virus_list))

    for empty in empties:
      x, y = empty
      graph[x][y] = 0

  print(answer)

BOJ14502()
