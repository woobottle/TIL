from itertools import combinations

def solution(arr):
    # answer = 0
    for i in range(3, len(arr) + 1) :
      print(list(combinations(arr, i)))
    # return answer


print(solution([0, 1, 2, 5, 3, 7]))	# 3
# print(solution([1, 2, 3, 2, 1]))  # 4
# print(solution([1, 2, 3, 2, 1, 4, 3, 2, 2, 1]))  # 6
# print(solution([1, 2, 1, 2, 1]))  # 2
