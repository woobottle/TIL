from itertools import permutations

def solution(n, weak, dist):
  answer = len(dist) + 1
  weak_length = len(weak)
  for i in range(weak_length) :
    weak.append(weak[i] + n)
  
  dist_permutations = list(map(list,permutations(dist, len(dist))))

  for i in range(weak_length) :
    temporary_range = [weak[j] for j in range(i, i + weak_length)]

    for dist_permutes in dist_permutations :
      result = 1
      friend_index = 0
      checked_length = temporary_range[0] + dist_permutes[friend_index]
      for k in range(weak_length) :
        if temporary_range[k] > checked_length :
          result += 1
          
          if result > len(dist_permutes) :
            break
          
          friend_index += 1
          checked_length = temporary_range[k] + dist_permutes[friend_index]
      
      answer = min(answer, result)

  if answer > len(dist) :
    return -1
  return answer


# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# print(solution(n, weak, dist))

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# print(solution(n, weak, dist))

# N = 200
# weak = [0, 100]
# dist = [1, 1]
# print(solution(N, weak, dist)) # 2

N = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]
print(solution(N, weak, dist))  # 3
