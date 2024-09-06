#include "kalman.h"

float ave(std::vector<float> data) {
	float sum = 0;
	float data_count = data.size();
	for (int i = 0; (i < data_count); i++) {
		sum += data[i];
	}
	float average = sum / data_count;
	return average;
}

float std_dev(std::vector<float> data) {
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

std::vector<float> filter(std::vector<float> data) {
	std::cout << "filtering data..." << std::endl;
	std::vector<float> filtered = data;
	float data_count = data.size();
	float st_d = std_dev(data);
	//start with initial guesses
	float x1 = ave(data);
	float p1 = st_d*st_d;
	float r1 = st_d * st_d;  //standard deviation squared
	for (int i = 0; i < data_count; i++) {
		float z1 = data[i];  //measurement
		float K1 = (p1) / (p1 + r1);
		float x2 = x1 + K1 * (z1 - x1);  //estimate
		float p2 = (1 - K1) * p1;  //estimate variance
		filtered[i] = x2;  //putting estimate into filtered results
		x1 = x2;  //update x for next iteration
		p1 = p2;  //update p for next iteration
	}
	
	return filtered;
}