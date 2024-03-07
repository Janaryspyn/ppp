def copy_file(source_file, destination_file):
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as new:
                new.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
   

source_file = "H.txt"
destination_file = "A.txt"
copy_file(source_file, destination_file)