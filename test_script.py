#python script to run an executable written in c++
#last updated on: 8/27/24

import os
import random
from file_funcs import write_list, write_spec, read_data
from data_funcs import rand_list, mod_data, check_result()

def test(count, lower, upper, severity):
    data_file = "true_data.txt"
    data = rand_list(count, lower, upper)
    write_list(data_file, data)
    create_data(severity)

    try:
        print("Running the program")
        os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
        print("Program is finished")
    except:
        print("Something went wrong")

    #checking the results
    check_result()

print("First Test...")
test(100, 1, 100, 5)

print("Second Test...")
test(100, 1, 100, 10)

input("\n\nPress enter to close.")
