//definitions and includes for file operations

#include <string>
#include <fstream>
#include <iostream>
#include <vector>

//reads the file whose name is passed into the function and determines how many lines it has
//returns the number of lines as an integer
int count_lines(std::string fileName);

//reads each line of the passed file and copies it into a vector
//the vector is returned by the function
//the starting position can be changed by the second parameter
//the number of lines to be read can be limited by the third parameter
std::vector<float> copy_data(std::string fileName, int start, int limit);

//writes the results of the program to a new text file
//returns an integer to let the main program know if it succeeded
//start and end control the endpoints of the vector to be copied
int write_result(std::vector<float> data, int start, int end);