def solution(iterable):
  iterable.sort(key=len)
  count = 0
  keep = True
  for value in enumerate(list(iterable[0])):
    [index, data] = value
    for checked in iterable :
      if checked[index] != data :
        keep = False
        break
    if keep :
      count += 1
    else : 
      break
  return count

# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))  # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))  # 0
