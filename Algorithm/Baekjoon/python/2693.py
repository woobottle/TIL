import sys
input = sys.stdin.readline

def BOJ2693() :
  def bubble_sort(array) :
    for i in range(len(array)):
      for j in range(len(array)) :
        if array[i] > array[j] :
          array[i], array[j] = array[j], array[i]
    return array

  n = int(input())
  for _ in range(n) :
    A = list(map(int, input().split()))
    A = bubble_sort(A)
    print(A[-8])

BOJ2693()
