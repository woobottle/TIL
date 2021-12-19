def BOJ9252():
  first = input()
  second = input()
  array = [[[0, '']] * (len(second) + 1) for _ in range(len(first) + 1)]
  l = []
  for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
      if first[i-1] == second[j-1]:
        array[i][j] = [array[i-1][j-1][0] + 1, array[i-1][j-1][1] + first[i-1]]
      else:
        if array[i-1][j][0] > array[i][j-1][0] :
          array[i][j] = [array[i-1][j][0], array[i-1][j][1]]
        elif array[i-1][j][0] < array[i][j-1][0]:
          array[i][j] = [array[i][j-1][0], array[i][j-1][1]]
        else :
          array[i][j] = [array[i][j-1][0], array[i][j-1][1]]

  print(array[len(first)][len(second)][0])
  print(array[len(first)][len(second)][1])


BOJ9252()
