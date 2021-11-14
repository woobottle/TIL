def solution(gems):
  answer = []
  gem_set = set(gems)
  gem_dict = {}
  GEM_LENGTH = len(gems)
  start = 0
  end = 0
  while start <= GEM_LENGTH and end <= GEM_LENGTH :
    if len(gem_dict) < len(gem_set) :
      if end >= GEM_LENGTH:
        break
      if gem_dict.get(gems[end]) :
        gem_dict[gems[end]] += 1
      else :  
        gem_dict[gems[end]] = 1
      end += 1
    else :
      answer.append([start, end - 1])
      gem_dict[gems[start]] -= 1
      if gem_dict.get(gems[start]) == 0 :
        del gem_dict[gems[start]]
      start += 1
    
  answer.sort(key= lambda x : (x[1] - x[0], x[0]))
  first, second = answer[0]
  return [first+1, second+1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))


# result = [[{}] * len(gems) for _ in range(len(gems))]
#  l = set(gems)
#   answer = []
#    for i in range(len(gems)):
#         for j in range(i, len(gems)):
#             result[j][i] = set(gems[i:j + 1])

#     for i in range(len(result)):
#         for j in range(len(result[0])):
#             if len(result[j][i]) == len(l):
#                 answer.append([i, j])

#     answer.sort(key=lambda x: (x[1] - x[0], x[0]))
#     first, second = answer[0]
#     return [first+1, second+1]
