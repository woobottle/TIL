def solution(rows, columns, connections, queries):
    answer = [] 
    # array = [[0] * (columns + 1) for _ in range(rows + 1)]
    
    temp = []
    for r1, c1, r2, c2 in connections :
      temp.append([[(r1 + r2) / 2, (c1 + c2) / 2],True])
      
    for query in queries :
        r1, c1, r2, c2 = query
        cnt = 0
        rectangle = []
        
        for i in range(min(r1, r2), max(r1, r2) + 1):
            for j in range(min(c1, c2), max(c1, c2) + 1):
                rectangle.append([i, j])

        rectangle[0] = [rectangle[0][0] - 0.5, rectangle[0][1] - 0.5]
        rectangle[1] = [rectangle[1][0] - 0.5, rectangle[1][1] + 0.5]
        rectangle[2] = [rectangle[2][0] + 0.5, rectangle[2][1] - 0.5]
        rectangle[3] = [rectangle[3][0] + 0.5, rectangle[3][1] + 0.5]

        # print(rectangle)
        for tc in temp :
            [x1, y1], flag = tc
            if flag :
              for rc in rectangle :
                  x, y = rc
                  if x1 != x and y1 != y:
                    pass
                  else :
                    cnt += 1
                    tc[1] = False
                    break

        answer.append(cnt)    
    return answer


print(solution(4, 3,	[[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]))	# [4, 2]
# print(solution(2,	2,	[[1, 1, 1, 2], [2, 2, 1, 2], [2, 1, 1, 1], [2, 2, 2, 1]], [[1, 1, 2, 2], [1, 1, 2, 1], [2, 1, 2, 2]])) # [0, 2, 2]
# print(solution(3,	3,	[[1, 1, 2, 1], [2, 1, 3, 1], [1, 2, 2, 2], [2, 2, 3, 2], [1, 3, 2, 3], [2, 3, 3, 3]], [[1, 1, 3, 1], [1, 2, 3, 2], [1, 3, 3, 3]])) # [0, 0, 0]
