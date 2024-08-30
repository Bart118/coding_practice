#python script to run an executable written in c++
#last updated on: 8/27/24

import os
import random
from file_funcs import write_list, write_spec, read_data

def rand_list(amount, lower, upper):
    data = []
    for i in range(amount):
        data.append(random.randint(lower, upper))
    print("True data:", data)
    return data

#modifies each point of "true" data by adding or subtracting a random number
#the severity variable controls how large the random number can be
def create_data(severity):
    print("modifying data...")
    test_data = []
    true_data = read_data("true_data.txt")
    t_data_int = [int(s) for s in true_data]
    for i in t_data_int:
        pm = random.randint(1,2)
        if(pm < 2):
            test_data.append(i + random.randint(1, severity))
        else:
            test_data.append(i - random.randint(1, severity))
    print("New data:", test_data)
    write_list("script_data.txt", test_data)
    

def check_result():
    print("Checking results...")
    correct = 0
    wrong = 0
    t_data = read_data("true_data.txt")
    e_data = read_data("results.txt")
    t_data_int = [int(s) for s in t_data]
    e_data_int= [int(s) for s in e_data]
    print("true data:", t_data_int)
    print("results:", e_data_int)
    for i in range(len(t_data_int)):
        if (t_data_int[i] == e_data_int[i]):
            correct += 1
        else:
            wrong += 1
    print("correct:", correct, "incorrect:", wrong)
    
    
#first attempt, results should be equal
data_file = "true_data.txt"
data_count = 10
lower_limit = 1
upper_limit = 20
severity = 5
print("First test")
data = rand_list(data_count, lower_limit, upper_limit)
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

#2nd attempt, results should be greater than start by 5
print("Second test")
severity = 10
data = rand_list(data_count, lower_limit, upper_limit)
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

input("\n\nPress enter to close.")
