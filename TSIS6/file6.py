import os
def generate_files():
    start = ord('A')
    end = ord('Z') + 1
    for ascii_val in range(start, end):
        letter = chr(ascii_val)
        filename = f"{letter}.txt"
        with open(filename, 'w') as f:
            f.write(f"This is file {filename}\n")
generate_files()