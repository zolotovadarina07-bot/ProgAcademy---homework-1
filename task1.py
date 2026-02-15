import math
side_a = float(input('Input side a: '))
side_b = float(input('Input side b: '))
side_c = float(input('Input side c: '))
semi_perimeter = (side_a + side_b + side_c) / 2
area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))
print('Triangle area =', area)


