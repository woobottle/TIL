import sys
input = sys.stdin.readline

def BOJ2309() :
  def bubble_sort(array) :
    for i in range(len(array)):
      for j in range(i, len(array)):
        if array[i] > array[j]:
          array[i], array[j] = array[j], array[i]

    return array

  l = [] 
  for _ in range(9) :
    l.append(int(input()))
  
  for i in range(8) :
    for j in range(i+1, 9) :
      for idx, value in enumerate(l) :
        if sum(l) - (l[i] + l[j]) == 100 :
          l[i], l[j] = 0, 0
          break
        
  l = list(filter(lambda x : x != 0, l))
  
  l = bubble_sort(l)
  for i in l :
    print(i)

BOJ2309()
