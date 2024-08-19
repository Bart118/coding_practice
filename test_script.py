#python script to run an executable written in c++
#last updated on: 7/31/24

import os
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

def read_data():
    print("Reading file...")
    result_file = open("results.txt")
    results = result_file.readlines()
    return results
    
#first attempt, use less than 50 lines of data
write_data(10)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#read the results
results1 = read_data()

#2nd attempt, using more lines
write_data(100)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#read the results
results2 = read_data()

input("\n\nPress enter to close.")
