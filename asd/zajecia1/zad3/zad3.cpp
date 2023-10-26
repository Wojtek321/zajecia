#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int licznik;
void naiwyny(int *tab, int size);
void optymalny(int *tab, int size);
ofstream output("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia1\\zad3\\Out0103.txt");

int main() {
    ifstream file("C:\\Users\\Wojtek\\Desktop\\zajecia\\asd\\zajecia1\\zad3\\In0103.txt");

    int n, a, i=0;
    file>>n;
    int *tab = new int[n];

    while(file>>a)
    {
        tab[i]=a;
        i++;
    }
    file.close();

    licznik = 0;
    naiwyny(tab, n);
    licznik = 0;
    optymalny(tab, n);

    delete []tab;
    output.close();
}

void optymalny(int *tab, int size)
{
    int maxsuma=0, suma = 0, maxstart=0, start=0, koniec=0;
    for(int i=0; i<size; i++)
    {
        if(suma+tab[i] > 0)
        {
            suma += tab[i];
        }
        else
        {
            suma = 0;
            start = i+1;
        }

        if(suma>maxsuma)
        {
            maxsuma = suma;
            maxstart = start;
            koniec = i;
        }
    }
    maxstart++;
    koniec++;


    output<<maxstart<<", "<<koniec<<", "<<maxsuma<<endl;

}

void naiwyny(int *tab, int size)
{
    int maxsuma=0, start=0, koniec=0;
    for(int i=0; i<size; i++)
    {
        int suma = 0;
        for(int j=i; j<size; j++)
        {
            suma += tab[j];
            licznik++;

            if (suma>maxsuma)
            {
                maxsuma = suma;
                start = i;
                koniec = j;
            }
        }
    }
    start++;
    koniec++;
    licznik += 2;

    output<<start<<", "<<koniec<<", "<<maxsuma<<", licz = "<<licznik<<endl;
}