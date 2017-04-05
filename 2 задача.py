import math
y = int(input())
k = int(input())
r = math.sqrt(math.sin(y)**2+6.835)/(math.log10(y+k)+3*(y**2))
print(r)
