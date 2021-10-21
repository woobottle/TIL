def solution(nums, target):
  results = []
  used = [0 for _ in range(len(nums))]

  def get_all_lists(elements, start, end, used) :
    if (len(elements) == 4 and sum(elements) == target) :
      sorted_elements = sorted(elements)
      if sorted_elements not in results :
        results.append(sorted_elements[:])
      return

    for i in range(0, end) :
      if not used[i] :
        elements.append(nums[i])
        used[i] = 1
        get_all_lists(elements, i+1, end-1, used)
        used[i] = 0
        elements.pop()

  get_all_lists([], 0, len(nums), used)
  return results

nums = [1, 0, -1, 0, -2, 2]
target = 0

solution(nums, target) # [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]