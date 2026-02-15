number = int(input())
part_one = number // 10000
part_two = number % 10000 // 1000
part_three = number % 1000 // 100
part_four = number % 100 // 10
part_five = number % 10
print(part_one)
print(part_two)
print(part_three)
print(part_four)
print(part_five)
