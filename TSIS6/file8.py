import os
 
def delete(file_path):
        if not os.path.exists(file_path):
            print(f"The file '{file_path}' does not exist.")
            return
        if not os.access(file_path, os.W_OK):
            print(f"You do not have permission to delete the file '{file_path}'.")
            return
        os.remove(file_path)
        print(f"The file '{file_path}' has been successfully deleted.")

 

file_path = "G.txt"  
delete(file_path)