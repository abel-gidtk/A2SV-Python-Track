# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

line_ab = int(input())
line_bc = int(input())

line_ac = math.sqrt(math.pow(line_ab, 2) + math.pow(line_bc, 2))
angle_degree = math.degrees(math.asin(line_ab/line_ac))

if (angle_degree - math.floor(angle_degree) >= 0.5):
    angle_degree = math.ceil(angle_degree)
else:
    angle_degree = math.floor(angle_degree)
print(f"{angle_degree}\N{DEGREE SIGN}")
