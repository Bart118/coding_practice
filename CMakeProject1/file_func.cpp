//contains functions controlling file operations

#include "file_func.h"

//int count_lines(std::string fileName);

int count_lines(std::string fileName) {
	std::string mytext;
	std::ifstream MyReadFile(fileName);
	int i = 0;
	while (std::getline(MyReadFile, mytext)) {
		i++;
	}
	return i;
}

std::vector<int> copy_data(std::string fileName, int start, int limit) {
	std::cout << "starting copy" << std::endl;
	std::vector<int> num_arry(limit);
	std::string my_text;
	std::ifstream MyReadFile(fileName);
	int i = 0;
	while (std::getline(MyReadFile, my_text)) {
		if ((i < limit) && (i >= start)) {
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
		i++;
	}
	MyReadFile.close();
	std::cout << "finished copying" << std::endl;
	return num_arry;
}

int write_result(std::vector<int> data, int start, int end) {
	std::cout << "writing data..." << std::endl;
	int result = 0;
	std::string fileName = "results.txt";
	std::ofstream myFile(fileName);

	if (myFile.is_open()) {
		for (int i = start; i < end; i++) {
			myFile << std::to_string(data[i]) << std::endl;
		}
		result = 1;
		myFile.close();
	}
	else {
		result = 0;
	}

	return result;
}