#include <iostream>
#include <fstream>

using namespace std;

void przeciecie(int A[], int B[], int n, ofstream &out);
bool binary_search(int a, int tab[], int l, int r);

int main()
{
    int n;
    ifstream file(R"(In0209.txt)");
    file>>n;
    int *A = new int[n];
    int *B = new int[n];

    for(int i=0; i<n; i++)
        file>>A[i];
    for(int i=0; i<n; i++)
        file>>B[i];

    file.close();


    ofstream out(R"(Out0209.txt)");
    przeciecie(A, B, n, out);
    out.close();
}

void przeciecie(int A[], int B[], int n, ofstream &out)
{
    int licznik = 0;

    for(int i=0; i<n; i++)
    {
        if(binary_search(A[i], B, 0, n-1))
        {
            out<<A[i]<<" ";
            licznik++;
        }
    }

    out<<endl<<licznik<<endl;
}

bool binary_search(int a, int tab[], int l, int r)
{
    int sr = (l+r)/2;

    if(l > r)
    {
        return false;
    }
    else if(a > tab[sr])
    {
        return binary_search(a, tab, sr + 1, r);
    }
    else if(a < tab[sr])
    {
        return binary_search(a, tab, l, sr-1);
    }
    else
    {
        return true;
    }
}