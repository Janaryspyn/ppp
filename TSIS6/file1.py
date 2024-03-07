import os
path = 'C:\\Users\\123\\Documents\\pp2'
print("\nOnly directories")
print([name for name in os.listdir(path) if os.path.isdir(name)])
print("\nOnly files")
print([name for name in os.listdir(path) if os.path.isfile(name)])
print("\All directries and files")
print([name for name in os.listdir(path)])