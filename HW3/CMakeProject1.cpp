#include <iostream>
#include <xtensor/xarray.hpp>
#include <xtensor/xio.hpp>
#include <xtensor/xview.hpp>
using namespace std;
const double pi = 3.14;

int main(int argc, char* argv[])
{
    xt::xarray<double>arr1={ 1.0, 2.0, 3.0 };
    cout << arr1 << endl;
    xt::xarray<double>arr2={ 5.0, 6.0, 7.0 };
    cout << arr2<<endl;
    xt::xarray<double>arr3 = arr1 + arr2;
    cout << arr3 << endl;
    xt::xarray<double>arr4 = arr2 - arr1;
    cout << arr4<< endl;
    xt::xarray<double>arr5 = arr1 * arr2;
    cout << arr5 << endl;
    xt::xarray<double>arr6 = arr2/arr1;
    cout << arr6 << endl;

    xt::xarray<double>Sarray2D = {{1.0, 2.0, 3.0},{4.0,5.0,6.0}};
    xt::xarray<double>Darray2D = {{1.0, 2.0, 3.0},{4.0,5.0,6.0}};

    xt::xarray<double>newarr3 = Sarray2D + Darray2D;
    cout << newarr3 << endl;
    xt::xarray<double>newarr4 = Darray2D - Sarray2D;
    cout << newarr4 << endl;
    xt::xarray<double>newarr5 = Sarray2D * Darray2D;
    cout << newarr5 << endl;
    xt::xarray<double>newarr6 = Darray2D / Sarray2D;
    cout << newarr6 << endl;



  
    return 0;
}