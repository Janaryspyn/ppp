from functools import reduce
 
def multiply_list(numbers):
    if not numbers:
        return 0 
    result = reduce(lambda x, y: x * y, numbers)
    return result
numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)