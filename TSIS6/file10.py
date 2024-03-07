def count_upper_lower(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count
 
text = input()
upper_count, lower_count = count_upper_lower(text)
 
print(upper_count)
print( lower_count)