def solution(N, K1, K2, W, V):
  answer = [[0] * (K2 + 1)] * (K1 + 1)
  
  for index in range(N) :
    for w1 in range(K1, 0, -1) :
      for w2 in range(K2, 0, -1) :
        weight = W[index]
        cost = V[index]
        if w1 >= weight and w2 >= weight :
          answer[w1][w2] = max(
            answer[w1][w2], max(answer[w1-weight][w2] + cost , answer[w1][w2-weight] + cost))
        elif w1 >= weight :
          answer[w1][w2] = max(answer[w1][w2], answer[w1-weight][w2] + cost)
        elif w2 >= weight :
          answer[w1][w2] = max(answer[w1][w2], answer[w1][w2-weight] + cost)

  return answer

print(solution(4, 3, 8, [1,5,6,3], [5,2,14,6])) # 25

# 동적프로그래밍 같은데....
# 순회를 어떻게 할건데???