import sys 
input = sys.stdin.readline
INF = int(1e9)

def BOJ2098() :
  N = int(input())
  dp = [[INF for _ in range(1 << N)] for _ in range(N) ]
  graph = []
  
  def dfs(curr, visited) :
    if visited == (1 << N) - 1 :  # 모든 도시를 방문한 경우
      if graph[curr][0] : # 출발점으로 가는 경로가 있을때
        return graph[curr][0]
      else :
        return INF
    
    if dp[curr][visited] != INF : # 이미 최소비용이 계산되어 있는 경우
      return dp[curr][visited]

    for next in range(N) :
      if visited & (1 << next) : # 이미 방문한 경우
        continue
        
      if graph[curr][next] == 0 : # 해당 지점에 방문할 수 없는 경우
        continue 
      
      next_visited = visited | (1 << next)
      # 원래 점화식 dp[curr][visited] = min(dp[curr][visited], dp[next][next_visited] + graph[curr][next])
      dp[curr][visited] = min(dp[curr][visited], dfs(next, next_visited) + graph[curr][next])
      
    return dp[curr][visited]

  for _ in range(N) :
    graph.append(list(map(int, input().split())))
  
  # 한번만 호출해도 되는 경우는 사이클을 이루기 때문 0 -> 1 -> 2 -> 3 -> 0 은 1에서 출발하나 2에서 출발하나 비용에 대한 계산은 같다
  print(dfs(0, 1))

BOJ2098()


# https://hongcoding.tistory.com/83
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90%EC%88%9C%ED%9A%8C-Python
