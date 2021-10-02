data1 = (0,1,2,3,4,5,6,7,8,9)
data2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
result = list(data1)[:6] + data2[::2]
print(result)