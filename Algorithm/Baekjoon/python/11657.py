import sys
input = sys.stdin.readline
INF = 1e9

def BOJ11657() :
  N, M = map(int, input().split())
  edges = []
  dist = [INF] * (N + 1)
  negative_cycle = False

  for _ in range(M) :
    A, B, C = map(int, input().split())
    edges.append((A,B,C))

  dist[1] = 0
  for i in range(N) :
    for edge in edges :
      curr_node, next_node, cost = edge
      if dist[curr_node] != INF and dist[next_node] > dist[curr_node] + cost :
        dist[next_node] = dist[curr_node] + cost
        if i == N-1 :  # N-1 라운드에서도 값을 갱신하려 한다면 음의 순환이 존재한다는 것
          negative_cycle = True

  if negative_cycle :
    print("-1")
  else :
    for i in range(1, N+1) :
      if dist[i] == INF :
        print("-1")
      else :
        print(dist[i])

BOJ11657()

# https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm


