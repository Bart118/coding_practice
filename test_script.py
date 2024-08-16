#python script to run an executable written in c++
#last updated on: 7/31/24

import os
import random

#first attempt, use less than 50 lines of data
print("creating a text file to pass parameters to executable")
text_file = open("script_data.txt", "w")
data_count = 10  #lines of data to put in text file
number_data = random.randint(1,1000)
for i in range(data_count):
    text_file.write(str(number_data))
    text_file.write("\n")
    number_data = random.randint(1,1000)
text_file.close()

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#read the results
result_file = open("results.txt")
results = result_file.readlines()
print(len(results))
for line in results:
    print(line)
result_file.close()

#2nd attempt, use more than 50 lines
print("creating a text file to pass parameters to executable")
text_file = open("script_data.txt", "w")
data_count = 60
number_data = random.randint(1,1000)
for i in range(data_count):
    text_file.write(str(number_data))
    text_file.write("\n")
    number_data = random.randint(1,1000)
text_file.close()

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

#read the results
result_file = open("results.txt")
results = result_file.readlines()
print(len(results))
for line in results:
    print(line)
result_file.close()

input("\n\nPress enter to close.")
