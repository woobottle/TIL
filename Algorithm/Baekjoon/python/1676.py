import sys
n = int(sys.stdin.readline())

two_count = 0
five_count = 0

two = 2 
while two <= n :
  two_count += n // two
  two *= 2

five = 5
while five <= n:
  five_count += n // five
  five *= 5

print(min(two_count, five_count))
