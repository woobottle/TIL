import sys
input = sys.stdin.readline

def BOJ10830() :
  N, B = map(int, input().split())

  def matrix_mul(a, b) :
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
      for j in range(N):
        for k in range(N):
          result[i][j] += (a[i][k] * b[k][j]) % 1000
    
    for i in range(N) :
      for j in range(N) :
        result[i][j] %= 1000

    return result
  
  def divide(a, count) :
    if count == 1 :
      return a
    tmp = divide(a, count // 2)
    if count % 2 == 1 :
      return matrix_mul(matrix_mul(tmp, tmp), a)
    else :
      return matrix_mul(tmp, tmp)

  array = []
  for _ in range(N) :
    array.append(list(map(int, input().split())))

  answer = divide(array, B)

  for i in range(N) :
    for j in range(N) :
      print(answer[i][j] % 1000, end = " ")
    print()

BOJ10830()
