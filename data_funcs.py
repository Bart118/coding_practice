#functions to create, modify, and check data

import os
import random
import statistics
from file_funcs import read_data, write_list

def rand_list(amount, lower, upper):
    data = []
    for i in range(amount):
        data.append(random.randint(lower,upper))
    return data

#modifies each point of "true" data by adding or subtracting a random number
#the severity variable controls how large the random number can be
def mod_data(severity):
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
    average = statistics.mean(test_data)
    std_dev = statistics.stdev(test_data)
    true_data.append(average)
    true_data.append(std_dev)
    write_list("true_data.txt", true_data)
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
