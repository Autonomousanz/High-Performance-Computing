//question1
//time complexity of the problem is O(n)
#include <iostream>
#include<map>

using namespace std;
class Sumproblem {
public:
	void findSum(int arr[], int target) {
		std::map<int, int> myMap;
		std::map<int, int>::iterator it;
		for (int i = 0; i < 4; i++) {
			int difference = target - arr[i];
			//cout << trg << "**" << arr[i] << " " << difference << endl;
			//cout << arrMap.find(difference);
			it = myMap.find(difference);
			if (it != myMap.end()) {
				cout << myMap[difference] << " " << arr[i];

			}
			else {
				if (i == 4) {
					cout << "no solution found!"<< endl;
				}
				myMap.insert(std::pair<int, int>(arr[i], arr[i]));
			}
		}
		

	}

};
//twoelements sum
int main() {
	int arrayIn[4];
	int target;

	cout << "Enter the array" << endl;
	for (int i = 0; i < 4; i++) {
		cin >> arrayIn[i];
	}
	cout << "Enter the sum target" << endl;
	cin >> target;
	Sumproblem getResult;
	getResult.findSum(arrayIn, target);
	
}

