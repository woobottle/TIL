#4
# 과제 4번 코드란
# 우병
def solution(N, trust):
  trustGraph = [[0] * (N + 1) for _ in range(N + 1)]
  for a, b in trust:
    trustGraph[b][a] = 1

  maeulpansa = -1
  for i in range(1, N + 1):
    if (sum(trustGraph[i])) == N-1 and trustGraph[i][i] == 0 and getVerticalSum(trustGraph, N, i) == 0:
      maeulpansa = i

  return maeulpansa


def getVerticalSum(graph, n, index):
  verticalSum = 0
  for j in range(1, n + 1):
    verticalSum += graph[j][index]

  return verticalSum


print(solution(2, [[1,2]])) # 2
print(solution(3,	[[1, 3], [2, 3]]))	# 3
print(solution(3,	[[1, 3], [2, 3], [3, 1]])) # -1
print(solution(3,	[[1, 2], [2, 3]])) # -1
print(solution(4,	[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))	# 3
