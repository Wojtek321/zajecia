#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream plik("C:\\Users\\wojte\\Desktop\\zajecia\\asd\\zajecia3\\zad2\\In0302.txt");
    int n, W;
    plik>>n>>W;

    int** tab = new int*[n];
    for(int i = 0; i < n; i++)
        tab[i] = new int[2];

    for(int i=0; i<n; i++)
    {
        plik>>tab[i][0]>>tab[i][1];
    }
    plik.close();


    for(int i=0; i<n; i++)
    {
        cout<<tab[i][0]<<" "<<tab[i][1]<<endl;
    }


    int S[5][5] = {};
    
}
