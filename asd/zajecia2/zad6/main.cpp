#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n;
    ifstream file(R"(C:\Users\Wojtek\Desktop\zajecia\asd\zajecia2\zad6\In0206.txt)");
    file >> n;
    int *tab = new int[n*n];
    



    file.close();

}
