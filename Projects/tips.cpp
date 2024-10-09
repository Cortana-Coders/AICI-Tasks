#include <iostream>


int main(){
    int numbers[5] = {1,2,3,4,5};

    for (auto n: numbers) {
    std::cout<<"iteration "<<n<<" : "<<numbers[n-1]<<std::endl;
    }

    // Swapping of 2 numbers
    /*
    Example
    int a = 10;
    int b = 30;
    int temp = a; // 10
    a = b; // 30
    b = temp; // 10
    */

   int a = 10;
   int b = 30;
   a ^= b;
   b ^= a;
   a ^= b;
    std::cout << "A = " << a << "\nB = " << b <<std::endl;




    return 0;
}