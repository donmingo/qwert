import math
s = float(input())
a = float(input())
b = float(input())
count = 0
while s>b:
    b=b*1.03
    s=s+a-b
    count=count+1
print(count)
    















