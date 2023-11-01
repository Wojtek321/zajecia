#include <iostream>
#include <fstream>

using namespace std;

void przeciecie(int A[], int B[], int n, ofstream &out);
bool szukaj(int a, int tab[], int n);

int main()
{
    int A[] = {9, 4, 6, 11, 24, 12, 16, 49, 33, 16, 8, 18};
    int B[] = {1, 3, 4, 6, 7, 8, 9, 12, 16, 18, 25, 27};

    ofstream out(R"(C:\Users\Wojtek\Desktop\zajecia\asd\zajecia2\zad9\Out0209.txt)");
    przeciecie(A, B, 12, out);
    out.close();
}

void przeciecie(int A[], int B[], int n, ofstream &out)
{
    int licznik = 0;

    for(int i=0; i<n; i++)
    {
        if(szukaj(A[i], B, 12))
        {
            out<<A[i]<<" ";
            licznik++;
        }
    }

    out<<endl<<licznik<<endl;
}

bool szukaj(int a, int tab[], int n)
{
    int l = 0, r = n-1, sr;

    while(l <= r)
    {
        sr = (l+r)/2;

        if(a > tab[sr])
        {
            l = sr + 1;
        }
        else if(a < tab[sr])
        {
            r = sr - 1;
        }
        else
        {
            return true;
        }
    }
    return false;
}