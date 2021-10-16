def searchMatrix(matrix, target) :
  spreadedArray = []
  for array in matrix:
    spreadedArray.extend(array);

  matrixHasTarget = binary_search(spreadedArray, target, 0, len(spreadedArray))
  return matrixHasTarget
  

def binary_search(array, target, start, end) :
  if start > end :
    return False
  
  mid = (start + end) // 2
  
  if array[mid] == target :
    return True
  elif array[mid] > target :
    end = mid - 1
  elif array[mid] < target :
    start = mid + 1

  return binary_search(array, target, start, end)

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3

print(searchMatrix(matrix, target)) # True

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 13

print(searchMatrix(matrix, target)) # False
