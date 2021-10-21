# binary_search + 조건문 

def solution(x) :
  start_index = 1
  end_index = len(x)
  peak = 0

  def binary_search(array, start, end) :
    mid = (start + end) // 2
    if start > end :
      return 

    if (is_peak(array[mid-1],array[mid],array[mid+1])):
      peak = array[mid]
      print(peak)
      return
    
    binary_search(array, start + 1, mid)
    binary_search(array, mid, end - 1)

  binary_search(x, start_index, end_index)
  return peak
  
def is_peak(a, target, b) :
  return a < target and b < target

solution([-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]) # 6 
solution([-1, -1, -1, -1, 0, 1, 20, 19, 17]) # 20
