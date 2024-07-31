#python script to run an executable written in c++
#last updated on: 7/31/24

import os

try:
    print("Running the program")
    os.system("C:/Users/sbart/Documents/coding_practice/CMakeProject1/out/build/x64-debug/CMakeProject1.exe")
    print("Program is finished")
except:
    print("Something went wrong")

input("\n\nPress enter to close.")
