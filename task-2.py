import math
a = float(input('Input side a: '))
b = float(input('Input side b: '))
c = float(input('Input side c: '))
semi_perimeter = (a + b + c) / 2
area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
print('Triangle area =', area)