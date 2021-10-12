#include <iostream>
#include <vector>
using namespace std;

bool differentChar(string str, int i, int j)
{

    vector<bool> visitedChar(26);
    for (int k = i; k <= j; k++) {
        if (visitedChar[str[k] - 'a'] == true)
            return false;
        visitedChar[str[k] - 'a'] = true;
    }
    return true;
}
int uniqueString(string str)
{
    int lengthOfString = str.size();
    int resultSum = 0;
    for (int i = 0; i < lengthOfString; i++)
        for (int j = i; j < lengthOfString; j++)
            if (differentChar(str, i, j))
                resultSum = max(resultSum, j - i + 1);
    return resultSum;
}
int main()
{
    string inputString = "";
    cout << "Please enter input string  " << endl;
    cin >> inputString;
    cout << "The input string is " << inputString << endl;
    int lengthOfString = uniqueString(inputString);
    cout << "The length of the longest non-repeating "
        "character substring is "
        << lengthOfString;
    return 0;
}