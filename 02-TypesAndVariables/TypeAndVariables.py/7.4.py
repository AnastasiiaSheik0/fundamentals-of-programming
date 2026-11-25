import math


tree_circumference = int(input('enter tree circumference in cm: '))
tcbcd = tree_circumference/math.pi >= 50
print(f'tree can be cut down: {tcbcd}')