import sys 
input = sys.stdin.readline
INF = int(1e4)

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
  for i in range(N) :
    print(dp[i])
BOJ2098()

# dp[i][j] 는 현재 i점이며 이진수 j지점들을 방문했고 시작점으로 돌아갈때의 최소 비용
# 0011 0과 1을 이동한 비용
# 0111 0과 1과 2를 이동한 비용
# 1111 0과 1과 2와 3을 이동한 비용
# 0101 0과 2를 이동한 비용 
# 0110 1과 2를 순회한 비용
# 1110 1과 2와 3을 순회한 비용 14
# https://hongcoding.tistory.com/83
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90%EC%88%9C%ED%9A%8C-Python
# 비트마스크를 쓰는이유는 백트래킹으로 접근하면 16!(20922789888000) 20조 정도의 케이스를 탐색해야 한다 -> 시간초과
# 그래서 비트마스크를 쓰는데 몇 비트 정도로 모든 케이스를 잡을수 있고 이진수로 되어있어 컴퓨터의 연산에도 빠른 장점이 있다.
