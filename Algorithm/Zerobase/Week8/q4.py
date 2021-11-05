def solution(N, K1, K2, W, V):
  answer = [[0] * (K2 + 1)] * (K1 + 1)
  return answer

print(solution(4, 3, 8, [1,5,6,3], [5,2,14,6])) # 25

# 동적프로그래밍 같은데....
# 순회를 어떻게 할건데???