// CMakeProject1.cpp : Defines the entry point for the application.
//

#include "CMakeProject1.h"

int main()
{
	char exit_ans;
	std::cout << "Hello!" << std::endl;

	//reading from a text file and printing the results to the screen
	std::string my_text;
	int num_arry[50] = {};
	std::string fileName = "script_data.txt";
	int LineCount = count_lines(fileName);
	std::cout << "there are: " << LineCount << " lines" << std::endl;
	std::ifstream MyReadFile(fileName);
	int i = 0;
	bool end_early = false;  //decides if while loop should end early
	while (std::getline(MyReadFile, my_text) && end_early == false) {
		if (i < 50) {
			try {
				num_arry[i] = std::stoi(my_text);
			}
			catch (const std::invalid_argument& e) {
				std::cout << "Invalid input: " << e.what() << std::endl;
			}
			catch (const std::out_of_range& e) {
				std::cout << "Input out of range: " << e.what() << std::endl;
			}
		}
		else {
			std::cout << "Too many arguments" << std::endl;
			end_early = true;
		}
		std::cout << i << std::endl;
		i++;
	}
	MyReadFile.close();

	//print text values
	if (end_early == false) {
		for (int j = 0; j <= i; j++) {
			std::cout << num_arry[j] << std::endl;
		}
	}

	//waits for a user input to close the program
	std::cout << "Enter a character to exit" << std::endl;
	std::cin >> exit_ans;
	return 0;
}
