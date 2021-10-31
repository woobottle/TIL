def solution(intervals) :
  min_in_intervals = min(min(intervals))
  max_in_intervals = max(max(intervals))
  spread_intervals = [0] * (max_in_intervals + 1)
  answer = []

  for i in intervals :
    [start, end] = i
    for j in range(start, end+1) :
      spread_intervals[j] = 1

  temp = []
  for i in range(len(spread_intervals)) :
    if(spread_intervals[i] == 1 and len(temp) == 0) :
      temp.append(i)
    elif (i == len(spread_intervals) - 1 and len(temp) == 1) :
      temp.append(i)
    elif (spread_intervals[i] == 0 and len(temp) != 0) :
      temp.append(i-1)
    
    if (len(temp) == 2) :
      answer.append(temp)
      temp = []
  
  return answer

print(solution([[1,3], [2,6], [8,10], [15,18]])) # [[1,6], [8,10], [15,18]]
print(solution([[1,4], [4,5]])) # [[1,5]]
