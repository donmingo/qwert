import math
a = int(input('стоимость покупки в грн'))
if a > 1000 and a <2000:
    print('5%')
else:
    if a > 2000 and a < 5000:
        print('10%')
        
