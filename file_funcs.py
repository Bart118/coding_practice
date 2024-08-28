#functions for file operations

#writes a list to a file
def write_list(file, data):
    print("writing the list to a file...")
    text_file = open(file, "w")
    for line in data:
        text_file.write(str(line))
        text_file.write("\n")
    text_file.close()
    print("finished writing")
    
#writes user input to a file
def write_spec(file):
    print("writing to file...")
    amount = int(input("Enter how many lines you want: "))
    text_file = open(file, "w")
    for i in range(amount):
        print("Line ", i)
        line = input("Enter data: ")
        text_file.write(line)
        text_file.write("\n")
    text_file.close()

#reads a text file and returns a list of the results
def read_data(file):
    print("Reading file...")
    result_file = open(file)
    results = result_file.readlines()
    return results
