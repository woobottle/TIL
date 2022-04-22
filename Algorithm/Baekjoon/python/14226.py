from collections import deque
import sys
input = sys.stdin.readline

def BOJ14226() :
  S = int(input().strip())
  graph = [[-1 for _ in range(S+1)] for _ in range(S+1)]  # 개수 별 최소 시간
  graph[1][0] = 0
  
  def bfs() :
    queue = deque()
    queue.append([1, 0])

    while queue :
      curr_node, curr_clip  = queue.popleft()

      if graph[curr_node][curr_node] == -1 :
        graph[curr_node][curr_node] = graph[curr_node][curr_clip] + 1
        queue.append([curr_node, curr_node])
      
      next_node = curr_node + curr_clip
      if 0 < next_node <= S and graph[next_node][curr_clip] == -1 :
        graph[next_node][curr_clip] = graph[curr_node][curr_clip] + 1
        queue.append([next_node, curr_clip])
      
      next_node = curr_node - 1
      if 0 < next_node <= S and graph[next_node][curr_clip] == -1 :
        graph[next_node][curr_clip] = graph[curr_node][curr_clip] + 1
        queue.append([next_node, curr_clip])

  bfs()
  result = -1
  for i in range(S+1) :
    if graph[S][i] != -1 :
      if result == -1 :
        result = graph[S][i]
        continue
      result = min(result, graph[S][i])

  print(result)

BOJ14226()


# 3가지 동작중 하나를 수행, 동작 하나에 1초를 소요
# 화면의 모두를 복사해서 클립 보드에 저장
# 클립 보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 화면에 있는 이모티콘 중 하나를 삭제

# 2
# 1 -> 저장(1) -> 복사 2
# 4
# 1 -> 저장(1) -> 복사 2 -> 저장(2) -> 복사 4
# 6
# 1 -> 저장(1) -> 복사 2 -> 저장(2) -> 복사 4 -> 복사 6
# 18
# 1 -> 저장(1) -> 복사 2 -> 저장(2) -> 복사 4 -> 복사 6 -> 저장(6) -> 복사 12 -> 복사 18
