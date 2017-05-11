import math
k=int(input("введите число k "))
j=-1
p=0
while j<=k:
    p1=((j-j**2)*j)/(j+14)
    i=j
    while i<=(k+3):
        p2=((math.fabs(i-5))**(1/4))/(math.fabs(i-7))
        i=i+1
    p=p+(p1*p2)
    k=k+1
print("результат = ",p)
