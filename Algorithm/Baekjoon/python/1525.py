from collections import deque
import sys
def BOJ1525() :
  graph = []
  answer = "123456780"
  queue = []
  visited = {}
  direction = [[0,1], [0,-1], [1,0], [-1,0]]
  result = -1
  for _ in range(3) :
    for i in input().split() :
      graph.append(i)
  
  serialized_graph = graph
  start_index = serialized_graph.index("0")
  start_x, start_y = divmod(start_index, 3)
  visited["".join(serialized_graph)] = True
  queue.append(["".join(serialized_graph), 0, start_x, start_y])

  while queue:
    current_graph, count, curr_x, curr_y = queue.pop(0)

    if current_graph == answer:
      result = count
      break
    curr_location = curr_x * 3 + curr_y
    
    for dir_x, dir_y in direction :
      next_x = curr_x + dir_x
      next_y = curr_y + dir_y
      next_location = next_x * 3 + next_y
      if 0 <= next_x <= 2 and 0 <= next_y <= 2 :
        temp_graph = list(current_graph)
        temp_graph[next_location], temp_graph[curr_location] = temp_graph[curr_location], temp_graph[next_location]
        join_graph = "".join(temp_graph)
        if join_graph not in visited:
          visited[join_graph]=True
          queue.append([join_graph, count+1, next_x, next_y])

  print(result)

BOJ1525()


# 상, 하, 좌, 우
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def bfs():
#   while q:
#     now = q.popleft()
#     if now == "123456789":
#       return cntDict[now]
#     pos = now.find("9")
#     x = pos // 3
#     y = pos % 3
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < 3 and 0 <= ny < 3:
#         nPos = nx * 3 + ny
#         nextNum = list(now)
#         nextNum[nPos], nextNum[pos] = nextNum[pos], nextNum[nPos]
#         nextNum = "".join(nextNum)

#         if not cntDict.get(nextNum):
#           q.append(nextNum)
#           cntDict[nextNum] = cntDict[now] + 1


# start = ""
# for _ in range(3):
#   temp = sys.stdin.readline().strip()
#   temp = temp.replace(" ", "")
#   start += temp

# start = start.replace("0", "9")

# q = deque()
# q.append(start)

# cntDict = dict()
# cntDict[start] = 0

# result = bfs()
# print(result if result != None else "-1")

# https://cijbest.tistory.com/15
