#python script to run an executable written in c++
#last updated on: 7/31/24

import os
import random
from file_funcs import write_data, read_data

def check_result(option, amount):
    print("Checking results...")
    start_data = read_data("script_data.txt")
    start_data_int = [int(s) for s in start_data]
    end_data = read_data("results.txt")
    end_data_int = [int(s) for s in end_data]
    answers = [0,0]
    if (option == 1):
        print("Data should be equal")
        #checks if both files are equal
        if (len(start_data) == len(end_data)):
            j = 0
            for i in start_data_int:
                print(j)
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
write_data(10)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#checking the results
check_result(1, 0)

#2nd attempt, results should be greater than start by 5
write_data(10)

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#checking the results
check_result(2,5)

input("\n\nPress enter to close.")
