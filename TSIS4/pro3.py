import math
def areapolygon(n, l):
    area = n/4 * l**2 * 1 / math.tan(math.pi/n)
    return area
number = int(input())
length = int(input())
result = areapolygon(number, length)
print(int(result))