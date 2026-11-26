import range_checker

num = int(input("A number: "))
is_in = "yes" if range_checker.in_range(num, 2, 15) else "no"
print(f"Number {num} in the range <2,15>: {is_in}")
