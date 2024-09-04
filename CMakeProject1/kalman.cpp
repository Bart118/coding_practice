#include "kalman.h"

float ave(std::vector<int> data) {
	float sum = 0;
	float data_count = data.size();
	for (int i = 0; (i < data_count); i++) {
		sum += data[i];
	}
	float average = sum / data_count;
	return average;
}

float std_dev(std::vector<int> data) {
	std::cout << "calculating the standard deviation..." << std::endl;
	//equation
	//std_dev = sqrt((sum(data_pt - average)^2/(data_count - 1))
	float std_d = 0;
	float average = ave(data);
	float data_count = data.size();  //number of elements in data vector
	float sum = 0;
	float square = 0;
	for (int i = 0; (i < data_count); i++) {
		square = (data[i] - average) * (data[i] - average);
		sum += square;
	}
	float arg = sum / (data_count - 1);
	std_d = sqrtf(arg);
	return std_d;
}

std::vector<int> filter(std::vector<int> data, float std_dev) {
	std::cout << "filtering data..." << std::endl;
	//start with initial guesses
	//x^00 = estimated value
	//p00 = standard deviation of estimate squared = std_dev^2
	//make first prediction
	// x^10 = x^00
	// p10 = p00
	//measure
	// z1 = measurment 1
	// r1 = std_dev of measurement squared
	// update
	// find K1, x^11, p11
	// predict
	// x^21 = x^11
	// p21 = p11
	//equations
	//xnn = xnn-1 + Kn * (zn - xnn-1)
	//pnn = (1-Kn) * pnn-1
	//Kn = (pnn-1) / (pnn-1 + rn)
	
	//for constant dynamics
	//x^n+1n = xnn
	//pn+1n = pnn
	return data;
}