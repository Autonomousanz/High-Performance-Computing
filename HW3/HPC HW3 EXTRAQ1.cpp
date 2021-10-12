#include<iostream>
#include<climits>
using namespace std;

int maxSubArraySum(int a[], int size)
{
    int max_so_far = INT_MIN, max_ending_here = 0;
    for (int i = 0; i < size; i++)
    {
        max_ending_here = max_ending_here + a[i];
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;
        
        if (max_ending_here < 0)
            max_ending_here = 0;
    }
    return max_so_far;
}

/*Driver program to test maxSubArraySum*/
int main()
{
    const int maxArr = 100;
    int arrSize = 0;
    cout << "Input total number of elements in an array : " << endl;
    cin >> arrSize;
    int a[maxArr];
    cout << "Enter " << arrSize  << " integer values for the array" << endl;
    for (int i = 0; i < arrSize; i++) {
        cin >> a[i];
    }
    int n = sizeof(a) / sizeof(a[0]);
    int max_sum = maxSubArraySum(a, n);
    cout << "Maximum contiguous sum is " << max_sum;
    return 0;
}