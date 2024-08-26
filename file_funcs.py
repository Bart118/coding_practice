#functions for file operations
import random

def write_data(data_count):
    print("Writing to file...")
    text_file = open("script_data.txt", "w")
    number_data = random.randint(1,1000)
    for i in range(data_count):
        text_file.write(str(number_data))
        text_file.write("\n")
        number_data = random.randint(1,1000)
    text_file.close()

def read_data(file):
    print("Reading file...")
    result_file = open(file)
    results = result_file.readlines()
    return results
