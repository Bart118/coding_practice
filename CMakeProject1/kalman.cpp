#include "kalman.h"

float std_dev(std::vector<int> data) {
	std::cout << "calculating the standard deviation..." << std::endl;
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
}