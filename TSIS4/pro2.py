def area(a, b, h):
    calculate = ((a + b) / 2) * h
    return calculate

height = int(input())
base1 = int(input())
base2 = int(input())
result = area(base1, base2, height)
print(result)