def solution(array, commands):
  answer = []
  for command in commands:
    start, end, target = command
    temp = sorted(array[start-1:end])
    answer.append(temp[target-1])
  return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
