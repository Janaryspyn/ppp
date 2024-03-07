import time
import math

def cal(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = int(input())
milliseconds = 2123

result = cal(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
