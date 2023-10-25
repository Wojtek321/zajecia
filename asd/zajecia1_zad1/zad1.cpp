#include <iostream>
#include <fstream>

using namespace std;

int licznik;
int silnia(int n);
int SN1(int n, int k);
int SN3(int n, int k);


int main() {
    int n, k;
    ifstream file("In0101.txt");
    file>>n>>k;
    file.close();

    ofstream output("Out0101.txt");
    output<<"n="<<n<<" k="<<k<<endl;
    licznik = 0;
    output<<"SN1 = "<<SN1(n, k)<<", licz = "<<licznik<<endl;
    licznik = 0;
    output<<"SN3 = "<<SN3(n, k)<<", licz = "<<licznik<<endl;
    output.close();
}

int silnia(int n)
{
    int wynik = 1;
    for (int i=2; i<=n; i++)
    {
        wynik *= i;
        licznik++;
    }
    return wynik;
}

int SN1(int n, int k)
{
    int wynik = silnia(n)/(silnia(k)*silnia(n-k));
    licznik++;
    return wynik;
}

int SN3(int n, int k)
{
    if(k==0 || k==n)
        return 1;
    else
    {
        licznik++;
        return SN3(n-1, k-1) + SN3(n-1, k);
    }
}