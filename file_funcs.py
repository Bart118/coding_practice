#functions for file operations
import random

#writes the specified number of random integers between 1 and 1000
def write_rand(data_count, file):
    print("Writing to file...")
    text_file = open(file, "w")
    number_data = random.randint(1,1000)
    for i in range(data_count):
        text_file.write(str(number_data))
        text_file.write("\n")
        number_data = random.randint(1,1000)
    text_file.close()

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
