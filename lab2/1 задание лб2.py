a = 1
b = 0
c = 0
if a and not b or c:
    print('а true')
else:
    print('а false')
if a and (not b or c):
    print('б true')
else:
    print('б false')
if a or (not(b and c)):
    print('в true')
else:
    print('в false')
