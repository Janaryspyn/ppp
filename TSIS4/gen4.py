def square(a, b):
    for i in range(a, b + 1):
        yield i**2
start = int(input())
end = int(input())
for num in square(start, end):
    print(num)