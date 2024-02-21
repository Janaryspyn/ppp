def downto0(n):
    while n >= 0:
        yield n
        n-=1
x = int(input())
for num in downto0(x):
    print(num)