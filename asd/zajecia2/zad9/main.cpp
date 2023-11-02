#include <iostream>
#include <fstream>

using namespace std;

void przeciecie(int A[], int B[], int n, ofstream &out);
bool binary_search(int a, int tab[], int n);

int main()
{
    int n;
    ifstream file(R"(C:\Users\Wojtek\Desktop\zajecia\asd\zajecia2\zad9\In0209.txt)");
    file>>n;
    int *A = new int[n];
    int *B = new int[n];

    for(int i=0; i<n; i++)
        file>>A[i];
    for(int i=0; i<n; i++)
        file>>B[i];

    file.close();


    ofstream out(R"(C:\Users\Wojtek\Desktop\zajecia\asd\zajecia2\zad9\Out0209.txt)");
    przeciecie(A, B, 12, out);
    out.close();
}

void przeciecie(int A[], int B[], int n, ofstream &out)
{
    int licznik = 0;

    for(int i=0; i<n; i++)
    {
        if(binary_search(A[i], B, 12))
        {
            out<<A[i]<<" ";
            licznik++;
        }
    }

    out<<endl<<licznik<<endl;
}

bool binary_search(int a, int tab[], int n)
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