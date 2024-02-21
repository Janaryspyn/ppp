import math

def degreestorad(degree):
    rad = degree * (math.pi / 180)
    return rad

input_degree = float(input())

output_radian = degreestorad(input_degree)


print(output_radian)