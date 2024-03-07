def all_true_elements(tuple_values):
    return all(tuple_values)
tuple_values = (1,2,False)
result = all_true_elements(tuple_values)

if result:
    print("All are true")
else:
    print("FALSE!")
