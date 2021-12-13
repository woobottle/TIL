n, k = map(int, input().split())
MAX_LENGTH = 100001
visited = [[-1, 0] for _ in range(MAX_LENGTH)]

queue = []
queue.append(n)
# 처음 방문한 곳은 방문정보와 방법의 수를 업데이트
visited[n][0] = 0
visited[n][1] = 1

while queue :
  x = queue.pop(0)
  
  for i in [x-1, x+1, x*2] :
    if 0 <= i <= 100000 :
      # 방문한적이 없는 애들만 q에 넣어주자
      # 제일 처음 방문한 친구가 가장 최단 시간에 방문한 것일 거다.
      if visited[i][0] == -1 :
        visited[i][0] = visited[x][0] + 1
        visited[i][1] = visited[x][1]
        queue.append(i)
      
      # 방문한적이 있고 바로 다음 방문할 예정이라면
      # 방문예정인 곳의 방법의 수는 이전 스팟의 방법의 수를 더해주어야 한다.
      elif visited[i][0] == visited[x][0] + 1 :
        visited[i][1] += visited[x][1]

print(visited[k][0])
print(visited[k][1])

# https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-12851%EB%B2%88-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%884-Python-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89BFS