import math

x1 = int(input('Enter X1:'))
y1 = int(input('Enter Y1:'))
x2 = int(input('Enter X2:'))
y2 = int(input('Enter Y2:'))

juli = math.sqrt( (x1-x2) ** 2 + (y1-y2) ** 2 )

print(f'{juli:.2f}')
