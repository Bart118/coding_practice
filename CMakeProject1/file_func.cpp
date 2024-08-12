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