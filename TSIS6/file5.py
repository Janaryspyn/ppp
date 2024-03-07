def writelist(file_path, list):
        with open(file_path, "w") as file:
            for item in list:
                file.write(item)
        print("written to row.txt")
list = ['messi', 'suui', 'ibra', 'lewa']



file_path = 'row.txt'   
writelist(file_path, list)




