def countUniques(iterable):
  answer = [];
  for value in iterable :
    if value not in answer :
      answer.append(value);
  return len(answer)


# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14]))  # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))  # 2
