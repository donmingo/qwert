import math
a = int(input())
b = int(input())
c = int(input())
z = 1/(b+c)*math.sqrt(b*c*(a+b+c)*(b+c-a))
print(z)
