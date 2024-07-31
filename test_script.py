#python script to run an executable written in c++
#last updated on: 7/31/24

import os

print("creating a text file to pass parameters to executable")
text_file = open("script_data.txt", "w")
text_file.write("This is my text file\n")
my_data = input("Write the second line ")
text_file.write(my_data)
text_file.write("\n")
text_file.write("This is the third line\n")
text_file.close()

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

input("\n\nPress enter to close.")
