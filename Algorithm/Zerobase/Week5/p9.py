def quicksort(data_list) :
  if len(data_list) <= 1:
    return data_list

  pivot = data_list[0]

  left = [item for item in data_list[1:] if pivot > item]
  right = [item for item in data_list[1:] if pivot <= item]

  return quicksort(left) + [pivot] + quicksort(right)


data_list = [50, 90, 1, 14, 8, 21, 65]
print(quicksort(data_list))