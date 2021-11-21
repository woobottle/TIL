import math 

def calc_dist(x,y) :
  return math.sqrt(x ** 2 + y ** 2)

def solution(names, homes, grades):
    answer = []
    temp = {}
    array = []
    for name, [x,y], grade in zip(names, homes, grades) :
      array.append([name, calc_dist(x,y), int(grade // 1)])
    array.sort(key = lambda x : (-x[2], -x[1], x[0]))
    
    for i in range(len(array)):
        temp[array[i][0]] = i + 1

    for name in names :
      answer.append(temp[name])
      
    return answer


print(solution(["azad", "andy", "louis", "will", "edward"], [[3, 4], [-1, 5], [-4, 4], [3, 4], [-5, 0]],[4.19, 3.77, 4.41, 3.65, 3.58]))	# [2, 3, 1, 5, 4]
print(solution(["clanguage", "csharp", "java", "python"], [[3, -3], [-2, 7],[-1, -1], [5, 4]], [1.27, 4.31, 4.26, 3.99])) #[4, 1, 2, 3]
print(solution(["zzzzzzzzzz"], [[9999, -9999]], [1.0]))  # [1]
