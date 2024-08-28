#python script to run an executable written in c++
#last updated on: 8/27/24

import os
import random
from file_funcs import write_list, write_spec, read_data

def rand_list(amount, lower, upper):
    data = []
    for i in range(amount):
        data.append(random.randint(lower, upper))
    print(data)
    return data

def check_result(option, amount):
    print("Checking results...")
    start_data = read_data("script_data.txt")
    #add in error handling
    start_data_int = [int(s) for s in start_data]
    end_data = read_data("results.txt")
    #add in error handling
    end_data_int = [int(s) for s in end_data]
    answers = [0,0]
    if (option == 1):
        print("Data should be equal")
        #checks if both files are equal
        if (len(start_data) == len(end_data)):
            j = 0
            for i in start_data_int:
                if(start_data_int[j] == end_data_int[j]):
                    answers[0] += 1
                else:
                    answers[1] +=1
                    print("Point ", i, "is wrong")
                    print("start: ", start_data[j])
                    print("end: ", end_data[j])
                j += 1
            print("Correct Answers: ", answers[0])
            print("Wrong Answers: ", answers[1])
        else:
            print("Error, file sizes don't match")
    elif (option == 2):
        #checks if result is greater than start by a specified amount
        print("Result should be greater than the start")
        j = 0
        if (len(start_data) == len(end_data)):
            for i in start_data:
                compare = end_data_int[j] + amount
                if (start_data_int[j] >= compare):
                    answers[0] += 1
                else:
                    answers[1] += 1
                    print("Point", j, "is wrong")
                    print("start:", start_data[j], "end:", end_data[j])
                    #print("end: ", end_data[j])
                j += 1
            print("Correct Answers: ", answers[0])
            print("Wrong Answers: ", answers[1])
        else:
            print("Error, file sizes don't match")
    elif (option == 3):
        #checks if result is less than start by a specified amount
        print("Result should be less than the start")
        if (len(start_data) == len(end_data)):
            j = 0
            for i in start_data:
                compare = end_data_int[j] - amount
                if (start_data_int[j] <= compare):
                    answers[0] += 1
                else:
                    answers[1] += 1
                    print("Point ", j, "is wrong")
                    print("start: ", start_data[j])
                    print("end: ", end_data[j])
                j += 1
            print("Correct Answers: ", answers[0])
            print("Wrong Answers: ", answers[1])
        else:
            print("Error, file sizes don't match")
    else:
        print("Invalid option")
    
    
#first attempt, results should be equal
data_file = "script_data.txt"
print("First test")
data = rand_list(10, 1, 20)
write_list(data_file, data)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#checking the results
check_result(1, 0)

#2nd attempt, results should be greater than start by 5
print("Second test")
data = rand_list(20, 1, 5)
write_list(data_file, data)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#checking the results
check_result(2,5)

print("Third Test")
write_spec("script_data.txt")

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#checking the results
check_result(1, 0)

input("\n\nPress enter to close.")
