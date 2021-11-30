from itertools import combinations

n, k = map(int, input().split())
array = [x for x in range(1, n+1)]

print(list(combinations(array, k)))
