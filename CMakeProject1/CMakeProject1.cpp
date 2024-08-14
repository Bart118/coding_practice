// CMakeProject1.cpp : Defines the entry point for the application.
//

#include "CMakeProject1.h"

int main()
{
	char exit_ans;
	std::cout << "Hello!" << std::endl;

	//reading from a text file and printing the results to the screen
	std::string fileName = "script_data.txt";
	int LineCount = count_lines(fileName);
	std::vector<int> num_arry(LineCount);
	std::cout << "there are: " << LineCount << " lines" << std::endl;
	num_arry = copy_data(fileName, 0, LineCount);

	//print text values
	for (int j = 0; j < LineCount; j++) {
			std::cout << num_arry[j] << std::endl;
	}

	//waits for a user input to close the program
	std::cout << "Enter a character to exit" << std::endl;
	std::cin >> exit_ans;
	return 0;
}
