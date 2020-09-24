import math

xy = input('Enter (x1,y1):')
ab = input('Enter (x2,y2):')

x1,y1 = xy.split(",")
x2,y2 = ab.split(",")

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

juli = math.sqrt( (x1-x2) ** 2 + (y1-y2) ** 2 )

print(f'{juli:.2f}')
